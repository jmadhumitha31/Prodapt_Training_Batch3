no=list(map(int, input("Enter a list of integers seperated by spaces").split()))

#even
even_no=list(filter(lambda x:x%2==0,no))
square_even_no = list(map(lambda x: x ** 2, even_no))

print("Squared even numbers:",square_even_no)