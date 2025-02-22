'''
    write a program to display following pattern 
    1 2 1 2 1
    1 2 1 2
    1 2 1 
    1 2
    1
'''
for row in range(6,1,-1):
    for column in range(1,row):
        if column%2==0:
            print('2',end=' ')
        else:
            print('1',end=' ')
    print()
