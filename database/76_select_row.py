import connection as con 
#create cursor 
command = con.database.cursor(dictionary=True)

#create sql command 
sql = "select * from person order by name"

#run sql command 
command.execute(sql)

#fetch all rows 
table = command.fetchall()
print("Id   Name    Age     Gender")
for row in table:
    
    if row['gender'] == 1:
        temp = "Male"
    else:
        temp = "Female"
    output = str(row['id']) + " " + row['name'] + " " + str(row['age']) + " " + temp
    print(output)
    
