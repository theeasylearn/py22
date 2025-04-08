import connection as con 
person_id = int(input("Enter person id to update detail"))


name = input("Enter name")
age = int(input("Enter age"))
gender = int(input('enter gender (1 = male, 0 = female)'))

#create cursor type oboject 
command = con.database.cursor()

#create sql variable to store sql command 
sql = "update person set name=%s,gender=%s,age=%s where id=%s"

#as there are four placeholder (%s) in sql command one has to create list of 4
values = [name,gender,age,person_id]

#run sql command using command 
command.execute(sql,values)

#save changes
con.database.commit()

#check how many rows has been effected
count = command.rowcount
if count>=1:
    print(f"{count} rows has been updated")
else:
    print("no row has been updated")