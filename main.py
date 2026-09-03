# drill 2
from pyscript import display, document

def greetings(e):
    username = document.getElementById('user_input').value
    document.getElementById('greeting_result').innerHTML = ""
    display(f'Good day, {username}!', target='greeting_result')


def adding_numbers(e):
    document.getElementById('result').innerHTML= ""  #clear the previous result
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    sum = first_number + second_number  #add

    display(f'The sum of {first_number} and {second_number} is {sum}', target='result')

    
def subtracting_numbers(e):
    document.getElementById('result').innerHTML= ""  #clear the previous result
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    difference = first_number - second_number  #subtract

    display(f'The difference of {first_number} and {second_number} is {difference}', target='result')

    
def multiplying_numbers(e):
    document.getElementById('result').innerHTML= ""  #clear the previous result
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    product = first_number * second_number  #multiply

    display(f'The product of {first_number} and {second_number} is {product}', target='result')

    
def dividing_numbers(e):
    document.getElementById('result').innerHTML= ""  #clear the previous result
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    quotient = first_number / second_number  #divide

    display(f'The quotient of {first_number} and {second_number} is {quotient}', target='result')


def _modulo(e):
    document.getElementById('result').innerHTML= ""  #clear the previous result
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    answer = first_number % second_number  #percentage

    display(f'The modulo of {first_number} and {second_number} is {answer}', target='result')


def floor_division(e):
    document.getElementById('result').innerHTML= ""  #clear the previous result
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    result = first_number // second_number  #floor division

    display(f'The floor division of {first_number} and {second_number} is {result}', target='result')


def exponent(e):
    document.getElementById('result').innerHTML= ""  #clear the previous result
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    result = first_number ** second_number  #exponent

    display(f'The exponent of {first_number} and {second_number} is {result}', target='result')


