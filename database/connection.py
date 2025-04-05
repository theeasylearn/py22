import mysql.connector as connector
try:
    database = connector.connect(host='localhost',user='root',passwd='',database='py22',port='3306')
    print('connection create.....')
except connector.Error as e:
    print('Error occured (please read detail given below)')
    print(e.errno)
    print(e.msg)
    