import random
random_number = random.randint(1,50)

while True:
    num = int(input("enter a number: "))
    if num>random_number:
        print("Too high")
    elif num < random_number:
        print("Too small")
    else:
        print("you win")
        break