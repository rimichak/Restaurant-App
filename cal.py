def add(a , b):
    return a + b
def sub(a , b):
    return a - b
def mul(a , b):
    return a * b
def div(a , b):
    return a / b
print(" select your operations:\n",
"1. Add\n", "2. Subtract\n", "3. Multiplication\n", "4. Division\n")
operations = int(input("Enter your operation number:"))
a, b = map(int, (input("Enter your number:")).split())
if operations == 1:
    print("Addition:", add(a, b))
elif operations == 2:
    print("Subtraction:", sub(a,b))
elif operations == 3:
    print("multiplication:", mul(a,b))
elif operations == 4:
    print("Division:", div(a,b))
else:
    print("invalid operations")


