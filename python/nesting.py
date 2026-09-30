username = input("Enter your username: ")
password = input("Enter your password: ")

if (username == "admin" and password == "admin123"):
    print("welcome sir")

else:
    if(username != "admin"):
        print("invalid username")
    else:
        print("invalid password")
        