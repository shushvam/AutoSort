# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import os
from collections import defaultdict
import re
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/ping', methods=['GET'])
@cross_origin()
def pong():
    return 'pong'

@app.route('/sortedText', methods=['POST'])
@cross_origin()
def sortedText():
    print(request)
    s = request.json.get('text', '')
    s = re.split(",(?=(?:[^']*\'[^']*\')*[^']*$)",s)
    d = defaultdict(list)
    for i in range(len(s)):
        d[i // 3].append(s[i])

    res = sorted(d.items(), key=lambda e: int(e[1][2]), reverse=True)
    i = 0
    ans = defaultdict()
    while i < len(res):
        ans[i] = ','.join(map(str, res[i][1]))
        ans[i] = ans[i].replace('\r\n', ' ')
        i += 1
    
    return json.dumps(ans, indent = 4)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))