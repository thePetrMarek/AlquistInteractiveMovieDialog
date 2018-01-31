from flask import Flask, jsonify
from flask import request
from flask_cors import CORS

from data import Data

flask = Flask(__name__)
cors = CORS(flask)


@flask.route("/", methods=['GET'])
def get_message():
    try:
        message = request.args.get('message')
    except KeyError:
        # Missing 'text'
        return {"Error": "Missing message"}, 400
    response = Data().get_answer(message)
    return jsonify(response=response)
