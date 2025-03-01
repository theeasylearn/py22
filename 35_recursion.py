'''
    write  program to find & display binary of given decimal number 
    ---------------------------------------------------------------
    input : 05  output : 101
    input : 11  output : 1011
    input : 33  output : 100001

    steps
    1) create variable number and accept input from user 
    2) get reminder by dividing number with 2 and store it into reminder 
    3) print reminder 
    4) floor division number with 2
    5) repeat step 2 to 4 until number become 0
'''
def getBinary(number):
    if number>0:
        reminder = number % 2
        number = number // 2
        getBinary(number)
        print(reminder,end=' ')
number = int(input("Enter number to get it's binary"))
getBinary(number)

