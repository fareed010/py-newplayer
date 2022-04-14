




def login(password):
    if (password == "MrRobot"):
        print("Welcome to FSociety")
    else: 
        print("Wrong Password Hacker...!")

for attempt in range(0, 3):
    secret = input("Enter your password: ")
    login(secret)

    if(attempt == 2):
        print("Sorry you passed the maximum attempts, exiting...")