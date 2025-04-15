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
def getInput():
  title = input("Enter Title")
  author = input("Enter author")
  category = input("Enter category")
  publication_year = input("Enter publication year")
  status = int(input("Enter status (1=owned, 2 = borrowed)"))
  return title,author,category,publication_year,status #return multiple value as tuple
def showBooks(sql,data=None):
  '''
  [
    {'id':2,'title':'abc','author':'xyz','genre':'drama','year_published':2024,'status':1},
    {'id':2,'title':'abc','author':'xyz','genre':'drama','year_published':2024,'status':1},
    {'id':2,'title':'abc','author':'xyz','genre':'drama','year_published':2024,'status':1},
  ]
  '''
  tables = db.fetch(sql,data)
  count = len(tables)
  if count==0: # book not found
     print("book not found.")
  else:
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(f"{'id':<5} {'title':<64} {'author':<32} {'category':<32} {'year':<8} {'status':<10}")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for row in tables:
        msg = ''
        if row['status'] == 1:
           msg = "purchased"
        else:
           msg = "Borrowed" 
        output = f"{row['id']:<5} {row['title']:<64} {row['author']:<32} {row['genre']:<32} {row['year_published']:<8} {msg:<10}"
        print(output)
    print("-------------------------------------------------------------------------------------------------------")
    print(f"no of books in your libarary = {count}")
  pause = input('press any key')
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
            showBooks(sql)
        elif choice == 2:
          print("Enter book detail")
          book = getInput() # getinput function will return tuples (ready only list)
          # title,author,category,publication_year,status
          sql = "insert into books (title,author,genre,year_published,status) values(%s,%s,%s,%s,%s)"
          data = [book[0],book[1],book[2],book[3],book[4]]
          count = db.modify(sql,data)
          if count==1:
            print('Book added')
          else:
            print('Error occurred while inserting book')
          pause = input('press any key')
        elif choice == 3:
          sql = "select * from books order by title"
          showBooks(sql)
          bookID = int(input("Enter book id to update status")) 
          book = getInput() # getinput function will return tuples (ready only list)
          sql = "update books set title=%s,author=%s,genre=%s,year_published=%s,status=%s where id=%s";
          data = [book[0],book[1],book[2],book[3],book[4],bookID]
          count = db.modify(sql,data)
          if count==1:
            print('Book updated successfully')
          else:
            print('Error occurred while updating book')
          pause = int(input("press any key to continue"))
        elif choice == 4:
          showBooks()
          bookid = int(input("Enter book id"))
          sql = "delete from books where id=%s"
          data = [bookid]
          count = db.modify(sql,data)
          if count==0:
            print('book not found')
          else: 
            print('book has been deleted successfully')
        elif choice == 5:
          title = input("Enter few words of book title to search book by title")
          sql = "select * from books where title like %s"
          data = [f"%{title}%"]  # Add wildcards around the input
          showBooks(sql,data)
        elif choice == 6:
           author = input("Enter few words of book author to search book by author")
           sql = "select * from books where author like %s"
           data = [f"%{author}%"]
           showBooks(sql,data)
        elif choice == 7:
         sql = "select * from books order by title"
         showBooks(sql)
         bookID = int(input("Enter book id to update status")) 
         status = int(input("Enter book status 1 = purchased 2 = borrowed"))
         sql = "update books set status=%s where id=%s"
         data = [status,bookID]
         count = db.modify(sql,data)
         if count == 0:
            print('book not found')
         else:
            print('book updated')
        else:
         print('invalid choice')
    except ValueError as error:
        print("only number between (0 to 7) are allowed")