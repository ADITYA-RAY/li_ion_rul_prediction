from flask import Flask, request, jsonify, render_template
from database import get_cycle_db, get_instant_db
from flask_cors import CORS 



app = Flask(__name__)
CORS(app)

cycle_db = get_cycle_db()
instant_db = get_instant_db()

@app.route('/', methods=['GET'])
def serve_index():
    return render_template('index.html')

@app.route('/api/instant_data', methods=['GET'])
def get_instant_data():
    return jsonify(instant_db)

@app.route('/api/cycle_data', methods=['GET'])
def get_cycle_data():
    return jsonify(cycle_db)

@app.route('/api/data', methods=['POST'])
def status_control():
    try:
        new_data = request.json
        data_store.append(new_data)

        return jsonify({"message": "Data added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
