from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/capture-bid', methods=['POST'])
def capture_bid():
  bid_data = request.json
  
  # TODO: Log data
  print(f"Captured bid: {bid_data}")
  
  response = {
    "success": True,
    "response": "Bid captured"
  }
  
  return jsonify(response), 200

if __name__ == '__main__':
  app.run(port=5000)