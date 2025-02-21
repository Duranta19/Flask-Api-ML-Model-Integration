from flask import request, Flask, jsonify

app = Flask(__name__)

@app.route('/test', methods=["GET"])
def testApp():
    return jsonify({"message": "server is working", "status": "true", "code": 200})


if __name__ == "__main__":
    app.run(debug=True, port=5050)