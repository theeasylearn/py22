import connection as con 
import mysql.connector as connector
print("Insert new row into person table")
print("Enter person Detail")
while 1==1:
    try:
        name = input("Enter name")
        age = int(input("Enter age"))
        gender = int(input('enter gender (1 = male, 0 = female)'))

        #create cursor 
        command = con.database.cursor();

        #create sql statement 
        sql = "insert into person (name,age,gender) values (%s,%s,%s)";
        #create list of size of 3 
        values = [name,age,gender]
        command.execute(sql,values)
        con.database.commit()
        print('row inserted')
        break
    except connector.Error as e:
        print('Error occurred (please read detail given below)')
        print(e.errno)
        print(e.msg)
        break
    except ValueError as e:
        print('Error occurred (invalid input)')

print("Good bye...")