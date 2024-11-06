def create_account ():
    print("Create account")
    email=input("Please enter your email address: ")
    password=input("Please enter a secure password: ")


def login_account():
    print("Login to your account")
    entered_email=input("Please enter your email address: ")
    entered_password=input("Please enter your password: ")


def validate_login(email,password,entered_email,entered_password):
    while entered_email!=email or entered_password!=password:
        print("Wrong email address or password. Try again")
        entered_email=input("Please enter your email address: ")
        entered_password=input("Please enter your password: ")
    else:
        print("Welcome")