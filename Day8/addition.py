def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    # if b==0:
    #     raise ValueError("Cannot divide by zero")
    return a/b

def main():
    print("-----------simple Calculator-----------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice (1-4): "))
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if(choice==1):
        print("Addition of two numbers is: ",add(num1,num2))
    elif choice==2:
        print("Subtraction of two numbers is: ",subtract(num1,num2))
    elif choice==3:
        print("Multiplication of two numbers is: ",multiply(num1,num2))
    elif choice==4:
        print("Division of two numbers is: ",divide(num1,num2))
    else:
        print("Invalid choice. Please select a valid option.")

    if __name__ == "__main__":
        main()