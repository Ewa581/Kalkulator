"""
This module implements a simple calculator web app using Flask.
It provides functionality for basic arithmetic operations.
The app accepts input via GET requests and returns the result in JSON format.
"""
from flask import Flask, request, jsonify
app = Flask(__name__)

# HTML template for the home page
HOME_PAGE = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculator</title>
</head>
<body>
    <h1>Welcome to the Calculator!</h1>
    <form action="/calculate" method="get">
        <label for="arg1">First Number:</label>
        <input type="number" id="arg1" name="arg1" required><br><br>
        <label for="arg2">Second Number:</label>
        <input type="number" id="arg2" name="arg2" required><br><br>
        <label for="op">Operation:</label>
        <select id="op" name="op">
            <option value="sum">Addition</option>
            <option value="subtract">Subtraction</option>
            <option value="multiply">Multiplication</option>
            <option value="divide">Division</option>
        </select><br><br>
        <button type="submit">Calculate</button>
    </form>
</body>
</html>
'''
@app.route('/')
def home():
    """
    Renders the home page with the HTML form for the calculator.
    """
    return HOME_PAGE

@app.route('/calculate')
def calculate():
    """
    Performs the arithmetic operation based on the user's input and returns the result.
    The supported operations are: addition, subtraction, multiplication, and division.
    Returns the result as a JSON response.
    """

    op = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)

    if op is None or arg1 is None or arg2 is None:
        return jsonify({"error": "Invalid input parameters"}), 400

    if op == 'sum':
        result = arg1 + arg2
    elif op == 'subtract':
        result = arg1 - arg2
    elif op == 'multiply':
        result = arg1 * arg2
    elif op == 'divide':
        if arg2 == 0:
            return jsonify({"error": "Division by zero is not allowed"}), 400
        result = arg1 / arg2
    else:
        return jsonify({"error": "Unsupported operation"}), 400

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
