a = int(input("enter the first num "))
operator = input("operator(+,-,*,/,%) ")
b = int(input("enter the second num "))
if operator == "+":
    print(a+b)
elif operator == "-":
    print(a-b)
elif operator == "*":
    print(a*b)
elif operator == "/":
    print(a/b)
elif operator == "%":
    print(a%b)
else:
    print("u have enter wroung choice")