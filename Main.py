from tkinter import *
from tkinter import messagebox
import sqlite3
from datetime import date

con = sqlite3.connect("bookstore.db")
cr = con.cursor()
cr.execute("drop table bookstore")

cr.execute("CREATE TABLE IF NOT EXISTS 'bookstore' (Book_Name varchar(50), Book_Author varchar(50), Book_Price integer, Book_Quantity integer, Book_ISBN integer primary key)")
cr.execute("CREATE TABLE IF NOT EXISTS `users` (user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, firstname TEXT, surname TEXT, username TEXT)")
cr.execute("CREATE TABLE IF NOT EXISTS 'orders' (user_id INTEGER , Book_ISBN integer,due_date DATE)")
con.commit()

homepage = Tk()
homepage.resizable(False, False)
homepage.title("Bookstore")
back = Canvas(homepage)
back.pack(expand=True, fill=BOTH)
image = PhotoImage(file="bg.png")
back.img = image
back.create_image(0, 0, anchor=NW, image=image)
homepage.geometry('900x600')

def adminpage():
    admin = Tk()
    admin.resizable(False, False)
    admin.configure(background="light gray")
    admin.title("Administrator")
    admin.geometry('800x650')

    def showbook():
        showbook = Tk()
        showbook.resizable(False, False)
        showbook.configure(background="light gray")
        showbook.geometry('800x750')
        showbook.title("Menu")
        cr.execute("select Book_Name from bookstore order by Book_Name")
        name = cr.fetchall()
        cr.execute("select Book_Author from bookstore order by Book_Name")
        Author = cr.fetchall()
        cr.execute("select Book_Price from bookstore order by Book_Name")
        price = cr.fetchall()
        cr.execute("select Book_Quantity from bookstore order by Book_Name")
        quantity = cr.fetchall()
        cr.execute("select Book_ISBN from bookstore order by Book_Name")
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
            cr.execute("select Book_Name from bookstore order by Book_Name")
            name = cr.fetchall()
            name2 = str("('" + name1 + "',)")
            price = e3.get()
            quantity = e4.get()
            isbn1 = e5.get()

            cr.execute("select Book_ISBN from bookstore order by Book_Name")
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
                    cr.execute("insert into bookstore values (?, ?, ?, ?,?)", (name1, Author, price, quantity, isbn1))
                    con.commit()
                    messagebox.showinfo("Successfull", "Book has been added to Inventory.", command=addbook.destroy())

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
            cr.execute("select Book_Name from bookstore order by Book_Name")
            name = cr.fetchall()
            name2 = str("('" + name1 + "',)")

            if name1 == "":
                messagebox.showinfo("ERROR", "Please enter book name.")
            else:
                if name2 in str(name):
                    cr.execute("delete from bookstore where Book_Name=?", (name1,))
                    con.commit()
                    messagebox.showinfo("Successfull", "Book has been deleted from the bookstore.")
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
            cr.execute("select Book_Name from bookstore order by Book_Name")
            name = cr.fetchall()
            name2 = str("('" + name1 + "',)")

            if e1.get() == "" or e2.get() == "":
                messagebox.showinfo("Error", "One or more fields empty")
            else:
                if name2 in str(name):
                    cr.execute("update bookstore set Book_Price=? where Book_Name=?", (price, name1,))
                    con.commit()
                    messagebox.showinfo("Successfull", "Book price has been changed.",
                                        command=changeprice.destroy())
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
            cr.execute("select Book_Name from bookstore order by Book_Name")
            name = cr.fetchall()
            name2 = str("('" + name1 + "',)")
            if e1.get() == "" or e2.get() == "":
                messagebox.showinfo("Error", "One or more fields empty")
            else:
                if name2 in str(name):
                    cr.execute("update bookstore set Book_Quantity=? where Book_Name=?", (quantity, name1,))
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
            cr.execute("select Book_ISBN from bookstore order by Book_Name")
            isbn = cr.fetchall()
            cr.execute("select Book_Name from bookstore order by Book_Name")
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
                        cr.execute("select Book_Name from bookstore where Book_ISBN=?", (isbn1,))
                        books = cr.fetchall()
                        cr.execute("select Book_Name from bookstore where Book_ISBN=?", (isbn1,))
                        name = cr.fetchall()
                        cr.execute("select Book_Author from bookstore where Book_ISBN=?", (isbn1,))
                        Author = cr.fetchall()
                        cr.execute("select Book_Price from bookstore where Book_ISBN=?", (isbn1,))
                        price = cr.fetchall()
                        cr.execute("select Book_Quantity from bookstore where Book_ISBN=?", (isbn1,))
                        quantity = cr.fetchall()
                        cr.execute("select Book_ISBN from bookstore where Book_ISBN=?", (isbn1,))
                        isbn = cr.fetchall()

                        l = Label(showbook2, text="Name", font="Calibri 17", fg="black", bg="light gray",
                                  padx=20, pady=20)
                        l.grid(row=0, column=0)
                        l = Label(showbook2, text="Author", font="Calibri 17", fg="black",
                                  bg="light gray",
                                  padx=20, pady=20)
                        l.grid(row=0, column=1)
                        l = Label(showbook2, text="Price", font="Calibri 17", fg="black", bg="light gray",
                                  padx=20, pady=20)
                        l.grid(row=0, column=2)
                        l = Label(showbook2, text="Quantity", font="Calibri 17", fg="black",
                                  bg="light gray",
                                  padx=20, pady=20)
                        l.grid(row=0, column=3)
                        l = Label(showbook2, text="ISBN", font="Calibri 17", fg="black", bg="light gray",
                                  padx=20, pady=20)
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

                        submit = Button(showbook2, text="Ok", font="Calibri 15 bold", fg="Black",
                                        bg="Light grey", padx=25, pady=5, command=goback)
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
                        cr.execute("select Book_Name from bookstore where Book_Name=?", (name1,))
                        books = cr.fetchall()
                        print(books)
                        cr.execute("select Book_Name from bookstore where Book_Name=?", (name1,))
                        name = cr.fetchall()
                        cr.execute("select Book_Author from bookstore where Book_Name=?", (name1,))
                        Author = cr.fetchall()
                        cr.execute("select Book_Price from bookstore where Book_Name=?", (name1,))
                        price = cr.fetchall()
                        cr.execute("select Book_Quantity from bookstore where Book_Name=?", (name1,))
                        quantity = cr.fetchall()
                        cr.execute("select Book_ISBN from bookstore where Book_Name=?", (name1,))
                        isbn = cr.fetchall()

                        l = Label(showbook2, text="Name", font="Calibri 17", fg="black", bg="light gray",
                                  padx=20, pady=20)
                        l.grid(row=0, column=0)
                        l = Label(showbook2, text="Author", font="Calibri 17", fg="black", bg="light gray",
                                  padx=20, pady=20)
                        l.grid(row=0, column=1)
                        l = Label(showbook2, text="Price", font="Calibri 17", fg="black", bg="light gray",
                                  padx=20, pady=20)
                        l.grid(row=0, column=2)
                        l = Label(showbook2, text="Quantity", font="Calibri 17", fg="black", bg="light gray",
                                  padx=20, pady=20)
                        l.grid(row=0, column=3)
                        l = Label(showbook2, text="ISBN", font="Calibri 17", fg="black", bg="light gray",
                                  padx=20, pady=20)
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

        submit = Button(searchbook, text="Submit", font="Calibri 15 bold", fg="Black", bg="Light grey",
                        padx=7, pady=7, command=submit)
        submit.grid(row=3, column=1, pady=50)
        searchbook.mainloop()

    def addbook():
        addbook = Tk()
        addbook.resizable(False, False)
        addbook.configure(background="light gray")
        addbook.geometry('900x450')
        addbook.title("Add Book")

        l1 = Label(addbook, text="Name : ", font="Calibri 15 bold", fg="black", bg="light gray").grid(row=0,
                                                                                                      padx=200,
                                                                                                      pady=20)
        e1 = Entry(addbook, bd=5, font="Calibri 15", fg="Black")
        e1.grid(row=0, column=1)

        l2 = Label(addbook, text="Author : ", font="Calibri 15 bold", fg="black", bg="light gray").grid(row=1,
                                                                                                        padx=200,
                                                                                                        pady=15)
        e2 = Entry(addbook, bd=5, font="Calibri 15", fg="Black")
        e2.grid(row=1, column=1)

        l3 = Label(addbook, text="Price : ", font="Calibri 15 bold", fg="black", bg="light gray").grid(row=2,
                                                                                                       padx=200,
                                                                                                       pady=15)
        e3 = Entry(addbook, bd=5, font="Calibri 15", fg="Black")
        e3.grid(row=2, column=1)

        l4 = Label(addbook, text="Quantity : ", font="Calibri 15 bold", fg="black", bg="light gray").grid(row=3,
                                                                                                          padx=200,
                                                                                                          pady=15)
        e4 = Entry(addbook, bd=5, font="Calibri 15", fg="Black")
        e4.grid(row=3, column=1)

        l5 = Label(addbook, text="ISBN : ", font="Calibri 15 bold", fg="black", bg="light gray").grid(row=4,
                                                                                                      padx=200,
                                                                                                      pady=15)
        e5 = Entry(addbook, bd=5, font="Calibri 15", fg="Black")
        e5.grid(row=4, column=1)

        def submit():
            name1 = e1.get()
            Author = e2.get()
            cr.execute("select Book_Name from bookstore order by Book_Name")
            name = cr.fetchall()
            name2 = str("('" + name1 + "',)")
            price = e3.get()
            quantity = e4.get()
            isbn1 = e5.get()

            cr.execute("select Book_ISBN from bookstore order by Book_Name")
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
                    cr.execute("insert into bookstore values (?, ?, ?, ?,?)",
                               (name1, Author, price, quantity, isbn1))
                    con.commit()
                    messagebox.showinfo("Successfull", "Book has been added to the bookstore.",
                                        command=addbook.destroy())

        submit = Button(addbook, text="Submit", font="Calibri 15 bold", fg="Black", bg="Light grey", padx=5, pady=5,
                        command=submit)
        submit.grid(row=5, column=1, pady=50)
        addbook.mainloop()

    def adduser():
        adduser = Tk()
        adduser.resizable(False, False)
        adduser.configure(background="light gray")
        adduser.geometry('900x450')
        adduser.title("Add User")
        l1 = Label(adduser, text="First Name : ", font="Calibri 15 bold", fg="black", bg="light gray").grid(row=0,
                                                                                                            padx=200,
                                                                                                            pady=20)
        e1 = Entry(adduser, bd=5, font="Calibri 15", fg="Black")
        e1.grid(row=0, column=1)

        l2 = Label(adduser, text="Last Name : ", font="Calibri 15 bold", fg="black", bg="light gray").grid(row=1,
                                                                                                           padx=200,
                                                                                                           pady=15)
        e2 = Entry(adduser, bd=5, font="Calibri 15", fg="Black")
        e2.grid(row=1, column=1)

        l3 = Label(adduser, text="Username : ", font="Calibri 15 bold", fg="black", bg="light gray").grid(row=2,
                                                                                                          padx=200,
                                                                                                          pady=15)
        e3 = Entry(adduser, bd=5, font="Calibri 15", fg="Black")
        e3.grid(row=2, column=1)

        def submit():
            fname = e1.get()
            lname = e2.get()
            uname = e3.get()

            cr.execute("select username from users order by username")
            uname3 = cr.fetchall()
            if e1.get() == "" or e2.get() == "" or e3.get() == "":
                messagebox.showinfo("Error", "One or more fields empty")
            else:
                if uname in str(uname3):
                    messagebox.showinfo("ERROR", "A user with this username already exists.")
                else:
                    cr.execute("insert into users (firstname, surname, username) VALUES(?, ?, ?)",
                               (fname, lname, uname))
                    con.commit()
                    messagebox.showinfo("Successfull", "User has been added to the database.",
                                        command=adduser.destroy())

        submit = Button(adduser, text="Submit", font="Calibri 15 bold", fg="Black", bg="Light grey", padx=5, pady=5,
                        command=submit)
        submit.grid(row=5, column=1, pady=50)
        adduser.mainloop()

    def showusers():
        showusers = Tk()
        showusers.resizable(False, False)
        showusers.configure(background="light gray")
        showusers.geometry('800x750')
        showusers.title("Menu")
        cr.execute("select user_id from users order by user_id")
        name = cr.fetchall()
        cr.execute("select firstname from users order by user_id")
        Author = cr.fetchall()
        cr.execute("select surname from users order by user_id")
        price = cr.fetchall()
        cr.execute("select username from users order by user_id")
        quantity = cr.fetchall()

        l = Label(showusers, text="User ID", font="Calibri 17", fg="black", bg="light gray", padx=20, pady=20)
        l.grid(row=0, column=0)
        l = Label(showusers, text="First Name", font="Calibri 17", fg="black", bg="light gray", padx=20, pady=20)
        l.grid(row=0, column=1)
        l = Label(showusers, text="Last Name", font="Calibri 17", fg="black", bg="light gray", padx=20, pady=20)
        l.grid(row=0, column=2)
        l = Label(showusers, text="Username", font="Calibri 17", fg="black", bg="light gray", padx=20, pady=20)
        l.grid(row=0, column=3)

        count = 1
        for n in name:
            l = Label(showusers, text=n, font="Calibri 15", fg="black", bg="light gray", padx=20, pady=20)
            l.grid(row=count, column=0)
            count += 1

        count = 1
        for c in Author:
            l = Label(showusers, text=c, font="Calibri 15", fg="black", bg="light gray", padx=20, pady=20)
            l.grid(row=count, column=1)
            count += 1

        count = 1
        for p in price:
            l = Label(showusers, text=p, font="Calibri 15", fg="black", bg="light gray", padx=20, pady=20)
            l.grid(row=count, column=2)
            count += 1

        count = 1
        for q in quantity:
            l = Label(showusers, text=q, font="Calibri 15", fg="black", bg="light gray", padx=20, pady=20)
            l.grid(row=count, column=3)
            count += 1

        def goback():
            showusers.destroy()

        submit = Button(showusers, text="Ok", font="Calibri 15 bold", fg="Black", bg="Light grey", padx=25, pady=5,
                        command=goback)
        submit.grid(row=count + 1, column=2, pady=5)
        showusers.mainloop()

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

    def assign7():
        global op
        op = 7

    Label(admin, text="Welcome Admin", font="Calibri 15 bold", fg="Black", bg="lightgray").grid(padx=300, pady=10)
    Radiobutton(admin, text="Show Book Inventory", command=assign0, value=0, font="Calibri 13", fg="Black",
                bg="lightgray").grid(
        padx=260, pady=10)
    Radiobutton(admin, text="Add Book", command=assign1, value=1, font="Calibri 13", fg="Black", bg="lightgray").grid(
        padx=260, pady=10)
    Radiobutton(admin, text="Remove Book", command=assign2, value=2, font="Calibri 13", fg="Black",
                bg="lightgray").grid(padx=270, pady=10)
    Radiobutton(admin, text="Change Book Price", command=assign3, value=3, font="Calibri 13", fg="Black",
                bg="lightgray").grid(padx=270, pady=10)
    Radiobutton(admin, text="Change Book Quantity", command=assign4, value=4, font="Calibri 13", fg="Black",
                bg="lightgray").grid(padx=300, pady=10)
    Radiobutton(admin, text="Search Book", command=assign5, value=5, font="Calibri 13", fg="Black",
                bg="lightgray").grid(padx=300, pady=10)
    Radiobutton(admin, text="Add User", command=assign6, value=6, font="Calibri 13", fg="Black", bg="lightgray").grid(
        padx=300, pady=10)
    Radiobutton(admin, text="Show Users", command=assign7, value=7, font="Calibri 13", fg="Black", bg="lightgray").grid(
        padx=300, pady=10)

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
            adduser()
        elif op == 7:
            showusers()

    def gohome():
        global homepage
        homepage.iconify()
        homepage.deiconify()
        admin.destroy()

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


def userrequest():
    userrequest = Toplevel()
    userrequest.resizable(False, False)
    userrequest.title("User Panel")
    userrequest.geometry('800x450')
    userrequest.configure(background="light gray")
    l00 = Label(userrequest, text="Please Enter User Credentials Below ", font="Calibri 13 bold", fg="Black",
                bg="Light gray", padx=5, pady=5).place(x=250, y=40)

    l1 = Label(userrequest, text="Login ID: ", font="Calibri 14 bold", fg="Black", bg="Light gray", padx=5,
               pady=5).place(x=90, y=100)
    e1 = Entry(userrequest, bd=5, font="Calibri 15", fg="light gray")
    e1.place(x=180, y=100)

    sign = Button(userrequest, text="Signup", font="Calibri 15 bold", bg="Light grey", fg="Black", padx=7, pady=7)
    sign.place(x=550, y=100)

    l2 = Label(userrequest, text="Password: ", font="Calibri 15 bold", fg="Black", bg="Light gray", padx=5,
               pady=5).place(x=80, y=180)
    e2 = Entry(userrequest, bd=5, font="Calibri 15", fg="light gray", show="*")
    e2.place(x=180, y=180)

    logi = Button(userrequest, text="Login", font="Calibri 15 bold", bg="Light grey", fg="Black", padx=7, pady=7)
    logi.place(x=550, y=180)

    def gohome():
        global homepage
        homepage.iconify()
        homepage.deiconify()
        userrequest.destroy()

    def submit():
        login = e1.get()
        password = e2.get()
        if login == "admin" and password == "admin":
            userrequest.destroy()
            adminpage()
        else:
            messagebox.showerror("Error in login",
                                 "The entered ID/Password combination is incorrect. \nPlease try again.")

    submit = Button(userrequest, text="Submit", font="Calibri 15 bold", bg="Light grey", fg="Black", padx=7, pady=7,
                    command=submit)
    submit.place(x=280, y=350)
    homepage = Button(userrequest, text="Home", font="Calibri 15 bold", bg="Light grey", fg="Black", padx=7, pady=7,
                      command=gohome)
    homepage.place(x=400, y=350)
    userrequest.mainloop()


def userpage():
    user = Tk()
    user.resizable(False, False)
    user.title("Book rental and return")
    user.geometry('900x600')
    user.configure(background="light gray")

    def issuee():
        issue = Toplevel()
        issue.resizable(False, False)
        issue.title("Issue")
        issue.geometry('900x600')
        issue.configure(background="light gray")
        con.commit()
        h1 = Label(issue, text="Book Name", font="Calibri 15 bold", fg="Black", bg="light gray", padx=5, pady=5).grid(
            row=0, padx=50)
        h2 = Label(issue, text="Price", font="Calibri 15 bold", fg="Black", bg="light gray", padx=5, pady=5).grid(row=0,
                                                                                                                  column=1,
                                                                                                                  padx=50)
        cr.execute("select Book_Name from bookstore where Book_Quantity<>0 order by Book_Name")
        name = cr.fetchall()
        cr.execute("select Book_Price from bookstore where Book_Quantity<>0 order by Book_Name")
        price = cr.fetchall()

        arr = []
        namearr = []
        checkbuttons = []
        count = 0

        def checkchecks():
            total = 0
            for i in range(0, count):
                if arr[i].get():
                    book = namearr[i]
                    [b] = book
                    cr.execute("select Book_Price from bookstore where Book_Name=?", (b,))
                    price = cr.fetchone()[0]
                    total += price
                    cr.execute("select Book_Quantity from bookstore where Book_Name=?", (b,))
                    quantity = cr.fetchone()[0]
                    q = int(quantity)
                    q = q - 1
                    cr.execute("select Book_ISBN from bookstore where Book_Name=?", (b,))
                    global isbn
                    isbn = cr.fetchone()[0]
                    cr.execute("update bookstore set Book_Quantity=? where Book_Name=?", (q, b,))

                    cr.execute("select user_id from users where firstname=?", (fname,))
                    usernames = cr.fetchone()[0]

                    today = date.today()
                    cr.execute("insert into orders values(?,?,?)", (usernames, isbn, today))

                    con.commit()

            message2 = "Book {} issued to:\n{} {} username {} \nThe price is ${}\n60 days are left to return the book".format(
                b, fname, lname, uname, str(total))
            messagebox.showinfo('Successfully issued', message2, command=issue.destroy())

        for n in name:
            arr.append(BooleanVar())
            check = BooleanVar()
            chk = Checkbutton(issue, text=n, var=arr[count], font="Calibri 15", fg="black", bg="light gray", padx=5,
                              pady=5)
            chk.grid(row=count + 1, sticky=W)
            namearr.append(n)
            checkbuttons.append(chk)
            count = count + 1

        count = 0
        for p in price:
            l = Label(issue, text=p, font="Calibri 15", fg="black", bg="light gray", padx=5, pady=5)
            l.grid(row=count + 1, column=1)
            count += 1

        submit = Button(issue, text="Submit", font="Calibri 15 bold", fg="Black", bg="Light grey", padx=10, pady=10,
                        command=checkchecks).grid(row=count + 2, column=1)
        issue.mainloop()

    def returnn():
        returnn = Toplevel()
        returnn.resizable(False, False)
        returnn.title("Return Book")
        returnn.geometry('700x400')
        returnn.configure(background="light gray")
        l1 = Label(returnn, text="Book Name: ", font="Calibri 15 bold", bg="light gray", fg="black").place(x=90,
                                                                                                           y=40)
        e1 = Entry(returnn, bd=3, font="Calibri 15", fg="Black")
        e1.place(x=330, y=40)

        l2 = Label(returnn, text="No. of days since issued : ", font="Calibri 15 bold", bg="light gray",
                   fg="black").place(
            x=90, y=90)
        e2 = Entry(returnn, bd=3, font="Calibri 15", fg="Black")
        e2.place(x=330, y=90)

        def returnbook():
            flag = 0
            book = e1.get()
            days = int(e2.get())
            if days > 100:
                days = 100
            cr.execute("select Book_Name from bookstore where Book_Name=?", (book,))
            check = cr.fetchall()
            for c in check:
                flag = 1
            if flag == 1:
                cr.execute("select Book_Price from bookstore where Book_Name=?", (book,))
                price = cr.fetchone()[0]
                dys = e2.get()
                returnprice = 0
                if int(dys) > 60:
                    returnprice = 5 * (int(dys) - 60)

                cr.execute("select Book_Quantity from bookstore  where Book_Name=?", (book,))
                q = cr.fetchone()[0]
                q = q + 1
                cr.execute("update bookstore set Book_Quantity=? where Book_Name=?", (q, book,))
                global isbn
                cr.execute("delete from orders where Book_ISBN=?", (isbn,))
                con.commit()
                string2 = "Thank you {} for returning the book {}.\n" \
                          "You returned book after {} days\n" \
                          "Your total Bill is ${} ".format(lname, book, dys, str(returnprice))
                messagebox.showinfo("Return successfull", string2, command=returnn.destroy())
            else:
                messagebox.showinfo("Return unsuccessfull", "Book name entered is invalid. Please try again.")

        submit = Button(returnn, text="Submit", font="Calibri 15 bold", fg="Black", padx=10, pady=5,
                        command=returnbook)
        submit.place(x=280, y=170)
        returnn.mainloop()

    op = 0

    def assign1():
        global op
        op = 1

    def assign2():
        global op
        op = 2

    l1 = Label(user, text="First Name : ", font="Calibri 15 bold", fg="black", bg="light gray").grid(row=1, padx=200,
                                                                                                     pady=20)
    e1 = Entry(user, bd=5, font="Calibri 15", fg="Black")
    e1.grid(row=1, column=1)
    l2 = Label(user, text="Last Name : ", font="Calibri 15 bold", fg="black", bg="light gray").grid(row=2, padx=200,
                                                                                                    pady=15)
    e2 = Entry(user, bd=5, font="Calibri 15", fg="Black")
    e2.grid(row=2, column=1)
    l3 = Label(user, text="Username : ", font="Calibri 15 bold", fg="black", bg="light gray").grid(row=3, padx=200,
                                                                                                   pady=15)
    e3 = Entry(user, bd=5, font="Calibri 15", fg="Black")
    e3.grid(row=3, column=1)

    Label(user, text="Enter Details", font="Calibri 15 bold", fg="black", bg="light gray").grid(row=0, column=1)
    Radiobutton(user, text="Issue", font="Calibri 15", fg="black", bg="light gray", command=assign1, value=1).grid(
        row=4, column=1)
    Radiobutton(user, text="Return", font="Calibri 15", fg="black", bg="light gray", command=assign2, value=2).grid(
        row=5, column=1)

    def callfunc():
        global fname
        global lname
        global uname
        fname = e1.get()
        lname = e2.get()
        uname = e3.get()
        fname1 = "'" + fname + "'"
        lname1 = "'" + lname + "'"
        uname1 = "'" + uname + "'"

        if e1.get() == "" or e2.get() == "" or e3.get() == "":
            messagebox.showinfo("Error", "One or more fields empty")
        else:
            # cr.S `users` (user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, firstname TEXT, surname TEXT, username TEXT)")
            cr.execute("Select * from users where username=?", (uname,))
            global ulist
            ulist = cr.fetchall()
            for i in ulist:
                if i[1] == fname and i[2] == lname and i[3] == uname:
                    global op
                    if op == 1:
                        issuee()
                    elif op == 2:
                        returnn()
                else:
                    messagebox.showinfo("Error", "Wrong Credentials")

    def gohome():
        global homepage
        homepage.iconify()
        homepage.deiconify()
        user.destroy()

    submit = Button(user, text="Submit", font="Calibri 15 bold", fg="Black", padx=10, pady=5, command=callfunc).grid(
        row=8, column=0)
    homepage = Button(user, text="Home", font="Calibri 15 bold", fg="Black", padx=10, pady=5, command=gohome).grid(
        row=8, column=1)
    user.mainloop()


def admin():
    homepage.withdraw()
    adminrequest()


def user():
    homepage.withdraw()
    userpage()


adminbutton = Button(back, command=admin, text="Admin", font="Calibri 15 bold", fg="Black", padx=10, pady=10,
                     bg="Light grey", border=3).place(x=400, y=400)
userbutton = Button(back, command=user, text="Book rental and return", font="Calibri 15 bold", fg="Black", padx=17, pady=10,
                    bg="Light grey", border=3).place(x=400, y=475)
homepage.mainloop()
