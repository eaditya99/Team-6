import mysql.connector

db = mysql.connector.connect(
    host='127.0.0.1',  # Replace with your host, e.g., '127.0.0.1'
    port= '3306',       
    user='root',     # Replace with your MySQL username
    password='Cc10040014!!', # Replace with your MySQL password!!!
    database='perpustakaan'  # Replace with the name of your database
)

if db.is_connected():
    print("Berhasil terhubung ke database")

cursor = db.cursor()


#### COMMON FUNCTIONS ####

def validate_isbn():
    while True:  
        isbn_input = input("Insert 13 digits of ISBN number : ")
        if not isbn_input.isdigit() or len(isbn_input) != 13:
            print("\nPlease insert 13 digits of ISBN number\n")
        else: 
            break

    return isbn_input

def datatype_into_string(row):
    new_list = []
    for i in row:
        i = str(i)
        new_list.append(i)
    return new_list

def row_title(): 
    border =  "+-----------------+-----------------------------+-------------------+------------------------+------------------+----------------+"
    row_title = "|  ISBN           |  TITLE                      |  AUTHOR           |  PUBLISHER             |  YEAR PUBLISHED  |  AVAILABILITY  |"
    print(border)
    print(row_title)
    print(border)

def row_end():
    border =  "+-----------------+-----------------------------+-------------------+------------------------+------------------+----------------+"
    print(border)



#==========================================================================
######################## READ FUNCTIONS ###################################
#==========================================================================

## READ - search book by ISBN
def search_by_isbn():
    isbn = validate_isbn()
    print("\n")
    search_isbn_query = f"SELECT * FROM katalog WHERE isbn = {isbn}"
    cursor.execute(search_isbn_query)

    search_result = cursor.fetchall()
    if search_result == []:
        print("\nThere is no book with this ISBN number in the library.")
    else:
        row = search_result[0]
        isbn, title, author, publisher, year, availability = datatype_into_string(row)

        format_result = f"ISBN\t\t: {isbn}\nTitle\t\t: {title}\nAuthor\t\t: {author}\nPublisher\t: {publisher}\nYear\t\t: {year}\nAvailability\t: {availability}\n"
        print(format_result)
    print("\n")

    

## READ - search book by title
def search_by_title():
    title_search = input("Input book title: ")
     
    search_title_query = f"SELECT * FROM katalog WHERE title LIKE '%{title_search}%';"
    cursor.execute(search_title_query)

    search_result = cursor.fetchall()

    if search_result == []:
        print("\nThere is no book with this ISBN number in the library.")
    else:
        row_title()
        for row in search_result:
            isbn, title, author, publisher, year, availability = datatype_into_string(row)
            
            if len(title)>25:                   ## formatting in case book title is very long
                title = title[0:22] + "..."
            elif len(title)<25:
                n = 25-len(title)
                title = title + " "*(n)

            if len(author)>15:                  ## formatting in case author name is very long
                author = author[0:12] + "..."
            elif len(author)<15:
                n = 15-len(author)
                author = author + " "*(n)

            if len(publisher)>20:               ## formatting in case publisher name is very long
                publisher = publisher[0:17] + "..." 
            elif len(publisher)<20:
                n = 20-len(publisher)
                publisher = publisher + " "*(n)

            year = year + " "*10
            availability = availability + " "*(12-len(availability))
            
            print(f"|  {isbn}  |  {title}  |  {author}  |  {publisher}  |  {year}  |  {availability}  |")
        row_end()
        print("\n")


def read_all(): 
    read_all_query = f"SELECT * FROM katalog;"
    cursor.execute(read_all_query)

    read_all_result = cursor.fetchall()

    if read_all_result == []:
        print("\nThere is no book with in the library.")
    else:
        row_title()
        for row in read_all_result:
            isbn, title, author, publisher, year, availability = datatype_into_string(row)

            if len(title)>25:                   ## formatting in case book title is very long
                title = title[0:22] + "..."
            elif len(title)<25:
                n = 25-len(title)
                title = title + " "*(n)

            if len(author)>15:                  ## formatting in case author name is very long
                author = author[0:12] + "..."
            elif len(author)<15:
                n = 15-len(author)
                author = author + " "*(n)

            if len(publisher)>20:               ## formatting in case publisher name is very long
                publisher = publisher[0:17] + "..." 
            elif len(publisher)<20:
                n = 20-len(publisher)
                publisher = publisher + " "*(n)

            year = year + " "*10
            availability = availability + " "*(12-len(availability))
            
            print(f"|  {isbn}  |  {title}  |  {author}  |  {publisher}  |  {year}  |  {availability}  |")
        row_end()
        print("\n")
