def user():
    password = ("abcdef")
    count = 0
    for i in range (3):
        user_input = input("Input the password: ")
        count += 1
        if(count >= 2 and password != user_input):
            print("Retry")
        elif(password == user_input):
            print("You have successfully logged in")
            continue
        elif(count == 3 and password != user_input):
            print("You have been denied access")
            continue
        else:
            print("You are done!")
user()