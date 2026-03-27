-- SQLite

--exercise 1

-- Get Books with author names 
--hint use books table and join on author_id
Select A.name, B.title
FROM Books B
join authors A on B.author_id=A.author_id;


--exercise 2

-- Get Books never borrowed
-- hint: compare book_id in books table with book_id in borrowings table
SELECT title
FROM books
WHERE book_id NOT IN (SELECT book_id FROM borrowings);

--exercise 3 
-- Select all Members with fines
-- hint: join member_id from borrowings and members  
select distinct m.name
from members m
join borrowings b on m.member_id=b.member_id;




--exercise 4
--Members who borrowed books published before 1950
--hint: use subquery 
select distinct m.name, bks.title, bks.publication_year
from members m
join borrowings b on m.member_id=b.member_id
join books bks on bks.book_id=b.book_id and bks.publication_year < 1950;





--exercise 5 

-- use web scraping to scrap data from any website 


/*
import requests
from bs4 import BeautifulSoup

# Target URL
url = "https://www.masrawy.com/gold#Nav-Gold"

# Send HTTP request
response = requests.get(url, timeout=10)
response.raise_for_status()

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Look for price values (example selectors)
# This depends on the actual page structure — may need adjustment
# Here we look for key text and then grab the next element
prices = {}
labels = ["24", "21", "18", "14","10"]

for label in labels:
    # Search for text like "سعر الذهب عيار 24"
    el = soup.find(text=lambda t: f"عيار {label}" in t)
    if el:
        # Next element might be the numeric value
        val = el.find_next().text.strip()
        prices[f"Gold {label}K"] = val

# Print results
for karat, price in prices.items():
    print(f"{karat}: {price} EGP")


*/