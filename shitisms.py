from flask import Flask,Response
import json
import random

app = Flask(__name__)

# Simple output if people come in the web browser. Don't even send a header.
@app.route('/')
def http():
    return get_shit()

# CLI is pretty well the same, except has a newline
@app.route('/cli')
def cli():
    return get_shit()+"\n"


@app.route('/chat', methods=['POST'])
def rocketchat():
    rtrn_json={}
    rtrn_json['text'] = get_shit()
    resp = Response(response=json.dumps(rtrn_json), status=200, mimetype="application/json")
    return resp

# Get shit function
def get_shit():
	return random.choice(open('shitisms.txt').read().splitlines())


# Start the flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
