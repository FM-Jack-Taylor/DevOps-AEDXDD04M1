import pyodbc  

def sqlupdate(query):
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    conn.close()

def sqlinsert(insert):
    for row in insert:
        connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
        conn = pyodbc.connect(connectionString)
        cur = conn.cursor()
        cur.execute(row)
        conn.commit()
        conn.close()

def sqlview(viewquery):
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()
    select = cur.execute(viewquery).fetchall()
    conn.close()
    return select


drop = "DROP TABLE Student"
create = "CREATE TABLE Student (StudentID int NOT NULL, FirstName nvarchar(40) NOT NULL, Surname nvarchar(30) NULL, Course nvarchar(30) NULL, City nvarchar(15) NULL)"
view = "SELECT * from Student"
insert = ["INSERT INTO Student (StudentID,FirstName,Surname,Course,City) VALUES (1977,'Anakin','Skywalker','Sports Nutrition','London')"
          "INSERT INTO Student (StudentID,FirstName,Surname,Course,City) VALUES (1978,'Obi-Wan','Kenobi','Coding Masterclass','London')"
          "INSERT INTO Student (StudentID,FirstName,Surname,Course,City) VALUES (1979,'Wilhuff','Tarkin','Complete Stock Trading','Manchester')"
          "INSERT INTO Student (StudentID,FirstName,Surname,Course,City) VALUES (1980,'Saw','Gerrera','Music Production','Scotland')"
          "INSERT INTO Student (StudentID,FirstName,Surname,Course,City) VALUES (1981,'Ahsoka','Tano','Web Design','Irland')"]
update = "UPDATE Student SET City='Scotland' WHERE FirstName='Obi-Wan' AND Surname='Kenobi'"

print("Dropping Student Table")
sqlupdate(drop)
print("Creating Student Table")
sqlupdate(create)
print("Inserting Table Data")
sqlinsert(insert)

results = sqlview(view)
print("\n*****Viewing Student Table*****")
for line in results:
    print(line)

print("\nObi-Wan has moved from London to Scotland updating table")
sqlupdate(update)

results = sqlview(view)
print("\n*****Viewing Student Table*****")
for line in results:
    print(line)