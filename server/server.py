import numpy as np
from flask import Flask, request, jsonify, make_response, Response
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import pickle
import time
import os

app = Flask(__name__)

CORS(app)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top

model = pickle.load(open('./lgbm.pkl','rb'))

pathModel = f"{APP_ROOT}/model/lgbm.pkl"

@app.route("/")
def check_api():
    return "API ONLINE v1.0", 200

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict(np.array([list(data.values())]))
    result = prediction[0]

    res = {'ID_code': int(result)}
    return jsonify(res)


if __name__ == '__main__':
    app.run(threaded=True, host="0.0.0.0", port=5003)
