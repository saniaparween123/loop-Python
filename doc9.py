# 9. Write a program to display all even numbers that fall between two numbers
# (exclusive both numbers) entered by the user.


user = int(input("enter start num"))
user1 = int(input("enter end num"))
while user <= user1:
    if user % 2 == 0:
        print(user, "even num")
    user = user + 1
