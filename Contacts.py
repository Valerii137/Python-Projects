import sqlite3
import random

conn = sqlite3.connect("contacts.db")
curr = conn.cursor()
'''
curr.execute("""CREATE TABLE contacts (
                id integer NOT NULL,
                name text NOT NULL,
                phone_number integer NOT NULL
                )""")
'''
def cnt():
    print("Welcome to the Contacts\nEnter 1 to add contact || 321 to clear all data || 201 to watch data || 0 to exit.")
    s = int(input())
    if s == 1:
        i = random.randint(1000, 9999)  # number in contacts
        nm = input("Enter the name:")  # name
        pn = input("Enter phone number:")  # phone number
        curr.execute("INSERT INTO contacts VALUES ('{}', '{}', '{}')".format(i, nm, pn))
        conn.commit()
        curr.execute("SELECT * FROM contacts")
        print("New contact successfully added!", curr.fetchall())
        #conn.close()
        cnt()
    elif s == 0:
        print("Contacts successfully saved, goodbye!")
    elif s == 321:
        curr.execute("DROP TABLE contacts")
        conn.commit()   # !!!!notice that after droping database you should create it again.
    elif s == 201:
        curr.execute("SELECT * FROM contacts")
        print("Current contacts:", curr.fetchall())
    else:
        print("You should use 1 or 0 only!")
        cnt()

cnt()

