from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)

# Allow CORS for specific origin
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

# Load the CSV file
def load_csv(file_path):
    try:
        df = pd.read_csv(file_path)  # Read the CSV file
        return df
    except Exception as e:
        return str(e)

# Endpoint to get all data
@app.route('/data', methods=['GET'])
def get_data():
    try:
        df = load_csv('file.csv')  # Path to your CSV file
        if isinstance(df, str):  # Handle error string
            raise ValueError(df)
        data = df.to_dict(orient='records')  # Convert DataFrame to list of dictionaries
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return HTTP 500 for server errors

if __name__ == '__main__':
    app.run(debug=True)
