from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('FireExtinguisherDB.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/retrieve', methods=['POST'])
def retrieve():
    id = request.json['id']
    conn = get_db_connection()
    extinguisher = conn.execute('SELECT * FROM info WHERE Id = ?', (id,)).fetchone()
    conn.close()
    if extinguisher:
        result = dict(extinguisher)
        return jsonify(result)
    else:
        return jsonify({"message": "No data found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
