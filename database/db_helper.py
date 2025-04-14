'''
    module to work upon mysql database 
'''
import connection as con 
import mysql.connector as connector
# modify function will be used to execute insert,update,delete sql command
def modify(sql,data):
    try:
        #create cursor type object
        command = con.database.cursor();
        print(sql)
        print(data)
        #exceute sql command
        command.execute(sql,data)
        #save changes into database
        con.database.commit()
        
        count = command.rowcount
        return count
    except connector.Error as e:
        print('Error occurred (please read detail given below)')
        print(e.errno)
        print(e.msg) 
        return -1

def fetch(sql,data=None):
    try:
        command = con.database.cursor(dictionary=True);
        print(sql)
        if data!=None:
            print(data)
            command.execute(sql,data)    
        else:
            command.execute(sql)
        return command.fetchall()
    except connector.Error as e:
        print('Error occurred (please read detail given below)')
        print(e.errno)
        print(e.msg) 
        return None