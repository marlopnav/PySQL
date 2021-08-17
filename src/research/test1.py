import sqlite3

db = sqlite3.connect('CRAC_info.db')

# Create a cursor
c = db.cursor()

contingencies = [
    ('HE-ARG','Hernani-Argia 1','FR-ES'),
    ('ALD-POC','Aldeadavila-Pocinho 1','PT-ES'),
    ('BIE-PRG','Biescas-Pragneres 1','FR-ES')
]

overloads = [
    ('10-10-2021 20:00','PST Pragneres','120 %', 'HE-ARG'),
    ('10-10-2021 21:00','PST Pragneres','125 %', 'HE-ARG'),
    ('10-10-2021 22:00','PST Pragneres','128 %', 'HE-ARG'),
    ('10-10-2021 20:00','Random line','158 %', 'ALD-POC'),
    ('10-10-2021 21:00','Random line','158 %', 'ALD-POC'),
    ('10-10-2021 22:00', 'Random line', '158 %', 'ALD-POC'),
    ('10-10-2021 20:00', 'Hernani Argia 1', '98 %', 'HE-ARG'),
    ('10-10-2021 21:00', 'Hernani Argia 1', '103 %', 'BIE-PRG'),
    ('10-10-2021 22:00', 'Hernani Argia 1', '112 %', 'BIE-PRG')
]

# Create a table
c.execute("""CREATE TABLE contingencies (
    name text,
    line text,
    country text
)""")

c.execute("""CREATE TABLE overloads (
    date text,
    line text,
    load text,
    contingency text
)""")

# Create a table
c.executemany("INSERT INTO contingencies VALUES (?,?,?)", contingencies)

c.executemany("INSERT INTO overloads VALUES (?,?,?,?)", overloads)

# Commit our command
db.commit()

# Close our connection
db.close()