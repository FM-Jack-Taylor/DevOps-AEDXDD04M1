min = 0
max = 101
attempt = 0
var = False
while var == False:
    userinput = int(input ("Please enter a number between 1 and 100: "))
    attempt = attempt + 1
    if attempt == 3:
        print("None")
        break
    elif userinput > min and userinput < max:
        print(userinput)
        break
