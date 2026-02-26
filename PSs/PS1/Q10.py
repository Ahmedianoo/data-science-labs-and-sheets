response_data = { 
    "total_results": 2, 
    "books": [ 
        { 
            "id": "B001", 
            "title": "Python Basics", 
            "authors": ["Ahmed Ali", "Sara Mohamed"], 
            "price": {"amount": 250, "currency": "EGP"}, 
            "ratings": {"average": 4.5, "count": 120}, 
            "available": True 
        }, 
        { 
            "id": "B002", 
            "title": "Data Science 101", 
            "authors": ["Omar Hassan"], 
            "price": {"amount": 300, "currency": "EGP"}, 
            "ratings": {"average": 4.8, "count": 85}, 
            "available": False 
        } 
    ] 
} 
#Part A (3 points): Complete this code to extract specific information: 
import pandas as pd 
 
# TODO: Extract into a list of dictionaries with these fields: 
# - book_id 
# - title 
# - first_author (only the first author's name) 
# - price_egp (just the amount) 
# - avg_rating 
# - in_stock 
 
books_list = [] 
for book in response_data['books']: 
    books_list.append({ 
        'book_id': book['id'],
        'title': book['title'], 
        'first_author': book['authors'][0], 
        'price_egp': book['price']['amount'], 
        'avg_rating': book['ratings']['average'], 
        'in_stock':  book['available']
    }) 
 
df = pd.DataFrame(books_list)
print(df.head())


df_available = df[df['in_stock'] == True] 
df_sorted = df_available.sort_values('avg_rating', ascending=False) 
print(df_sorted[['title', 'price_egp', 'avg_rating']]) 