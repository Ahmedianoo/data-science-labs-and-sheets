import sqlite3
import pandas as pd



def fetch_data_from_db(connection_string, query): 
    """ 
        Your code here 
    """ 

    conn = None

    try: 
        conn = sqlite3.connect(connection_string)

        df = pd.read_sql_query(query, conn)

        return df

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return df

    finally:
        if conn:
            conn.close()



