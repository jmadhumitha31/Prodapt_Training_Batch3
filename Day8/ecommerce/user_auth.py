class UserAuth:
    def __init__(self):
        self.users={"admin":"admin123"}
    

    def register(self,username,password):
        if username in self.users: 
            return False
        self.users[username]=password
        return True


    def login(self,username,password):
        return self.users[username] == password

    def display_users(self):
        print("Registered users:")
        print(self.users)

print("UserAuth class defined sucessfully")
print("1. Register")
print("2. Login")   
print("3. Display Users")
print("4. Exit")


username=input("Enter username: ")
password=input("Enter password: ")
choice=input("Enter your choice")



if choice =="1":
    auth=UserAuth()
    if auth.register(username,password):
        print("User registered successfully")
    else:
        