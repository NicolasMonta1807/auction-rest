from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Load Environment Variables
PORT = os.getenv("PORT", "8080")
CAPTURE = os.getenv("CAPTURE_URL", "http://bid-capture-service:5000/capture-bid")
TRACKING = os.getenv("TRACKING_URL", "http://bid-tracking-service:5001/track-bid")
ANALYTICS = os.getenv("ANALYTICS_URL", "http://bid-analytics-service:5002/analyse-bid")

@app.route('/produce-bid', methods=['POST'])
def produce_bid():
  bid_data = request.json

  capture_response = requests.post(CAPTURE, json=bid_data)
  
  tracking_response = requests.post(TRACKING, json=bid_data)
  
  analytics_response = requests.post(ANALYTICS, json=bid_data)
  
  return jsonify({
    "capture": capture_response.text,
    "tracking": tracking_response.text,
    "analytics": analytics_response.text
  }), 200
  
if __name__ == '__main__':
  app.run( port=PORT)
  