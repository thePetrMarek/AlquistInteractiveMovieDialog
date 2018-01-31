from data import Data
from web_interface import flask

if __name__ == '__main__':
    Data().process("data.json")
    flask.run(port=5678, debug=False, threaded=True, host="0.0.0.0", use_reloader=False)
