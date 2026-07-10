bal=5000
amt=int(input("Enter the amt"))
if amt <= bal and amt %100 ==0:
    bal-=amt
    print("Withdrawal success")
    print(f"Remaining balance:{bal}")
else:
    print("Invalid withdrawal amount or insuffient funds.")