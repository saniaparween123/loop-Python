# 12345
#  1234
#   123
#    12
#     1

i = 5
k = 0
while i >= 1:
    j = 1
    while j <= i:
        if j == 1:
            r = " "*k
            print(r, j, end="")
        else:
            print(j, end="")
        j = j+1
    k = k+1
    i = i-1
    print()
