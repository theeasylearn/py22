'''
    write a program to display following pattern 
    *
    * *
    * * *
    * * * *
    * * * * *
'''
for row in range(1,6): #outer for loop 
    for column in range(1,row+1): #inner for loop
        print('* ',end='')
    print('')
