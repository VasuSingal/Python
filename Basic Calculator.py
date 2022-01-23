def calculate(a,b, op):
    if op == 1:
        return a+b
    elif op == 2:
        return a-b
    elif op ==3:
        return a*b
    elif op==4:
        return a/b
    elif op ==5:
        return a**b
    else:
        return "Invalid Choice"

print("Enter: \n1 for addition\n2 for subtraction\n3 for multiplication\n4 for division\n5 for exponent function")
choice = int(input("Choice: "))

a = float(input("a: "))
b = float(input("b: "))

c = calculate(a,b,choice)
print("Output: ",c)