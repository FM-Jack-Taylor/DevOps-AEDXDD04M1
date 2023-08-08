ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,7,9,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

#Part1
print ("Length of age list: ",len(ages))

#Part2
for agelist in ages:
   print("Full age list: ",agelist)

#Part3
listlocation = 0
for agelist in ages:
    ages[listlocation]+=1
    print("Full age list with +1 added to all ages: ",ages[listlocation])
    listlocation = listlocation + 1

#Part4
ages1665 = []
for agelist in ages:
    if agelist > 16 and agelist < 65:
        ages1665.append(agelist)
print("Ages between 16 to 65: ",ages1665)

#Part5
agesort = []
for agelist in ages1665:
    if agelist > 16 and agelist < 25:
        agesort.append(agelist)
        agesort.sort(reverse=False)

#Part6
print("Ages between 16-25: ",agelist)

#Part7
print("Sorted ages: ",agesort)

#Part8
print("How many ages fall between 16-25? ",len(agesort))