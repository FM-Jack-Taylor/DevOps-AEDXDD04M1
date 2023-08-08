initial = int(input ("Enter initial investment: "))
target = int(input("Enter target value: "))
intrest = float(input ("Enter intrest rate: ")) /100
intrest = (intrest+1)
year = 0
while initial < target:
    year = year + 1
    initial = initial * intrest
    if initial > target:
        print(year)
        break

