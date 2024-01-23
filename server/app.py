#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f"<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:param>')
def print_string(param):
    print(f"{param}")
    return f"{param}"

@app.route('/count/<int:num>')
def count(num):
    numbers = f''
    # x=0
    for n in range(num):
        numbers+= f'{n}\n'
    # for numb in numbers:
    #     return numb
    return numbers
        

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, num2, operation):
    if operation == '+':
        result = num1 + num2
    elif(operation== '-'):
        result = num1 - num2
    elif(operation=='*'):
        result = num1 * num2
    elif(operation== 'div'):
        result= num1/num2
    elif(operation== '%'):
        result= num1 % num2
    else:
        return "Invalid Operation!"
    return f"{result}"



if __name__ == '__main__':
    app.run(port=5555, debug=True)
