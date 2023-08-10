import pyodbc 

def sqlupdate(query):
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    conn.close()

def sqlview(viewquery):
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()
    select = cur.execute(viewquery).fetchall()
    conn.close()
    return select

view1 = "SELECT * FROM company"
view2 = "SELECT * FROM salesperson"
update1 = "INSERT INTO company (company_no,company_name,tel,county,post_code) VALUES (4500,'QA','01234 567890','London','W1 1AA')"
update2 = "UPDATE company SET county='West London' WHERE county='London'"
update3 = "DELETE salesperson WHERE first_name='Inge'"

results = sqlview(view1)
print("\n*****Viewing company Table*****")
for line in results:
    print(line)

sqlupdate(update1)
sqlupdate(update2)

results = sqlview(view1)
print("\n\n*****Viewing company Table after update*****")
for line in results:
    print(line)


results = sqlview(view2)
print("\n\n*****Viewing salesperson Table*****")
for line in results:
    print(line)

sqlupdate(update3)

results = sqlview(view2)
print("\n\n*****Viewing salesperson Table after update*****")
for line in results:
    print(line)