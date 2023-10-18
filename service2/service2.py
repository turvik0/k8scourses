import requests
from flask import Flask
app = Flask(__name__)
@app.route('/')
def getstring():
    response = requests.get("http://localhost:8080/")
    if response.status_code == 200:
        return response.text
    else:
        return "Error getting response from Hello service"
if __name__ == '__main__':
    app.run(port=8081)