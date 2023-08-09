def getincometax(salary):
    if salary > 11850:
        posttax = salary - 11850
        if posttax < 34500:
            taxedamount = 20/100*posttax
            return taxedamount
        if posttax > 34501 and posttax < 150000:
            taxedamount = 40/100*posttax
            return taxedamount
        if posttax > 150000:
            taxedamount = 45/100*posttax
            return taxedamount


salary = int(input("Please enter you salary: "))
taxedamount = getincometax(salary)
print(taxedamount)