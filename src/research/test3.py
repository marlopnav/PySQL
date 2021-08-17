import sqlite3
import pandas as pd

db = sqlite3.connect('customer.db')

# Create a cursor
c = db.cursor()

# Create a table
c.execute("SELECT rowid, * FROM customers")
data_list = c.fetchall()
data_df = pd.DataFrame(data_list)

# Commit our command
db.commit()

# Close our connection
db.close()