a=int(input("Enter the number:"))
b=int(input("Enter the number2:"))
try:
    div=a/b
    print(div)
except ZeroDivisionError:
    print("Unexpected Error")
