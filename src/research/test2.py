import sqlite3

db = sqlite3.connect('customer.db')

# Create a cursor
c = db.cursor()

many_customers = [
    ('Paco','Gomez','pg@aa.com'),
    ('Fran','Faboam','rf@aa.com'),
    ('Roberto','Sandro','rs@aa.com'),
]

# Create a table
c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# Commit our command
db.commit()

# Close our connection
db.close()