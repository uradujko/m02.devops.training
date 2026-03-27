from flask import Flask, jsonify, request

app = Flask(__name__)

history_log = []


def validate_input(data):
    if data is None:
        return None, None, jsonify({"error": "Invalid or missing JSON"}), 400
    if "a" not in data:
        return None, None, jsonify({"error": "Missing field: a"}), 400
    if "b" not in data:
        return None, None, jsonify({"error": "Missing field: b"}), 400
    a, b = data["a"], data["b"]
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        return None, None, jsonify({"error": "Invalid data type for field: a"}), 400
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        return None, None, jsonify({"error": "Invalid data type for field: b"}), 400
    return a, b, None, None


@app.route("/")
def home():
    return "Welcome to the Flask App!"


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/add", methods=["POST"])
def add():
    data = request.get_json(silent=True)
    a, b, err, code = validate_input(data)
    if err:
        return err, code
    res = a + b
    history_log.append({"operation": "add", "a": a, "b": b, "result": res})
    return jsonify({"result": res})


@app.route("/subtract", methods=["POST"])
def subtract():
    data = request.get_json(silent=True)
    a, b, err, code = validate_input(data)
    if err:
        return err, code
    res = a - b
    history_log.append({"operation": "subtract", "a": a, "b": b, "result": res})
    return jsonify({"result": res})


@app.route("/multiply", methods=["POST"])
def multiply():
    data = request.get_json(silent=True)
    a, b, err, code = validate_input(data)
    if err:
        return err, code
    res = a * b
    history_log.append({"operation": "multiply", "a": a, "b": b, "result": res})
    return jsonify({"result": res})


@app.route("/divide", methods=["POST"])
def divide():
    data = request.get_json(silent=True)
    a, b, err, code = validate_input(data)
    if err:
        return err, code
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
