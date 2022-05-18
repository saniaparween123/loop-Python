#    *
# *     *
#    *


r = 1
while r <= 3:
    c = 1
    while c <= 3:
        if ((r == 1 and c == 2) or (r == 2 and (c == 1 or c == 3))
                or (r == 3 and c == 2)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
        c = c+1
    r = r+1
    print()
