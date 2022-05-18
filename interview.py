# 1
# 12
# 358
# 1347
# 1123
# 58134

i = 1
a = 0
b = 1
print(b)
while i <= 4:
    j = 0
    while j <= i:
        c = a + b
        a = b
        b = c
        if c == 13:
            print(1, 3, end=" ")
            a = 1
            b = 3
        else:
            if c == 11:
                print("\n1 1 2 3", end="")
                a = 2
                b = 3
            else:
                print(c, end=" ")
        j = j+1
    i = i+1
    print()
