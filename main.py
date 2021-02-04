import tkinter as tk
from tkinter import ttk
from DatabaseTables import *


class PetShopDialog(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = petshopvalues
        self.view_values()

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
                                      compound=tk.TOP, command=self.delete_values)
        btn_delete_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='zoom_in.png')
        btn_search_dialog = tk.Button(toolbar, text='Search', bg='#d7d8e0', bd=0, image=self.search_img,
                                      compound=tk.TOP, command=self.search_diaolog)
        btn_search_dialog.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='refresh.png')
        btn_search_dialog = tk.Button(toolbar, text='Refresh', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                      compound=tk.TOP, command=self.view_values)
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

        self.tree = ttk.Treeview(self, columns=('PetShopID', 'Name', 'Adress', 'PostalCode', 'City', 'Phone'),
                                 height=29, show='headings')

        self.tree.column('PetShopID', width=130, anchor=tk.CENTER)
        self.tree.column('Name', width=150, anchor=tk.CENTER)
        self.tree.column('Adress', width=235, anchor=tk.CENTER)
        self.tree.column('PostalCode', width=155, anchor=tk.CENTER)
        self.tree.column('City', width=155, anchor=tk.CENTER)
        self.tree.column('Phone', width=150, anchor=tk.CENTER)

        self.tree.heading('PetShopID', text='PetShopID', command=self.sort_values_by_id)
        self.tree.heading('Name', text='Name', command=self.sort_values_by_name)
        self.tree.heading('Adress', text='Adress', command=self.sort_values_by_adress)
        self.tree.heading('PostalCode', text='PostalCode', command=self.sort_values_by_postalcode)
        self.tree.heading('City', text='City', command=self.sort_values_by_city)
        self.tree.heading('Phone', text='Phone', command=self.sort_values_by_phone)

        self.tree.pack()

    def open_dialog(self):
        AddPetShop()

    def open_update_dialog(self):
        UpdatePetShop()

    def search_diaolog(self):
        SearchPetShop()

    def add_values(self, Name, Adress, PostalCode, City, Phone):
        self.db.insert_values(Name, Adress, PostalCode, City, Phone)
        self.view_values()

    def view_values(self):
        self.db.c.execute('''SELECT * FROM PetShop''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def update_values(self, Name, Adress, PostalCode, City, Phone):
        self.db.c.execute('''UPDATE PetShop SET Name=?, Adress=?, City=?, PostalCode=?, Phone=? WHERE PetShopID=?''',
                          (Name, Adress, PostalCode, City, Phone, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_values()

    def search_values(self, Name):
        Name = ('%' + Name + '%',)
        self.db.c.execute('''SELECT * FROM PetShop WHERE Name LIKE ?''', Name)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def delete_values(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('''DELETE FROM PetShop WHERE PetShopID=?''', (self.tree.set(selection_item, '#1'),))
        self.db.conn.commit()
        self.view_values()

    def sort_values_by_id(self):
        self.db.c.execute('SELECT * FROM PetShop ORDER BY PetShopID')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_name(self):
        self.db.c.execute('SELECT * FROM PetShop ORDER BY Name')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_adress(self):
        self.db.c.execute('SELECT * FROM PetShop ORDER BY Adress')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_postalcode(self):
        self.db.c.execute('SELECT * FROM PetShop ORDER BY PostalCode')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_city(self):
        self.db.c.execute('SELECT * FROM PetShop ORDER BY City')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_phone(self):
        self.db.c.execute('SELECT * FROM PetShop ORDER BY Phone')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

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


class AddPetShop(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_child()
        self.view = pet_shop_table

    def init_child(self):
        self.title("Insert Values")
        self.geometry('600x400')
        self.resizable(False, False)

        label_name = tk.Label(self, text='Name:')
        label_name.place(x=180, y=50)
        label_adress = tk.Label(self, text='Adress:')
        label_adress.place(x=180, y=80)
        label_postal_code = tk.Label(self, text='PostalCode:')
        label_postal_code.place(x=180, y=110)
        label_city = tk.Label(self, text='City:')
        label_city.place(x=180, y=140)
        label_phone = tk.Label(self, text='Phone:')
        label_phone.place(x=180, y=170)

        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=325, y=50)

        self.entry_adress = ttk.Entry(self)
        self.entry_adress.place(x=325, y=80)

        self.entry_postal_code = ttk.Entry(self)
        self.entry_postal_code.place(x=325, y=110)

        self.entry_city = ttk.Entry(self)
        self.entry_city.place(x=325, y=140)

        self.entry_phone = ttk.Entry(self)
        self.entry_phone.place(x=325, y=170)

        btn_cancel = ttk.Button(self, text='Close', command=self.destroy)
        btn_cancel.place(x=350, y=300)

        self.btn_add = ttk.Button(self, text='Add')
        self.btn_add.place(x=200, y=300)
        self.btn_add.bind('<Button-1>', lambda event: self.view.add_values(self.entry_name.get(),
                                                                           self.entry_adress.get(),
                                                                           self.entry_postal_code.get(),
                                                                           self.entry_city.get(),
                                                                           self.entry_phone.get()))


class UpdatePetShop(AddPetShop):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = pet_shop_table

    def init_edit(self):
        self.title('Edit')
        btn_edit = ttk.Button(self, text='Edit')
        btn_edit.place(x=200, y=300)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_values(self.entry_name.get(),
                                                                          self.entry_adress.get(),
                                                                          self.entry_postal_code.get(),
                                                                          self.entry_city.get(),
                                                                          self.entry_phone.get()))
        self.btn_add.destroy()


class SearchPetShop(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = pet_shop_table

    def init_search(self):
        self.title('Search For Values')
        self.geometry('300x100+400+300')
        self.resizable(False, False)

        label_search = tk.Label(self, text='Name: ')
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text='Close', command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text='Search')
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_values(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class CustomerDialog(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_customer()
        self.db = CustomerTable()
        self.view_values()

    def init_customer(self):
        self.title("Customer Table")
        self.geometry("1550x715")
        self.resizable(False, False)

        self.add_img = tk.PhotoImage(file="button_grey_add.png")
        btn_open_dialog = tk.Button(self, text='Add', command=self.open_dialog_customer, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img, padx="10", pady="3", font="10")
        btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file='database_download.png')
        btn_edit_dialog = tk.Button(self, text='Edit', command=self.update_dialog_customer, bg='#d7d8e0', bd=0,
                                    image=self.update_img, compound=tk.TOP, padx="10", pady="3", font="10")
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file='button_grey_delete.png')
        btn_delete_dialog = tk.Button(self, text='Delete', bg='#d7d8e0', bd=0, image=self.delete_img,
                                      compound=tk.TOP, padx="10", pady="3", font="10", command=self.delete_customer)
        btn_delete_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='zoom_in.png')
        btn_search_dialog = tk.Button(self, text='Search', bg='#d7d8e0', bd=0, image=self.search_img,
                                      compound=tk.TOP, padx="10", pady="3", font="10", command=self.search_diaolog)
        btn_search_dialog.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='refresh.png')
        btn_search_dialog = tk.Button(self, text='Refresh', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                      compound=tk.TOP, padx="10", pady="3", font="10", command=self.view_values)
        btn_search_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('CustomerID', 'LastName', 'FirstName', 'Adress', 'City', 'Phone',
                                                'PetShopID'),
                                 height=34, show='headings')

        self.tree.column('CustomerID', width=170, anchor=tk.CENTER)
        self.tree.column('LastName', width=200, anchor=tk.CENTER)
        self.tree.column('FirstName', width=190, anchor=tk.CENTER)
        self.tree.column('Adress', width=200, anchor=tk.CENTER)
        self.tree.column('City', width=150, anchor=tk.CENTER)
        self.tree.column('Phone', width=170, anchor=tk.CENTER)
        self.tree.column('PetShopID', width=90, anchor=tk.CENTER)

        self.tree.heading('CustomerID', text='CustomerID', command=self.sort_values_by_customerid)
        self.tree.heading('LastName', text='LastName', command=self.sort_values_by_lastname)
        self.tree.heading('FirstName', text='FirstName', command=self.sort_values_by_firstname)
        self.tree.heading('Adress', text='Adress', command=self.sort_values_by_adress)
        self.tree.heading('City', text='City', command=self.sort_values_by_city)
        self.tree.heading('Phone', text='Phone', command=self.sort_values_by_phone)
        self.tree.heading('PetShopID', text='PetShopID', command=self.sort_values_by_petshopid)

        self.tree.pack()

    def add_customer(self, LastName, FirstName, Adress, City, Phone, PetShopID):
        self.db.insert_values(LastName, FirstName, Adress, City, Phone, PetShopID)
        self.view_values()

    def view_values(self):
        self.db.c.execute('''SELECT * FROM Customer''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def update_customer(self, LastName, FirstName, Adress, City, Phone, PetShopID):
        self.db.c.execute('''UPDATE Customer SET LastName=?, FirstName=?, Adress=?, City=?, Phone=?,
         PetShopID=? WHERE CustomerID=?''',
                          (LastName, FirstName, Adress, City, Phone, PetShopID,
                           self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_values()

    def search_customer(self, LastName):
        LastName = ('%' + LastName + '%',)
        self.db.c.execute('''SELECT * FROM Customer WHERE LastName LIKE ?''', LastName)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def delete_customer(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('''DELETE FROM Customer WHERE CustomerID=?''', (self.tree.set(selection_item, '#1'),))
        self.db.conn.commit()
        self.view_values()

    def sort_values_by_customerid(self):
        self.db.c.execute('SELECT * FROM Customer ORDER BY CustomerID')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_lastname(self):
        self.db.c.execute('SELECT * FROM Customer ORDER BY LastName')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_firstname(self):
        self.db.c.execute('SELECT * FROM Customer ORDER BY FirstName')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_adress(self):
        self.db.c.execute('SELECT * FROM Customer ORDER BY Adress')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_city(self):
        self.db.c.execute('SELECT * FROM Customer ORDER BY City')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_phone(self):
        self.db.c.execute('SELECT * FROM Customer ORDER BY Phone')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_petshopid(self):
        self.db.c.execute('SELECT * FROM Customer ORDER BY PetShopID')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def open_dialog_customer(self):
        AddCustomer(self)

    def update_dialog_customer(self):
        UpdateCustomer(self)

    def search_diaolog(self):
        SearchCustomer(self)


class AddCustomer(tk.Toplevel):
    def __init__(self, CustomerDialog):
        super().__init__(pet_shop_dialog)
        self.init_child()
        self.view = CustomerDialog

    def init_child(self):
        self.title("Insert Values")
        self.geometry('600x400')
        self.resizable(False, False)

        label_lastname = tk.Label(self, text='LastName:')
        label_lastname.place(x=180, y=50)
        label_firstname = tk.Label(self, text='FirstName:')
        label_firstname.place(x=180, y=80)
        label_adress = tk.Label(self, text='Adress:')
        label_adress.place(x=180, y=110)
        label_city = tk.Label(self, text='City:')
        label_city.place(x=180, y=140)
        label_phone = tk.Label(self, text='Phone:')
        label_phone.place(x=180, y=170)
        label_petshopid = tk.Label(self, text='PetShopID:')
        label_petshopid.place(x=180, y=200)

        self.entry_lastname = ttk.Entry(self)
        self.entry_lastname.place(x=325, y=50)

        self.entry_firstname = ttk.Entry(self)
        self.entry_firstname.place(x=325, y=80)

        self.entry_adress = ttk.Entry(self)
        self.entry_adress.place(x=325, y=110)

        self.entry_city = ttk.Entry(self)
        self.entry_city.place(x=325, y=140)

        self.entry_phone = ttk.Entry(self)
        self.entry_phone.place(x=325, y=170)

        self.entry_petshopid = ttk.Entry(self)
        self.entry_petshopid.place(x=325, y=200)

        btn_cancel = ttk.Button(self, text='Close', command=self.destroy)
        btn_cancel.place(x=350, y=300)

        self.btn_add = ttk.Button(self, text='Add')
        self.btn_add.place(x=200, y=300)
        self.btn_add.bind('<Button-1>', lambda event: self.view.add_customer(self.entry_lastname.get(),
                                                                             self.entry_firstname.get(),
                                                                             self.entry_adress.get(),
                                                                             self.entry_city.get(),
                                                                             self.entry_phone.get(),
                                                                             self.entry_petshopid.get()))


class UpdateCustomer(AddCustomer):
    def __init__(self, CustomerDialog):
        super().__init__(pet_shop_dialog)
        self.init_edit()
        self.view = CustomerDialog

    def init_edit(self):
        self.title('Edit')
        btn_edit = ttk.Button(self, text='Edit')
        btn_edit.place(x=200, y=300)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_customer(self.entry_lastname.get(),
                                                                            self.entry_firstname.get(),
                                                                            self.entry_adress.get(),
                                                                            self.entry_city.get(),
                                                                            self.entry_phone.get(),
                                                                            self.entry_petshopid.get()))

        self.btn_add.destroy()


class SearchCustomer(tk.Toplevel):
    def __init__(self, CustomerDialog):
        super().__init__()
        self.init_search()
        self.view = CustomerDialog

    def init_search(self):
        self.title('Search For Values')
        self.geometry('300x100+400+300')
        self.resizable(False, False)

        label_search = tk.Label(self, text='LastName:')
        label_search.place(x=40, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text='Close', command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text='Search')
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_customer(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class EmployeeDialog(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_employee()
        self.db = EmployeeTable()
        self.view_values()

    def init_employee(self):
        self.title("Employee Table")
        self.geometry("1550x720")
        self.resizable(False, False)

        self.add_img = tk.PhotoImage(file="button_grey_add.png")
        btn_open_dialog = tk.Button(self, text='Add', command=self.open_dialog_employee, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img, padx="15", pady="6", font="15")
        btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file='database_download.png')
        btn_edit_dialog = tk.Button(self, text='Edit', command=self.update_dialog_employee, bg='#d7d8e0', bd=0,
                                    image=self.update_img, compound=tk.TOP, padx="15", pady="6", font="15")
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file='button_grey_delete.png')
        btn_delete_dialog = tk.Button(self, text='Delete', bg='#d7d8e0', bd=0, image=self.delete_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15", command=self.delete_employee)
        btn_delete_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='zoom_in.png')
        btn_search_dialog = tk.Button(self, text='Search', bg='#d7d8e0', bd=0, image=self.search_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15", command=self.search_diaolog)
        btn_search_dialog.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='refresh.png')
        btn_search_dialog = tk.Button(self, text='Refresh', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15", command=self.view_values)
        btn_search_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('EmployeeID', 'LastName', 'FirstName', 'TitleOfCourtesy', 'HireDate',
                                                'Adress', 'City', 'Phone', 'Salary', 'PetShopID'),
                                 height=34, show='headings')

        self.tree.column('EmployeeID', width=120, anchor=tk.CENTER)
        self.tree.column('LastName', width=100, anchor=tk.CENTER)
        self.tree.column('FirstName', width=100, anchor=tk.CENTER)
        self.tree.column('TitleOfCourtesy', width=100, anchor=tk.CENTER)
        self.tree.column('HireDate', width=100, anchor=tk.CENTER)
        self.tree.column('Adress', width=150, anchor=tk.CENTER)
        self.tree.column('City', width=90, anchor=tk.CENTER)
        self.tree.column('Phone', width=150, anchor=tk.CENTER)
        self.tree.column('Salary', width=120, anchor=tk.CENTER)
        self.tree.column('PetShopID', width=90, anchor=tk.CENTER)

        self.tree.heading('EmployeeID', text='EmployeeID', command=self.sort_values_by_employeeid)
        self.tree.heading('LastName', text='LastName', command=self.sort_values_by_lastname)
        self.tree.heading('FirstName', text='FirstName', command=self.sort_values_by_firstname)
        self.tree.heading('TitleOfCourtesy', text='TitleOfCourtesy', command=self.sort_values_by_toc)
        self.tree.heading('HireDate', text='HireDate', command=self.sort_values_by_hiredate)
        self.tree.heading('Adress', text='Adress', command=self.sort_values_by_adress)
        self.tree.heading('City', text='City', command=self.sort_values_by_city)
        self.tree.heading('Phone', text='Phone', command=self.sort_values_by_phone)
        self.tree.heading('Salary', text='Salary', command=self.sort_values_by_salary)
        self.tree.heading('PetShopID', text='PetShopID', command=self.sort_values_by_petshopid)

        self.tree.pack()

    def add_employee(self, LastName, FirstName, TitleOfCourtesy, HireDate, Adress, City, Phone, Salary, PetShopID):
        self.db.insert_values(LastName, FirstName, TitleOfCourtesy, HireDate, Adress, City, Phone, Salary, PetShopID)
        self.view_values()

    def view_values(self):
        self.db.c.execute('''SELECT * FROM Employee''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def update_employee(self, LastName, FirstName, TitleOfCourtesy, HireDate, Adress, City, Phone, Salary, PetShopID):
        self.db.c.execute('''UPDATE Employee SET LastName=?, FirstName=?, TitleOfCourtesy=?, HireDate=?, Adress=?,
         City=?, Phone=?, Salary=?, PetShopID=? WHERE EmployeeID=?''',
                          (LastName, FirstName, TitleOfCourtesy, HireDate, Adress, City, Phone, Salary, PetShopID,
                           self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_values()

    def search_employee(self, LastName):
        LastName = ('%' + LastName + '%',)
        self.db.c.execute('''SELECT * FROM Employee WHERE LastName LIKE ?''', LastName)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def delete_employee(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('''DELETE FROM Employee WHERE EmployeeID=?''', (self.tree.set(selection_item, '#1'),))
        self.db.conn.commit()
        self.view_values()

    def sort_values_by_employeeid(self):
        self.db.c.execute('SELECT * FROM Employee ORDER BY EmployeeID')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_lastname(self):
        self.db.c.execute('SELECT * FROM Employee ORDER BY LastName')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_firstname(self):
        self.db.c.execute('SELECT * FROM Employee ORDER BY FirstName')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_toc(self):
        self.db.c.execute('SELECT * FROM Employee ORDER BY TitleOfCourtesy')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_hiredate(self):
        self.db.c.execute('SELECT * FROM Employee ORDER BY HireDate')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_adress(self):
        self.db.c.execute('SELECT * FROM Employee ORDER BY Adress')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_city(self):
        self.db.c.execute('SELECT * FROM Employee ORDER BY City')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_phone(self):
        self.db.c.execute('SELECT * FROM Employee ORDER BY Phone')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_salary(self):
        self.db.c.execute('SELECT * FROM Employee ORDER BY Salary')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_petshopid(self):
        self.db.c.execute('SELECT * FROM Employee ORDER BY PetShopID')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def open_dialog_employee(self):
        AddEmployee(self)

    def update_dialog_employee(self):
        UpdateEmployee(self)

    def search_diaolog(self):
        SearchEmployee(self)


class AddEmployee(tk.Toplevel):
    def __init__(self, EmployeeDialog):
        super().__init__(pet_shop_dialog)
        self.init_child()
        self.view = EmployeeDialog

    def init_child(self):
        self.title("Insert Values")
        self.geometry('600x400')
        self.resizable(False, False)

        label_lastname = tk.Label(self, text='LastName:')
        label_lastname.place(x=180, y=50)
        label_firstname = tk.Label(self, text='FirstName:')
        label_firstname.place(x=180, y=80)
        label_toc = tk.Label(self, text='TitleOfCourtesy:')
        label_toc.place(x=180, y=110)
        label_hd = tk.Label(self, text='HireDate:')
        label_hd.place(x=180, y=140)
        label_adress = tk.Label(self, text='Adress:')
        label_adress.place(x=180, y=170)
        label_city = tk.Label(self, text='City:')
        label_city.place(x=180, y=200)
        label_phone = tk.Label(self, text='Phone:')
        label_phone.place(x=180, y=230)
        label_salary = tk.Label(self, text='Salary:')
        label_salary.place(x=180, y=260)
        label_petshopid = tk.Label(self, text='PetShopID:')
        label_petshopid.place(x=180, y=290)

        self.entry_lastname = ttk.Entry(self)
        self.entry_lastname.place(x=325, y=50)

        self.entry_firstname = ttk.Entry(self)
        self.entry_firstname.place(x=325, y=80)

        self.entry_toc = ttk.Entry(self)
        self.entry_toc.place(x=325, y=110)

        self.entry_hd = ttk.Entry(self)
        self.entry_hd.place(x=325, y=140)

        self.entry_adress = ttk.Entry(self)
        self.entry_adress.place(x=325, y=170)

        self.entry_city = ttk.Entry(self)
        self.entry_city.place(x=325, y=200)

        self.entry_phone = ttk.Entry(self)
        self.entry_phone.place(x=325, y=230)

        self.entry_salary = ttk.Entry(self)
        self.entry_salary.place(x=325, y=260)

        self.entry_petshopid = ttk.Entry(self)
        self.entry_petshopid.place(x=325, y=290)

        btn_cancel = ttk.Button(self, text='Close', command=self.destroy)
        btn_cancel.place(x=350, y=350)

        self.btn_add = ttk.Button(self, text='Add')
        self.btn_add.place(x=200, y=350)
        self.btn_add.bind('<Button-1>', lambda event: self.view.add_employee(self.entry_lastname.get(),
                                                                             self.entry_firstname.get(),
                                                                             self.entry_toc.get(),
                                                                             self.entry_hd.get(),
                                                                             self.entry_adress.get(),
                                                                             self.entry_city.get(),
                                                                             self.entry_phone.get(),
                                                                             self.entry_salary.get(),
                                                                             self.entry_petshopid.get()))


class UpdateEmployee(AddEmployee):
    def __init__(self, EmployeeDialog):
        super().__init__(pet_shop_dialog)
        self.init_edit()
        self.view = EmployeeDialog

    def init_edit(self):
        self.title('Edit')
        btn_edit = ttk.Button(self, text='Edit')
        btn_edit.place(x=200, y=350)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_employee(self.entry_lastname.get(),
                                                                            self.entry_firstname.get(),
                                                                            self.entry_toc.get(),
                                                                            self.entry_hd.get(),
                                                                            self.entry_adress.get(),
                                                                            self.entry_city.get(),
                                                                            self.entry_phone.get(),
                                                                            self.entry_salary.get(),
                                                                            self.entry_petshopid.get()))

        self.btn_add.destroy()


class SearchEmployee(tk.Toplevel):
    def __init__(self, EmployeeDialog):
        super().__init__()
        self.init_search()
        self.view = EmployeeDialog

    def init_search(self):
        self.title('Search For Values')
        self.geometry('300x100+400+300')
        self.resizable(False, False)

        label_search = tk.Label(self, text='LastName:')
        label_search.place(x=40, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text='Close', command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text='Search')
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_employee(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class OrderDialog(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_order()
        self.db = OrderTable()
        self.view_values()

    def init_order(self):
        self.title("Order Table")
        self.geometry("1300x750")
        self.resizable(False, False)

        self.add_img = tk.PhotoImage(file="button_grey_add.png")
        btn_open_dialog = tk.Button(self, text='Add', command=self.open_dialog_order, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img, padx="15", pady="6", font="15")
        btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file='database_download.png')
        btn_edit_dialog = tk.Button(self, text='Edit', command=self.update_dialog_order, bg='#d7d8e0', bd=0,
                                    image=self.update_img, compound=tk.TOP, padx="15", pady="6", font="15")
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file='button_grey_delete.png')
        btn_delete_dialog = tk.Button(self, text='Delete', bg='#d7d8e0', bd=0, image=self.delete_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15", command=self.delete_order)
        btn_delete_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='zoom_in.png')
        btn_search_dialog = tk.Button(self, text='Search', bg='#d7d8e0', bd=0, image=self.search_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15", command=self.search_diaolog)
        btn_search_dialog.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='refresh.png')
        btn_search_dialog = tk.Button(self, text='Refresh', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15", command=self.view_values)
        btn_search_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('OrderID', 'DateOfSale', 'Discount', 'PetShopID', 'EmployeeID',
                                                'CustomerID', 'PetID', 'PetAccessoryID', 'PetFoodID'),
                                 height=34, show='headings')

        self.tree.column('OrderID', width=150, anchor=tk.CENTER)
        self.tree.column('DateOfSale', width=100, anchor=tk.CENTER)
        self.tree.column('Discount', width=100, anchor=tk.CENTER)
        self.tree.column('PetShopID', width=90, anchor=tk.CENTER)
        self.tree.column('EmployeeID', width=90, anchor=tk.CENTER)
        self.tree.column('CustomerID', width=90, anchor=tk.CENTER)
        self.tree.column('PetID', width=90, anchor=tk.CENTER)
        self.tree.column('PetAccessoryID', width=90, anchor=tk.CENTER)
        self.tree.column('PetFoodID', width=90, anchor=tk.CENTER)

        self.tree.heading('OrderID', text='OrderID', command=self.sort_values_by_orderid)
        self.tree.heading('DateOfSale', text='DateOfSale', command=self.sort_values_by_dos)
        self.tree.heading('Discount', text='Discount', command=self.sort_values_by_discount)
        self.tree.heading('PetShopID', text='PetShopID', command=self.sort_values_by_petshopid)
        self.tree.heading('EmployeeID', text='EmployeeID', command=self.sort_values_by_employeeid)
        self.tree.heading('CustomerID', text='CustomerID', command=self.sort_values_by_customerid)
        self.tree.heading('PetID', text='PetID', command=self.sort_values_by_petid)
        self.tree.heading('PetAccessoryID', text='PetAccessoryID', command=self.sort_values_by_petaccessoryid)
        self.tree.heading('PetFoodID', text='PetFoodID', command=self.sort_values_by_petfoodid)

        self.tree.pack()

    def add_order(self, DateOfSale, Discount, PetShopID, EmployeeID, CustomerID, PetID, PetAccessoryID, PetFoodID):
        self.db.insert_values(DateOfSale, Discount, PetShopID, EmployeeID, CustomerID, PetID, PetAccessoryID, PetFoodID)
        self.view_values()

    def view_values(self):
        self.db.c.execute('''SELECT * FROM OrderTable''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def update_order(self, DateOfSale, Discount, PetShopID, EmployeeID, CustomerID, PetID, PetAccessoryID, PetFoodID):
        self.db.c.execute('''UPDATE OrderTable SET DateOfSale=?, Discount=?, PetShopID=?, EmployeeID=?, CustomerID=?,
         PetID=?, PetAccessoryID=?, PetFoodID=? WHERE OrderID=?''',
                          (DateOfSale, Discount, PetShopID, EmployeeID, CustomerID, PetID, PetAccessoryID, PetFoodID,
                           self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_values()

    def search_order(self, DateOfSale):
        DateOfSale = ('%' + DateOfSale + '%',)
        self.db.c.execute('''SELECT * FROM OrderTable WHERE DateOfSale LIKE ?''', DateOfSale)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def delete_order(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('''DELETE FROM OrderTable WHERE OrderID=?''', (self.tree.set(selection_item, '#1'),))
        self.db.conn.commit()
        self.view_values()

    def sort_values_by_orderid(self):
        self.db.c.execute('SELECT * FROM OrderTable ORDER BY OrderID')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_dos(self):
        self.db.c.execute('SELECT * FROM OrderTable ORDER BY DateOfSale')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_discount(self):
        self.db.c.execute('SELECT * FROM OrderTable ORDER BY Discount')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_petshopid(self):
        self.db.c.execute('SELECT * FROM OrderTable ORDER BY PetShopID')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_employeeid(self):
        self.db.c.execute('SELECT * FROM OrderTable ORDER BY EmployeeID')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_customerid(self):
        self.db.c.execute('SELECT * FROM OrderTable ORDER BY CustomerID')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_petid(self):
        self.db.c.execute('SELECT * FROM OrderTable ORDER BY PetID')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_petaccessoryid(self):
        self.db.c.execute('SELECT * FROM OrderTable ORDER BY PetAccessoryID')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_petfoodid(self):
        self.db.c.execute('SELECT * FROM OrderTable ORDER BY PetFoodID')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_salary(self):
        self.db.c.execute('SELECT * FROM OrderTable ORDER BY Salary')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def open_dialog_order(self):
        AddOrder(self)

    def update_dialog_order(self):
        UpdateOrder(self)

    def search_diaolog(self):
        SearchOrder(self)

class AddOrder(tk.Toplevel):
    def __init__(self, OrderDialog):
        super().__init__(pet_shop_dialog)
        self.init_child()
        self.view = OrderDialog

    def init_child(self):
        self.title("Insert Values")
        self.geometry('600x400')
        self.resizable(False, False)

        label_dateofsale = tk.Label(self, text='DateOfSale:')
        label_dateofsale.place(x=180, y=50)
        label_discount = tk.Label(self, text='Discount:')
        label_discount.place(x=180, y=80)
        label_petshopid = tk.Label(self, text='PetShopID:')
        label_petshopid.place(x=180, y=110)
        label_employeeid = tk.Label(self, text='EmployeeID:')
        label_employeeid.place(x=180, y=140)
        label_customerid = tk.Label(self, text='CustomerID:')
        label_customerid.place(x=180, y=170)
        label_petid = tk.Label(self, text='PetID:')
        label_petid.place(x=180, y=200)
        label_petaccessoryid = tk.Label(self, text='PetAccessoryID:')
        label_petaccessoryid.place(x=180, y=230)
        label_petfoodid = tk.Label(self, text='PetFoodID:')
        label_petfoodid.place(x=180, y=260)

        self.entry_dateofsale = ttk.Entry(self)
        self.entry_dateofsale.place(x=325, y=50)

        self.entry_discount = ttk.Entry(self)
        self.entry_discount.place(x=325, y=80)

        self.entry_petshopid = ttk.Entry(self)
        self.entry_petshopid.place(x=325, y=110)

        self.entry_employeeid = ttk.Entry(self)
        self.entry_employeeid.place(x=325, y=140)

        self.entry_customerid = ttk.Entry(self)
        self.entry_customerid.place(x=325, y=170)

        self.entry_petid = ttk.Entry(self)
        self.entry_petid.place(x=325, y=200)

        self.PetAccessoryID = ttk.Entry(self)
        self.PetAccessoryID.place(x=325, y=230)

        self.PetFoodID = ttk.Entry(self)
        self.PetFoodID.place(x=325, y=260)

        btn_cancel = ttk.Button(self, text='Close', command=self.destroy)
        btn_cancel.place(x=350, y=320)

        self.btn_add = ttk.Button(self, text='Add')
        self.btn_add.place(x=200, y=320)
        self.btn_add.bind('<Button-1>', lambda event: self.view.add_order(self.entry_dateofsale.get(),
                                                                          self.entry_discount.get(),
                                                                          self.entry_petshopid.get(),
                                                                          self.entry_employeeid.get(),
                                                                          self.entry_customerid.get(),
                                                                          self.entry_petid.get(),
                                                                          self.PetAccessoryID.get(),
                                                                          self.PetFoodID.get()))


class UpdateOrder(AddOrder):
    def __init__(self, OrderDialog):
        super().__init__(pet_shop_dialog)
        self.init_edit()
        self.view = OrderDialog

    def init_edit(self):
        self.title('Edit')
        btn_edit = ttk.Button(self, text='Edit')
        btn_edit.place(x=200, y=320)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_order(self.entry_dateofsale.get(),
                                                                          self.entry_discount.get(),
                                                                          self.entry_petshopid.get(),
                                                                          self.entry_employeeid.get(),
                                                                          self.entry_customerid.get(),
                                                                          self.entry_petid.get(),
                                                                          self.PetAccessoryID.get(),
                                                                          self.PetFoodID.get()))

        self.btn_add.destroy()

class SearchOrder(tk.Toplevel):
    def __init__(self, OrderDialog):
        super().__init__()
        self.init_search()
        self.view = OrderDialog

    def init_search(self):
        self.title('Search For Values')
        self.geometry('300x100+400+300')
        self.resizable(False, False)

        label_search = tk.Label(self, text='DateOfSale:')
        label_search.place(x=40, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text='Close', command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text='Search')
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_order(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

class PetDialog(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_pet()
        self.db = PetTable()
        self.view_values()

    def init_pet(self):
        self.title("Pet Table")
        self.geometry("1400x700")
        self.resizable(False, False)

        self.add_img = tk.PhotoImage(file="button_grey_add.png")
        btn_open_dialog = tk.Button(self, text='Add', command=self.open_dialog_pet, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img, padx="15", pady="6", font="15")
        btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file='database_download.png')
        btn_edit_dialog = tk.Button(self, text='Edit', command=self.update_dialog_pet, bg='#d7d8e0', bd=0,
                                    image=self.update_img, compound=tk.TOP, padx="15", pady="6", font="15")
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file='button_grey_delete.png')
        btn_delete_dialog = tk.Button(self, text='Delete', bg='#d7d8e0', bd=0, image=self.delete_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15", command=self.delete_pet)
        btn_delete_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='zoom_in.png')
        btn_search_dialog = tk.Button(self, text='Search', bg='#d7d8e0', bd=0, image=self.search_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15", command=self.search_diaolog)
        btn_search_dialog.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='refresh.png')
        btn_search_dialog = tk.Button(self, text='Refresh', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15", command=self.view_values)
        btn_search_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('PetID', 'Specie', 'Color', 'Gender', 'Age', 'Description'),
                                 height=34, show='headings')

        self.tree.column('PetID', width=150, anchor=tk.CENTER)
        self.tree.column('Specie', width=140, anchor=tk.CENTER)
        self.tree.column('Color', width=100, anchor=tk.CENTER)
        self.tree.column('Gender', width=100, anchor=tk.CENTER)
        self.tree.column('Age', width=120, anchor=tk.CENTER)
        self.tree.column('Description', width=380, anchor=tk.CENTER)

        self.tree.heading('PetID', text='PetID', command=self.sort_values_by_petid)
        self.tree.heading('Specie', text='Specie', command=self.sort_values_by_specie)
        self.tree.heading('Color', text='Color', command=self.sort_values_by_color)
        self.tree.heading('Gender', text='Gender', command=self.sort_values_by_gender)
        self.tree.heading('Age', text='Age', command=self.sort_values_by_age)
        self.tree.heading('Description', text='Description', command=self.sort_values_by_desc)

        self.tree.pack()

    def add_pet(self, Specie, Color, Gender, Age, Description):
        self.db.insert_values(Specie, Color, Gender, Age, Description)
        self.view_values()

    def view_values(self):
        self.db.c.execute('''SELECT * FROM Pet''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def update_pet(self, Specie, Color, Gender, Age, Description):
        self.db.c.execute('''UPDATE Pet SET Specie=?, Color=?, Gender=?, Age=?, Description=? WHERE PetID=?''',
                          (Specie, Color, Gender, Age, Description, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_values()

    def search_pet(self, Description):
        Description = ('%' + Description + '%',)
        self.db.c.execute('''SELECT * FROM Pet WHERE Description LIKE ?''', Description)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def delete_pet(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('''DELETE FROM Pet WHERE PetID=?''', (self.tree.set(selection_item, '#1'),))
        self.db.conn.commit()
        self.view_values()

    def sort_values_by_petid(self):
        self.db.c.execute('SELECT * FROM Pet ORDER BY PetID')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_specie(self):
        self.db.c.execute('SELECT * FROM Pet ORDER BY Specie')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_color(self):
        self.db.c.execute('SELECT * FROM Pet ORDER BY Color')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_gender(self):
        self.db.c.execute('SELECT * FROM Pet ORDER BY Gender')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_age(self):
        self.db.c.execute('SELECT * FROM Pet ORDER BY Age')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_desc(self):
        self.db.c.execute('SELECT * FROM Pet ORDER BY Description')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def open_dialog_pet(self):
        AddPet(self)

    def update_dialog_pet(self):
        UpdatePet(self)

    def search_diaolog(self):
        SearchOrder(self)


class AddPet(tk.Toplevel):
    def __init__(self, PetDialog):
        super().__init__(pet_shop_dialog)
        self.init_child()
        self.view = PetDialog
    def init_child(self):
        self.title("Insert Values")
        self.geometry('600x400')
        self.resizable(False, False)

        Specie = tk.Label(self, text='Specie:')
        Specie.place(x=180, y=50)
        Color = tk.Label(self, text='Color:')
        Color.place(x=180, y=80)
        Gender = tk.Label(self, text='Gender:')
        Gender.place(x=180, y=110)
        Age = tk.Label(self, text='Age:')
        Age.place(x=180, y=140)
        Description = tk.Label(self, text='Description:')
        Description.place(x=180, y=170)

        self.Specie = ttk.Entry(self)
        self.Specie.place(x=325, y=50)

        self.Color = ttk.Entry(self)
        self.Color.place(x=325, y=80)

        self.Gender = ttk.Entry(self)
        self.Gender.place(x=325, y=110)

        self.Age = ttk.Entry(self)
        self.Age.place(x=325, y=140)

        self.Description = ttk.Entry(self)
        self.Description.place(x=325, y=170)

        btn_cancel = ttk.Button(self, text='Close', command=self.destroy)
        btn_cancel.place(x=350, y=300)

        self.btn_add = ttk.Button(self, text='Add')
        self.btn_add.place(x=200, y=300)
        self.btn_add.bind('<Button-1>', lambda event: self.view.add_pet(self.Specie.get(),
                                                                          self.Color.get(),
                                                                          self.Gender.get(),
                                                                          self.Age.get(),
                                                                          self.Description.get()))


class UpdatePet(AddPet):
    def __init__(self, PetDialog):
        super().__init__(pet_shop_dialog)
        self.init_edit()
        self.view = PetDialog


    def init_edit(self):
        self.title('Edit')
        btn_edit = ttk.Button(self, text='Edit')
        btn_edit.place(x=200, y=300)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_pet(self.Specie.get(),
                                                                          self.Color.get(),
                                                                          self.Gender.get(),
                                                                          self.Age.get(),
                                                                          self.Description.get()))

        self.btn_add.destroy()

class SearchPet(tk.Toplevel):
    def __init__(self, PetDialog):
        super().__init__()
        self.init_search()
        self.view = PetDialog

    def init_search(self):
        self.title('Search For Values')
        self.geometry('300x100+400+300')
        self.resizable(False, False)

        label_search = tk.Label(self, text='Description:')
        label_search.place(x=30, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text='Close', command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text='Search')
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_pet(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

class PetFoodDialog(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_pet_food()
        self.db = PetFoodTable()
        self.view_values()



    def init_pet_food(self):
        self.title("PetFood Table")
        self.geometry("1460x700")
        self.resizable(False, False)

        self.add_img = tk.PhotoImage(file="button_grey_add.png")
        btn_open_dialog = tk.Button(self, text='Add', command=self.open_dialog_pet_food, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img, padx="15", pady="6", font="15")
        btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file='database_download.png')
        btn_edit_dialog = tk.Button(self, text='Edit', command=self.update_dialog_pet_food, bg='#d7d8e0', bd=0,
                                    image=self.update_img, compound=tk.TOP, padx="15", pady="6", font="15")
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file='button_grey_delete.png')
        btn_delete_dialog = tk.Button(self, text='Delete', bg='#d7d8e0', bd=0, image=self.delete_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15", command=self.delete_petfood)
        btn_delete_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='zoom_in.png')
        btn_search_dialog = tk.Button(self, text='Search', bg='#d7d8e0', bd=0, image=self.search_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15", command=self.search_diaolog)
        btn_search_dialog.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='refresh.png')
        btn_search_dialog = tk.Button(self, text='Refresh', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15", command=self.view_values)
        btn_search_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('PetFoodID', 'Name', 'Price', 'PackageType', 'Weight', 'PetID',
                                                'ManufacturerID'),
                                 height=34, show='headings')

        self.tree.column('PetFoodID', width=130, anchor=tk.CENTER)
        self.tree.column('Name', width=150, anchor=tk.CENTER)
        self.tree.column('Price', width=150, anchor=tk.CENTER)
        self.tree.column('PackageType', width=200, anchor=tk.CENTER)
        self.tree.column('Weight', width=150, anchor=tk.CENTER)
        self.tree.column('PetID', width=100, anchor=tk.CENTER)
        self.tree.column('ManufacturerID', width=155, anchor=tk.CENTER)

        self.tree.heading('PetFoodID', text='PetFoodID', command=self.sort_values_by_petfoodid)
        self.tree.heading('Name', text='Name', command=self.sort_values_by_name)
        self.tree.heading('Price', text='Price', command=self.sort_values_by_price)
        self.tree.heading('PackageType', text='PackageType', command=self.sort_values_by_pt)
        self.tree.heading('Weight', text='Weight', command=self.sort_values_by_weight)
        self.tree.heading('PetID', text='PetID', command=self.sort_values_by_petid)
        self.tree.heading('ManufacturerID', text='ManufacturerID', command=self.sort_values_by_manid)

        self.tree.pack()

    def add_petfood(self, Name, Price, PackageType, Weight, PetID, ManufacturerID):
        self.db.insert_values(Name, Price, PackageType, Weight, PetID, ManufacturerID)
        self.view_values()

    def view_values(self):
        self.db.c.execute('''SELECT * FROM PetFood''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def update_petfood(self, Name, Price, PackageType, Weight, PetID, ManufacturerID):
        self.db.c.execute('''UPDATE PetFood SET Name=?, Price=?, PackageType=?, Weight=?, PetID=?, ManufacturerID=?
         WHERE PetFoodID=?''',
                          (Name, Price, PackageType, Weight, PetID, ManufacturerID,
                           self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_values()

    def search_petfood(self, Name):
        Name = ('%' + Name + '%',)
        self.db.c.execute('''SELECT * FROM PetFood WHERE Name LIKE ?''', Name)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def delete_petfood(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('''DELETE FROM PetFood WHERE PetFoodID=?''', (self.tree.set(selection_item, '#1'),))
        self.db.conn.commit()
        self.view_values()

    def sort_values_by_petfoodid(self):
        self.db.c.execute('SELECT * FROM PetFood ORDER BY PetFoodID')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_name(self):
        self.db.c.execute('SELECT * FROM PetFood ORDER BY Name')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_price(self):
        self.db.c.execute('SELECT * FROM PetFood ORDER BY Price')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_pt(self):
        self.db.c.execute('SELECT * FROM PetFood ORDER BY PackageType')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_weight(self):
        self.db.c.execute('SELECT * FROM PetFood ORDER BY Weight')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_petid(self):
        self.db.c.execute('SELECT * FROM PetFood ORDER BY PetID')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_manid(self):
        self.db.c.execute('SELECT * FROM PetFood ORDER BY ManufacturerID')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def open_dialog_pet_food(self):
        AddPetFood(self)

    def update_dialog_pet_food(self):
        UpdatePetFood(self)

    def search_diaolog(self):
        SearchPetFood(self)

class AddPetFood(tk.Toplevel):
    def __init__(self, PetFoodDialog):
        super().__init__(pet_shop_dialog)
        self.init_child()
        self.view = PetFoodDialog

    def init_child(self):
        self.title("Insert Values")
        self.geometry('600x400')
        self.resizable(False, False)

        Name = tk.Label(self, text='Name:')
        Name.place(x=180, y=50)
        Price = tk.Label(self, text='Price:')
        Price.place(x=180, y=80)
        PackageType = tk.Label(self, text='PackageType:')
        PackageType.place(x=180, y=110)
        Weight = tk.Label(self, text='Weight:')
        Weight.place(x=180, y=140)
        PetID = tk.Label(self, text='PetID:')
        PetID.place(x=180, y=170)
        ManufacturerID = tk.Label(self, text='ManufacturerID:')
        ManufacturerID.place(x=180, y=200)

        self.Name = ttk.Entry(self)
        self.Name.place(x=325, y=50)

        self.Price = ttk.Entry(self)
        self.Price.place(x=325, y=80)

        self.PackageType = ttk.Entry(self)
        self.PackageType.place(x=325, y=110)

        self.Weight = ttk.Entry(self)
        self.Weight.place(x=325, y=140)

        self.PetID = ttk.Entry(self)
        self.PetID.place(x=325, y=170)

        self.ManufacturerID = ttk.Entry(self)
        self.ManufacturerID.place(x=325, y=200)

        btn_cancel = ttk.Button(self, text='Close', command=self.destroy)
        btn_cancel.place(x=350, y=300)

        self.btn_add = ttk.Button(self, text='Add')
        self.btn_add.place(x=200, y=300)
        self.btn_add.bind('<Button-1>', lambda event: self.view.add_petfood(self.Name.get(),
                                                                          self.Price.get(),
                                                                          self.PackageType.get(),
                                                                          self.Weight.get(),
                                                                          self.PetID.get(),
                                                                            self.ManufacturerID.get()))


class UpdatePetFood(AddPetFood):
    def __init__(self, PetFoodDialog):
        super().__init__(pet_shop_dialog)
        self.init_edit()
        self.view = PetFoodDialog


    def init_edit(self):
        self.title('Edit')
        btn_edit = ttk.Button(self, text='Edit')
        btn_edit.place(x=200, y=300)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_petfood(self.Name.get(),
                                                                          self.Price.get(),
                                                                          self.PackageType.get(),
                                                                          self.Weight.get(),
                                                                          self.PetID.get(),
                                                                            self.ManufacturerID.get()))
        self.btn_add.destroy()

class SearchPetFood(tk.Toplevel):
    def __init__(self, PetFoodDialog):
        super().__init__()
        self.init_search()
        self.view = PetFoodDialog

    def init_search(self):
        self.title('Search For Values')
        self.geometry('300x100+400+300')
        self.resizable(False, False)

        label_search = tk.Label(self, text='Name:')
        label_search.place(x=40, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text='Close', command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text='Search')
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_petfood(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

class PetAccessoryDialog(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_pet_accessory()
        self.db = PetAccessoryTable()
        self.view_values()


    def init_pet_accessory(self):
        self.title("PetAccessory Table")
        self.geometry("1230x715")
        self.resizable(False, False)

        self.add_img = tk.PhotoImage(file="button_grey_add.png")
        btn_open_dialog = tk.Button(self, text='Add', command=self.open_dialog_pet_accessory, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img, padx="15", pady="6", font="15")
        btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file='database_download.png')
        btn_edit_dialog = tk.Button(self, text='Edit', command=self.update_dialog_pet_accessory, bg='#d7d8e0', bd=0,
                                    image=self.update_img, compound=tk.TOP, padx="15", pady="6", font="15")
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file='button_grey_delete.png')
        btn_delete_dialog = tk.Button(self, text='Delete', bg='#d7d8e0', bd=0, image=self.delete_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15", command=self.delete_petaccessory)
        btn_delete_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='zoom_in.png')
        btn_search_dialog = tk.Button(self, text='Search', bg='#d7d8e0', bd=0, image=self.search_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15", command=self.search_diaolog)
        btn_search_dialog.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='refresh.png')
        btn_search_dialog = tk.Button(self, text='Refresh', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15", command=self.view_values)
        btn_search_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('PetAccessoryID', 'Name', 'Size', 'Price', 'PetID', 'ManufacturerID'),
                                 height=34, show='headings')

        self.tree.column('PetAccessoryID', width=150, anchor=tk.CENTER)
        self.tree.column('Name', width=120, anchor=tk.CENTER)
        self.tree.column('Size', width=150, anchor=tk.CENTER)
        self.tree.column('Price', width=150, anchor=tk.CENTER)
        self.tree.column('PetID', width=90, anchor=tk.CENTER)
        self.tree.column('ManufacturerID', width=140, anchor=tk.CENTER)

        self.tree.heading('PetAccessoryID', text='PetAccessoryID', command=self.sort_values_by_petaccessoryid)
        self.tree.heading('Name', text='Name', command=self.sort_values_by_name)
        self.tree.heading('Size', text='Size', command=self.sort_values_by_size)
        self.tree.heading('Price', text='Price', command=self.sort_values_by_price)
        self.tree.heading('PetID', text='PetID', command=self.sort_values_by_petid)
        self.tree.heading('ManufacturerID', text='ManufacturerID', command=self.sort_values_by_manid)

        self.tree.pack()

    def add_petaccessory(self, Name, Size, Price, PetID, ManufacturerID):
        self.db.insert_values(Name, Size, Price, PetID, ManufacturerID)
        self.view_values()

    def view_values(self):
        self.db.c.execute('''SELECT * FROM PetAccessoryTable''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def update_petaccessory(self, Name, Size, Price, PetID, ManufacturerID):
        self.db.c.execute('''UPDATE PetAccessoryTable SET Name=?, Size=?, Price=?, PetID=?, ManufacturerID=? 
        WHERE PetAccessoryID=?''',
                          (Name, Size, Price, PetID, ManufacturerID,
                           self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_values()

    def search_petaccessory(self, Name):
        Name = ('%' + Name + '%',)
        self.db.c.execute('''SELECT * FROM PetAccessoryTable WHERE Name LIKE ?''', Name)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def delete_petaccessory(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('''DELETE FROM PetAccessoryTable WHERE PetAccessoryID=?''',
                              (self.tree.set(selection_item, '#1'),))
        self.db.conn.commit()
        self.view_values()

    def sort_values_by_petaccessoryid(self):
        self.db.c.execute('SELECT * FROM PetAccessoryTable ORDER BY PetAccessoryID')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_name(self):
        self.db.c.execute('SELECT * FROM PetAccessoryTable ORDER BY Name')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_size(self):
        self.db.c.execute('SELECT * FROM PetAccessoryTable ORDER BY Size')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_price(self):
        self.db.c.execute('SELECT * FROM PetAccessoryTable ORDER BY Price')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_petid(self):
        self.db.c.execute('SELECT * FROM PetAccessoryTable ORDER BY PetID')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_manid(self):
        self.db.c.execute('SELECT * FROM PetAccessoryTable ORDER BY ManufacturerID')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]



    def open_dialog_pet_accessory(self):
        AddPetAccessory(self)

    def update_dialog_pet_accessory(self):
        UpdatePetAccessory(self)

    def search_diaolog(self):
        SearchPetAccessory(self)

class AddPetAccessory(tk.Toplevel):
    def __init__(self, PetAccessoryDialog):
        super().__init__(pet_shop_dialog)
        self.init_child()
        self.view = PetAccessoryDialog

    def init_child(self):
        self.title("Insert Values")
        self.geometry('600x400')
        self.resizable(False, False)

        Name = tk.Label(self, text='Name:')
        Name.place(x=180, y=50)
        Size = tk.Label(self, text='Size:')
        Size.place(x=180, y=80)
        Price = tk.Label(self, text='Price:')
        Price.place(x=180, y=110)
        PetID = tk.Label(self, text='PetID:')
        PetID.place(x=180, y=140)
        ManufacturerID = tk.Label(self, text='ManufacturerID:')
        ManufacturerID.place(x=180, y=170)

        self.Name = ttk.Entry(self)
        self.Name.place(x=325, y=50)

        self.Size = ttk.Entry(self)
        self.Size.place(x=325, y=80)

        self.Price = ttk.Entry(self)
        self.Price.place(x=325, y=110)

        self.PetID = ttk.Entry(self)
        self.PetID.place(x=325, y=140)

        self.ManufacturerID = ttk.Entry(self)
        self.ManufacturerID.place(x=325, y=170)

        btn_cancel = ttk.Button(self, text='Close', command=self.destroy)
        btn_cancel.place(x=350, y=300)

        self.btn_add = ttk.Button(self, text='Add')
        self.btn_add.place(x=200, y=300)
        self.btn_add.bind('<Button-1>', lambda event: self.view.add_petaccessory(self.Name.get(),
                                                                          self.Size.get(),
                                                                          self.Price.get(),
                                                                          self.PetID.get(),
                                                                          self.ManufacturerID.get()))


class UpdatePetAccessory(AddPetAccessory):
    def __init__(self, PetAccessoryDialog):
        super().__init__(pet_shop_dialog)
        self.init_edit()
        self.view = PetAccessoryDialog

    def init_edit(self):
        self.title('Edit')
        btn_edit = ttk.Button(self, text='Edit')
        btn_edit.place(x=200, y=300)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_petaccessory(self.Name.get(),
                                                                          self.Size.get(),
                                                                          self.Price.get(),
                                                                          self.PetID.get(),
                                                                          self.ManufacturerID.get()))

        self.btn_add.destroy()

class SearchPetAccessory(tk.Toplevel):
    def __init__(self, PetAccessoryDialog):
        super().__init__()
        self.init_search()
        self.view = PetAccessoryDialog

    def init_search(self):
        self.title('Search For Values')
        self.geometry('300x100+400+300')
        self.resizable(False, False)

        label_search = tk.Label(self, text='Name:')
        label_search.place(x=40, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text='Close', command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text='Search')
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_petaccessory(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class ManufacturerDialog(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_manufacturer()
        self.db = ManufacturerTable()
        self.view_values()


    def init_manufacturer(self):
        self.title("Manufacturer Table")
        self.geometry("1100x720")
        self.resizable(False, False)

        self.add_img = tk.PhotoImage(file="button_grey_add.png")
        btn_open_dialog = tk.Button(self, text='Add', command=self.open_dialog_manufacturer, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img, padx="15", pady="6", font="15")
        btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file='database_download.png')
        btn_edit_dialog = tk.Button(self, text='Edit', command=self.update_dialog_manufacturer, bg='#d7d8e0', bd=0,
                                    image=self.update_img, compound=tk.TOP, padx="15", pady="6", font="15")
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file='button_grey_delete.png')
        btn_delete_dialog = tk.Button(self, text='Delete', bg='#d7d8e0', bd=0, image=self.delete_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15", command=self.delete_manufacturer)
        btn_delete_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='zoom_in.png')
        btn_search_dialog = tk.Button(self, text='Search', bg='#d7d8e0', bd=0, image=self.search_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15", command=self.search_diaolog)
        btn_search_dialog.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='refresh.png')
        btn_search_dialog = tk.Button(self, text='Refresh', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15", command=self.view_values)
        btn_search_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('ManufacturerID', 'Name', 'Adress', 'ProductsCategory'),
                                 height=34, show='headings')

        self.tree.column('ManufacturerID', width=140, anchor=tk.CENTER)
        self.tree.column('Name', width=155, anchor=tk.CENTER)
        self.tree.column('Adress', width=153, anchor=tk.CENTER)
        self.tree.column('ProductsCategory', width=200, anchor=tk.CENTER)

        self.tree.heading('ManufacturerID', text='ManufacturerID', command=self.sort_values_by_manufacturerid)
        self.tree.heading('Name', text='Name', command=self.sort_values_by_name)
        self.tree.heading('Adress', text='Adress', command=self.sort_values_by_adress)
        self.tree.heading('ProductsCategory', text='ProductsCategory', command=self.sort_values_by_pc)

        self.tree.pack()

    def add_manufacturer(self, Name, Adress, ProductsCategory):
        self.db.insert_values(Name, Adress, ProductsCategory)
        self.view_values()

    def view_values(self):
        self.db.c.execute('''SELECT * FROM Manufacturer''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def update_manufacturer(self,  Name, Adress, ProductsCategory):
        self.db.c.execute('''UPDATE Manufacturer SET Name=?, Adress=?, ProductsCategory=? WHERE ManufacturerID=?''',
                          (Name, Adress, ProductsCategory,
                           self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_values()

    def search_manufacturer(self, Name):
        Name = ('%' + Name + '%',)
        self.db.c.execute('''SELECT * FROM Manufacturer WHERE Name LIKE ?''', Name)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def delete_manufacturer(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('''DELETE FROM Manufacturer WHERE ManufacturerID=?''',
                              (self.tree.set(selection_item, '#1'),))
        self.db.conn.commit()
        self.view_values()

    def sort_values_by_manufacturerid(self):
        self.db.c.execute('SELECT * FROM Manufacturer ORDER BY ManufacturerID')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_name(self):
        self.db.c.execute('SELECT * FROM Manufacturer ORDER BY Name')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_adress(self):
        self.db.c.execute('SELECT * FROM Manufacturer ORDER BY Adress')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_values_by_pc(self):
        self.db.c.execute('SELECT * FROM Manufacturer ORDER BY ProductsCategory')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def open_dialog_manufacturer(self):
        AddManufacturer(self)

    def update_dialog_manufacturer(self):
        UpdateManufacturer(self)

    def search_diaolog(self):
        SearchManufacturer(self)

class AddManufacturer(tk.Toplevel):
    def __init__(self, ManufacturerDialog):
        super().__init__(pet_shop_dialog)
        self.init_child()
        self.view = ManufacturerDialog

    def init_child(self):
        self.title("Insert Values")
        self.geometry('600x400')
        self.resizable(False, False)

        Name = tk.Label(self, text='Name:')
        Name.place(x=180, y=50)
        Adress = tk.Label(self, text='Adress:')
        Adress.place(x=180, y=80)
        ProductsCategory = tk.Label(self, text='ProductsCategory:')
        ProductsCategory.place(x=180, y=110)

        self.Name = ttk.Entry(self)
        self.Name.place(x=325, y=50)

        self.Adress = ttk.Entry(self)
        self.Adress.place(x=325, y=80)

        self.ProductsCategory = ttk.Entry(self)
        self.ProductsCategory.place(x=325, y=110)

        btn_cancel = ttk.Button(self, text='Close', command=self.destroy)
        btn_cancel.place(x=350, y=250)

        self.btn_add = ttk.Button(self, text='Add')
        self.btn_add.place(x=200, y=250)
        self.btn_add.bind('<Button-1>', lambda event: self.view.add_manufacturer(self.Name.get(),
                                                                          self.Adress.get(),
                                                                          self.ProductsCategory.get()))


class UpdateManufacturer(AddManufacturer):
    def __init__(self, ManufacturerDialog):
        super().__init__(pet_shop_dialog)
        self.init_edit()
        self.view = ManufacturerDialog

    def init_edit(self):
        self.title('Edit')
        btn_edit = ttk.Button(self, text='Edit')
        btn_edit.place(x=200, y=250)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_manufacturer(self.Name.get(),
                                                                          self.Adress.get(),
                                                                          self.ProductsCategory.get()))

        self.btn_add.destroy()

class SearchManufacturer(tk.Toplevel):
    def __init__(self, ManufacturerDialog):
        super().__init__()
        self.init_search()
        self.view = ManufacturerDialog

    def init_search(self):
        self.title('Search For Values')
        self.geometry('300x100+400+300')
        self.resizable(False, False)

        label_search = tk.Label(self, text='Name:')
        label_search.place(x=40, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text='Close', command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text='Search')
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_manufacturer(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')



if __name__ == "__main__":
    pet_shop_dialog = tk.Tk()
    petshopvalues = PetShopTable()
    pet_shop_table = PetShopDialog(pet_shop_dialog)
    pet_shop_table.pack()
    pet_shop_dialog.title("PetShop Table")
    pet_shop_dialog.geometry("1020x700+300+200")
    pet_shop_dialog.resizable(False, False)

    pet_shop_dialog.mainloop()
