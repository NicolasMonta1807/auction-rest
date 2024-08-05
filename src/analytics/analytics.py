from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyse-bid', methods=['POST'])
def analyse_bid():
  bid_data = request.json
  
  #TODO: Log data
  print(f"Analysed bid: {bid_data}")
  
  response = {
    "success": True,
    "response": "Bid analysed"
  }
  
  return jsonify(response), 200

if __name__ == '__main__':
  app.run(port=5002)