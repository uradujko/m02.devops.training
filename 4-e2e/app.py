from flask import Flask, jsonify, request

app = Flask(__name__)

history_log = []

@app.route("/")
def home():
    return "Welcome to the Flask App!"


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    a, b = data["a"], data["b"]
    res = a + b
    history_log.append({"operation": "add", "a": a, "b": b, "result": res})
    return jsonify({"result": res})


@app.route("/subtract", methods=["POST"])
def subtract():
    data = request.get_json()
    a, b = data["a"], data["b"]
    res = a - b
    history_log.append({"operation": "subtract", "a": a, "b": b, "result": res})
    return jsonify({"result": res})


@app.route("/multiply", methods=["POST"])
def multiply():
    data = request.get_json()
    a, b = data["a"], data["b"]
    res = a * b
    history_log.append({"operation": "multiply", "a": a, "b": b, "result": res})
    return jsonify({"result": res})


@app.route("/divide", methods=["POST"])
def divide():
    data = request.get_json()
    a, b = data["a"], data["b"]
    if b == 0:
        return jsonify({"error": "Division by zero"}), 400
    res = a / b
    history_log.append({"operation": "divide", "a": a, "b": b, "result": res})
    return jsonify({"result": res})


@app.route("/history", methods=["GET"])
def history():
    return jsonify({"history": history_log})


if __name__ == "__main__":
    app.run(debug=True)
