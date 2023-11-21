from flask import Flask, request, jsonify, render_template, g
from database import get_cycle_db, get_instant_db
from flask_cors import CORS 
import sqlite3

app = Flask(__name__)
CORS(app)

DATABASE = 'lion_dataset.db'  

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
    return g.db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'db'):
        g.db.close()

@app.route('/', methods=['GET'])
def serve_index():
    return render_template('index.html')

@app.route('/api/instant_data', methods=['GET'])
def get_instant_data():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM instant_data")
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)

@app.route('/api/cycle_data', methods=['GET'])
def get_cycle_data():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM cycle_data")
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)

@app.route('/api/state', methods=['GET'])
def get_status():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM status")
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)

@app.route('/api/status', methods=['POST'])
def status_control():
    try:
        res = request.json
        status = "Charging" if res['status'] else "Discharging"
        msg = "1" if res['status'] else "0"

        print("status change request recieved")
        print("status changed to ", status )


        return jsonify({"message": "Data added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        db = get_db()
        cursor = db.cursor()
        # cursor.execute("SELECT * FROM status")
        cursor.execute('''
                UPDATE status
                SET status = ?
                WHERE id = 1
            ''', (msg))

        db.commit()
        cursor.close()
    

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
