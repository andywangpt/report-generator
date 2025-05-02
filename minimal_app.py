from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from minimal Flask app!"

if __name__ == '__main__':
    print("about to run the flask app...")
    app.run(debug=True, host='127.0.0.1', port=5000)