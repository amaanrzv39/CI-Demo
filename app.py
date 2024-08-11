from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

@app.route("/add", methods=['GET'])
def add():
    x = request.args.get('x', type = int)
    y = request.args.get('y', type = int)
    return jsonify({"result":x + y})

if __name__ == "__main__":
    app.run(host = "localhost")
