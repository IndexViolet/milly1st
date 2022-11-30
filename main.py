print("hello world")


question = input("which question would you like? 10 / 11 / 12 /13 ")
if question == "11":
    direction = input("up or down ")

    if direction == "down":
        number = int(input("enter a number below 20 "))
        if number < 20:
            for i in range(21, number, -1):
                print(i-1)
        else:
            number = int(input("enter a number below 20 "))

    if direction == "up":
        number = int(input("enter the number you will count to. "))
        for i in range(number):
            print(i+1)
    else:
        print("I don't understand")


if question == "10":
    name = input("what's your name? ")
    number = int(input("enter a number! "))
    if number < 10:
        for i in range(number):
            print(name)

    else:
        for i in range(3):
            print("too high")

if question == "12":
    count = 0
    names = []
    invite = "yes"

    while invite == "yes":
        name = input("who would you like to invite? ")
        names.append(name)
        print(f"{name} has now been invited! ")
        invite = input("would you like to invite anyone else? ")
    print(f"{len(names)} have been invited")
    print(names)

if question == "13":
    while True:
        try:
            value=int(input("whats your number bro? "))

        except ValueError:
            print(f"That wasn't even a number! bro! Please enter a valid number")
        
        else:
            if (value in range(1,6)):
                print(f"Yey numbers I like include: {value}")
                break
            else:
                print(f"{value} isn't valid, please try again. ")


