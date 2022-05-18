# Question 8

# 1
# Now, we will change the previous game a little. We only checked whether the
#  number given by the user is equal to the input number or not.

# 2
# Now, we will also tell the user if the number given by the user is greater
#  or smaller than the input number.

# 3
# If the user gives 4 as a number then we will check if 4 is less than 5 or
#  not so it's true then we will print "Number entered by you entered is small,
# try one more time ".

# 4
# We will again take input from the user. If the user gives 7as a number then
# we will check if 7 is less than 5 or not so it is False then we will print
#  "Number entered by you entered is greater, try one more time ".

# 5
# If the user gives 5 as input then this number is equal to the given number
# then we will print "Wow you guessed the correct number".


i = 1
while i <= 5:
    guess = int(input("enter"))
    if guess > 5:
        print("no its wrong guess", guess, "is greter than 5")
    elif guess < 5:
        print("no", guess, "is lesser than 5")
    elif guess == 5:
        print("5 is correct guess You are the winner")
        break
    print("You loss", i, "chance")
    i = i + 1
