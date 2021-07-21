import os
import io
import json
import math
import random
import urllib
import argparse
import configparser

import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from werkzeug.datastructures import FileStorage

from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask_restplus import Api, Resource

import py_eureka_client.netint_utils as netint_utils
import py_eureka_client.eureka_client as eureka_client

import torch
import numpy as np
from PIL import Image

device = torch.device('cuda' if torch.cuda.is_available() else ('cpu'))


app = Flask(__name__)
CORS(app)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

api = Api(app,version='1.0',title='Test-Page',description='')
ns = api.namespace('Test-Page')
app.config.SWAGGER_UI_DOC_EXPANSION = 'full'

upload_parser = ns.parser()
upload_parser.add_argument('file', required=True, location='files', type=FileStorage, help='image')

@api.route('/Test/predict')
@api.expect(upload_parser)
class UploadDemo(Resource):
	def post(self):
		returns = {}
		
		args = upload_parser.parse_args()
		
		if args['file']:
			img_bytes = args.get('file').read()
			img = Image.open(io.BytesIO(img_bytes)).convert('RGB')
		
		returns['test'] ='image open success'
		return jsonify(returns)    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='which server?')
    parser.add_argument('--port_number', '-p', type=int, default=30017, help='port number default id 30017')
    args = parser.parse_args()

    config = configparser.ConfigParser()
    port_number = args.port_number

    app.run(port=port_number, host='0.0.0.0')
