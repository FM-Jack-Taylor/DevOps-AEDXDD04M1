import pyodbc  

connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
conn = pyodbc.connect(connectionString)
cur = conn.cursor()

result1 = cur.execute("SELECT * FROM company WHERE county='London'").fetchall()
result2 = cur.execute("SELECT * FROM salesperson WHERE first_name LIKE 'F%'").fetchall()
result3 = cur.execute("SELECT * FROM sale WHERE order_value<'10'").fetchall()
result4 = cur.execute("SELECT * FROM salesperson WHERE county IN ('London','Surrey')").fetchall()
result5 = cur.execute("SELECT * FROM dept WHERE sales_target='5.0000'").fetchall()
result6 = cur.execute("SELECT * FROM company WHERE company_no BETWEEN 1000 AND 2000").fetchall()

print("\n*****Companys in London*****")
for line in result1:
    print(line)

print("\n*****Employees with first name starting with F*****")
for line in result2:
    print(line)

print("\n*****Sales with Values less than 10*****")
for line in result3:
    print(line)

print("\n*****Sales People in London and Surrey*****")
for line in result4:
    print(line)

print("\n*****Departments with a sales target of 5.0000*****")
for line in result5:
    print(line)

print("\n*****Companys with ID between 1000 - 2000*****")
for line in result6:
    print(line)