from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import uuid
import sqlite3
from sqlite3 import Error
import tkinter.ttk as ttk
from tkinter.ttk import Treeview

from datetime import datetime
import tkinter.ttk as tk
from pip._internal import main as pipmain
from decimal import*
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

def sql_connection():

    try:

        con = sqlite3.connect('Self_Checkout.db')

        print("Connection successfull!")

        return con

    except Error:

        print("Error")

#------------------------------------------------------------------------CUSTOMER SIGN UP---------------------------------------------------------------------------------

def regNewCust():
    rootlr = Tk()
    rootlr.geometry("680x570+100+30")
    rootlr.title("New Entry")
    rootlr.config(bg="#212121")

    cust_type = StringVar()
    cust_type = "customer"
    username2 = StringVar(rootlr)
    phno = IntVar(rootlr)

    def username_check2(con,username2):
        c=con.cursor()
        c.execute("INSERT INTO customer(cname,cmobnum,type) VALUES(?,?,?)",(username2.get(),phno.get(),cust_type,))
        con.commit()
        messagebox.showinfo("Success","Customer added")
        print("Customer added!")

    con = sql_connection()

    heading = Label(rootlr,text="Customer Sign up",font=("Noto sans",17,"bold"),
                    fg="#ffffff",bg="#212121")
    heading.place(x=250,y=35)

    loginframe = Frame(rootlr,bg="#ffffff",height=380,width=450)
    loginframe.place(x=120,y=120)

    userlabel = Label(loginframe,text="New Username : ",font=("Noto sans",12,"bold"),
                      bg="#ffffff")
    userlabel.place(x=40,y=70)


    userentry = Entry(loginframe,width=34,relief="flat",bg="#c2c2c2",textvariable=username2,
                      font=("Oxygen",13))
    userentry.place(x=45,y=120)


    passlabel = Label(loginframe,text="New Phone number : ",font=("Noto sans",12,"bold"),
                      bg="#ffffff")
    passlabel.place(x=40,y=170)

    passentry = Entry(loginframe,width=34,relief="flat",bg="#c2c2c2",textvariable=phno,
                      font=("Oxygen",13))
    passentry.place(x=45,y=220)

    submitbtn = Button(loginframe,text="Submit",font=("Nunito",13,"bold"),bg="#ffb300",
                      fg="#000000",relief="flat",width=8,activebackground="#ffb300"
                       ,command=lambda : username_check2(con,username2))
    submitbtn.place(x=195,y=300)

    quitbtn = Button(loginframe,text="Quit",font=("Nunito",13,"bold"),bg="#ff5722",
                      fg="#000000",relief="flat",width=8,activebackground="#ff5722",
                     command=rootlr.destroy)
    quitbtn.place(x=320,y=300)


    rootlr.mainloop()

#-------------------------------------------------------------------------------RETAILER SIGN UP-------------------------------------------------------------------------------------------------------------------------------------
def regNewAdmin():
    rootad = Tk()
    rootad.geometry("680x570+100+30")
    rootad.title("New Entry")
    rootad.config(bg="#212121")

    cust_type = StringVar()
    cust_type = "admin"
    username2 = StringVar(rootad)
    phno = IntVar(rootad)

    def username_checkR(con,username2):
        c=con.cursor()
        c.execute("INSERT INTO customer(cname,cmobnum,type) VALUES(?,?,?)",(username2.get(),phno.get(),cust_type,))
        con.commit()
        messagebox.showinfo("Success","Retailer added")
        print("Retailer added!")

    con = sql_connection()

    heading = Label(rootad,text="Retailer Sign up",font=("Noto sans",17,"bold"),
                    fg="#ffffff",bg="#212121")
    heading.place(x=250,y=35)

    loginframe = Frame(rootad,bg="#ffffff",height=380,width=450)
    loginframe.place(x=120,y=120)

    userlabel = Label(loginframe,text="New Username : ",font=("Noto sans",12,"bold"),
                      bg="#ffffff")
    userlabel.place(x=40,y=70)


    userentry = Entry(loginframe,width=34,relief="flat",bg="#c2c2c2",textvariable=username2,
                      font=("Oxygen",13))
    userentry.place(x=45,y=120)

    passlabel = Label(loginframe,text="New Phone number : ",font=("Noto sans",12,"bold"),
                      bg="#ffffff")
    passlabel.place(x=40,y=170)

    passentry = Entry(loginframe,width=34,relief="flat",bg="#c2c2c2",textvariable=phno,
                      font=("Oxygen",13))
    passentry.place(x=45,y=220)

    submitbtn = Button(loginframe,text="Submit",font=("Nunito",13,"bold"),bg="#ffb300",
                      fg="#000000",relief="flat",width=8,activebackground="#ffb300"
                       ,command=lambda : username_checkR(con,username2))
    submitbtn.place(x=195,y=300)

    quitbtn = Button(loginframe,text="Quit",font=("Nunito",13,"bold"),bg="#ff5722",
                      fg="#000000",relief="flat",width=8,activebackground="#ff5722",
                     command=rootad.destroy)
    quitbtn.place(x=320,y=300)


    rootad.mainloop()

#--------------------------------------------------------------------------------CUSTOMER LOGIN CONFIRMATION------------------------------------------------------------------------------------------------------------------------
def customerloginConfirm(phno2):
    rootl = Tk()
    rootl.geometry("680x570+100+30")
    rootl.title("Login window")
    rootl.config(bg="#212121")

    username = StringVar(rootl)
    phno = IntVar(rootl)


    def user_check(con,username,phno2):
        cur = con.cursor()
        cur2 = con.cursor()
        cur3 = con.cursor()
        phno2 = phno
        cur.execute("SELECT cname FROM customer where cname = ?",(username.get(),))
        cur2.execute("SELECT cmobnum FROM customer where cmobnum = ? and cname = ?",(phno.get(),username.get(),))
        cur3.execute("SELECT type FROM customer where cmobnum = ?",(phno.get(),))
        arows = cur3.fetchone()
        rows = cur.fetchone()
        prows = cur2.fetchone()

        if rows is None:
             rootl.destroy()
             messagebox.showerror("Error", "Incorrect username")
        if prows is None:
             rootl.destroy()
             messagebox.showerror("Error", "Incorrect phone number")
        else:
             for row in rows:
                  if(row == username.get()):
                       for prow in prows:
                            if(prow == phno.get()):
                                for a in arows:
                                    if(a == 'customer'):
                                        rootl.destroy()
                                        customer_homePage(phno2)
                                    else:
                                        rootl.destroy()
                                        messagebox.showerror("Error","Incorrect login type!")


    con = sql_connection()

    heading = Label(rootl,text="LOGIN",font=("Oxygen",25,"bold"),
                    fg="#ffffff",bg="#212121")
    heading.place(x=270,y=35)

    loginframe2 = Frame(rootl,bg="#ffffff",height=380,width=450)
    loginframe2.place(x=120,y=120)

    userlabel = Label(loginframe2,text="Username : ",font=("Noto sans",12,"bold"),
                      bg="#ffffff")
    userlabel.place(x=40,y=70)


    userentry = Entry(loginframe2,width=34,relief="flat",bg="#c2c2c2",textvariable=username,
                      font=("Oxygen",13))
    userentry.place(x=45,y=120)


    passlabel = Label(loginframe2,text="Phone number : ",font=("Noto sans",12,"bold"),
                      bg="#ffffff")
    passlabel.place(x=40,y=170)

    passentry = Entry(loginframe2,width=34,relief="flat",bg="#c2c2c2",textvariable=phno,
                      font=("Oxygen",13))
    passentry.place(x=45,y=220)

    loginbtn = Button(loginframe2,text="Login",font=("Nunito",13,"bold"),bg="#ffb300",
                      fg="#000000",relief="flat",width=8,activebackground="#ffb300"
                       ,command=lambda : user_check(con,username,phno2))
    loginbtn.place(x=195,y=300)

    registerbtn = Button(loginframe2,text="Sign up",font=("Nunito",13,"bold"),bg="#ff5722",
                      fg="#000000",relief="flat",width=8,activebackground="#ff5722",
                     command=lambda : regNewCust())
    registerbtn.place(x=320,y=300)


    rootl.mainloop()


#--------------------------------------------------------------------------------RETAILER LOGIN CONFIRMATION--------------------------------------------------------------------------------

def adminloginConfirm():
    rootl = Tk()
    rootl.geometry("680x570+100+30")
    rootl.title("Login window")
    rootl.config(bg="#212121")

    username = StringVar(rootl)
    phno = IntVar(rootl)

    def user_check(con,username):
        cur = con.cursor()
        cur2 = con.cursor()
        cur3 = con.cursor()
        cur.execute("SELECT cname FROM customer where cname = ?",(username.get(),))
        cur2.execute("SELECT cmobnum FROM customer where cmobnum = ? and cname = ?",(phno.get(),username.get(),))
        cur3.execute("SELECT type FROM customer where cmobnum = ?",(phno.get(),))
        arows = cur3.fetchone()
        rows = cur.fetchone()
        prows = cur2.fetchone()

        if rows is None:
             rootl.destroy()
             messagebox.showerror("Error", "Incorrect username")
        if prows is None:
             rootl.destroy()
             messagebox.showerror("Error", "Incorrect phone number")
        else:
             for row in rows:
                  if(row == username.get()):
                       for prow in prows:
                            if(prow == phno.get()):
                                for a in arows:
                                    if(a == 'admin'):
                                        rootl.destroy()
                                        retailer_homePage()
                                    else:
                                        rootl.destroy()
                                        messagebox.showerror("Error","Incorrect login type!")


    con = sql_connection()

    heading = Label(rootl,text="LOGIN",font=("Noto sans",17,"bold"),
                    fg="#ffffff",bg="#212121")
    heading.place(x=260,y=35)

    loginframe2 = Frame(rootl,bg="#ffffff",height=380,width=450)
    loginframe2.place(x=120,y=120)

    userlabel = Label(loginframe2,text="Username : ",font=("Noto sans",12,"bold"),
                      bg="#ffffff")
    userlabel.place(x=40,y=70)


    userentry = Entry(loginframe2,width=34,relief="flat",bg="#c2c2c2",textvariable=username,
                      font=("Oxygen",13))
    userentry.place(x=45,y=120)


    passlabel = Label(loginframe2,text="Phone number : ",font=("Noto sans",12,"bold"),
                      bg="#ffffff")
    passlabel.place(x=40,y=170)

    passentry = Entry(loginframe2,width=34,relief="flat",bg="#c2c2c2",textvariable=phno,
                      font=("Oxygen",13))
    passentry.place(x=45,y=220)

    loginbtn = Button(loginframe2,text="Login",font=("Nunito",13,"bold"),bg="#ffb300",
                      fg="#000000",relief="flat",width=8,activebackground="#ffb300"
                       ,command=lambda : user_check(con,username))
    loginbtn.place(x=195,y=300)

    registerbtn = Button(loginframe2,text="Sign up",font=("Nunito",13,"bold"),bg="#ff5722",
                      fg="#000000",relief="flat",width=8,activebackground="#ff5722",
                     command=lambda : regNewAdmin())
    registerbtn.place(x=320,y=300)


    rootl.mainloop()

#---------------------------------------------------------------------------RETAILER HOME PAGE------------------------------------------------------------------------------------------------------------------------------------------------------------------

def retailer_homePage():

    def analysis_page():

        def get_selected_date(selection):
            selected_date = selection
            print (selected_date)

        def change_piechart():
            z1 = con.cursor()
            z1.execute("select sum(pprice) as inventory_total from inventory;")
            f1 = z1.fetchone()

            z2 = con.cursor()
            z2.execute("select sum(pprice) as sales_total from inventory , sales where inventory.pid = sales.pid and sales.date = ? ;",(selected_date.get(),))
            f2 = z2.fetchone()

            for x in f1:
                val1 = x

            for y in f2:
                val2 = y

            labels = [val1,val2]

            fig2 = matplotlib.figure.Figure(figsize=(4,3))
            ax = fig2.add_subplot(111)
            ax.pie([f1,f2],labels=labels,startangle=90)
            ax.legend(["Total","Gain"])
            circle=matplotlib.patches.Circle( (0,0), 0.7, color='white')
            ax.add_artist(circle)
            fig2.set_facecolor("#4fc3f7")

            canvas2 = FigureCanvasTkAgg(fig2, master=rootan)
            canvas2.get_tk_widget().place(x=270,y=330)
            canvas2.draw()


        rootan = Tk()
        rootan.geometry("940x610+100+50")
        rootan.title("Retailer Analysis")
        rootan.config(bg="#4fc3f7")
        selected_date = StringVar(rootan)

        x = []
        y = []

        analysislabel = Label(rootan,text="Retailer Analysis",font=("Lobster Two",20,"bold"),fg="#ffffff",
                              bg="#4fc3f7")
        analysislabel.pack()
        # navbar = Frame(rootan,bg="#212121",height=50,width=920)
        # navbar.place(x=0,y=0)
        g1 = con.cursor()
        g1.execute("select pcategory as purchased from inventory,sales where inventory.pid = sales.pid GROUP by pcategory;")
        fetch = g1.fetchall()

        for data in fetch:
            x.extend(data)

        g2 = con.cursor()
        g2.execute("select count(sales.pid) as purchased from inventory,sales where inventory.pid = sales.pid GROUP by pcategory;")
        fet = g2.fetchall()

        for dat in fet:
            y.extend(dat)

        fig = Figure(figsize=(5,3), dpi=90)
        fig.suptitle('Category - wise', fontsize = 16)
        axes = fig.add_subplot(111)
        axes.plot(x,y)

        canvas = FigureCanvasTkAgg(fig,rootan)
        canvas.get_tk_widget().pack(side=LEFT,anchor=NW,pady=(20,0),padx=(10,0))
        fig.set_facecolor("#81d4fa")

        top5 = Label(rootan,text="Top 5 items :",font=("Oxygen",14,"bold"),fg="#212121",
                                  bg="#4fc3f7")
        top5.place(x=650,y=60)

        c = con.cursor()
        top = c.execute("select pname,pcategory,count(pname) from inventory,sales where inventory.pid = sales.pid group by pname order by count(pname) DESC LIMIT 5;")
        fetc = c.fetchall()

        tree = Treeview(rootan,columns=('pname','pcategory','count(pname)'))
        tree.heading('pname', text='Product Name')
        tree.heading('pcategory', text='Category')
        tree.heading('count(pname)', text='Purchased count')
        tree.column("pname",width=90)
        tree.column("pcategory",width=90)
        tree.column("count(pname)",width=90)
        tree.pack(side=RIGHT,anchor=NE,pady=(52,0) , padx=(0,10))
        tree['show'] = 'headings'

        for data in fetc:
            tree.insert('', 'end', values=(data))

        options = []

        d = con.cursor()
        d.execute("select distinct(date) from sales;")
        val = d.fetchall()

        for data in val:
            options.extend(data)

        selected_date.set(options[1])

        w = OptionMenu(rootan, selected_date,*options ,command = get_selected_date)
        w.place(x=100,y=460)
        w.configure(background="#ffffff",relief="flat")

        date_show_pie = Button(rootan,text="Show",font=("Nunito",10,"bold"),bg="#ff5722",
                              fg="#000000",relief="flat",width=8,activebackground="#ff5722",command = change_piechart)
        date_show_pie.place(x=100,y=500)

        rootan.mainloop()

    def updateStock():
        a=con.cursor()
        a.execute("UPDATE stock SET total_quantity = ? WHERE pid =?",(updateNewQuantity.get(),updateStockId.get(),))
        a.execute("UPDATE inventory SET pprice = ? WHERE pid = ?",(updateStockPrice.get(),updateStockId.get(),))
        con.commit()
        rootm.destroy()
        retailer_homePage()


    def addItem():
        c=con.cursor()
        x=con.cursor()
        c.execute("INSERT INTO inventory (pname,pprice) VALUES(?,?)",(itemName.get(),itemPrice.get(),))
        x.execute("INSERT INTO stock(total_quantity) VALUES(?)",(itemStock.get(),))
        con.commit()
        rootm.destroy()
        retailer_homePage()

    def removeItem():
        a=con.cursor()
        b=con.cursor()
        a.execute("DELETE FROM inventory where pid = ?",(removeItemId.get(),))
        b.execute("DELETE FROM stock where pid = ?",(removeItemId.get(),))
        con.commit()
        rootm.destroy()
        retailer_homePage()


    rootm = Tk()
    rootm.geometry("920x570+100+50")
    rootm.title("Home")
    rootm.config(bg="#ffe0b2")

    itemName = StringVar(rootm)
    itemPrice = IntVar(rootm)
    itemStock = IntVar(rootm)
    removeItemId = IntVar(rootm)
    updateStockId = IntVar(rootm)
    updateNewQuantity = IntVar(rootm)
    updateStockPrice = IntVar(rootm)

    searchVar = StringVar(rootm)
    treeVals = []

    c=con.cursor()
    def command(self, *args):
        selections = []

        for i in range(len(treeVals)):
            if searchVar.get() != "" and searchVar.get() == treeVals[i][:len(searchVar.get())]:
                selections.append(ids[i])
                print(selections)#if it matches it appends the id to the selections list

        tree.selection_set(selections) # Highlights the name in treeview

    c.execute("SELECT inventory.pid,pname,pprice,total_quantity FROM `inventory`,`stock`  where stock.pid=inventory.pid ORDER BY inventory.pid ASC")
    fetch = c.fetchall()

    tree = Treeview(rootm,columns=('pid','pname','pprice','total_quantity'))
    tree.heading('pid', text='Product ID')
    tree.heading('pname', text='Product Name')
    tree.heading('pprice', text='Price')
    tree.heading('total_quantity', text='Stock Quantity')
    tree.column("pid",width=90)
    tree.column("pname",width=90)
    tree.column("pprice",width=90)
    tree.column("total_quantity",width=90)
    tree.pack(side=RIGHT,anchor=NE,fill='y',pady=(52,0))
    tree['show'] = 'headings'

    ids = []
    for data in fetch:
        ids.append(tree.insert('', 'end', values=(data)))

    for child in tree.get_children():
        treeVals.append(tree.item(child)['values'][1])

    navbar = Frame(rootm,bg="#212121",height=50,width=920)
    navbar.place(x=0,y=0)

    searchVar.trace("w",command)
    search =  Entry(rootm,width=34,relief="flat",bg="#ffffff",textvariable=searchVar,
                      font=("Oxygen",10))
    search.insert(0,'Quick Search')
    search.place(x=500,y=15)

    print(ids)
    print(treeVals)

    analysisbtn = Button(navbar,text="Analysis",font=("Noto sans",12,"bold"),fg="#ffffff",
                        bg="#2979ff",relief = "flat",command= lambda: analysis_page())
    analysisbtn.place(x=230,y=5)

    outbtn= Button(navbar,text="Back",font=("Noto sans",12,"bold"),fg="#ffffff",
                        bg="#c62828",relief = "flat",command=rootm.destroy)
    outbtn.place(x=830,y=5)

    addFrame = Frame(rootm,bg="#03a9f4",height=160,width=520)
    addFrame.place(x=10,y=55)

    removeFrame = Frame(rootm,bg="#03a9f4",height=160,width=520)
    removeFrame.place(x=10,y=230)

    updateFrame = Frame(rootm,bg="#03a9f4",height=160,width=520)
    updateFrame.place(x=10,y=405)

#-----------------------------------------Update Stock Button------------------------------------------------------------------------------------------------

    update_button = Button(updateFrame, text='Update',font=("Nunito",10,"italic"),bg="#ffb300",
                  fg="#000000",relief="flat",width=7,activebackground="#ffb300",command = lambda :  updateStock())
    update_button.place(x=450,y=125)

    updateHeadingLabel = Label(updateFrame,text="Update Item :",font=("Roboto",12,"underline"),
                fg="#212121",bg="#03a9f4")
    updateHeadingLabel.place(x=5,y=10)

    updateitemLabel = Label(updateFrame,text="Enter item id  : ",font=("Noto sans",10,"bold"),
                fg="#212121",bg="#03a9f4")
    updateitemLabel.place(x=5,y=70)

    updateitemEntry =  Entry(updateFrame,width=34,relief="flat",bg="#ffffff",textvariable=updateStockId,
                  font=("Oxygen",10))
    updateitemEntry.place(x=200,y=70)

    updateitemLabel = Label(updateFrame,text="Enter item price  : ",font=("Noto sans",10,"bold"),
                    fg="#212121",bg="#03a9f4")
    updateitemLabel.place(x=5,y=100)

    updateitemEntry =  Entry(updateFrame,width=34,relief="flat",bg="#ffffff",textvariable=updateStockPrice,
                      font=("Oxygen",10))
    updateitemEntry.place(x=200,y=100)

    updateitemLabel = Label(updateFrame,text="Enter  new quantity  : ",font=("Noto sans",10,"bold"),
                fg="#212121",bg="#03a9f4")
    updateitemLabel.place(x=5,y=130)

    updateitemEntry =  Entry(updateFrame,width=34,relief="flat",bg="#ffffff",textvariable=updateNewQuantity,
                  font=("Oxygen",10))
    updateitemEntry.place(x=200,y=130)


#-----------------------------------------Add Button-------------------------------------------------------------------------------------------

    add_button = Button(addFrame, text='Add',font=("Nunito",10,"italic"),bg="#ffb300",
                  fg="#000000",relief="flat",width=7,activebackground="#ffb300",command = lambda :  addItem())
    add_button.place(x=450,y=125)

    addLabel = Label(addFrame,text="Add New Item : ",font=("Roboto",12,"underline"),
                fg="#212121",bg="#03a9f4")
    addLabel.place(x=5,y=10)

    newitemLabel = Label(addFrame,text="New Item Name : ",font=("Noto sans",10,"bold"),
                fg="#212121",bg="#03a9f4")
    newitemLabel.place(x=5,y=40)

    newitemEntry =  Entry(addFrame,width=34,relief="flat",bg="#ffffff",textvariable=itemName,
                  font=("Oxygen",10))
    newitemEntry.place(x=200,y=40)

    newitemPriceLabel = Label(addFrame,text="New Item Price : ",font=("Noto sans",10,"bold"),
                fg="#212121",bg="#03a9f4")
    newitemPriceLabel.place(x=5,y=70)

    newitemPriceEntry =  Entry(addFrame,width=34,relief="flat",bg="#ffffff",textvariable=itemPrice,
                  font=("Oxygen",10))
    newitemPriceEntry.place(x=200,y=70)

    newitemStockLabel = Label(addFrame,text="New Item Quantity/Stock : ",font=("Noto sans",10,"bold"),
                fg="#212121",bg="#03a9f4")
    newitemStockLabel.place(x=5,y=100)

    newitemStockEntry =  Entry(addFrame,width=34,relief="flat",bg="#ffffff",textvariable=itemStock,
                  font=("Oxygen",10))
    newitemStockEntry.place(x=200,y=100)

#-------------------------------------------------Remove Button-------------------------------------------------------------------------------------------
    remove_button = Button(removeFrame, text='Remove',font=("Nunito",10,"italic"),bg="#ffb300",
                  fg="#000000",relief="flat",width=7,activebackground="#ffb300",command = lambda :  removeItem())
    remove_button.place(x=450,y=125)

    removeHeadingLabel = Label(removeFrame,text="Remove item :",font=("Roboto",12,"underline"),
                fg="#212121",bg="#03a9f4")
    removeHeadingLabel.place(x=5,y=10)

    removeitemLabel = Label(removeFrame,text="Enter item id  : ",font=("Noto sans",10,"bold"),
                fg="#212121",bg="#03a9f4")
    removeitemLabel.place(x=5,y=70)

    removeitemEntry =  Entry(removeFrame,width=34,relief="flat",bg="#ffffff",textvariable=removeItemId,
                  font=("Oxygen",10))
    removeitemEntry.place(x=200,y=70)

    rootm.mainloop()


#----------------------------------------------------------CUSTOMER HOME PAGE----------------------------------------------------------------------------------------------------------------------------------------------------


def customer_homePage(phno2):

    def customer_analysis():
        print(phno2.get())

        def get_selected_date(selection):
            selected_date = selection
            print (selected_date)

        rootan = Tk()
        rootan.geometry("940x610+100+50")
        rootan.title("Customer Analysis")
        rootan.config(bg="#4fc3f7")
        selected_date = StringVar(rootan)

        x = []
        y = []
        a = []
        b = []

        analysislabel = Label(rootan,text="Customer Analysis",font=("Lobster Two",20,"bold"),fg="#ffffff",
                              bg="#4fc3f7")
        analysislabel.pack()

        g1 = con.cursor()
        g1.execute("select pcategory as purchased from inventory,sales where inventory.pid = sales.pid and cmobnum = ? GROUP by pcategory;",(phno2.get(),))
        fetch = g1.fetchall()

        for data in fetch:
            x.extend(data)

        g2 = con.cursor()
        g2.execute("select count(sales.pid) as purchased from inventory,sales where inventory.pid = sales.pid and cmobnum = ? GROUP by pcategory;",(phno2.get(),))
        fet = g2.fetchall()

        for dat in fet:
            y.extend(dat)

        fig = Figure(figsize=(5,3), dpi=80)
        fig.suptitle('Category - wise', fontsize = 16)
        axes = fig.add_subplot(111)
        axes.plot(x,y)

        canvas = FigureCanvasTkAgg(fig,rootan)
        canvas.get_tk_widget().place(x = 20 , y=350)
        fig.set_facecolor("#81d4fa")

        c = con.cursor()
        top = c.execute("select pname,pcategory,count(pname) from inventory,sales where inventory.pid = sales.pid and cmobnum = ? group by pname order by count(pname) DESC LIMIT 5;",(phno2.get(),))
        fetc = c.fetchall()

        top5 = Label(rootan,text="Most recently bought :",font=("Oxygen",16,"bold"),fg="#212121",
                              bg="#4fc3f7")
        top5.place(x=650,y=100)

        tree = Treeview(rootan,columns=('pname','pcategory','count(pname)'))
        tree.heading('pname', text='Product Name')
        tree.heading('pcategory', text='Category')
        tree.heading('count(pname)', text='Purchased count')
        tree.column("pname",width=90)
        tree.column("pcategory",width=90)
        tree.column("count(pname)",width=90)
        tree.place(x=650,y=150)
        tree['show'] = 'headings'

        for data in fetc:
            tree.insert('', 'end', values=(data))

        options = []

        d = con.cursor()
        d.execute("select distinct(date) from sales;")
        val = d.fetchall()

        for data in val:
            options.extend(data)

        selected_date.set(options[1])

        p = con.cursor()
        p.execute("""select sum(pprice) from inventory,sales where sales.pid = inventory.pid and cmobnum = ? group by strftime("%m",date) order by strftime("%m",date)""",(phno2.get(),))
        fetc = p.fetchall()

        i = con.cursor()
        i.execute("""select distinct  strftime("%m",date) as month from sales order by month;""")
        fet = i.fetchall()


        for dat in fetc:
            a.extend(dat)

        for data in fet:
            b.extend(data)


        fig2 = Figure(figsize=(5,3), dpi=80)
        fig2.suptitle('Monthly Spendings', fontsize = 16)
        axes2 = fig2.add_subplot(111)
        axes2.plot(b,a)

        canvas2 = FigureCanvasTkAgg(fig2,rootan)
        canvas2.get_tk_widget().place(x=20 , y=80)
        fig2.set_facecolor("#81d4fa")


        outbtn= Button(rootan,text="Back",font=("Noto sans",12,"bold"),fg="#ffffff",
                                bg="#c62828",relief = "flat",command=rootan.destroy)
        outbtn.place(x=830,y=5)

        rootan.mainloop()


    def add_sales(roots):
        roots.destroy()
        a=con.cursor()
        b=con.cursor()
        c=con.cursor()
        d=con.cursor()
        flag=0
        for data in tree2.get_children():
            val=(tree2.item(data)["values"][0])
            a.execute("SELECT pid FROM inventory WHERE pname = ?",(val,))
            fetch = a.fetchone()
            for x in fetch:
                d.execute("SELECT total_quantity FROM stock WHERE pid = ?",(x,))
                val = d.fetchone()
                for y in val:
                    print(y)
                    if(y >=1):
                        b.execute("INSERT INTO sales(cmobnum,pid,date) VALUES (?,?,?)",(phno2.get(),x,datetime.date(datetime.now()),))
                        c.execute("UPDATE stock SET total_quantity = total_quantity -1 WHERE pid = ?",(x,))
                        flag = flag+1
                    else:
                        messagebox.showerror("Error","Stock Empty!")

        if flag > 0:
            messagebox.showinfo("Success","Item Purchased")
        # charge()
        con.commit()

    def submit(tree2):
        roots = Tk()
        roots.geometry("920x570+100+50")
        roots.title("Billing")
        roots.config(bg="#ffe0b2")

        c=con.cursor()

        s=0
        for child in tree2.get_children():
            s=s+tree2.item(child)["values"][1]
        totalSum.set(s)

        navbar2 = Frame(roots,bg="#212121",height=50,width=920)
        navbar2.place(x=0,y=0)

        outbtn= Button(navbar2,text="Back",font=("Noto sans",12,"bold"),fg="#ffffff",
                            bg="#c62828",relief = "flat",command=roots.destroy)
        outbtn.place(x=830,y=5)


        tree3 = Treeview(roots,columns=('pname','pprice'))
        tree3.heading('pname', text='Product Name')
        tree3.heading('pprice', text='Price')
        tree3.column("pname",width=90)
        tree3.column("pprice",width=90)
        tree3.pack(side=LEFT,anchor=N,fill='x',expand=TRUE,pady=(90,0))
        tree3['show'] = 'headings'

        for data in tree2.get_children():
            tree3.insert('', '0', values=(tree2.item(data)["values"]))

        buyButton= Button(roots,text="Buy",font=("Noto sans",12,"bold"),fg="#ffffff",
                            bg="#c62828",relief = "flat",command=lambda : add_sales(roots) )
        buyButton.place(x=830,y=450)

        total_label =  Label(roots,text="Total : ",font=("Noto sans",12,"bold"),
                fg="#212121",bg="#ffe0b2")
        total_label.place(x=200,y=400)

        total_labelVal =  Label(roots,text=totalSum.get(),font=("Noto sans",12,"bold"),
                fg="#212121",bg="#ffe0b2")
        total_labelVal.place(x=260,y=400)

        roots.mainloop()


    rootc = Tk()
    rootc.geometry("920x570+100+50")
    rootc.title("Home")
    rootc.config(bg="#ffe0b2")

    searchVar = StringVar(rootc)
    totalSum = IntVar(rootc)
    treeVals = []
    loginName = StringVar()
    c=con.cursor()

    navbar = Frame(rootc,bg="#212121",height=50,width=920)
    navbar.place(x=0,y=0)

    u = con.cursor()
    u.execute("SELECT cname from customer where cmobnum = ?",(phno2.get(),))
    fe = u.fetchone()

    for x in fe:
        loginName.set(x)

    welcomeUser = Label(navbar,text="Hello : ",font=("Noto sans",12,"bold"),
            fg="#ffffff",bg="#212121")
    welcomeUser.place(x=10,y=8)

    welcomeUserVal = Label(navbar,text=loginName.get(),font=("Oxygen",12,"bold"),
            fg="#ffffff",bg="#212121")
    welcomeUserVal.place(x=70,y=8)

    analysisbtn = Button(navbar,text="Analysis",font=("Noto sans",12,"bold"),fg="#ffffff",
                            bg="#2979ff",relief = "flat",command= lambda: customer_analysis())
    analysisbtn.place(x=260,y=5)

    outbtn= Button(navbar,text="Back",font=("Noto sans",12,"bold"),fg="#ffffff",
                        bg="#c62828",relief = "flat",command=rootc.destroy)
    outbtn.place(x=830,y=5)

    def check():
        s=0
        for child in tree2.get_children():
            s=s+tree2.item(child)["values"][1]
        totalSum.set(s)
        total_label =  Label(rootc,text=totalSum.get(),font=("Noto sans",12,"bold"),
                fg="#212121",bg="#ffe0b2")
        total_label.place(x=245,y=544)

    def add_name():

        x = tree.focus()
        y = tree.item(x,"values")
        tree2.insert('', '0', values=(y))

    def remove_name():
        x = tree2.selection()
        tree2.delete(x)

    def command(self, *args):
        selections = []

        for i in range(len(treeVals)):
            if searchVar.get() != "" and searchVar.get() == treeVals[i][:len(searchVar.get())]:
                selections.append(ids[i])
                print(selections)#if it matches it appends the id to the selections list
        tree.selection_set(selections)


    c.execute("SELECT pname,pprice FROM `inventory` ORDER BY pid ASC")
    fetch = c.fetchall()


    selection_label = Label(rootc,text="Select Product To Add  ",font=("Noto sans",10,"bold"),
                fg="#212121",bg="#ffe0b2")
    selection_label.place(x=740,y=52)


    tree = Treeview(rootc,columns=('pname','pprice'))
    tree.heading('pname', text='Product Name')
    tree.heading('pprice', text='Price')
    tree.column("pname",width=90)
    tree.column("pprice",width=90)
    tree.pack(side=RIGHT,anchor=NE,fill='y',pady=(72,0))
    tree['show'] = 'headings'

    searchVar.trace("w",command)
    search =  Entry(rootc,width=34,relief="flat",bg="#ffffff",textvariable=searchVar,
                  font=("Oxygen",10))
    search.insert(0,'Quick Search')
    search.place(x=500,y=15)

    ids = []
    for data in fetch:
        ids.append(tree.insert('', 'end', values=(data)))


    for child in tree.get_children():
        treeVals.append(tree.item(child)['values'][0])

    print(ids)
    print(treeVals)

    cart_label = Label(rootc,text="Your Cart : Select to remove an item ",font=("Noto sans",10,"bold"),
                fg="#212121",bg="#ffe0b2")
    cart_label.place(x=2,y=52)

    tree2 = Treeview(rootc,columns=('pname','pprice'))
    tree2.heading('pname', text='Product Name')
    tree2.heading('pprice', text='Price')
    tree2.column("pname",width=90)
    tree2.column("pprice",width=90)
    tree2.pack(side=LEFT,anchor=W,fill='y',pady=(72,0))
    tree2['show'] = 'headings'


    add_button = Button(rootc, text='Add',font=("Oxygen",10,"bold"),fg="#ffffff",
                        bg="#0091ea",relief = "flat",command=add_name)
    add_button.place(x=380,y=235)

    remove_button = Button(rootc, text='Remove',font=("Oxygen",10,"bold"),fg="#ffffff",
                        bg="#0091ea",relief = "flat",command=remove_name)
    remove_button.place(x=428,y=235)

    check_button = Button(rootc, text='Check',font=("Oxygen",10,"bold"),fg="#ffffff",
                        bg="#0091ea",relief = "flat",command=check)
    check_button.place(x=500,y=235)

    submit_button = Button(rootc, text='Submit',font=("Oxygen",10,"bold"),fg="#ffffff",
                        bg="#1de9b6",relief = "flat",command= lambda : submit(tree2))
    submit_button.place(relx=0.5, rely=0.5, anchor=CENTER)


    total_label =  Label(rootc,text="Total : ",font=("Noto sans",12,"bold"),
                fg="#212121",bg="#ffe0b2")
    total_label.pack(side=BOTTOM,anchor=SW)


    con.commit()
    rootc.mainloop()


#--------------------------------------------------------------------------MAIN MENU----------------------------------------------------------------------------------------------------------------------------------------------------
root = Tk()
root.geometry("920x570+100+50")
root.title("SelfCheckout")
root.config(bg="#ffe0b2")

con = sql_connection()

username = StringVar()
phno2 = IntVar()

def entered_home(event):
        retailer_button.config(fg="#000000",bg="#ffa000")

def left_home(event):
        retailer_button.config(fg="#000000",bg="#ffb300")

def entered_customer(event):
         customer_button.config(fg="#000000",bg="#ffa000")

def left_customer(event):
        customer_button.config(fg="#000000",bg="#ffb300")

def entered_edit(event):
        edit_button.config(fg="#000000",bg="#ffa000")

def left_edit(event):
        edit_button.config(fg="#000000",bg="#ffb300")

def entered_userlabel(event):
        userlabel.config(fg="#ff7043",bg="#212121")

def left_userlabel(event):
        userlabel.config(fg="#ffffff",bg="#212121")


navbar = Frame(root,bg="#212121",height=50,width=920)
navbar.place(x=0,y=0)

userlabel = Label(navbar,text="Self Checkout - Home",font=("Lobster Two",14,"bold"),fg="#ffffff",
                      bg="#212121")
userlabel.place(x=380,y=8)
userlabel.bind("<Enter>", entered_userlabel)
userlabel.bind("<Leave>", left_userlabel)



menu =  Frame(root,bg="#ffffff",height=470,width=920)
menu.place(x=0,y=100)

#-------------------------------------------------------------------------------------------------------------------------

fra1 = Frame(menu,bg="#03a9f4",height=260,width=260)
fra1.place(x=110,y=95)


img1 = ImageTk.PhotoImage(Image.open("edit.jpg"))

retailerimg = Label(fra1, image = img1,height=160,width=230)
retailerimg.place(x=13,y=15)


retailer_button = Button(fra1,text="Retailer",bg="#ffb300",fg="#000000",
                         font=("Nunito",11,"bold"),relief="flat",width=8,
                         activebackground="#ffb300",command= lambda: adminloginConfirm())
retailer_button.place(x=85,y=200)
retailer_button.bind("<Enter>", entered_home)
retailer_button.bind("<Leave>", left_home)

#-------------------------------------------------------------------------------------------------------------------------

fra2 = Frame(menu,bg="#03a9f4",height=260,width=260)
fra2.place(x=560,y=95)

img2 = ImageTk.PhotoImage(Image.open("customer.png"))
cateimage = Label(fra2, image = img2,height=160,width=230)
cateimage.place(x=13,y=15)

customer_button = Button(fra2,text="Customer",bg="#ffb300",fg="#000000",
                         font=("Nunito",11,"bold"),relief="flat",width=8,
                         activebackground="#ffb300",command= lambda: customerloginConfirm(phno2))
customer_button.place(x=85,y=200)
customer_button.bind("<Enter>", entered_customer)
customer_button.bind("<Leave>", left_customer)

root.mainloop()
