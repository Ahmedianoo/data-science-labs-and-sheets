import sqlite3
import pandas as pd
from datetime import datetime, timedelta


# Create database connection
conn = sqlite3.connect('library.db')
cursor = conn.cursor()


# Step 1: Create Authors table
cursor.execute('''
CREATE TABLE IF NOT EXISTS authors (
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    country TEXT,
    birth_year INTEGER
)
''')


# Step 2: Create Books table
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER NOT NULL,
    isbn TEXT UNIQUE,
    publication_year INTEGER,
    genre TEXT,
    copies_available INTEGER DEFAULT 1 CHECK(copies_available >= 0),
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
)
''')


# Step 3: Create Members table
cursor.execute('''
CREATE TABLE IF NOT EXISTS members (
    member_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    join_date DATE DEFAULT CURRENT_DATE,
    membership_type TEXT CHECK(membership_type IN ('student', 'faculty', 'public'))
)
''')


# Step 4: Create Borrowings table
cursor.execute('''
CREATE TABLE IF NOT EXISTS borrowings (
    borrow_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    member_id INTEGER NOT NULL,
    borrow_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE,
    fine_amount REAL DEFAULT 0,
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (member_id) REFERENCES members(member_id)
)
''')


# Insert sample authors
authors_data = [
    ('Naguib Mahfouz', 'mahfouz@literature.eg', 'Egypt', 1911),
    ('Taha Hussein', 'taha@literature.eg', 'Egypt', 1889),
    ('Nawal El Saadawi', 'nawal@literature.eg', 'Egypt', 1931),
    ('Alaa Al Aswany', 'alaa@literature.eg', 'Egypt', 1957),
    ('Ahdaf Soueif', 'ahdaf@literature.eg', 'Egypt', 1950)
]


cursor.executemany('''
    INSERT INTO authors (name, email, country, birth_year)
    VALUES (?, ?, ?, ?)
''', authors_data)


# Insert sample books
books_data = [
    ('Cairo Trilogy', 1, '978-0307947109', 1956, 'Fiction', 3),
    ('The Days', 2, '978-9774160011', 1929, 'Biography', 2),
    ('Woman at Point Zero', 3, '978-1848134171', 1975, 'Fiction', 2),
    ('The Yacoubian Building', 4, '978-0060878139', 2002, 'Fiction', 4),
    ('The Map of Love', 5, '978-0385720038', 1999, 'Fiction', 2),
    ('Palace Walk', 1, '978-0307947093', 1956, 'Fiction', 2),
    ('Children of Gebelawi', 1, '978-0894108723', 1959, 'Fiction', 1),
    ('God Dies by the Nile', 3, '978-1848134188', 1974, 'Fiction', 3)
]


cursor.executemany('''
    INSERT INTO books (title, author_id, isbn, publication_year, genre, copies_available)
    VALUES (?, ?, ?, ?, ?, ?)
''', books_data)


# Insert sample members
members_data = [
    ('Ahmed Hassan', 'ahmed.hassan@university.edu', '0101234567', 'student'),
    ('Fatima Ali', 'fatima.ali@university.edu', '0109876543', 'student'),
    ('Mohamed Ibrahim', 'mohamed.ibrahim@university.edu', '0105555555', 'faculty'),
    ('Layla Mahmoud', 'layla.mahmoud@gmail.com', '0102222222', 'public'),
    ('Omar Khaled', 'omar.khaled@university.edu', '0103333333', 'student')
]


cursor.executemany('''
    INSERT INTO members (name, email, phone, membership_type)
    VALUES (?, ?, ?, ?)
''', members_data)


# Insert sample borrowings
import random
from datetime import datetime, timedelta


borrowings_data = []
base_date = datetime(2024, 2, 1)


for i in range(20):
    book_id = random.randint(1, 8)
    member_id = random.randint(1, 5)
    days_ago = random.randint(1, 60)
    borrow_date = (base_date - timedelta(days=days_ago)).strftime('%Y-%m-%d')
    due_date = (base_date - timedelta(days=days_ago) + timedelta(days=14)).strftime('%Y-%m-%d')
    
    # Some books returned, some still borrowed
    if random.random() > 0.3:  # 70% returned
        return_date = (base_date - timedelta(days=days_ago) + timedelta(days=random.randint(1, 20))).strftime('%Y-%m-%d')
        # Calculate fine if overdue
        due = datetime.strptime(due_date, '%Y-%m-%d')
        returned = datetime.strptime(return_date, '%Y-%m-%d')
        days_late = max(0, (returned - due).days)
        fine = days_late * 2.0  # 2 EGP per day
    else:
        return_date = None
        fine = 0
    
    borrowings_data.append((book_id, member_id, borrow_date, due_date, return_date, fine))


cursor.executemany('''
    INSERT INTO borrowings (book_id, member_id, borrow_date, due_date, return_date, fine_amount)
    VALUES (?, ?, ?, ?, ?, ?)
''', borrowings_data)


conn.commit()
print("✓ Library database created successfully!")
print(f"  - {len(authors_data)} authors")
print(f"  - {len(books_data)} books")
print(f"  - {len(members_data)} members")
print(f"  - {len(borrowings_data)} borrowings")



# Query 1: View all books
query = "SELECT * FROM books LIMIT 5"
df = pd.read_sql_query(query, conn)
print("All Books:")
print(df)
