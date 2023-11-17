from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from get_data import get_data
from soc import get_socc

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def get_all_data():
    data = get_data()
    new_data = []
    current = []
    for entry in reversed(data):
        current.append(entry["Current (A)"])
        mode = entry["Mode"]
        new_data.append(entry)
        new_data[-1]["SOCC"] = get_socc(current,mode)
    return jsonify(new_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
    
