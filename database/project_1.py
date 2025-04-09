'''
1st version of the project
    Create Menu
    Add menu into loop  that stop only when user give 0 in choice
    add condition for each and every choice
    add try catch block to prevent crash of program in case of invalid input type
'''
while 1:
    try:
        print("Press 1 to view all books")
        print("Press 2 to add new book")
        print("Press 3 to update book")
        print("Press 4 to delete book")
        print("Press 5 to search book by title")
        print("Press 6 to search book by author")
        print("Press 7 to update book status")
        print("Press 0 to exit")
        choice = int(input("Enter your choice"))
        if choice == 0:
            print("Good bye")
            break
        elif choice == 1:
          print('we will display all book')
        elif choice == 2:
          print('we will insert book')
        elif choice == 3:
          print('we will update book')
        elif choice == 4:
         print('we will delete book')
        elif choice == 5:
         print('we will search book by title')
        elif choice == 6:
         print('we will search book by author')
        elif choice == 7:
         print('we will update book status')
        else:
         print('invalid choice')
    except ValueError as error:
        print("only number between (0 to 7) are allowed")