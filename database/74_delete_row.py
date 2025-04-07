import connection as con 
import mysql.connector as connector
id = int(input("Enter person id to delete person detail"))
sql = "delete from person where id=%s"
values = [id]
command = con.database.cursor()
command.execute(sql,values)
count = command.rowcount
if count !=0:
    print('row deleted')
else:
    print('no row found')
    
print('good bye....')
