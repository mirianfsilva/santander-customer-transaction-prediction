import time, os, pickle
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, make_response, Response
from flask_restplus import Api, fields, Resource
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

app = Flask(__name__)
CORS(app)

app = Flask(__name__)

api = Api(
    app, 
    version='1.0', 
    title='Santander Customer Transaction Prediction API',
    description='Customer Transaction Prediction API')

ns = api.namespace('transaction_prediction', description='Transaction Prediction')
model = pickle.load(open('./lgbm.pkl','rb'))

parser = api.parser()
#In this case, my number of features: length=202
number_features = 200

#parse features for API
for idx in range(number_features):
    parser.add_argument(
        'var_'+str(idx),
        type=float, 
        required=True, 
        help='feature'+str(idx), 
        location='form'
    )
parser.add_argument(
    'ID_code',
    type=str, 
    required=False, 
    help='id', 
    location='form'
)
# Setup the request parameters, feed them into the model, and determine the transaction prediction (prababilites).
resource_fields = api.model('Resource', {
    'result': fields.List(fields.Float)
})

upload_parser = api.parser()
upload_parser.add_argument('file', location='files', type=FileStorage, required=True)


@ns.route('/upload/')
@api.expect(upload_parser)
class Upload(Resource):
    def post(self):
        args = upload_parser.parse_args()
        file = args.get('file')  # This is FileStorage instance
        result = pd.read_csv(file)
        return {'url': result}, 201
    
    def get_results(self, file):
        df = pd.DataFrame(file)
        features = [c for c in df.columns if c not in ["ID_code"]]
        
        result = model.predict(features)
        return result

@ns.route('/predict')
class PredictionApi(Resource):
    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)

    def post(self):
        file = request.files['file']
        data = pd.read_csv(file)

        args = parser.parse_args()
        result = self.get_results(args)
        return result, 201

    def get_results(self, args):
        for idx in range(number_features):
            var[idx] = args['var_'+str(idx)] 

        df = pd.DataFrame([[ 'var_'+str(idx) for idx in args ]])

        clf = pickle.load('model.pkl');

        result = clf.predict(df)

        res = {'ID_code' : result}
        return jsonify(res)



if __name__ == '__main__':
    app.run(threaded=True, host="0.0.0.0", port=5003, debug=True)
