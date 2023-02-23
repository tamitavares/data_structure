# Simple calculator

print("Enter 2 numbers to make te account")
a = float(input("Number 1: "))
b = float(input("Number 2: "))
op = input("Operator: ")

if op == '+':
    c = a+b
elif op == '-':
    c = a-b
elif op == '*':
    c = a*b
elif op == '/':
    c = a/b
else:
    c='Error'

print('Result: ', c)