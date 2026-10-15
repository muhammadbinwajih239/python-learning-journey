
a = float(input("Enter 1st number: "))
operation = input("Enter operation (+, -, *, /, **, %): ")
b = float(input("Enter 2nd number: "))

if operation == "+":
    print(a+b)
elif operation == "-":
    print(a-b)
elif operation == "/":
    if b != 0:
        print(a/b)
    else:
        print("Cannot divide by zero")
elif operation == "*":
    print(a*b)
elif operation == "**":
    print(a**b)
elif operation == "%":
    print(a%b)
else:
    print("INVALID OPERATION") 
    
