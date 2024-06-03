#==========================================================================
######################## CONNECT TO DATABASE ##############################
#==========================================================================
import mysql.connector

db = mysql.connector.connect(
    host='127.0.0.1',  # Replace with your host, e.g., '127.0.0.1'
    port= '3306',       
    user='Team6',     # Replace with your MySQL username
    password='TEAM6sql123!', # Replace with your MySQL password
    database='perpustakaan'  # Replace with the name of your database
)

if db.is_connected():
    print("Berhasil terhubung ke database")

cursor = db.cursor()


#==========================================================================
######################## COMMON FUNCTIONS #################################
#==========================================================================
def Login():
    try_log_in = 0
    try_limit = 5

    while try_log_in < try_limit:
        print('=' * 50)
        id_input = input('Username: ')
        pass_input = input('Password: ')
        print('=' * 50, '\n')

        cursor = db.cursor()
        cursor.execute("SELECT Password, PrimKey FROM Password WHERE Username = %s", (id_input,))
        user_data = cursor.fetchone()

        if user_data is None:
            print(f'Username not registered! You can try {try_limit - try_log_in - 1} times more\n')
            try_log_in += 1
        elif pass_input != user_data[0]:
            print(f'Wrong Password, You can try {try_limit - try_log_in - 1} times more\n')
            try_log_in += 1
        else:
            print('Welcome\n')
            print('=' * 50)
            if user_data[1] == 'Admin':
                print('Admin Login')
            elif user_data[1] == 'Super':
                print('SuperAdmin Login')
            elif user_data[1] == 'User':
                print('User Login')
            return id_input

    print('Login Try Limit.\n')
    return None

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

def validate_choice(): 
    while True:
        choice = input('Please enter your choice : ')
        if not choice.isdigit() or len(choice)!=1:
            print('Your choice is invalid\n')
        else :
            break
    return choice

def confirm_action(action):
    while True:
        print(f"\nYou're about to {action}. ")
        answer = input("Are you sure? (Y/N) : ")
        
        if answer.upper() == "Y":
            return True
        elif answer.upper() == "N":
            return False
        else : 
            print("Your choice is invalid\n")

def validate_username(existing_usernames):
    status_ok = False
    while not status_ok:
        input_username = input("Masukkan User ID yang diinginkan : ")

        if not input_username.isalnum():
            print("Format Username salah. Masukkan hanya kombinasi huruf dan angka.\n")
        elif len(input_username) < 6 or len(input_username) > 20:
            print("Format Username salah. Masukkan User ID antara 6 - 20 karakter.\n")
        else:
            if input_username in existing_usernames:
                print("User ID sudah terpakai. Silakan masukkan User ID yang lain\n")
            else:
                print("User ID berhasil dibuat\n")
                return input_username

def validate_password():
    while True:
        password = input("Masukkan password : ")

        count_upper = 0
        count_lower = 0
        count_number = 0
        count_spchar = 0

        for c in password:
            if c.isupper():
                count_upper += 1
            elif c.islower():
                count_lower += 1
            elif c.isdigit():
                count_number += 1
            elif not c.isalnum():
                count_spchar += 1

        if count_upper > 0 and count_lower > 0 and count_number > 0 and count_spchar > 0:
            print("Password berhasil divalidasi\n")
            return password
        else:
            print("Pastikan password memiliki kombinasi huruf kapital, huruf kecil, angka dan karakter khusus\n")

def validate_email():
    while True:
        user_input = input("Masukkan alamat email: ")

        if user_input.count('@') != 1:
            print("Email Tidak Valid, Alasan: Jumlah '@' harus tepat satu.\n")
            continue

        username, remaining = user_input.split('@')
        hostname, extension = remaining.split('.', 1)

        if not username[0].isalnum() or not (username.replace('_', '').replace('.', '').isalnum()):
            print("Email Tidak Valid, Alasan: Format Username salah.\n")
            continue
        if not hostname[0].isalnum() or not hostname.isalnum():
            print("Email Tidak Valid, Alasan: Format Hostname salah.\n")
            continue
        if not extension.isalpha() or not (len(extension) <= 5 and '.' not in extension):
            print("Email Tidak Valid, Alasan: Format Ekstensi salah.\n")
            continue
        if extension in ['co', 'id', 'my', 'sg']:
            if '.' in extension:
                print("Email Tidak Valid, Alasan: Format Ekstensi salah.\n")
                continue

            second_extension = input("Masukkan ekstensi kedua (max 5 karakter): ")
            if not second_extension.isalpha() or len(second_extension) > 5:
                print("Email Tidak Valid, Alasan: Format Ekstensi kedua salah.\n")
                continue

        print("Alamat Email yang Anda Masukkan Valid\n")
        return user_input

def register():
    print("Welcome to the registration process.")
    
    cursor.execute("SELECT Username FROM Password")
    existing_usernames = cursor.fetchall()
    existing_usernames = {username[0] for username in existing_usernames}  # Convert to set for faster lookups

    username = validate_username(existing_usernames)
    email = validate_email()
    password = validate_password()
    
    user_role = input("Enter your role (User/Admin/Super): ")
    while user_role not in ['User', 'Admin', 'Super']:
        print("Invalid role. Please enter 'User', 'Admin', or 'Super'.\n")
        user_role = input("Enter your role (User/Admin/Super): ")
    
    # Insert the new user data into the database
    cursor.execute("INSERT INTO Password (Username, Email, Password, PrimKey) VALUES (%s, %s, %s, %s)", (username, email, password, user_role))
    db.commit()
    
    print("Registration successful. You can now log in with your new account.\n")

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
    return isbn, search_result
    
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

## READ - show all books in database
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
    


#==========================================================================
######################## DELETE FUNCTIONS #################################
#==========================================================================

def delete_all():
    try: 
        action = "remove this book from the catalogue?"
        if confirm_action(action) == True:
            delete_all_query = f"DELETE FROM katalog;"
            cursor.execute(delete_all_query)

            db.commit()
            print("Success! All books has been deleted\n") 
        else: 
            print("Delete all is cancelled\n")
    except:
        if db:
            db.rollback()  # Rollback the transaction on error
            print("Transaction rolled back due to error.")

def delete_by_isbn():
    try:
        isbn_input,_ = search_by_isbn()

        if isbn_input != "":
            action = "remove this book from the catalogue?"
            if confirm_action(action) == True:
                delete_query = f"DELETE FROM katalog WHERE isbn = {isbn_input}"
                cursor.execute(delete_query)

                db.commit()
                print("Success! Books has been deleted\n") 
            else: 
                print("Delete is cancelled\n")
        else: 
            print("\nThere is no book with this ISBN number in the library.")
    except:
        if db:
            db.rollback()  # Rollback the transaction on error
            print("Transaction rolled back due to error.")


#==========================================================================
######################## CREATE FUNCTIONS #################################
#==========================================================================

def validate_year():  
    import datetime
    current_year = datetime.datetime.now().year 
    
    while True:
        year_input = input("Please enter the year the book was published : ")
        if not year_input.isdigit():
            print("Please enter a valid year\n")
        elif int(year_input) < 1600 or int(year_input) > current_year:
            print("Please enter a year between 1600 and current year\n")
        else:
            break
    year = int(year_input)

    return year

def validate_availability():
    while True:
        availability_input = input("Please enter how many books are available in the library : ")
        if not availability_input.isdigit():
            print("Please enter a valid number\n")
        elif int(availability_input) > 100:
            print("Please enter a number between 0 and 100\n")
        else:
            break
    
    availability = int(availability_input)
        
    return availability

### ADD BOOK ###
def add_book():
    try: 
        isbn_input = validate_isbn()
        search_isbn_query = f"SELECT isbn FROM katalog WHERE isbn = {isbn_input}"
        cursor.execute(search_isbn_query)

        isbn = cursor.fetchall()

        if isbn != []: 
            print("There's already an existing book with this ISBN. Please go to update menu instead\n")
        else: 
            title = input("Insert book title : ")
            author = input("Insert the book author : ")
            publisher = input("Insert book publisher : ")
            year = validate_year()
            availability = validate_availability()
        
            print("\nThis is the data you've input: ")
            print(f" ISBN \t\t: {isbn_input}\n Title \t\t: {title.title()}\n Author \t: {author.title()}\n Publisher \t: {publisher.capitalize()}\n Year \t\t: {year}\n Availability \t: {availability}\n")

            action = "add this book into the catalogue"
            if confirm_action(action) == True:
                create_query = f"INSERT INTO katalog (isbn, title, author, publisher, published_year, availability) VALUES (%s, %s, %s, %s, %s, %s);"
                values = (isbn_input, title, author, publisher, year, availability)
                cursor.execute(create_query, values)
                db.commit()
                print("Success! The book has been added to the catalogue\n") 
            else: 
                print("Add book is cancelled\n")
    except:
        if db:
            db.rollback()  # Rollback the transaction on error
            print("Transaction rolled back due to error.")


#==========================================================================
######################## UPDATE FUNCTIONS #################################
#==========================================================================

def update_book():
    try:
        isbn_input, search_result = search_by_isbn()
        
        row = search_result[0]
        isbn, title, author, publisher, year, availability = datatype_into_string(row)


        if isbn_input != "":
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
                        title = title.title()
                    elif choice == "2":
                        author = input("Please enter the new author : ") 
                        author = author.title()
                    elif choice == "3":
                        publisher = input("Please enter the new publisher : ") 
                        publisher = publisher.capitalize()
                    elif choice == "4":
                        year = validate_year()
                    elif choice == "5":
                        availability = validate_availability()

                    print("\nThis is the data you've input: ")        
                    print(f" ISBN \t\t: {isbn}\n Title \t\t: {title}\n Author \t: {author}\n Publisher \t: {publisher}\n Year \t\t: {year}\n Availability \t: {availability}\n")

                    action = "save this update into the catalogue"
                    if confirm_action(action) == True:
                        update_query = f"UPDATE katalog SET title = '{title}', author = '{author}', publisher = '{publisher}', published_year = {year}, availability = {availability} WHERE isbn = '{isbn_input}';"
                        cursor.execute(update_query)
                        db.commit()
                        print("Success! The book has been updated\n") 
                    else: 
                        print("Update is cancelled\n")
                
                elif choice == "0" :
                    print("\n")
                    break

                else: 
                    print('Your choice is invalid\n')   
    
    except:
        if db:
            db.rollback()  # Rollback the transaction on error
            print("Transaction rolled back due to error.")



#==========================================================================
############################# MAIN MENU ###################################
#==========================================================================
def search_menu():
    while True:
        print("Choose from the following options : ")
        print(" 1 \t: Display all books\n",
              "2 \t: Search book by title\n",
              "3 \t: Search book by ISBN\n",
              "0 \t: Return to main menu\n")
        choice = validate_choice()
        print("\n")

        if choice == "0":  # return to main menu
            print("\n")
            break
        elif choice == "1":  # display all books
            read_all()
        elif choice == "2":  # search book by title
            search_by_title()
        elif choice == "3":  # search book by isbn
            search_by_isbn()
        else:
            print('Your choice is invalid\n')

def add_book_menu():
    while True:
        print("Choose from the following options : ")
        print(" 1 \t: Add new book entry\n",
              "0 \t: Return to main menu\n")
        choice = validate_choice()
        print("\n")

        if choice == "0":
            print("\n")
            break
        elif choice == "1":
            add_book()
        else:
            print("Your choice is invalid\n")

def update_menu():
    while True:
        print("Choose from the following options : ")
        print(" 1 \t: Update book entry\n",
              "0 \t: Return to main menu\n")
        choice = validate_choice()
        print("\n")

        if choice == "0":
            print("\n")
            break
        elif choice == "1":
            update_book()
        else:
            print("Your choice is invalid\n")

def delete_menu():
    while True:
        print("Choose from the following options : ")
        print(" 1 \t: Delete book\n",
              "2 \t: Delete all books\n",
              "0 \t: Return to main menu\n")
        choice = validate_choice()
        print("\n")

        if choice == "0":
            print("\n")
            break
        elif choice == "1":
            delete_by_isbn()
        elif choice == "2":
            delete_all()
        else:
            print("Your choice is invalid\n")

def main_menu(user_role):
    while True:
        print("Main Menu")
        print("Choose from the following menu options : ")
        print(" 1 \t: Search for book(s)\n",
              "2 \t: Add a new book entry\n",
              "3 \t: Update book data\n",
              "4 \t: Delete book(s)\n\n",
              "0 \t: Exit\n")

        entry = validate_choice()
        print("\n")

        if entry == "0":
            print("=" * 53)
            print("Thank you for using Lucia's digital library catalogue")
            print("=" * 53)
            print("\n")
            break
        elif entry == "1":
            search_menu()
        elif entry == "2":
            if user_role in ['Admin', 'Super']:
                add_book_menu()
            else:
                print("You do not have permission to add a new book entry.\n")
        elif entry == "3":
            if user_role in ['Admin', 'Super']:
                update_menu()
            else:
                print("You do not have permission to update book data.\n")
        elif entry == "4":
            if user_role == 'Super':
                delete_menu()
            else:
                print("You do not have permission to delete books.\n")
        else:
            print('Your choice is invalid\n')


def main():
    while True:
        print("Choose from the following menu options : ")
        print(" 1 \t: Login\n",
              "2 \t: Register\n",
              "0 \t: Exit\n")
        
        entry = input("Please enter your choice: ")
        print("\n")
        
        if entry == '0':
            print("="*53)
            print("Thank you for using Lucia's digital library catalogue")
            print("="*53)
            print("\n")
            cursor.close()
            db.close()
            break
        elif entry == '1':
            # Continue with the login process
            user_id = Login()
            if user_id:
                cursor.execute("SELECT PrimKey FROM Password WHERE Username = %s", (user_id,))
                user_role = cursor.fetchone()[0]
                main_menu(user_role)
        elif entry == '2':
            # Prompt user to register
            register()
        else:
            print("Invalid choice. Please try again.\n")

main()