# MAGIC NUMBER


m = int(input("enter"))
a = m
s = 0
while m > 0:
    c = m % 10
    m = m//10
    s = s + c
    p = 0
    while s > 0:
        r = s % 10
        s = s//10
        p = p+r
if p == 1:
    print(a, "its magic number")
else:
    print(a, "its not a magic number")
