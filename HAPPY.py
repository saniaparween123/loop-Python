# HAPPY NUMBER


h = int(input("enter"))
a = h
s = 0
while h > 0:
    t = h % 10
    h = h//10
    c = t**2
    s = s + c
    p = 0
    while s > 0:
        u = s % 10
        s = s//10
        r = u**2
        p = p+r
if p == 1:
    print(a, "its happy number")
else:
    print(a, "its not a happy number")
