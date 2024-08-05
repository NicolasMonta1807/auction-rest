from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/track-bid', methods=['POST'])
def track_bid():
  bid_data = request.json
  
  # TODO: Log data
  print(f"Tracked bid: {bid_data}")
  
  response = {
    "success": True,
    "response": "Bid tracked"
  }
  
  return jsonify(response), 200

if __name__ == '__main__':
  app.run(port=5001)