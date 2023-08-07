age = input ("how old are you? ")
ageint = int(age)

if ageint > 18:
    print ("You are in category A")
elif ageint == 16 or ageint == 17:
    print ("You are in cataegory B")
elif ageint < 16:
    print ("You are in category C")
else:
    print ("Error - pleate input your age")