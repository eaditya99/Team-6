from database_functions import *    # Database and multiple-use functions
from crud_menus import *            # CRUD menus

# Simulated user database for login
datalogin = {'Admin001': {'Email': 'admin@luciadigitaldiary.com', 'Password': 'Admin123!'},
        'Super001': {'Email': 'superadmin@luciadigitaldiary.com', 'Password': 'Super123!'},
        'User001' : {'Email': 'user@luciadigitaldiary.com', 'Password': 'User123!'}
        }

def Login():
    global datalogin
    global id_input

    try_log_in = 0
    try_limit = 5

    while try_log_in < try_limit:
        print('=' * 50)
        id_input = input('Username: ')
        pass_input = input('Password: ')
        print('=' * 50, '\n')

        if id_input not in datalogin:
            print(f'Username not registered! You can try {try_limit - try_log_in - 1} times more\n')
            try_log_in += 1
        elif pass_input != datalogin[id_input]['Password']:
            print(f'Wrong Password, You can try {try_limit - try_log_in - 1} times more\n')
            try_log_in += 1
        else:
            print('Welcome\n')
            print('=' * 50)
            if id_input == 'Admin001':
                print('Admin Login')
            elif id_input == 'Super001':
                print('SuperAdmin Login')
            elif id_input == 'User001':
                print('User Login')
            return id_input
    print('Login Try Limit.\n')

data = database()

#### DEF CRUD FUNCTIONS ####

## DEF READ ##

def print_all():
    if data == empty_database():
        print(" ==== The catalogue is empty ====")
    else: 
        
        row_title()
        for isbn in data.keys():
            title, author, publisher, year, availability = data[isbn].values()
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

def search_title():
    title_search = input("Input book title: ")
    
    isbn_print = []
    for isbn, book in data.items():
        if title_search.lower() in book["title"].lower():
            isbn_print.append(isbn)
    
    if len(isbn_print) == 0 :
        print("\nWe couldn't find the book you're looking for.\n\n")
    else: 
        
        print("Book(s) found : ")
        row_title()
        for isbn in isbn_print:
            title, author, publisher, year, availability = data[isbn].values()
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

def search_isbn():
    isbn, found = validate_isbn(data)

    if found: 
        title, author, publisher, year, availability = list(data[isbn].values())
        print("\nBook found : ")   
        print(f" ISBN \t\t: {isbn}\n Title \t\t: {title.title()}\n Author \t: {author.title()}\n Publisher \t: {publisher.capitalize()}\n Year \t\t: {year}\n Availability \t: {availability}\n")
    else:
        print("\nThere is no book with this ISBN number in the library.")
        print("="*55)
        print("\n")
    
    return isbn, found


## DEF CREATE ##
def add_book(): 
    isbn, found = validate_isbn(data)

    if found: 
        print("There's already an existing book with this ISBN. Please go to update menu instead\n")
        save = False
        isbn = title = author = publisher = year = availability = ""

    else:
        title = input("Insert book title : ")
        author = input("Insert the book author : ")
        publisher = input("Insert book publisher : ")
        year = validate_year()
        availability = validate_availability()

        print("\nThis is the data you've input: ")
        print(f" ISBN \t\t: {isbn}\n Title \t\t: {title.title()}\n Author \t: {author.title()}\n Publisher \t: {publisher.capitalize()}\n Year \t\t: {year}\n Availability \t: {availability}\n")

        action = "add this book into the catalogue"
        save = yes_or_no(action)

    return save, isbn, title, author, publisher, year, availability


## DEF UPDATE ##
def update_book(isbn): 
    title, author, publisher, year, availability = list(data[isbn].values())
    data_temp = ({isbn : {
                        "title" : title.title(),
                        "author" : author.title(),
                        "publisher": publisher.capitalize(),
                        "year" : year,
                        "availability" : availability
                        }})
    
    while True:
        print("\nChoose the field you want to update: ")
        print(" 1 \t: Title\n",
                "2 \t: Author\n",
                "3 \t: Publisher\n",
                "4 \t: Year\n",
                "5 \t: Availability\n\n",
                "0 \t: Return to previous menu\n")
                
        choice = validate_choice()

        if choice in "12345":
            if choice == "1":
                title = input("Please enter the new title : ")
            elif choice == "2":
                author = input("Please enter the new author : ") 
            elif choice == "3":
                publisher = input("Please enter the new publisher : ") 
            elif choice == "4":
                year = validate_year()
            elif choice == "5":
                availability = validate_availability()

            print("\nThis is the data you've input: ")
            data_temp = ({isbn : {
                    "title" : title.title(),
                    "author" : author.title(),
                    "publisher": publisher.capitalize(),
                    "year" : year,
                    "availability" : availability
                    }})          
            print(f" ISBN \t\t: {isbn}\n Title \t\t: {title.title()}\n Author \t: {author.title()}\n Publisher \t: {publisher.capitalize()}\n Year \t\t: {year}\n Availability \t: {availability}\n")

            action = "add this book into the catalogue"
            save = yes_or_no(action)

        elif choice == "0" :
            print("\n")
            break

        else: 
            print('Your choice is invalid\n')    

    return save, isbn, title, author, publisher, year, availability


## DEF DELETE ##
def delete_book(isbn):
    action = "remove this book from the catalogue?"
    delete = yes_or_no(action)
    return delete, isbn

def delete_all_books():
    print("!!! WARNING !!!")
    action = "remove all books from the catalogue"
    delete = yes_or_no(action)
    return delete


# MAIN TITLE
main = "   welcome to lucia's digital library catalogue"
Login()
menu_title(main)

### MAIN MENU ###
while True:
    print("Choose from the following menu options : ")
    print(" 1 \t: Search for book(s)\n",
          "2 \t: Add a new book entry\n",
          "3 \t: Update book data\n",
          "4 \t: Delete book(s)\n\n",
          "0 \t: Exit\n")
    
    entry = validate_choice()
    print("\n")
    
    ## READ ##
    if entry == "1":
        read = "book searching menu"
        menu_title(read)

        while True:
            choice = menu_read()
            if choice == "1":  # display all books
                print_all()
            elif choice == "2":  # search book by title
                search_title()
            elif choice == "3":  # search book by isbn
                search_isbn()
            elif choice == "0":  # return to prev menu
                print("\n")
                break
            else:
                print('Your choice is invalid\n')
    
    ## CREATE ##
    elif entry == "2":
        if id_input in ['Admin001', 'Super001']:
            create = "add new book entry"
            menu_title(create)

            while True:
                choice = menu_create()
                # Add book entry
                if choice == "1":
                    save, isbn, title, author, publisher, year, availability = add_book()
                    # confirm to saving entry into database
                    if not save:
                        print("Book entry is cancelled\n")
                    else:
                        data.update({isbn: {
                            "title": title.title(),
                            "author": author.title(),
                            "publisher": publisher.capitalize(),
                            "year": year,
                            "availability": availability
                        }})
                        print("Success! Your new book has been saved\n")

                elif choice == "0":  # Return to prev menu
                    print("\n")
                    break
                else:
                    print('Your choice is invalid\n')
        else:
            print("You do not have permission to add a new book entry.\n")
    
    ## UPDATE ##
    elif entry == "3":
        if id_input in ['Admin001', 'Super001']:
            update = "book update menu"
            menu_title(update)

            while True:
                choice = menu_update()

                if choice == "1":  # Update book entry
                    isbn, found = search_isbn()
                    if found:
                        save, isbn, title, author, publisher, year, availability = update_book(isbn)
                        # confirm to saving update into database
                        if not save:
                            print("Book entry cancelled\n")
                        else:
                            data.update({isbn: {
                                "title": title.title(),
                                "author": author.title(),
                                "publisher": publisher.capitalize(),
                                "year": year,
                                "availability": availability
                            }})
                            print("Success! Your book has been updated\n")

                elif choice == "0":  # Return to prev menu
                    print("\n")
                    break

                else:
                    print('Your choice is invalid\n')
        else:
            print("You do not have permission to update book data.\n")

    ## DELETE ##
    elif entry == "4":
        if id_input == 'Super001':
            delete = "delete book menu"
            menu_title(delete)

            while True:
                choice = menu_delete()
                if choice == "1":  # Delete book
                    isbn, found = search_isbn()
                    if found:
                        delete, isbn = delete_book(isbn)
                        if not delete:
                            print("Delete is cancelled\n")
                        else:
                            del data[isbn]
                            print("Success! The book has been deleted\n")

                elif choice == "2":  # Delete all books
                    delete = delete_all_books()
                    if not delete:
                        print("Delete all is cancelled\n")
                    else:
                        data.clear()
                        data = empty_database()
                        print("Success! All books have been deleted\n")

                elif choice == "0":
                    print("\n")
                    break

                else:
                    print('Your choice is invalid\n')
        else:
            print("You do not have permission to delete books.\n")
    
    ## EXIT ##
    elif entry == "0":
        print("=" * 53)
        print("Thank you for using Lucia's digital library catalogue")
        print("=" * 53)
        print("\n")
        break

    else:  # invalid
        print('Your choice is invalid\n')

