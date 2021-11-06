import sqlite3

conn = sqlite3.connect('pets.db') #connect to the database

cur = conn.cursor() #once you have a cursor you can start executing sql commnands



if __name__ == "__main__":
    pass

