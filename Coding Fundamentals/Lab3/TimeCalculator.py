userop = int(input ("Please select an option\n1. Add 2 times\n2. Find the difference between 2 times\n3. Convert to Hours\n4. Convert to Minutes\n.5 Convert Minutes to Time\n6. Convert Hours to Time\n7. Convert Days to Time\n8. Exit"))
if userop == 1:
    time1 = str(input ("please enter time DD:HH:MM: "))
    time2 = str(input ("please enter time DD:HH:MM: "))
    time1 = time1.split()
    time2 = time2.split()
    min1 = int(time1[2])
    hour1 = int(time1[1])
    day1 = int(time1[0])
    min2 = int(time2[2])
    hour2 = int(time2[1])
    day2 = int(time2[0])
    totalmin = min1+min2
    totalhour = hour1+hour2
    totalday = day1+day2

    while totalmin > 60:
        totalhour = totalhour + 1
        totalmin = totalmin - 60

    while totalhour > 24:
        totalday = totalday + 1
        totalhour = totalhour - 24

    if totalhour < 9 and totalmin < 9:
        print(f"{totalday}:0{totalhour}:0{totalmin}")
        input
    if totalhour > 9 and totalmin > 9:
        print(f"{totalday}:{totalhour}:{totalmin}")
        input

if userop == 2:
    time1 = str(input ("please enter time DD:HH:MM: "))
    time2 = str(input ("please enter time DD:HH:MM: "))
if userop == 3:
    time1 = str(input ("please enter time DD: "))

if userop == 4:
    time1 = str(input ("please enter time HH: "))
if userop == 5:
    time1 = str(input ("please enter time MM: "))
if userop == 6:
    time1 = str(input ("please enter time HH: "))
if userop == 7:
    time1 = str(input ("please enter time DD: "))
if userop == 8:
    exit
