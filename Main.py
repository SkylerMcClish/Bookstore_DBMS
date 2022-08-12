from tkinter import *
from tkinter import messagebox
import sqlite3
from array import *

# Connect to database
con = sqlite3.connect("Bookstore.db")
cr = con.cursor()
# Create data tables
cr.execute(
    "CREATE TABLE IF NOT EXISTS 'library' (Book_Name varchar(50) primary key, Book_Author varchar(50), Book_Price integer, Book_Quantity integer, Book_ISBN integer)")
cr.execute(
    "CREATE TABLE IF NOT EXISTS `users` (user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, firstname TEXT, surname TEXT, username TEXT)")
cr.execute(
    "CREATE TABLE IF NOT EXISTS 'orders' (order_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, user_id REFERENCES users(user_id), Book_Name REFERENCES library(Book_Name))")

con.commit()

# Create homepage
homepage = Tk()
homepage.resizable(False, False)
homepage.title("Library")

back = Canvas(homepage)
back.pack(expand=True, fill=BOTH)
homepage.geometry('900x600')


# Create admin page
def adminpage():
    admin = Tk()
    admin.resizable(False, False)
    admin.configure(background="light gray")
    admin.title("Administrator")
    admin.geometry('800x550')

    def createuser():
        createuser = Tk()
        createuser.resizable(False, False)
        createuser.configure(background="light gray")
        createuser.geometry('800x750')
        createuser.title("Create User")

        Label(createuser, text="First Name: ", font="Calibri 15 bold", fg="black", bg="light gray").grid(row=0,
                                                                                                         padx=200,
                                                                                                         pady=20)
        e1 = Entry(createuser, bd=5, font="Calibri 15", fg="Black")
        e1.grid(row=0, column=1)

        Label(createuser, text="Last Name: ", font="Calibri 15 bold", fg="black", bg="light gray").grid(row=1, padx=200,
                                                                                                        pady=15)
        e2 = Entry(createuser, bd=5, font="Calibri 15", fg="Black")
        e2.grid(row=1, column=1)

        Label(createuser, text="UserName : ", font="Calibri 15 bold", fg="black", bg="light gray").grid(row=2, padx=200,
                                                                                                        pady=15)
        e3 = Entry(createuser, bd=5, font="Calibri 15", fg="light gray")
        e3.grid(row=2, column=1)

        def submit():
            first_name = e1.get()
            last_name = e2.get()
            user_name = e3.get()

            # check if user_id already exists
            cr.execute("select username from users order by username")
            name = cr.fetchall()
            name2 = str("('" + user_name + "',)")
            if e1.get() == "" or e2.get() == "" or e3.get() == "":
                messagebox.showinfo("Error", "One or more fields empty")
            else:
                if name2 in str(name):
                    messagebox.showinfo("ERROR", "A book with this name already exists.")
                else:
                    # Enter new user in users database
                    cr.execute("INSERT INTO users (firstname, surname, username) VALUES (?,?,?)",
                               (first_name, last_name, user_name))
                    con.commit()
                    messagebox.showinfo("Successfull", "User has been added.", command=createuser.destroy())

        submit = Button(createuser, text="Submit", font="Calibri 15 bold", fg="Black", bg="Light grey", padx=5, pady=5,
                        command=submit)
        submit.grid(row=5, column=1, pady=50)
        createuser.mainloop()

    def showbook():
        showbook = Tk()
        showbook.resizable(False, False)
        showbook.configure(background="light gray")
        showbook.geometry('800x750')
        showbook.title("Book Inventory")
        cr.execute("select Book_Name from library order by Book_Name")
        name = cr.fetchall()
        cr.execute("select Book_Author from library order by Book_Name")
        Author = cr.fetchall()
        cr.execute("select Book_Price from library order by Book_Name")
        price = cr.fetchall()
        cr.execute("select Book_Quantity from library order by Book_Name")
        quantity = cr.fetchall()
        cr.execute("select Book_ISBN from library order by Book_Name")
        isbn = cr.fetchall()

        l = Label(showbook, text="Name", font="Calibri 17", fg="black", bg="light gray", padx=20, pady=20)
        l.grid(row=0, column=0)
        l = Label(showbook, text="Author", font="Calibri 17", fg="black", bg="light gray", padx=20, pady=20)
        l.grid(row=0, column=1)
        l = Label(showbook, text="Price", font="Calibri 17", fg="black", bg="light gray", padx=20, pady=20)
        l.grid(row=0, column=2)
        l = Label(showbook, text="Quantity", font="Calibri 17", fg="black", bg="light gray", padx=20, pady=20)
        l.grid(row=0, column=3)
        l = Label(showbook, text="ISBN", font="Calibri 17", fg="black", bg="light gray", padx=20, pady=20)
        l.grid(row=0, column=4)

        count = 1
        for n in name:
            l = Label(showbook, text=n, font="Calibri 15", fg="black", bg="light gray", padx=20, pady=20)
            l.grid(row=count, column=0)
            count += 1

        count = 1
        for c in Author:
            l = Label(showbook, text=c, font="Calibri 15", fg="black", bg="light gray", padx=20, pady=20)
            l.grid(row=count, column=1)
            count += 1

        count = 1
        for p in price:
            l = Label(showbook, text=p, font="Calibri 15", fg="black", bg="light gray", padx=20, pady=20)
            l.grid(row=count, column=2)
            count += 1

        count = 1
        for q in quantity:
            l = Label(showbook, text=q, font="Calibri 15", fg="black", bg="light gray", padx=20, pady=20)
            l.grid(row=count, column=3)
            count += 1

        count = 1
        for i in isbn:
            l = Label(showbook, text=i, font="Calibri 15", fg="black", bg="light gray", padx=20, pady=20)
            l.grid(row=count, column=4)
            count += 1

        def goback():
            showbook.destroy()

        submit = Button(showbook, text="Ok", font="Calibri 15 bold", fg="Black", bg="Light grey", padx=25, pady=5,
                        command=goback)
        submit.grid(row=count + 1, column=2, pady=5)
        showbook.mainloop()

    def addbook():
        addbook = Tk()
        addbook.resizable(False, False)
        addbook.configure(background="light gray")
        addbook.geometry('900x450')
        addbook.title("Add Book")

        l1 = Label(addbook, text="Name : ", font="Calibri 15 bold", fg="black", bg="light gray").grid(row=0, padx=200,
                                                                                                      pady=20)
        e1 = Entry(addbook, bd=5, font="Calibri 15", fg="Black")
        e1.grid(row=0, column=1)

        l2 = Label(addbook, text="Author : ", font="Calibri 15 bold", fg="black", bg="light gray").grid(row=1, padx=200,
                                                                                                        pady=15)
        e2 = Entry(addbook, bd=5, font="Calibri 15", fg="Black")
        e2.grid(row=1, column=1)

        l3 = Label(addbook, text="Price : ", font="Calibri 15 bold", fg="black", bg="light gray").grid(row=2, padx=200,
                                                                                                       pady=15)
        e3 = Entry(addbook, bd=5, font="Calibri 15", fg="Black")
        e3.grid(row=2, column=1)

        l4 = Label(addbook, text="Quantity : ", font="Calibri 15 bold", fg="black", bg="light gray").grid(row=3,
                                                                                                          padx=200,
                                                                                                          pady=15)
        e4 = Entry(addbook, bd=5, font="Calibri 15", fg="Black")
        e4.grid(row=3, column=1)

        l5 = Label(addbook, text="ISBN : ", font="Calibri 15 bold", fg="black", bg="light gray").grid(row=4, padx=200,
                                                                                                      pady=15)
        e5 = Entry(addbook, bd=5, font="Calibri 15", fg="Black")
        e5.grid(row=4, column=1)

        def submit():
            name1 = e1.get()
            Author = e2.get()
            cr.execute("select Book_Name from library order by Book_Name")
            name = cr.fetchall()
            name2 = str("('" + name1 + "',)")
            price = e3.get()
            quantity = e4.get()
            isbn1 = e5.get()

            cr.execute("select Book_ISBN from library order by Book_Name")
            isbn = cr.fetchall()
            isbn2 = str("(" + isbn1 + ",)")

            if e1.get() == "" or e2.get() == "" or e3.get() == "" or e4.get() == "" or e5.get() == "":
                messagebox.showinfo("Error", "One or more fields empty")
            else:
                if name2 in str(name):
                    messagebox.showinfo("ERROR", "A book with this name already exists.")
                elif isbn2 in str(isbn):
                    messagebox.showinfo("ERROR", "A book with this ISBN already exists.")
                else:
                    cr.execute("insert into library values (?, ?, ?, ?,?)", (name1, Author, price, quantity, isbn1))
                    con.commit()
                    messagebox.showinfo("Successfull", "Book has been added to the library.", command=addbook.destroy())

        submit = Button(addbook, text="Submit", font="Calibri 15 bold", fg="Black", bg="Light grey", padx=5, pady=5,
                        command=submit)
        submit.grid(row=5, column=1, pady=50)
        addbook.mainloop()

    def removebook():
        removebook = Tk()
        removebook.resizable(False, False)
        removebook.geometry('700x350')
        removebook.configure(background="light gray")
        removebook.title("Remove")
        l1 = Label(removebook, text="Name :", font="Calibri 15 bold", bg="light gray", fg="black").place(x=180, y=50)
        e1 = Entry(removebook, bd=4, font="Calibri 15", fg="Black")
        e1.place(x=250, y=50)

        def submit():
            name1 = e1.get()
            cr.execute("select Book_Name from library order by Book_Name")
            name = cr.fetchall()
            name2 = str("('" + name1 + "',)")
            if name1 == "":
                messagebox.showinfo("ERROR", "Please enter book name.")
            else:
                if name2 in str(name):
                    cr.execute("delete from library where Book_Name=?", (name1,))
                    con.commit()
                    messagebox.showinfo("Successfull", "Book has been deleted from the library.")
                    command = removebook.destroy()
                else:
                    messagebox.showinfo("Error", "No book with such name exists")

        submit = Button(removebook, text="Submit", font="Calibri 15 bold", fg="Black", bg="Light grey", padx=7, pady=7,
                        command=submit)
        submit.place(x=300, y=150)
        removebook.mainloop()

    def changeprice():
        changeprice = Tk()
        changeprice.resizable(False, False)
        changeprice.geometry('900x300')
        changeprice.configure(background="light gray")
        changeprice.title("Price")
        l1 = Label(changeprice, text="Name : ", font="Calibri 15 bold", bg="light gray", fg="black").grid(row=0,
                                                                                                          padx=175,
                                                                                                          pady=20)
        e1 = Entry(changeprice, bd=5, font="Calibri 15", fg="Black")
        e1.grid(row=0, column=1)

        l2 = Label(changeprice, text="Price : ", font="Calibri 15 bold", bg="light gray", fg="black").grid(row=1,
                                                                                                           column=0)
        e2 = Entry(changeprice, bd=5, font="Calibri 15", fg="Black")
        e2.grid(row=1, column=1)

        def submit():
            name1 = e1.get()
            price = e2.get()
            cr.execute("select Book_Name from library order by Book_Name")
            name = cr.fetchall()
            name2 = str("('" + name1 + "',)")

            if e1.get() == "" or e2.get() == "":
                messagebox.showinfo("Error", "One or more fields empty")
            else:
                if name2 in str(name):
                    cr.execute("update library set Book_Price=? where Book_Name=?", (price, name1,))
                    con.commit()
                    messagebox.showinfo("Successfull", "Book price has been changed.", command=changeprice.destroy())
                else:
                    messagebox.showinfo("Error", "No book with such name exists")

        submit = Button(changeprice, text="Submit", font="Calibri 15 bold", fg="Black", bg="Light grey", padx=7, pady=7,
                        command=submit)
        submit.grid(row=3, column=1, pady=50)
        changeprice.mainloop()

    def changequantity():
        changequantity = Tk()
        changequantity.resizable(False, False)
        changequantity.geometry('800x350')
        changequantity.configure(background="light gray")
        changequantity.title("Quantity")
        l1 = Label(changequantity, text="Name : ", font="Calibri 15 bold", bg="light gray", fg="black").grid(row=0,
                                                                                                             padx=175,
                                                                                                             pady=50)
        e1 = Entry(changequantity, bd=5, font="Calibri 15", fg="Black")
        e1.grid(row=0, column=1)

        l2 = Label(changequantity, text="Quantity : ", font="Calibri 15 bold", bg="light gray", fg="black").grid(row=1,
                                                                                                                 column=0)
        e2 = Entry(changequantity, bd=5, font="Calibri 15", fg="Black")
        e2.grid(row=1, column=1)

        def submit():
            name1 = e1.get()
            quantity = e2.get()
            cr.execute("select Book_Name from library order by Book_Name")
            name = cr.fetchall()
            name2 = str("('" + name1 + "',)")
            if e1.get() == "" or e2.get() == "":
                messagebox.showinfo("Error", "One or more fields empty")
            else:
                if name2 in str(name):
                    cr.execute("update library set Book_Quantity=? where Book_Name=?", (quantity, name1,))
                    con.commit()
                    messagebox.showinfo("Successfull", "Book quantity has been changed.",
                                        command=changequantity.destroy())
                else:
                    messagebox.showinfo("Error", "No book with such name exists")

        submit = Button(changequantity, text="Submit", font="Calibri 15 bold", fg="Black", bg="Light grey", padx=7,
                        pady=7, command=submit)
        submit.grid(row=2, column=1, pady=30)
        changequantity.mainloop()

    def searchbook():
        searchbook = Tk()
        searchbook.resizable(False, False)
        searchbook.geometry('900x300')
        searchbook.configure(background="light gray")
        searchbook.title("Search Book")
        l1 = Label(searchbook, text="Name : ", font="Calibri 15 bold", bg="light gray", fg="black").grid(row=0,
                                                                                                         padx=175,
                                                                                                         pady=20)
        e1 = Entry(searchbook, bd=5, font="Calibri 15", fg="Black")
        e1.grid(row=0, column=1)

        l2 = Label(searchbook, text="ISBN : ", font="Calibri 15 bold", bg="light gray", fg="black").grid(row=1,
                                                                                                         column=0)
        e2 = Entry(searchbook, bd=5, font="Calibri 15", fg="Black")
        e2.grid(row=1, column=1)

        def submit():
            name1 = e1.get()
            isbn1 = e2.get()
            cr.execute("select Book_ISBN from library order by Book_Name")
            isbn = cr.fetchall()
            cr.execute("select Book_Name from library order by Book_Name")
            name = cr.fetchall()
            name2 = str("('" + name1 + "',)")
            isbn2 = str("(" + isbn1 + ",)")

            if e1.get() == "" and e2.get() == "":
                messagebox.showinfo("Error", "Both fields empty")
            else:
                if e1.get() == "":
                    if isbn2 in str(isbn):
                        showbook2 = Tk()
                        showbook2.resizable(False, False)
                        showbook2.configure(background="light gray")
                        showbook2.geometry('800x750')
                        showbook2.title("Book By Name")
                        cr.execute("select Book_Name from library where Book_ISBN=?", (isbn1,))
                        books = cr.fetchall()
                        cr.execute("select Book_Name from library where Book_ISBN=?", (isbn1,))
                        name = cr.fetchall()
                        cr.execute("select Book_Author from library where Book_ISBN=?", (isbn1,))
                        Author = cr.fetchall()
                        cr.execute("select Book_Price from library where Book_ISBN=?", (isbn1,))
                        price = cr.fetchall()
                        cr.execute("select Book_Quantity from library where Book_ISBN=?", (isbn1,))
                        quantity = cr.fetchall()
                        cr.execute("select Book_ISBN from library where Book_ISBN=?", (isbn1,))
                        isbn = cr.fetchall()

                        l = Label(showbook2, text="Name", font="Calibri 17", fg="black", bg="light gray", padx=20,
                                  pady=20)
                        l.grid(row=0, column=0)
                        l = Label(showbook2, text="Author", font="Calibri 17", fg="black", bg="light gray", padx=20,
                                  pady=20)
                        l.grid(row=0, column=1)
                        l = Label(showbook2, text="Price", font="Calibri 17", fg="black", bg="light gray", padx=20,
                                  pady=20)
                        l.grid(row=0, column=2)
                        l = Label(showbook2, text="Quantity", font="Calibri 17", fg="black", bg="light gray", padx=20,
                                  pady=20)
                        l.grid(row=0, column=3)
                        l = Label(showbook2, text="ISBN", font="Calibri 17", fg="black", bg="light gray", padx=20,
                                  pady=20)
                        l.grid(row=0, column=4)

                        count = 1
                        for n in name:
                            l = Label(showbook2, text=n, font="Calibri 15", fg="black", bg="light gray", padx=20,
                                      pady=20)
                            l.grid(row=count, column=0)
                            count += 1

                        count = 1
                        for c in Author:
                            l = Label(showbook2, text=c, font="Calibri 15", fg="black", bg="light gray", padx=20,
                                      pady=20)
                            l.grid(row=count, column=1)
                            count += 1

                        count = 1
                        for p in price:
                            l = Label(showbook2, text=p, font="Calibri 15", fg="black", bg="light gray", padx=20,
                                      pady=20)
                            l.grid(row=count, column=2)
                            count += 1

                        count = 1
                        for q in quantity:
                            l = Label(showbook2, text=q, font="Calibri 15", fg="black", bg="light gray", padx=20,
                                      pady=20)
                            l.grid(row=count, column=3)
                            count += 1

                        count = 1
                        for i in isbn:
                            l = Label(showbook2, text=i, font="Calibri 15", fg="black", bg="light gray", padx=20,
                                      pady=20)
                            l.grid(row=count, column=4)
                            count += 1

                        def goback():
                            showbook2.destroy()

                        submit = Button(showbook2, text="Ok", font="Calibri 15 bold", fg="Black", bg="Light grey",
                                        padx=25, pady=5, command=goback)
                        submit.grid(row=count + 1, column=2, pady=5)
                        showbook2.mainloop()
                    else:
                        messagebox.showinfo("Error", "No book with such ISBN exists")
                else:
                    if name2 in str(name):
                        showbook2 = Tk()
                        showbook2.resizable(False, False)
                        showbook2.configure(background="light gray")
                        showbook2.geometry('800x750')
                        showbook2.title("Book By Name")
                        cr.execute("select Book_Name from library where Book_Name=?", name1)
                        books = cr.fetchall()
                        print(books)
                        cr.execute("select Book_Name from library where Book_Name=?", (name1,))
                        name = cr.fetchall()
                        cr.execute("select Book_Author from library where Book_Name=?", (name1,))
                        Author = cr.fetchall()
                        cr.execute("select Book_Price from library where Book_Name=?", (name1,))
                        price = cr.fetchall()
                        cr.execute("select Book_Quantity from library where Book_Name=?", (name1,))
                        quantity = cr.fetchall()
                        cr.execute("select Book_ISBN from library where Book_Name=?", (name1,))
                        isbn = cr.fetchall()

                        l = Label(showbook2, text="Name", font="Calibri 17", fg="black", bg="light gray", padx=20,
                                  pady=20)
                        l.grid(row=0, column=0)
                        l = Label(showbook2, text="Author", font="Calibri 17", fg="black", bg="light gray", padx=20,
                                  pady=20)
                        l.grid(row=0, column=1)
                        l = Label(showbook2, text="Price", font="Calibri 17", fg="black", bg="light gray", padx=20,
                                  pady=20)
                        l.grid(row=0, column=2)
                        l = Label(showbook2, text="Quantity", font="Calibri 17", fg="black", bg="light gray", padx=20,
                                  pady=20)
                        l.grid(row=0, column=3)
                        l = Label(showbook2, text="ISBN", font="Calibri 17", fg="black", bg="light gray", padx=20,
                                  pady=20)
                        l.grid(row=0, column=4)

                        count = 1
                        for n in name:
                            l = Label(showbook2, text=n, font="Calibri 15", fg="black", bg="light gray",
                                      padx=20, pady=20)
                            l.grid(row=count, column=0)
                            count += 1

                        count = 1
                        for c in Author:
                            l = Label(showbook2, text=c, font="Calibri 15", fg="black", bg="light gray",
                                      padx=20, pady=20)
                            l.grid(row=count, column=1)
                            count += 1

                        count = 1
                        for p in price:
                            l = Label(showbook2, text=p, font="Calibri 15", fg="black", bg="light gray",
                                      padx=20, pady=20)
                            l.grid(row=count, column=2)
                            count += 1

                        count = 1
                        for q in quantity:
                            l = Label(showbook2, text=q, font="Calibri 15", fg="black", bg="light gray",
                                      padx=20, pady=20)
                            l.grid(row=count, column=3)
                            count += 1

                        count = 1
                        for i in isbn:
                            l = Label(showbook2, text=i, font="Calibri 15", fg="black", bg="light gray",
                                      padx=20, pady=20)
                            l.grid(row=count, column=4)
                            count += 1

                        def goback():
                            showbook2.destroy()

                        submit = Button(showbook2, text="Ok", font="Calibri 15 bold", fg="Black", bg="Light grey",
                                        padx=25, pady=5, command=goback)
                        submit.grid(row=count + 1, column=2, pady=5)
                        showbook2.mainloop()

                    else:
                        messagebox.showinfo("Error", "No book with such name exists")

        submit = Button(searchbook, text="Submit", font="Calibri 15 bold", fg="Black", bg="Light grey", padx=7, pady=7,
                        command=submit)
        submit.grid(row=3, column=1, pady=50)
        searchbook.mainloop()

    op = 0

    def assign0():
        global op
        op = 0

    def assign1():
        global op
        op = 1

    def assign2():
        global op
        op = 2

    def assign3():
        global op
        op = 3

    def assign4():
        global op
        op = 4

    def assign5():
        global op
        op = 5

    def assign6():
        global op
        op = 6

    # main admin landing page
    Label(admin, text="Welcome Admin", font="Calibri 15 bold", fg="Black", bg="lightgray").grid(padx=300, pady=10)

    Radiobutton(admin, text="Show Book", command=assign0, value=0, font="Calibri 13", fg="Black", bg="lightgray").grid(
        padx=260, pady=10)
    Radiobutton(admin, text="Add Book", command=assign1, value=1, font="Calibri 13", fg="Black", bg="lightgray").grid(
        padx=260, pady=10)
    Radiobutton(admin, text="Remove Book", command=assign2, value=2, font="Calibri 13", fg="Black",
                bg="lightgray").grid(padx=270, pady=10)
    Radiobutton(admin, text="Change Price", command=assign3, value=3, font="Calibri 13", fg="Black",
                bg="lightgray").grid(padx=270, pady=10)
    Radiobutton(admin, text="Change Quantity", command=assign4, value=4, font="Calibri 13", fg="Black",
                bg="lightgray").grid(padx=300, pady=10)
    Radiobutton(admin, text="Search Book", command=assign5, value=5, font="Calibri 13", fg="Black",
                bg="lightgray").grid(padx=300, pady=10)
    Radiobutton(admin, text="Create User", command=assign6, value=6, font="Calibri 13", fg="Black",
                bg="lightgray").grid(
        padx=260, pady=10)

    def callfunc():
        global op
        if op == 0:
            showbook()
        elif op == 1:
            addbook()
        elif op == 2:
            removebook()
        elif op == 3:
            changeprice()
        elif op == 4:
            changequantity()
        elif op == 5:
            searchbook()
        elif op == 6:
            createuser()

    def gohome():
        global homepage
        homepage.iconify()
        homepage.deiconify()
        admin.destroy()

    # submit button and home button
    submit = Button(admin, text="Submit", font="Calibri 14 bold", fg="Black", bg="Light grey", padx=10, pady=5,
                    command=callfunc)
    submit.grid(padx=20, pady=10)
    homepage = Button(admin, text="Home", font="Calibri 14 bold", fg="Black", bg="Light grey", padx=10, pady=5,
                      command=gohome).grid(padx=20, pady=0)
    admin.mainloop()


def adminrequest():
    adminrequest = Toplevel()
    adminrequest.resizable(False, False)
    adminrequest.title("Admin Panel")
    adminrequest.geometry('800x450')
    adminrequest.configure(background="light gray")
    l00 = Label(adminrequest, text="Please Enter Admin Credentials Below ", font="Calibri 13 bold", fg="Black",
                bg="Light gray", padx=5, pady=5).place(x=250, y=40)
    l1 = Label(adminrequest, text="Login ID: ", font="Calibri 14 bold", fg="Black", bg="Light gray", padx=5,
               pady=5).place(x=90, y=100)
    e1 = Entry(adminrequest, bd=5, font="Calibri 15", fg="light gray")
    e1.place(x=180, y=100)
    l2 = Label(adminrequest, text="Password: ", font="Calibri 15 bold", fg="Black", bg="Light gray", padx=5,
               pady=5).place(x=80, y=180)
    e2 = Entry(adminrequest, bd=5, font="Calibri 15", fg="light gray", show="*")
    e2.place(x=180, y=180)

    def gohome():
        global homepage
        homepage.iconify()
        homepage.deiconify()
        adminrequest.destroy()

    def submit():
        login = e1.get()
        password = e2.get()
        if login == "admin" and password == "admin":
            adminrequest.destroy()
            adminpage()
        else:
            messagebox.showerror("Error in login",
                                 "The entered ID/Password combination is incorrect. \nPlease try again.")

    submit = Button(adminrequest, text="Submit", font="Calibri 15 bold", bg="Light grey", fg="Black", padx=7, pady=7,
                    command=submit)
    submit.place(x=280, y=300)
    homepage = Button(adminrequest, text="Home", font="Calibri 15 bold", bg="Light grey", fg="Black", padx=7, pady=7,
                      command=gohome)
    homepage.place(x=400, y=300)
    adminrequest.mainloop()


def userpage():
    user = Tk()
    user.resizable(False, False)
    user.title("Book checkout/return")
    user.geometry('460x400')
    user.configure(background="light gray")

    Label(user, text="Enter Customer information : ", font="Calibri 15 bold", fg="black", bg="light gray").grid(row=0,
                                                                                                                pady=20,
                                                                                                                padx=5,
                                                                                                                columnspan=3)
    Label(user, text="Username : ", font="Calibri 15 bold", fg="black", bg="light gray").grid(row=1, pady=20, padx=5,
                                                                                              columnspan=1)
    e1 = Entry(user, bd=5, font="Calibri 15", fg="Black")
    e1.grid(row=1, column=1)

    def gohome():
        global homepage
        homepage.iconify()
        homepage.deiconify()
        user.destroy()

    def checkin():
        user_name = e1.get()
        cr.execute("SELECT user_id FROM users WHERE username = ?", user_name)
        user_id = cr.fetchall()
        print(user_id)
    def checkout():
        user_name = e1.get()
        checkout = Tk()
        checkout.resizable(False, False)
        checkout.geometry('900x300')
        checkout.configure(background="light gray")
        checkout.title("Checkout Book")

        Label(checkout, text="Enter Book Name or Book ISBN to checkout", font="Calibri 15 bold", bg="light gray",
              fg="black").grid(row=0, padx=175, pady=20, columnspan=3)
        Label(checkout, text="Name : ", font="Calibri 15 bold", bg="light gray", fg="black").grid(row=1, padx=175,
                                                                                                  pady=20)
        e2 = Entry(checkout, bd=5, font="Calibri 15", fg="Black")
        e2.grid(row=1, column=1)

        Label(checkout, text="ISBN : ", font="Calibri 15 bold", bg="light gray", fg="black").grid(row=2, column=0)
        e3 = Entry(checkout, bd=5, font="Calibri 15", fg="Black")
        e3.grid(row=2, column=1)

        def submit():
            name1 = e2.get()
            isbn1 = e3.get()
            cr.execute("select Book_ISBN from library order by Book_Name")
            isbn = cr.fetchall()
            cr.execute("select Book_Name from library order by Book_Name")
            name = cr.fetchall()
            name2 = str("('" + name1 + "',)")
            isbn2 = str("(" + isbn1 + ",)")

            if e2.get() == "" and e3.get() == "":
                messagebox.showinfo("Error", "Both fields empty")
            else:
                if e2.get() == "":
                    if isbn2 in str(isbn):
                        showbook2 = Tk()
                        showbook2.resizable(False, False)
                        showbook2.configure(background="light gray")
                        showbook2.geometry('800x750')
                        showbook2.title("Book By Name")
                        cr.execute("select Book_Name from library where Book_ISBN=?", (isbn1,))
                        books = cr.fetchall()
                        cr.execute("select Book_Name from library where Book_ISBN=?", (isbn1,))
                        name = cr.fetchall()
                        cr.execute("select Book_Author from library where Book_ISBN=?", (isbn1,))
                        Author = cr.fetchall()
                        cr.execute("select Book_Price from library where Book_ISBN=?", (isbn1,))
                        price = cr.fetchall()
                        cr.execute("select Book_Quantity from library where Book_ISBN=?", (isbn1,))
                        quantity = cr.fetchall()
                        cr.execute("select Book_ISBN from library where Book_ISBN=?", (isbn1,))
                        isbn = cr.fetchall()
                        print(isbn)

                        l = Label(showbook2, text="Name", font="Calibri 17", fg="black", bg="light gray", padx=20,
                                  pady=20)
                        l.grid(row=0, column=0)
                        l = Label(showbook2, text="Author", font="Calibri 17", fg="black", bg="light gray", padx=20,
                                  pady=20)
                        l.grid(row=0, column=1)
                        l = Label(showbook2, text="Price", font="Calibri 17", fg="black", bg="light gray", padx=20,
                                  pady=20)
                        l.grid(row=0, column=2)
                        l = Label(showbook2, text="Quantity", font="Calibri 17", fg="black", bg="light gray", padx=20,
                                  pady=20)
                        l.grid(row=0, column=3)
                        l = Label(showbook2, text="ISBN", font="Calibri 17", fg="black", bg="light gray", padx=20,
                                  pady=20)
                        l.grid(row=0, column=4)

                        count = 1
                        for n in name:
                            l = Label(showbook2, text=n, font="Calibri 15", fg="black", bg="light gray", padx=20,
                                      pady=20)
                            l.grid(row=count, column=0)
                            count += 1

                        count = 1
                        for c in Author:
                            l = Label(showbook2, text=c, font="Calibri 15", fg="black", bg="light gray", padx=20,
                                      pady=20)
                            l.grid(row=count, column=1)
                            count += 1

                        count = 1
                        for p in price:
                            l = Label(showbook2, text=p, font="Calibri 15", fg="black", bg="light gray", padx=20,
                                      pady=20)
                            l.grid(row=count, column=2)
                            count += 1

                        count = 1
                        for q in quantity:
                            l = Label(showbook2, text=q, font="Calibri 15", fg="black", bg="light gray", padx=20,
                                      pady=20)
                            l.grid(row=count, column=3)
                            count += 1

                        count = 1
                        for i in isbn:
                            l = Label(showbook2, text=i, font="Calibri 15", fg="black", bg="light gray", padx=20,
                                      pady=20)
                            l.grid(row=count, column=4)
                            count += 1

                        def goback():
                            showbook2.destroy()

                        submit = Button(showbook2, text="Ok", font="Calibri 15 bold", fg="Black", bg="Light grey",
                                        padx=25, pady=5, command=goback)
                        submit.grid(row=count + 1, column=2, pady=5)
                        showbook2.mainloop()
                    else:
                        messagebox.showinfo("Error", "No book with such ISBN exists")
                else:
                    if name2 in str(name):
                        showbook2 = Tk()
                        showbook2.resizable(False, False)
                        showbook2.configure(background="light gray")
                        showbook2.geometry('800x750')
                        showbook2.title("Book By Name")
                        cr.execute("select Book_Name from library where Book_Name=?", (name1,))
                        books = cr.fetchall()
                        cr.execute("select Book_Name from library where Book_Name=?", (name1,))
                        name = cr.fetchall()
                        cr.execute("select Book_Author from library where Book_Name=?", (name1,))
                        Author = cr.fetchall()
                        cr.execute("select Book_Price from library where Book_Name=?", (name1,))
                        price = cr.fetchall()
                        cr.execute("select Book_Quantity from library where Book_Name=?", (name1,))
                        quantity = cr.fetchall()
                        cr.execute("select Book_ISBN from library where Book_Name=?", (name1,))
                        isbn = cr.fetchall()

                        l = Label(showbook2, text="Name", font="Calibri 17", fg="black", bg="light gray", padx=20,
                                  pady=20)
                        l.grid(row=0, column=0)
                        l = Label(showbook2, text="Author", font="Calibri 17", fg="black", bg="light gray", padx=20,
                                  pady=20)
                        l.grid(row=0, column=1)
                        l = Label(showbook2, text="Price", font="Calibri 17", fg="black", bg="light gray", padx=20,
                                  pady=20)
                        l.grid(row=0, column=2)
                        l = Label(showbook2, text="Quantity", font="Calibri 17", fg="black", bg="light gray", padx=20,
                                  pady=20)
                        l.grid(row=0, column=3)
                        l = Label(showbook2, text="ISBN", font="Calibri 17", fg="black", bg="light gray", padx=20,
                                  pady=20)
                        l.grid(row=0, column=4)

                        count = 1
                        for n in name:
                            l = Label(showbook2, text=n, font="Calibri 15", fg="black", bg="light gray",
                                      padx=20, pady=20)
                            l.grid(row=count, column=0)
                            count += 1

                        count = 1
                        for c in Author:
                            l = Label(showbook2, text=c, font="Calibri 15", fg="black", bg="light gray",
                                      padx=20, pady=20)
                            l.grid(row=count, column=1)
                            count += 1

                        count = 1
                        for p in price:
                            l = Label(showbook2, text=p, font="Calibri 15", fg="black", bg="light gray",
                                      padx=20, pady=20)
                            l.grid(row=count, column=2)
                            count += 1

                        count = 1
                        for q in quantity:
                            l = Label(showbook2, text=q, font="Calibri 15", fg="black", bg="light gray",
                                      padx=20, pady=20)
                            l.grid(row=count, column=3)
                            count += 1

                        count = 1
                        for i in isbn:
                            l = Label(showbook2, text=i, font="Calibri 15", fg="black", bg="light gray",
                                      padx=20, pady=20)
                            l.grid(row=count, column=4)
                            count += 1

                        def goback():
                            showbook2.destroy()

                        submit = Button(showbook2, text="Ok", font="Calibri 15 bold", fg="Black", bg="Light grey",
                                        padx=25, pady=5, command=goback)
                        submit.grid(row=count + 1, column=2, pady=5)
                        showbook2.mainloop()

                    else:
                        messagebox.showinfo("Error", "No book with such name exists")

        Button(checkout, text="Submit", font="Calibri 15 bold", fg="Black", bg="Light grey", padx=7, pady=7,
               command=submit).grid(row=3, column=1)

    Button(user, text="Check out book", font="Calibri 15 bold", fg="Black", padx=10, pady=5, command=checkout).grid(
        row=3, column=0)
    Button(user, text="Check in book", font="Calibri 15 bold", fg="Black", padx=10, pady=5, command=checkin).grid(row=3,
                                                                                                                  column=1)
    Button(user, text="Home", font="Calibri 15 bold", fg="Black", padx=10, pady=5, command=gohome).grid(row=3, column=2)
    user.mainloop()


def admin():
    homepage.withdraw()
    adminrequest()


def user():
    homepage.withdraw()
    userpage()


Button(back, command=admin, text="Admin", font="Calibri 15 bold", fg="Black", padx=10, pady=10, bg="Light grey",
       border=3).place(x=400, y=400)
Button(back, command=user, text="Book check in/ check out", font="Calibri 15 bold", fg="Black", padx=17, pady=10,
       bg="Light grey", border=3).place(x=400, y=475)
homepage.mainloop()
