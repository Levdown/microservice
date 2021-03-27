from flask import Flask
import requests

PORT = "8080"
app = Flask(__name__)

@app.route('/myapi/<name>')
def get_data(name):
    req_api = requests.get(f'http://127.0.0.1:8000/api/{name}')
    req_db = requests.get(f'http://127.0.0.1:5000/api/info/{name}').text
    return req_db

app.run(port=PORT)
