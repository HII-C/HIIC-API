from argparse import ArgumentParser
from flask import Flask,request,render_template
from flask_restful import Api
import json
from get_items import get_items
from get_associations import get_associations
from flask_cors import CORS, cross_origin


# Set ''default'' parameters for database connections
params = {'user': 'api',
          'host': 'localhost',
          'db': 'mimiciiiv14',
          'password': ''}

# parse command line (or dockerfile) modifications to the default params
parser = ArgumentParser()
parser.add_argument('--user')
parser.add_argument('--host')
parser.add_argument('--db')
parser.add_argument('--password')
args = parser.parse_args()

# iterate all vars in namespace 'args' and set their param equiv to passed value
#for arg in vars(args):
    # print(arg, vars(args)[arg])
    #params[arg] = str(vars(args)[arg])

print(params)

app = Flask(__name__)
api = Api(app)
CORS(app)

client = None


@app.route('/')
def main():
    return render_template("home.html")

#api.add_resource(get_mapppings, '/get_mappings', methods=['GET'])
api.add_resource(get_items, '/get_items',
                 methods=['GET'], resource_class_kwargs={"db_params": params})
api.add_resource(get_associations, '/get_associations',
                 methods=['GET'], resource_class_kwargs={"db_params": params})

app.debug = True

app.run(host='0.0.0.0', port='80', threaded=True)
