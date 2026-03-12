import sqlite3
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# 1. Setup Connection
db_name = 'customers.db'
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Drop tables if they exist to restart fresh
cursor.execute("DROP TABLE IF EXISTS customers")
cursor.execute("DROP TABLE IF EXISTS cleaning_logs")

# 2. Create Schema
# Customers table with intended dirty data
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    cust_id TEXT,
    full_name TEXT,
    email TEXT,
    age TEXT, -- Stored as text to allow type inconsistencies
    income TEXT, -- Stored as text to allow symbols like '$' or ','
    join_date TEXT,
    city TEXT
)
''')

# Logging table for Data Cleaning Reports
cursor.execute('''
CREATE TABLE IF NOT EXISTS cleaning_logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    step_number INTEGER,
    action_type TEXT, -- e.g., 'Imputation', 'Removal', 'Transformation'
    column_affected TEXT,
    details TEXT,
    reason TEXT, -- Explanation for why this method was chosen
    rows_affected INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')
np.random.seed(42)
# 3. Data Generation Configuration
num_records = 200 # Increased for better practice
cities = ['New York', 'NY', 'new york', 'London', 'london', 'Cairo', 'CAIRO', 'Paris', None]

data = []
for i in range(1, num_records + 1):
    # Base Data
    cid = f"C{1000+i}"
    name = f"User {i}"
    email = f"user{i}@example.com"
    
    # Age: Mostly integers, some text, some outliers
    # age_raw = random.randint(18, 80)
    age_raw = int(np.random.lognormal(mean=2.5, sigma=0.7))
    
    # Income: Mostly floats, some formatted strings
    income_raw = np.random.lognormal(mean=10.5, sigma=0.9) 
    
    # Date: Mostly correct, some weird formats
    date_obj = datetime(2023, 1, 1) + timedelta(days=random.randint(0, 365))
    date_str = date_obj.strftime('%Y-%m-%d')
    
    city = random.choice(cities)
    
    # --- Injecting Dirt ---
    
    # A. Missing Data (Increased Frequency)
    if i % 8 == 0: email = None # MCAR
    if i % 6 == 0: city = None
    if i % 10 == 0: income_raw = None # MNAR potentially
    
    # B. Type Inconsistencies & Format Issues
    # Age
    age_val = str(age_raw)
    if i % 15 == 0: age_val = f"{age_raw} years"
    if i % 20 == 0: age_val = "unknown"
    if i % 25 == 0: age_val = float(age_raw) # stored as string "45.0"
    
    # Income
    income_val = str(round(income_raw, 2)) if income_raw is not None else None
    # print(pd.to_numeric(income_val, errors='coerce').max())
    if income_val and i % 12 == 0: income_val = f"${income_val}" # Currency symbol
    
    # Date
    if i % 18 == 0: date_str = date_obj.strftime('%d/%m/%Y') # Different format
    if i % 30 == 0: date_str = "not_available"
    if i % 25 == 0: 
        future_date = datetime.now() + timedelta(days=random.randint(10, 365))
        date_str = future_date.strftime('%Y-%m-%d')

    # Email Casing
    if email and i % 5 == 0: email = email.upper()
    
    # C. Outliers
    if i == 7: age_val = "250" # Impossible age
    if i == 42: age_val = "-5" # Negative age
    if i == 13: income_val = "200000.0" # Massive income
    # print(pd.to_numeric(income_val, errors='coerce').max())
    # Add this line to create future dates for some records
    data.append((cid, name, email, age_val, income_val, date_str, city))

# D. Duplicate Records
# Append some existing records again
data.extend(data[:10]) 

# 4. Insert into SQLite
cursor.executemany('INSERT INTO customers VALUES (?,?,?,?,?,?,?)', data)
conn.commit()

print(f"Database '{db_name}' created with {len(data)} records.")
print("Tables created: 'customers', 'cleaning_logs'.")

conn.close()
