print("Welcome to the Pythagoras Calculator!!!")
operation = input ("please select an option\n 1. Find the length of A given B and C\n 2. Find the length of B given A and C\n 3. Find the length of C given A and B\n")
operationint = int(operation)

if operationint == 1:
    b = input ("input b: ")
    c = input ("input c: ")
    bint = int(b)
    cint = int(c)
    print((cint**2-bint**2)**0.5)
elif operationint == 2:
    a = input ("input a: ")
    c = input ("input c: ")
    aint = int(a)
    cint = int(c)
    print((cint**2-aint**2)**0.5)
elif operationint == 3:
    a = input ("input a: ")
    b = input ("input b: ")
    bint = int(b)
    aint = int(a)
    print((aint**2+bint**2)**0.5)
else:
    print("Error")