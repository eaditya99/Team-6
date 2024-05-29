from database_functions import validate_choice

### DEF CRUD MENUS ###
def menu_read():
    print("Choose from the following menu options : ")
    print(" 1 \t: Display of all books\n",
        "2 \t: Search book by title\n",
        "3 \t: Search book by ISBN\n\n",
        "0 \t: Return to main menu\n")
    
    choice = validate_choice()
    return choice

def menu_create():
    print("Choose from the following menu options : ")
    print(" 1 \t: Add a new book\n",
            "0 \t: Return to main menu\n")
    
    choice = validate_choice()
    return choice

def menu_update():
    print("Choose from the following menu options : ")
    print(" 1 \t: Update book entry\n",
        "0 \t: Return to main menu\n\n")

    choice = validate_choice()
    return choice

def menu_delete():
    print("Choose from the following menu options : ")
    print(" 1 \t: Remove a specific book\n",
            "2 \t: Remove all books\n\n",
            "0 \t: Return to main menu\n")
    
    choice = validate_choice()
    return choice

