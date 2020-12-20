import tkinter as tk
from tkinter import ttk
import sqlite3


class PetShopDialog(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    # self.db = db

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="button_grey_add.png")
        btn_open_dialog = tk.Button(toolbar, text='Add', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file='database_download.png')
        btn_edit_dialog = tk.Button(toolbar, text='Edit', bg='#d7d8e0', bd=0, image=self.update_img,
                                    compound=tk.TOP, command=self.open_update_dialog)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file='button_grey_delete.png')
        btn_delete_dialog = tk.Button(toolbar, text='Delete', bg='#d7d8e0', bd=0, image=self.delete_img,
                                      compound=tk.TOP)
        btn_delete_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='zoom_in.png')
        btn_search_dialog = tk.Button(toolbar, text='Search', bg='#d7d8e0', bd=0, image=self.search_img,
                                      compound=tk.TOP)
        btn_search_dialog.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='refresh.png')
        btn_search_dialog = tk.Button(toolbar, text='Refresh', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                      compound=tk.TOP)
        btn_search_dialog.pack(side=tk.LEFT)

        btn_customer_table = tk.Button(toolbar, text='Customer', command=self.customer_table, bg='#d7d8e0', bd=0,
                                       compound=tk.TOP)
        btn_customer_table.pack(side=tk.RIGHT)

        btn_employee_table = tk.Button(toolbar, text='Employee', command=self.employee_table, bg='#d7d8e0', bd=0,
                                       compound=tk.TOP)
        btn_employee_table.pack(side=tk.RIGHT)

        btn_order_table = tk.Button(toolbar, text='Order', command=self.order_table, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP)
        btn_order_table.pack(side=tk.RIGHT)

        btn_pet_table = tk.Button(toolbar, text='Pet', command=self.pet_table, bg='#d7d8e0', bd=0, compound=tk.TOP)
        btn_pet_table.pack(side=tk.RIGHT)

        btn_pet_food_table = tk.Button(toolbar, text='PetFood', command=self.pet_food_table, bg='#d7d8e0', bd=0,
                                       compound=tk.TOP)
        btn_pet_food_table.pack(side=tk.RIGHT)

        btn_pet_accessory_table = tk.Button(toolbar, text='PetAccessory', command=self.pet_accessory_table,
                                            bg='#d7d8e0', bd=0,
                                            compound=tk.TOP)
        btn_pet_accessory_table.pack(side=tk.RIGHT)

        btn_manufacturer_table = tk.Button(toolbar, text='Manufacturer', command=self.manufacturer_table, bg='#d7d8e0',
                                           bd=0,
                                           compound=tk.TOP)
        btn_manufacturer_table.pack(side=tk.RIGHT)

        self.tree = ttk.Treeview(self, columns=('ID', 'PetShopID', 'Name', 'Adress', 'PostalCode', 'Phone'),
                                 height=38, show='headings')

        self.tree.column('ID', width=100, anchor=tk.CENTER)
        self.tree.column('PetShopID', width=100, anchor=tk.CENTER)
        self.tree.column('Name', width=150, anchor=tk.CENTER)
        self.tree.column('Adress', width=200, anchor=tk.CENTER)
        self.tree.column('PostalCode', width=150, anchor=tk.CENTER)
        self.tree.column('Phone', width=250, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('PetShopID', text='PetShopID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Adress', text='Adress')
        self.tree.heading('PostalCode', text='PostalCode')
        self.tree.heading('Phone', text='Phone')

        self.tree.pack()

    def employee_table(self):
        EmployeeDialog()

    def customer_table(self):
        CustomerDialog()

    def order_table(self):
        OrderDialog()

    def pet_table(self):
        PetDialog()

    def pet_accessory_table(self):
        PetAccessoryDialog()

    def pet_food_table(self):
        PetFoodDialog()

    def manufacturer_table(self):
        ManufacturerDialog()

    def open_dialog(self):
        Child()

    def open_update_dialog(self):
        Update()


class CustomerDialog(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_main()

    # self.db = db

    def init_main(self):
        self.title("Customer Table")
        self.geometry("1020x900+300+200")
        self.resizable(False, False)
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="button_grey_add.png")
        btn_open_dialog = tk.Button(self, toolbar, text='Add', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file='database_download.png')
        btn_edit_dialog = tk.Button(self, toolbar, text='Edit', bg='#d7d8e0', bd=0, image=self.update_img,
                                    compound=tk.TOP, command=self.open_update_dialog)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file='button_grey_delete.png')
        btn_delete_dialog = tk.Button(self, toolbar, text='Delete', bg='#d7d8e0', bd=0, image=self.delete_img,
                                      compound=tk.TOP)
        btn_delete_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='zoom_in.png')
        btn_search_dialog = tk.Button(self, toolbar, text='Search', bg='#d7d8e0', bd=0, image=self.search_img,
                                      compound=tk.TOP)
        btn_search_dialog.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='refresh.png')
        btn_search_dialog = tk.Button(self, toolbar, text='Refresh', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                      compound=tk.TOP)
        btn_search_dialog.pack(side=tk.LEFT)

    def open_dialog(self):
        Child()

    def open_update_dialog(self):
        Update()


class EmployeeDialog(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_main()
        self.view = pet_shop_table

    # self.db = db

    def init_main(self):
        self.title("Employee Table")
        self.geometry("1020x900+300+200")
        self.resizable(False, False)
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="button_grey_add.png")
        btn_open_dialog = tk.Button(self, toolbar, text='Add', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file='database_download.png')
        btn_edit_dialog = tk.Button(self, toolbar, text='Edit', bg='#d7d8e0', bd=0, image=self.update_img,
                                    compound=tk.TOP, command=self.open_update_dialog)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file='button_grey_delete.png')
        btn_delete_dialog = tk.Button(self, toolbar, text='Delete', bg='#d7d8e0', bd=0, image=self.delete_img,
                                      compound=tk.TOP)
        btn_delete_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='zoom_in.png')
        btn_search_dialog = tk.Button(self, toolbar, text='Search', bg='#d7d8e0', bd=0, image=self.search_img,
                                      compound=tk.TOP)
        btn_search_dialog.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='refresh.png')
        btn_search_dialog = tk.Button(self, toolbar, text='Refresh', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                      compound=tk.TOP)
        btn_search_dialog.pack(side=tk.LEFT)

    def open_dialog(self):
        Child()

    def open_update_dialog(self):
        Update()


class OrderDialog(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_main()

    # self.db = db

    def init_main(self):
        self.title("Order Table")
        self.geometry("1020x900+300+200")
        self.resizable(False, False)
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="button_grey_add.png")
        btn_open_dialog = tk.Button(self, toolbar, text='Add', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file='database_download.png')
        btn_edit_dialog = tk.Button(self, toolbar, text='Edit', bg='#d7d8e0', bd=0, image=self.update_img,
                                    compound=tk.TOP, command=self.open_update_dialog)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file='button_grey_delete.png')
        btn_delete_dialog = tk.Button(self, toolbar, text='Delete', bg='#d7d8e0', bd=0, image=self.delete_img,
                                      compound=tk.TOP)
        btn_delete_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='zoom_in.png')
        btn_search_dialog = tk.Button(self, toolbar, text='Search', bg='#d7d8e0', bd=0, image=self.search_img,
                                      compound=tk.TOP)
        btn_search_dialog.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='refresh.png')
        btn_search_dialog = tk.Button(self, toolbar, text='Refresh', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                      compound=tk.TOP)
        btn_search_dialog.pack(side=tk.LEFT)

    def open_dialog(self):
        Child()

    def open_update_dialog(self):
        Update()


class PetDialog(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_main()

    # self.db = db

    def init_main(self):
        self.title("Pet Table")
        self.geometry("1020x700+300+200")
        self.resizable(False, False)
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="button_grey_add.png")
        btn_open_dialog = tk.Button(self, toolbar, text='Add', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file='database_download.png')
        btn_edit_dialog = tk.Button(self, toolbar, text='Edit', bg='#d7d8e0', bd=0, image=self.update_img,
                                    compound=tk.TOP, command=self.open_update_dialog)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file='button_grey_delete.png')
        btn_delete_dialog = tk.Button(self, toolbar, text='Delete', bg='#d7d8e0', bd=0, image=self.delete_img,
                                      compound=tk.TOP)
        btn_delete_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='zoom_in.png')
        btn_search_dialog = tk.Button(self, toolbar, text='Search', bg='#d7d8e0', bd=0, image=self.search_img,
                                      compound=tk.TOP)
        btn_search_dialog.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='refresh.png')
        btn_search_dialog = tk.Button(self, toolbar, text='Refresh', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                      compound=tk.TOP)
        btn_search_dialog.pack(side=tk.LEFT)

    def open_dialog(self):
        Child()

    def open_update_dialog(self):
        Update()


class PetFoodDialog(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_main()

    # self.db = db

    def init_main(self):
        self.title("PetFood Table")
        self.geometry("1020x900+300+200")
        self.resizable(False, False)
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="button_grey_add.png")
        btn_open_dialog = tk.Button(self, toolbar, text='Add', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file='database_download.png')
        btn_edit_dialog = tk.Button(self, toolbar, text='Edit', bg='#d7d8e0', bd=0, image=self.update_img,
                                    compound=tk.TOP, command=self.open_update_dialog)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file='button_grey_delete.png')
        btn_delete_dialog = tk.Button(self, toolbar, text='Delete', bg='#d7d8e0', bd=0, image=self.delete_img,
                                      compound=tk.TOP)
        btn_delete_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='zoom_in.png')
        btn_search_dialog = tk.Button(self, toolbar, text='Search', bg='#d7d8e0', bd=0, image=self.search_img,
                                      compound=tk.TOP)
        btn_search_dialog.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='refresh.png')
        btn_search_dialog = tk.Button(self, toolbar, text='Refresh', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                      compound=tk.TOP)
        btn_search_dialog.pack(side=tk.LEFT)

    def open_dialog(self):
        Child()

    def open_update_dialog(self):
        Update()


class PetAccessoryDialog(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_main()

    # self.db = db

    def init_main(self):
        self.title("PetAccessory Table")
        self.geometry("1020x900+300+200")
        self.resizable(False, False)
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="button_grey_add.png")
        btn_open_dialog = tk.Button(self, toolbar, text='Add', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file='database_download.png')
        btn_edit_dialog = tk.Button(self, toolbar, text='Edit', bg='#d7d8e0', bd=0, image=self.update_img,
                                    compound=tk.TOP, command=self.open_update_dialog)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file='button_grey_delete.png')
        btn_delete_dialog = tk.Button(self, toolbar, text='Delete', bg='#d7d8e0', bd=0, image=self.delete_img,
                                      compound=tk.TOP)
        btn_delete_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='zoom_in.png')
        btn_search_dialog = tk.Button(self, toolbar, text='Search', bg='#d7d8e0', bd=0, image=self.search_img,
                                      compound=tk.TOP)
        btn_search_dialog.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='refresh.png')
        btn_search_dialog = tk.Button(self, toolbar, text='Refresh', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                      compound=tk.TOP)
        btn_search_dialog.pack(side=tk.LEFT)

    def open_dialog(self):
        Child()

    def open_update_dialog(self):
        Update()


class ManufacturerDialog(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_main(toolbar=tk.Frame(bg='#d7d8e0', bd=2))
        self.open_dialog()
        self.open_update_dialog()

    # self.db = db

    def init_main(self, toolbar):
        self.title("Manufacturer Table")
        self.geometry("1020x900+300+200")
        self.resizable(False, False)
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="button_grey_add.png")
        btn_open_dialog = tk.Button(self, toolbar, text='Add', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file='database_download.png')
        btn_edit_dialog = tk.Button(self, toolbar, text='Edit', bg='#d7d8e0', bd=0, image=self.update_img,
                                    compound=tk.TOP)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file='button_grey_delete.png')
        btn_delete_dialog = tk.Button(self, toolbar, text='Delete', bg='#d7d8e0', bd=0, image=self.delete_img,
                                      compound=tk.TOP)
        btn_delete_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='zoom_in.png')
        btn_search_dialog = tk.Button(self, toolbar, text='Search', bg='#d7d8e0', bd=0, image=self.search_img,
                                      compound=tk.TOP)
        btn_search_dialog.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='refresh.png')
        btn_search_dialog = tk.Button(self, toolbar, text='Refresh', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                      compound=tk.TOP)
        btn_search_dialog.pack(side=tk.LEFT)


    def open_dialog(self):
        Child()

    def open_update_dialog(self):
        Update()


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_child()
        self.view = pet_shop_table

    def init_child(self):
        self.title("Insert Values")
        self.geometry('600x400')
        self.resizable(False, False)

        label_pet_shop_id = tk.Label(self, text='PetShopID:')
        label_pet_shop_id.place(x=180, y=50)
        label_name = tk.Label(self, text='Name:')
        label_name.place(x=180, y=80)
        label_adress = tk.Label(self, text='Adress:')
        label_adress.place(x=180, y=110)
        label_postal_code = tk.Label(self, text='PostalCode:')
        label_postal_code.place(x=180, y=140)
        label_phone = tk.Label(self, text='Phone:')
        label_phone.place(x=180, y=170)

        self.entry_pet_shop_id = ttk.Entry(self)
        self.entry_pet_shop_id.place(x=325, y=50)

        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=325, y=80)

        self.entry_adress = ttk.Entry(self)
        self.entry_adress.place(x=325, y=110)

        self.entry_postal_code = ttk.Entry(self)
        self.entry_postal_code.place(x=325, y=140)

        self.entry_phone = ttk.Entry(self)
        self.entry_phone.place(x=325, y=170)

        btn_cancel = ttk.Button(self, text='Close', command=self.destroy)
        btn_cancel.place(x=350, y=300)

        self.btn_add = ttk.Button(self, text='Add')
        self.btn_add.place(x=200, y=300)
        self.btn_add.bind('<Button-1>')



class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = pet_shop_table

    def init_edit(self):
        self.title('Edit')
        btn_edit = ttk.Button(self, text='Edit')
        btn_edit.place(x=200, y=300)
        btn_edit.bind('<Button-1>')

        self.btn_add.destroy()


class PetShopTable:
    def __init__(self):
        self.conn = sqlite3.connect("PetShop.db")
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXIST PetShop(ID integer primary key, PetShopID integer, Name varchar(10),
         Adress varchar(30), PostalCode varchar(10), Phone bigint)''')
        self.conn.commit()

    def insert_values(self, ID, PetShopID, Name, Adress, PostalCode, Phone):
        self.c.execute('''INSERT INTO PetShop(PetShopID, Name, Adress, PostalCode, Phone) VALUES(?, ?, ?, ?, ?)''',
                       (ID, PetShopID, Name, Adress, PostalCode, Phone))
        self.conn.commit()


class EmployeeTable:
    def __init__(self):
        self.conn = sqlite3.connect("PetShop.db")
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXIST PetShop(ID integer primary key, PetShopID integer, Name varchar(10),
         Adress varchar(30), PostalCode varchar(10), Phone bigint)''')
        self.conn.commit()

    def insert_values(self, ID, PetShopID, Name, Adress, PostalCode, Phone):
        self.c.execute('''INSERT INTO PetShop(PetShopID, Name, Adress, PostalCode, Phone) VALUES(?, ?, ?, ?, ?)''',
                       (ID, PetShopID, Name, Adress, PostalCode, Phone))
        self.conn.commit()


class OrderTable:
    def __init__(self):
        self.conn = sqlite3.connect("PetShop.db")
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXIST PetShop(ID integer primary key, PetShopID integer, Name varchar(10),
         Adress varchar(30), PostalCode varchar(10), Phone bigint)''')
        self.conn.commit()

    def insert_values(self, ID, PetShopID, Name, Adress, PostalCode, Phone):
        self.c.execute('''INSERT INTO PetShop(PetShopID, Name, Adress, PostalCode, Phone) VALUES(?, ?, ?, ?, ?)''',
                       (ID, PetShopID, Name, Adress, PostalCode, Phone))
        self.conn.commit()


class PetTable:
    def __init__(self):
        self.conn = sqlite3.connect("PetShop.db")
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXIST PetShop(ID integer primary key, PetShopID integer, Name varchar(10),
         Adress varchar(30), PostalCode varchar(10), Phone bigint)''')
        self.conn.commit()

    def insert_values(self, ID, PetShopID, Name, Adress, PostalCode, Phone):
        self.c.execute('''INSERT INTO PetShop(PetShopID, Name, Adress, PostalCode, Phone) VALUES(?, ?, ?, ?, ?)''',
                       (ID, PetShopID, Name, Adress, PostalCode, Phone))
        self.conn.commit()


class PetAccessoryTable:
    def __init__(self):
        self.conn = sqlite3.connect("PetShop.db")
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXIST PetShop(ID integer primary key, PetShopID integer, Name varchar(10),
         Adress varchar(30), PostalCode varchar(10), Phone bigint)''')
        self.conn.commit()

    def insert_values(self, ID, PetShopID, Name, Adress, PostalCode, Phone):
        self.c.execute('''INSERT INTO PetShop(PetShopID, Name, Adress, PostalCode, Phone) VALUES(?, ?, ?, ?, ?)''',
                       (ID, PetShopID, Name, Adress, PostalCode, Phone))
        self.conn.commit()


class PetFoodTable:
    def __init__(self):
        self.conn = sqlite3.connect("PetShop.db")
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXIST PetShop(ID integer primary key, PetShopID integer, Name varchar(10),
         Adress varchar(30), PostalCode varchar(10), Phone bigint)''')
        self.conn.commit()

    def insert_values(self, ID, PetShopID, Name, Adress, PostalCode, Phone):
        self.c.execute('''INSERT INTO PetShop(PetShopID, Name, Adress, PostalCode, Phone) VALUES(?, ?, ?, ?, ?)''',
                       (ID, PetShopID, Name, Adress, PostalCode, Phone))
        self.conn.commit()


class CustomerTable:
    def __init__(self):
        self.conn = sqlite3.connect("PetShop.db")
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXIST PetShop(ID integer primary key, PetShopID integer, Name varchar(10),
         Adress varchar(30), PostalCode varchar(10), Phone bigint)''')
        self.conn.commit()

    def insert_values(self, ID, PetShopID, Name, Adress, PostalCode, Phone):
        self.c.execute('''INSERT INTO PetShop(PetShopID, Name, Adress, PostalCode, Phone) VALUES(?, ?, ?, ?, ?)''',
                       (ID, PetShopID, Name, Adress, PostalCode, Phone))
        self.conn.commit()


class ManufacturerTable:
    def __init__(self):
        self.conn = sqlite3.connect("PetShop.db")
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXIST PetShop(ID integer primary key, PetShopID integer, Name varchar(10),
         Adress varchar(30), PostalCode varchar(10), Phone bigint)''')
        self.conn.commit()

    def insert_values(self, ID, PetShopID, Name, Adress, PostalCode, Phone):
        self.c.execute('''INSERT INTO PetShop(PetShopID, Name, Adress, PostalCode, Phone) VALUES(?, ?, ?, ?, ?)''',
                       (ID, PetShopID, Name, Adress, PostalCode, Phone))
        self.conn.commit()


if __name__ == "__main__":
    pet_shop_dialog = tk.Tk()
    pet_shop_table = PetShopDialog(pet_shop_dialog)
    pet_shop_table.pack()
    pet_shop_dialog.title("PetShop Table")
    pet_shop_dialog.geometry("1020x700+300+200")
    pet_shop_dialog.resizable(False, False)

    pet_shop_dialog.mainloop()
