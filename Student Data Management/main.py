#Menu-driven program to demonstrate Student Data Management
#performed on a table through MySQL-Python connectivity

import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(host="localhost", user="root", password="mysql")

# Create a cursor
cursor = db.cursor()

# If the database does not exist, create it
mydb = "CREATE DATABASE IF NOT EXISTS school"
cursor.execute(mydb)

def menu():
    c = 'y'
    print("Welcome to Student Data Management")
    while (c == 'y'):
        print("\n1. Add a record.")
        print("2. Update a record.")
        print("3. Delete a record.")
        print("4. Display records.")
        print("5. Exiting\n")
        choice=int(input("Enter your choice: "))
        if choice == 1:
            adddata()
        elif choice == 2:
            updatedata()
        elif choice == 3:
            deldata()
        elif choice == 4:
            fetchdata()
        elif choice == 5:
            print("Exiting")
            break
    else:
        print("wrong input")

def fetchdata():
    import mysql.connector
    try:
        db = mysql.connector.connect(host="localhost",user="root",password='mysql',database='school')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM student" )
        results = cursor.fetchall()
        print("Name  |  Roll No  |  Branch\n")
        for x in results:
            print(x)
    except:
        print ("Error: unable to fetch data")
        
def adddata():
    import mysql.connector
    db = mysql.connector.connect(host='localhost',user='root',password='mysql',database='school')
    cursor = db.cursor()
    table = "CREATE TABLE IF NOT EXISTS student (name VARCHAR(30), rollno INT, branch VARCHAR(30))"
    cursor.execute(table)
    name = input("\nEnter the name of the student :")
    roll = int(input("\nEnter the Roll No. :"))
    branch = input("\nEnter the branch :")
    query = "INSERT INTO student (name, rollno, branch) VALUES (%s, %s, %s)"
    values = (name, roll, branch)
    cursor.execute(query, values)
    db.commit()
    print("\nRecords added\n") 
        

def updatedata():
    import mysql.connector
    try:
        db = mysql.connector.connect(host="localhost",user="root",password='mysql',database='school')
        cursor = db.cursor()
        name = input("Enter the student name (update):")
        field = input("Which data you want to update? :")
        value = input("Enter new data :")
        sql = f"UPDATE student SET {field} = '{value}' WHERE name = '{name}'"
        cursor.execute(sql)
        print("\nRecord Updated\n")
        db.commit()
    except Exception as e:
        print (e)
        
def deldata():
    import mysql.connector
    db = mysql.connector.connect(host="localhost",user="root",password='mysql',database='school')
    cursor = db.cursor()
    name = input("Enter the student name (delete):")
    sql = f"delete from student where name='{name}'"
    cursor.execute(sql)
    print("\nRecord Deleted\n")
    db.commit()
    
menu()
