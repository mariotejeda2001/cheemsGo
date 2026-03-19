from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({"succese": True, "Message":"Hello world"}), 200

if __name__ == "__name__":
    app.run(port=5001)
