import sqlite3
import pandas as pd

class DataBase():
    def __init__(self, path):
        self.path = path

    def insert_customers(self,customers):
        #Connect to db
        db = sqlite3.connect(self.path)

        # Create a cursor
        c = db.cursor()

        #If customers is not a list conver it into one
        many_customers = customers if type(customers) is list else [customers]

        c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)


        db.commit()
        db.close()

    def get_table(self, table):
        db = sqlite3.connect(self.path)

        # Create a cursor
        c = db.cursor()

        # Get table
        c.execute("SELECT rowid, * FROM {}".format(table))
        data_list = c.fetchall()

        # Get headers
        c.execute("PRAGMA table_info({})".format(table))

        headers = ['id'] + [h[1] for h in c.fetchall()]

        # Commit our command
        db.commit()

        # Close our connection
        db.close()

        return headers, data_list

    def get_table_df(self,table):
        db = sqlite3.connect(self.path)

        # Create a cursor
        c = db.cursor()

        #Get table
        c.execute("SELECT rowid, * FROM {}".format(table))
        data_list = c.fetchall()

        #Get headers
        c.execute("PRAGMA table_info({})".format(table))

        headers = ['id'] + [h[1] for h in c.fetchall()]

        # Commit our command
        db.commit()

        # Close our connection
        db.close()



        data_df = pd.DataFrame(data_list)
        data_df.columns = headers
        data_df.set_index('id',drop=True, inplace=True)

        return data_df

    def get_tables_names(self):
        #Connect to db
        db = sqlite3.connect(self.path)

        # Create a cursor
        c = db.cursor()

        c.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
        tl = c.fetchall()

        tables_list = [t[0] for t in tl]

        # Commit our command
        db.commit()

        # Close our connection
        db.close()

        return tables_list

    def get_all_tables(self):

        tables = self.get_tables_names()

        return {t:self.get_table(t) for t in tables}

    def update_table(self,table,fields):

        header, old_data = self.get_table(table)

        #Connect to db
        db = sqlite3.connect(self.path)

        # Create a cursor
        c = db.cursor()

        for row in fields:

            if len(row) == len(header):
                query = "UPDATE {} set".format(table)
                for i in range(1, len(row)):
                    query += " {} = '{}',".format(header[i],row[i])

                query = query[:-1] + "WHERE rowid = {}".format(row[0])
                c.execute(query)

        # Commit our command
        db.commit()

        # Close our connection
        db.close()

    def export_table_to_excel(self, path, tables=""):

        if tables == "":
            tables = self.get_tables_names()
        if not isinstance(tables,list):
            tables = [tables]

        writer = pd.ExcelWriter(path)
        for table in tables:
            self.get_table_df(table).to_excel(writer,sheet_name=table)

        writer.save()





if __name__ == "__main__":
    dbconexion = DataBase('../research/customer.db')
    customers = dbconexion.get_table('customers')
    dbconexion.get_customers()