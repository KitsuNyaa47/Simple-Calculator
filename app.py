from flask import Flask, render_template, request

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def exponent(x, y):
    return x ** y

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def calculator():
    result = None

    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            if operation == "+":
                result = round(add(num1, num2), 2)

            elif operation == "-":
                result = round(subtract(num1, num2), 2)

            elif operation == "x":
                result = round(multiply(num1, num2), 2)

            elif operation == "/":
                result = round(divide(num1, num2), 2)

            elif operation == "^":
                result = round(exponent(num1, num2), 2)

        except ValueError:
            result = "Invalid input"
        except ZeroDivisionError:
            result = "Can't divide by zero!"

    return render_template("calculator.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
