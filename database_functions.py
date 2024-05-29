### DATABASE ###
def empty_database():
    data = {
        "             " : {
            "title" : "",
            "author" : "",
            "publisher": "",
            "year" : "    ",
            "availability" : ""
            }
        } 
    return data

def database():  # dummy data : contains 7 books info
    data = {
    "9780471778646" : {
        "title" : "Python for Dummies",
        "author" : "Stef Maruch",
        "publisher" : "For Dummies",
        "year": "2006",
        "availability" : "4"
        } ,

    "9781492041139" : {
        "title" : "Data Science from Scratch",
        "author" : "Joel Grus",
        "publisher" : "O'Reilly Media",
        "year": "2019",
        "availability" : "1"
        },

    "9789793062797" : {
        "title" : "Laskar Pelangi",
        "author" : "Andrea Hirata",
        "publisher" : "Bentang Pustaka",
        "year": "2005",
        "availability" : "3"
        },

    "9780147514011" : {
        "title" : "Little Woman",
        "author" : "Anna Bond",
        "publisher" : "Penguin LLC US",
        "year": "2014",
        "availability" : "4"
        },

    "9786020329260" : {
        "title" : "The Architecture of Love",
        "author" : "Ika Natassa",
        "publisher" : "Gramedia Pustaka Utama",
        "year": "2016",
        "availability" : "2"
        },

    "9786230002274" : {
        "title" : "Logika Pemrogaman Python",
        "author" : "Abdul Kadir",
        "publisher" : "Gramedia Pustaka Utama",
        "year": "2019",
        "availability" : "6"
        },

    "9780747532699" : {
        "title" : "Harry Potter and the Philosopher's Stone",
        "author" : "J. K. Rowling",
        "publisher" : "Bloomsbury",
        "year": "1997",
        "availability" : "3"
    }
    }
    return data


### DEF MULTIPLE_USE FUNCTIONS ###

def validate_isbn(data):
    while True:  
        isbn_input = input("Insert 13 digits of ISBN number : ")
        if not isbn_input.isdigit() or len(isbn_input) != 13:
            print("\nPlease insert 13 digits of ISBN number\n")
        else: 
            break
    
    found = False
    for i in data.keys(): 
        if isbn_input == i:
            found = True
            break
        else: 
            found = False

    return isbn_input, found


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
    
    return year_input


def validate_availability():
    while True:
        availability_input = input("Please enter how many books are available in the library : ")
        if not availability_input.isdigit():
            print("Please enter a valid number\n")
        elif int(availability_input) > 100:
            print("Please enter a number between 0 and 100\n")
        else:
            break
    
    return availability_input


def yes_or_no(action):  
    while True:
        print(f"\nYou're about to {action}. ")
        answer = input("Are you sure? (Y/N) : ")
        
        if answer.upper() == "Y":
            yes = True
            break
        elif answer.upper() == "N":
            yes = False
            break
        else : 
            print("Your choice is invalid\n")
    
    return yes


def validate_choice(): 
    while True:
        choice = input('Please enter your choice : ')
        if not choice.isdigit() or len(choice)!=1:
            print('Your choice is invalid\n')
        else :
            break
    return choice


def menu_title(menu):  #formatting titles of each menu 
    print("","="*50, "\n", menu.upper(),"\n","="*50, "\n" )

def row_title(): 
    border =  "+-----------------+-----------------------------+-------------------+------------------------+------------------+----------------+"
    row_title = "|  ISBN           |  TITLE                      |  AUTHOR           |  PUBLISHER             |  YEAR PUBLISHED  |  AVAILABILITY  |"
    print(border)
    print(row_title)
    print(border)

def row_end():
    border =  "+-----------------+-----------------------------+-------------------+------------------------+------------------+----------------+"
    print(border)
