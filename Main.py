from tkinter import *
import Backend

root = Tk()
root.title("Bookstore Application")
Backend.create_tables()


def search_book():
    # Take current buttons off-screen

    # Create new user input option

    btnSearchByISBN = Label(root, text="Enter book ISBN", padx=40, pady=20).grid(row=0, column=0)
    btnSearchByISBN.grid(row=0, column=0)

    return


def button_add():
    return


def main():
    # Define buttons
    btnSearchBook = Button(root, text="Search inventory for book", padx=40, pady=20, command=search_book)
    btnSeeInventory = Button(root, text="View current inventory", padx=40, pady=20, command=button_add)
    btnSeeCheckedOut = Button(root, text="See current checked out books", padx=40, pady=20, command=button_add)

    # Add buttons to screen
    btnSearchBook.grid(row=0, column=0)
    btnSeeCheckedOut.grid(row=0, column=1)
    btnSeeInventory.grid(row=0, column=2)
    root.mainloop()
    Backend.close_db()


main()
