number1 = input ("Please input first number: ")
number2 = input ("PLease input second number: ")
operation = input ("Please select one from the menu\n Add +\n Subtract -\n multiply *\n Divide /\n Square s\n")

number1int = int(number1)
number2int = int(number2)

if operation == '+':
    print(number1int+number2int)
elif operation == '-':
    print(number1int-number2int)
elif operation == '*':
    print(number1int*number2int)
elif operation == '/':
    print(number1int/number2int)
elif operation == '**':
    print(number1int**number2int)
else:
    print('Error - Please try again')