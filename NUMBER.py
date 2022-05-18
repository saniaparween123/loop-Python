n = int(input("enter"))
i = 1
p = ""
while i <= n:
    r = n % 10
    n = n // 10
    p = p+str(r)
    s = int(p)
while s > 0:
    k = s % 10
    s = s//10
    if k == 0:
        print("zero", end=" ")
    if k == 1:
        print("one", end=" ")
    if k == 2:
        print("two", end=" ")
    if k == 3:
        print("three ", end=" ")
    if k == 4:
        print("four ", end=" ")
    if k == 5:
        print("five ", end=" ")
    if k == 6:
        print("six ", end=" ")
    if k == 7:
        print("seven", end=" ")
    if k == 8:
        print("eight", end=" ")
    if k == 9:
        print("nine", end=" ")
