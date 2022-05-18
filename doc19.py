# 19. Write a program to add first n terms of the following series using a
# while loop :

# 1/1! + 1/2! + 1/3! + …….. + 1/n!


i = 1
while i <= 10:
    print("1/"+str(i)+"! +", end=" ")
    i = i + 1
