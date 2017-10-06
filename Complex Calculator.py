from math import sqrt

# No doubt the most over-complicated calcuator you will see in all of coding
# By: Tejas Shah

class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

    def exponent(self):
        return self.num1 ** self.num2

    def modulo(self):
        return self.num1 % self.num2

    def squareroot(self):
        return sqrt(num1)

    def answer_to_life(self):
        return "42"

num10 = raw_input("What's the first number? ")
while not num10.isdigit():
    num10 = raw_input("That's not a number! What is your first number! ")
num1 = int(num10)
print ""
num20 = raw_input("What's the second number? ")
while not num20.isdigit():
    num20 = raw_input("That's not a number! What is your first number! ")
num2 = int(num20)
print ""
print "What would you like the calculator to do? Available answers: 'add', '+', 'subtract', '-', 'multiply', '*', 'divide', '/', "
print "'exponent', '^', 'modulo', '%', 'square root', or 'answer to life'. "
operation = raw_input()
available = ['add', '+', 'subtract', '-', 'multiply', '*', 'divide', '/', 'exponent', '^', 'modulo', '%', 'square root', 'answer to life']

while not operation in available:
    operation = raw_input("That is not a valid operation. Please try again. ")

calculate = Calculator(num1, num2)

if operation.lower() == 'add' or operation.lower() == '+':
    answer = calculate.add()
elif operation.lower() == 'subtract' or operation.lower() == '-':
    answer = calculate.subtract()
elif operation.lower() == 'multiply' or operation.lower() == '*':
    answer = calculate.multiply()
elif operation.lower() == 'divide' or operation.lower() == '/':
    answer = calculate.divide()
elif operation.lower() == 'exponent' or operation.lower() == '^':
    answer = calculate.exponent()
elif operation.lower() == 'modulo' or operation.lower() == '%':
    answer = calculate.modulo()
elif operation.lower() == 'square root':
    answer = calculate.squareroot()
else:
    answer = calculate.answer_to_life()

print "Here's your answer: ", answer
