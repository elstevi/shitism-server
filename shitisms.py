from flask import Flask,Response
import json
import random

app = Flask(__name__)

# Simple output if people come in the web browser. Don't even send a header.
@app.route('/', defaults={'type': "shitism"})
@app.route('/<type>')
def http(type):
    return get_shit(type)

# CLI is pretty well the same, except has a newline
@app.route('/cli', defaults={'type': "shitism"})
@app.route('/cli/<type>')
def cli(type):
    return get_shit(type)+"\n"


@app.route('/chat', methods=['POST'], defaults={'type': "shitism"})
@app.route('/chat/<type>', methods=['POST'])
def rocketchat(type):
    rtrn_json={}
    rtrn_json['text'] = get_shit(type)
    resp = Response(response=json.dumps(rtrn_json), status=200, mimetype="application/json")
    return resp

# Get shit function
def get_shit(type):
    if (type == "rickyism"):
	return random.choice(open('rickyisms.txt').read().splitlines())
    elif (type == "bofh"):
	return random.choice(open('bofh.txt').read().splitlines())
    else:
	return random.choice(open('shitisms.txt').read().splitlines())


# Start the flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
