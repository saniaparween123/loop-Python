# 14. Write a program to display the number names of the digits of
# if the number is 231 then output should be Two a number entered by user,
#  for example Three One

i = int(input("enter"))
reverse = 1
while i > 0:
    reverse = (i % 10)
    i = i // 10
print(reverse)
