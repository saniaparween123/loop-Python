# HCF


a = int(input("enter"))
b = int(input("enter"))
i = 1
while i <= a:
    if a % i == 0 and b % i == 0:
        hcf = i
    i = i+1
print(hcf)
