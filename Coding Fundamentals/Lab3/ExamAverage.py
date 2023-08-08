minmark = 1
maxmark = 100
mark1 = ""
mark2 = ""
mark3 = ""

for loop in range(0,1):
    if mark1 == "":
        mark1 = int(input("Please enter Maths marks: "))
    if mark1 < minmark or mark1 > maxmark:
        print("Invalid Maths mark entered")
        mark1 = int(input("Please enter Maths marks: "))
        continue
    if mark2 == "":
        mark2 = int(input("Please enter English marks: "))
    if mark2 < minmark or mark2 > maxmark:
        print("Invalid English mark entered")
        mark2 = int(input("Please enter English marks: "))
        continue
    if mark3 == "":
        mark3 = int(input("Please enter ICT marks: "))
    if mark3 < minmark or mark3 > maxmark:
        print("Invalid ICT mark entered")
        mark3 = int(input("Please enter ICT marks: "))
        continue

averagemark = (mark1+mark2+mark3)/3

if averagemark > 65 and averagemark < 100:
    print(averagemark, 'pass')
elif averagemark < 65:
    print(averagemark, 'Fail')