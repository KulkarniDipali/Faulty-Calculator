#Faulty calculator
a = int(input("a:"))
b = int(input("b:"))
c = input("operator:")
d = str(a) + c + str(b)
False_cal = {"56*5": 540, "45+19": 61, "56-18": 31}
if d in False_cal:
    print("Copied")
elif c == "+":
    print("Sum:", a + b)
elif c == "-":
    print("Sub:", a - b)
elif c == "*":
    print("Mul:", a * b)
elif c == "/":
    print("Div:", a / b)
else:
    print("Enter proper operator...")





