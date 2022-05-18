import random
i = 1
guess = random.randint(1, 5)
while i <= 3:
    user = int(input("enter your guess number"))
    if guess == user:
        print("you Won")
        break
    else:
        print("you loss")
    i = i+1
