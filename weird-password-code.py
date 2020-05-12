def password():
    passwords = ["password"]
    print("The password is " + passwords[0])
    while True:
        x = input("What is the password? ")
        if x in passwords or x = "":
            print("I am sorry, but that is not a correct password")
        else:
            passwords.append(x)
            print("Enter the password again for verification.")
