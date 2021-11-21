import sys
from joblib import load
from flask import Flask, request, jsonify, render_template, abort


try:
    model = load("model.joblib")  # deserialize model from file
except FileNotFoundError:
    print("Model file not found")
    sys.exit()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/rest_api", methods=["POST", "GET"])
def results():
    try:
        if request.method == "GET":
            height = float(request.args.get("height"))
            weight = float(request.args.get("weight"))
        elif request.method == "POST":
            data = request.get_json(force=True)
            height = float(data["height"])
            weight = float(data["weight"])
    except Exception:
        abort(400, "Invalid or incomplete parameter")
    try:
        prediction = model.predict([[height, weight]])
    except Exception:
        abort(400, "Invalid or incomplete parameter")
    else:
        output = prediction[0]
        return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
