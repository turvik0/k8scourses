from flask import Flask
app = Flask(__name__)
@app.route('/')
def returnstring():
    return "hi i am the message"
if __name__ == '__main__':
    app.run(port=8080)