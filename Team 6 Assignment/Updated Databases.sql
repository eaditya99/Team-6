USE perpustakaan;
 CREATE TABLE Katalog (
    ISBN CHAR(13) PRIMARY KEY,
    title VARCHAR(255) NOT NULL DEFAULT 'Untitled',
    author VARCHAR(100) DEFAULT 'Anonymous',
    publisher VARCHAR(100) DEFAULT 'Anonymous',
    published_year YEAR,
    availability TINYINT(3)
);
CREATE TABLE Password (
	Id INT auto_increment primary key,
    PrimKey ENUM('Super', 'Admin', 'User'),
    Username VARCHAR(100),
    Email VARCHAR(100),
   Password VARCHAR(100)
);

DESC katalog;
DESC password;
SELECT 
    *
FROM
    katalog;

INSERT INTO katalog (ISBN, title, author, publisher, published_year, availability) VALUES
	("9780123456472", 'The Great Adventure', 'John Doe', 'Fiction House', 2010, 2),
	("9781234567897", 'Data Science for Beginners', 'Jane Smith', 'Tech World', 2015, 10),
	("9780765432109", 'Understanding Artificial Intelligence', 'Alan Turing', 'AI Publications', 2020, 5),
	("9780456789123", 'The History of Mathematics', 'Euclid', 'Academic Press', 2005,3),
	("9781908765432", 'Modern Web Development', 'Tim Berners-Lee', 'Web Books', 2018, 7),
	("9780876543214", 'Quantum Physics Simplified', 'Albert Einstein', 'Science Works', 2012, 0),
	("9781876543225", 'Culinary Arts and Sciences', 'Gordon Ramsay', 'Culinary Publications', 2014, 0),
	("9780654321890", 'Introduction to Economics', 'Adam Smith', 'Economic Insights', 2017, 6),
	("9781654321111", 'The World of Plants', 'Jane Goodall', 'Nature Books', 2011, 9),
    ("9780987654321", 'Introduction to Machine Learning', 'Alice Johnson', 'Tech Press', 2016, 11),
	("9780543210445", 'Exploring Space', 'Neil Armstrong', 'Space Ventures', 2019, 1);
    
SELECT 
    *
FROM
    Katalog;

insert into password (PrimKey, Username, Email, Password)
values('Super', 'JohnBlack', 'johnblack@gmail.com', 'Super123!'),
('Admin', 'DoeWhite', 'doewhite@gmail.com', 'Admin123!'),
('User', 'LuckyJoe', 'luckyjoe@gmail.com', 'Lucky123!');

select * from password;
COMMIT;