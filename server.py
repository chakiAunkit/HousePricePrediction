from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import sys
import logging
import util

app = Flask(__name__)
# cors = CORS(app, resources={r"/*": {"origins": "*"}})
# app.config['CORS_HEADERS'] = 'Content-Type'

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.INFO)

CORS(app, support_credentials=True)


@app.route('/')
@cross_origin()
def model_load_test() :
    response = jsonify({
        'estimated_price': util.get_estimated_price('whitefield', 1200, 3, 3)
    })
    if response: 
        return {'msg':'Load Successful'}

@app.route('/get_location_names')
@cross_origin()
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    # response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['POST'])
@cross_origin(headers=['Content-Type'])
def predict_home_price():
    location = request.form['location']
    sqft = int(request.form['sqft'])
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, sqft, bhk, bath)
    })
    # response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Flask server")
    util.load_saved_artifacts()
    app.run()
