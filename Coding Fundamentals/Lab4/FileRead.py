carsale = open('C:/Users/Admin/source/repos/FM-Jack-Taylor/DevOps-AEDXDD04M1/Coding Fundamentals/Lab4/carSale.csv', "r")
#carsale = str(carsale.read())
#print(carsale)

companies = []
sales = [[],[],[],[],[],[],[],[]]


rows = carsale.readlines()
#row1 = rows[0].split(",")
#companies.append(row1[0])

line = 0
for lines in rows:
    row1 = rows[line].split(",")
    companies.append(row1[0])
    line = line + 1
#print(companies)

line = 0
for lines in rows:
    row1 = rows[line].split(",")
    sales[0].append(row1[1])
    sales[1].append(row1[2])
    sales[2].append(row1[3])
    sales[3].append(row1[4])
    sales[4].append(row1[5])
    sales[5].append(row1[6])
    sales[6].append(row1[7])
    line = line + 1
#print(sales)


line = 1
for colum in sales:
    print(colum)
    colum1 = (colum[1:6])
    map1 = map(int, colum1)
    colum2 = list(map1)
    print(colum2)
    input()
    columsum = sum(colum2)
    print (columsum)
    line = line + 1

input

