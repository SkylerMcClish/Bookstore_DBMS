import sqlite3


def create_tables():
    # Connect to database
    conn = sqlite3.connect('Bookstore.db')

    # Create a cursor
    c = conn.cursor()

    # Create customer datatable
    c.execute("""CREATE TABLE IF NOT EXISTS customer( 
                CustomerID INTEGER,
                FirstName TEXT,
                LastName TEXT,
                Phone INTEGER
                )""")
    # Create orders datatable
    c.execute("""CREATE TABLE IF NOT EXISTS orders( 
                    OrderNumber INTEGER,
                    CustomerID INTEGER,
                    BookID INTEGER,
                    CheckOutDate TEXT,
                    DueDate TEXT
                    )""")
    # Create book datatable
    c.execute("""CREATE TABLE IF NOT EXISTS book( 
                       OrderNumber INTEGER,
                       CustomerID INTEGER,
                       BookID INTEGER,
                       CheckOutDate TEXT,
                       DueDate TEXT
                       )""")
    # Commit changes
    conn.commit()


# Close connection to database
def close_db():
    conn = sqlite3.connect('Bookstore.db')
    conn.close()
