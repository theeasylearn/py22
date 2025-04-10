'''
1st version of the project
    Create Menu
    Add menu into loop  that stop only when user give 0 in choice
    add condition for each and every choice
    add try catch block to prevent crash of program in case of invalid input type
    
    create local module that has methods for 
      1 insert, update, delete operations
      2 to fetch data from table(s)
    
    develop insert book module 
    develop display book(s) module 
'''
import db_helper as db
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
          sql = "select * from books order by id desc"
          '''
          [
            {'id':2,'title':'abc','author':'xyz','genre':'drama','year_published':2024,'status':1},
            {'id':2,'title':'abc','author':'xyz','genre':'drama','year_published':2024,'status':1},
            {'id':2,'title':'abc','author':'xyz','genre':'drama','year_published':2024,'status':1},
          ]
          '''
          tables = db.fetch(sql)
          for row in tables:
            print(row)
            
        elif choice == 2:
          print("Enter book detail")
          title = input("Enter Title")
          author = input("Enter author")
          category = input("Enter category")
          publication_year = input("Enter publication year")
          status = int(input("Enter status (1=owned, 2 = borrowed)"))
          sql = "insert into books (title,author,genre,year_published,status) values(%s,%s,%s,%s,%s)"
          data = [title,author,category,publication_year,status]
          count = db.modify(sql,data)
          if count==1:
            print('Book added')
          else:
            print('Error occurred while inserting book')
          pause = input('press any key')
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