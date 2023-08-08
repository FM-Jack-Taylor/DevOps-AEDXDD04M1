userinput = int(input ("Please input a number: "))
oguserinput = userinput
while userinput > 0:
	userinput = userinput - 1
	oguserinput = (oguserinput*userinput)
	if userinput == 1:
		print (oguserinput)
	