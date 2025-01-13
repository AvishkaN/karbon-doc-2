from flask import Flask, jsonify, request
from flask_cors import CORS
import Inference as ManFunc


app = Flask(__name__)

CORS(app)

# Define a route for the home page
@app.route('/')
def home():
    return "Welcome to the Flask server!"

# Example route with JSON response
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"message": "Hello, Flask!", "status": "success"}
    return jsonify(data)

# Route to handle POST requests
@app.route('/api/send', methods=['POST'])
def send_data():
    input_data = request.json
    print(input_data['message'])
    result=ManFunc.getResults(input_data['message'])
    print('----')
    print('----')
    print('----')
    print(result)
    return jsonify(result)



# if __name__ == '__main__':
#     # app.run(debug=True)
app.run(debug=True)
