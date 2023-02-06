import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    record = {"Output": [[726]]}
    return jsonify(record)