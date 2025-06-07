from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["POST"])
def sum_numbers():
    a = int(request.form["num1"])
    b = int(request.form["num2"])
    return f"Sum: {a + b}"

app.run()
