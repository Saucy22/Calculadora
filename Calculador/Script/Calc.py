import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

ver = "1.0"

print("Welcome to calculador",ver)
print("Choose an operation: + - / *")
op = input()
if op == "+":
    print("Addition selected, First Number:")
    x = input()
    print("Second Number:")
    y = input()
    cls()
    print(x,"+",y,"=")
    print(float(x) + float(y))

if op == "-":
    print("Subtraction selected, First Number:")
    x = input()
    print("Second Number:")
    y = input()
    cls()
    print(x,"-",y,"=")
    print(float(x) - float(y))

if op == "*":
    print("Multiplication selected, First Number:")
    x = input()
    print("Second Number:")
    y = input()
    cls()
    print(x,"*",y,"=")
    print(float(x) * float(y))

if op == "/":
    print("Division selected, First Number:")
    x = input()
    print("Second Number:")
    y = input()
    cls()
    print(x,"/",y,"=")
    print(float(x) / float(y))
    print("Done!")

else:
    print("Done!")