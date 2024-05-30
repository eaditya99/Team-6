import mysql.connector

db = mysql.connector.connect(
    host='127.0.0.1',  # Replace with your host, e.g., '127.0.0.1'
    port= '3306',       
    user='root',     # Replace with your MySQL username
    password='password', # Replace with your MySQL password!!!
    database='perpustakaan'  # Replace with the name of your database
)

if db.is_connected():
    print("Berhasil terhubung ke database")

cursor = db.cursor()


#### SEARCH BOOK BY ISBN ####

isbn = input("Masukkan ISBN : ")
print("\n")


select_isbn_query = f"SELECT * FROM katalog where isbn = {isbn}"

cursor.execute(select_isbn_query)

isbn_result = cursor.fetchall()
isbn, title, author, publisher, year, availability = zip(*isbn_result)

format_isbn_result = f"ISBN\t\t: {str(isbn[0])}\nTitle\t\t: {str(title[0])}\nAuthor\t\t: {str(author[0])}\nPublisher\t: {str(publisher[0])}\nYear\t\t: {str(year[0])}\nAvailability\t: {str(availability[0])}\n"
print(format_isbn_result)



# Commit the transaction
db.commit()

# Closing the cursor and connection
cursor.close()
db.close()
