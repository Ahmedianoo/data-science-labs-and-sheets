# (c) Maximilian Schwarzmüller / Academind GmbH

import re

sql_driver = None
mongo_db_driver = None


class Database:
    """
    Acts as an adapter, connecting models to various database engines (SQL, MongoDB)
    """
    def __init__(self):
        self.db_engine = None

    def load_database_driver(self, engine):
        if engine == "sql":
            self.db_driver = sql_driver
        else:
            self.db_driver = mongo_db_driver

    def connect(self):
        self.db_driver.connect()  # This may fail and throw an error

    def insert_data(self, data):
        self.db_driver.insert(data) 

    def find_one(self, id):
        # Todo: Needs to be implemented
        return self.db_driver.find_one(id)


email_regex = re.compile(r"\S+@\S+\.\S+")

# Only works in browser environment
# In JS: localStorage.setItem("user", "test@test.com")
