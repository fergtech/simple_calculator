from flask import Flask, render_template, request
import calculator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        operation = request.form.get("operation")
        num1 = float(request.form.get("num1"))
        num2 = float(request.form.get("num2"))

        if operation == "add":
            result = calculator.add(num1, num2)
        elif operation == "subtract":
            result = calculator.subtract(num1, num2)
        elif operation == "multiply":
            result = calculator.multiply(num1, num2)
        elif operation == "divide":
            result = calculator.divide(num1, num2)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
