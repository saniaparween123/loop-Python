i = 1
while i <= 5:
    guess = int(input("enter"))
    if guess == 5:
        print("you win the game")
        break
    i = i + 1
    print("you loss")
