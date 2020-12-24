import tkinter as tk
from tkinter import ttk
import sqlite3


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

        self.tree = ttk.Treeview(self, columns=('PetShopID', 'Name', 'Adress', 'PostalCode', 'Phone'),
                                 height=29, show='headings')

        self.tree.column('PetShopID', width=130, anchor=tk.CENTER)
        self.tree.column('Name', width=250, anchor=tk.CENTER)
        self.tree.column('Adress', width=235, anchor=tk.CENTER)
        self.tree.column('PostalCode', width=155, anchor=tk.CENTER)
        self.tree.column('Phone', width=250, anchor=tk.CENTER)

        self.tree.heading('PetShopID', text='PetShopID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Adress', text='Adress')
        self.tree.heading('PostalCode', text='PostalCode')
        self.tree.heading('Phone', text='Phone')

        self.tree.pack()

    def open_dialog(self):
        AddPetShop()

    def open_update_dialog(self):
        UpdatePetShop()

    def add_values(self, Name, Adress, PostalCode, Phone):
        self.db.insert_values(Name, Adress, PostalCode, Phone)
        self.view_values()

    def view_values(self):
        self.db.c.execute('''SELECT * FROM PetShop''')
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

        label_pet_shop_id = tk.Label(self, text='Name:')
        label_pet_shop_id.place(x=180, y=50)
        label_name = tk.Label(self, text='Adress:')
        label_name.place(x=180, y=80)
        label_adress = tk.Label(self, text='PostalCode:')
        label_adress.place(x=180, y=110)
        label_postal_code = tk.Label(self, text='Phone:')
        label_postal_code.place(x=180, y=140)

        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=325, y=50)

        self.entry_adress = ttk.Entry(self)
        self.entry_adress.place(x=325, y=80)

        self.entry_postal_code = ttk.Entry(self)
        self.entry_postal_code.place(x=325, y=110)

        self.entry_phone = ttk.Entry(self)
        self.entry_phone.place(x=325, y=140)

        btn_cancel = ttk.Button(self, text='Close', command=self.destroy)
        btn_cancel.place(x=350, y=300)

        self.btn_add = ttk.Button(self, text='Add')
        self.btn_add.place(x=200, y=300)
        self.btn_add.bind('<Button-1>', lambda event: self.view.add_values(self.entry_name.get(),
                                                                       self.entry_adress.get(),
                                                                       self.entry_postal_code.get(),
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
        btn_edit.bind('<Button-1>')

        self.btn_add.destroy()


class CustomerDialog(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_customer()
        self.db = customervalues
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
                                      compound=tk.TOP, padx="10", pady="3", font="10")
        btn_delete_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='zoom_in.png')
        btn_search_dialog = tk.Button(self, text='Search', bg='#d7d8e0', bd=0, image=self.search_img,
                                      compound=tk.TOP, padx="10", pady="3", font="10")
        btn_search_dialog.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='refresh.png')
        btn_search_dialog = tk.Button(self, text='Refresh', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                      compound=tk.TOP, padx="10", pady="3", font="10")
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

        self.tree.heading('CustomerID', text='CustomerID')
        self.tree.heading('LastName', text='LastName')
        self.tree.heading('FirstName', text='FirstName')
        self.tree.heading('Adress', text='Adress')
        self.tree.heading('City', text='City')
        self.tree.heading('Phone', text='Phone')
        self.tree.heading('PetShopID', text='PetShopID')

        self.tree.pack()

    def add_values(self, LastName, FirstName, Adress, City, Phone, PetShopID):
        self.db.insert_values(LastName, FirstName, Adress, City, Phone, PetShopID)
        self.view_values()

    def view_values(self):
        self.db.c.execute('''SELECT * FROM Customer''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def open_dialog_customer(self):
        AddCustomer()

    def update_dialog_customer(self):
        UpdateCustomer()

class AddCustomer(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_child()

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
        self.btn_add.bind('<Button-1>', lambda event: self.view.add_values(self.entry_lastname.get(),
                                                                       self.entry_firstname.get(),
                                                                       self.entry_adress.get(),
                                                                        self.entry_city.get(),
                                                                        self.entry_phone.get(),
                                                                        self.entry_petshopid.get()))

class UpdateCustomer(AddCustomer):
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

class EmployeeDialog(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_employee()
        self.view = pet_shop_table

    # self.db = db

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
                                      compound=tk.TOP, padx="15", pady="6", font="15")
        btn_delete_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='zoom_in.png')
        btn_search_dialog = tk.Button(self, text='Search', bg='#d7d8e0', bd=0, image=self.search_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15")
        btn_search_dialog.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='refresh.png')
        btn_search_dialog = tk.Button(self, text='Refresh', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15")
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

        self.tree.heading('EmployeeID', text='EmployeeID')
        self.tree.heading('LastName', text='LastName')
        self.tree.heading('FirstName', text='FirstName')
        self.tree.heading('TitleOfCourtesy', text='TitleOfCourtesy')
        self.tree.heading('HireDate', text='HireDate')
        self.tree.heading('Adress', text='Adress')
        self.tree.heading('City', text='City')
        self.tree.heading('Phone', text='Phone')
        self.tree.heading('Salary', text='Salary')
        self.tree.heading('PetShopID', text='PetShopID')

        self.tree.pack()

    def open_dialog_employee(self):
        AddEmployee()

    def update_dialog_employee(self):
        UpdateEmployee()

class AddEmployee(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_child()
        self.view = pet_shop_table

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
        self.btn_add.bind('<Button-1>')

class UpdateEmployee(AddEmployee):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = pet_shop_table

    def init_edit(self):
        self.title('Edit')
        btn_edit = ttk.Button(self, text='Edit')
        btn_edit.place(x=200, y=350)
        btn_edit.bind('<Button-1>')

        self.btn_add.destroy()

class OrderDialog(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_order()

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
                                      compound=tk.TOP, padx="15", pady="6", font="15")
        btn_delete_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='zoom_in.png')
        btn_search_dialog = tk.Button(self, text='Search', bg='#d7d8e0', bd=0, image=self.search_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15")
        btn_search_dialog.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='refresh.png')
        btn_search_dialog = tk.Button(self, text='Refresh', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15")
        btn_search_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('OrderID', 'DateOfSale', 'Discount', 'PetShopID', 'EmployeeID',
                                                'CustomerID','PetID','PetAccessoryID', 'PetFoodId'),
                                 height=34, show='headings')

        self.tree.column('OrderID', width=150, anchor=tk.CENTER)
        self.tree.column('DateOfSale', width=100, anchor=tk.CENTER)
        self.tree.column('Discount', width=100, anchor=tk.CENTER)
        self.tree.column('PetShopID', width=90, anchor=tk.CENTER)
        self.tree.column('EmployeeID', width=90, anchor=tk.CENTER)
        self.tree.column('CustomerID', width=90, anchor=tk.CENTER)
        self.tree.column('PetID', width=90, anchor=tk.CENTER)
        self.tree.column('PetAccessoryID', width=90, anchor=tk.CENTER)
        self.tree.column('PetFoodId', width=90, anchor=tk.CENTER)

        self.tree.heading('OrderID', text='OrderID')
        self.tree.heading('DateOfSale', text='DateOfSale')
        self.tree.heading('Discount', text='Discount')
        self.tree.heading('PetShopID', text='PetShopID')
        self.tree.heading('EmployeeID', text='EmployeeID')
        self.tree.heading('CustomerID', text='CustomerID')
        self.tree.heading('PetID', text='PetID')
        self.tree.heading('PetAccessoryID', text='PetAccessoryID')
        self.tree.heading('PetFoodId', text='PetFoodId')


        self.tree.pack()

    def open_dialog_order(self):
        AddOrder()

    def update_dialog_order(self):
        UpdateOrder()

class AddOrder(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_child()
        self.view = pet_shop_table

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
        self.btn_add.bind('<Button-1>')

class UpdateOrder(AddOrder):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = pet_shop_table

    def init_edit(self):
        self.title('Edit')
        btn_edit = ttk.Button(self, text='Edit')
        btn_edit.place(x=200, y=320)
        btn_edit.bind('<Button-1>')

        self.btn_add.destroy()

class PetDialog(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_pet()

    # self.db = db

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
                                      compound=tk.TOP, padx="15", pady="6", font="15")
        btn_delete_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='zoom_in.png')
        btn_search_dialog = tk.Button(self, text='Search', bg='#d7d8e0', bd=0, image=self.search_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15")
        btn_search_dialog.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='refresh.png')
        btn_search_dialog = tk.Button(self, text='Refresh', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15")
        btn_search_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('PetID', 'Specie', 'Color', 'Gender', 'Age', 'Description'),
                                 height=34, show='headings')

        self.tree.column('PetID', width=150, anchor=tk.CENTER)
        self.tree.column('Specie', width=140, anchor=tk.CENTER)
        self.tree.column('Color', width=100, anchor=tk.CENTER)
        self.tree.column('Gender', width=100, anchor=tk.CENTER)
        self.tree.column('Age', width=120, anchor=tk.CENTER)
        self.tree.column('Description', width=380, anchor=tk.CENTER)

        self.tree.heading('PetID', text='PetID')
        self.tree.heading('Specie', text='Specie')
        self.tree.heading('Color', text='Color')
        self.tree.heading('Gender', text='Gender')
        self.tree.heading('Age', text='Age')
        self.tree.heading('Description', text='Description')

        self.tree.pack()

    def open_dialog_pet(self):
        AddPet()

    def update_dialog_pet(self):
        UpdatePet()

class AddPet(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_child()
        self.view = pet_shop_table

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
        self.btn_add.bind('<Button-1>')

class UpdatePet(AddPet):
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

class PetFoodDialog(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_pet_food()

    # self.db = db

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
                                      compound=tk.TOP, padx="15", pady="6", font="15")
        btn_delete_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='zoom_in.png')
        btn_search_dialog = tk.Button(self, text='Search', bg='#d7d8e0', bd=0, image=self.search_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15")
        btn_search_dialog.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='refresh.png')
        btn_search_dialog = tk.Button(self, text='Refresh', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15")
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

        self.tree.heading('PetFoodID', text='PetFoodID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Price', text='Price')
        self.tree.heading('PackageType', text='PackageType')
        self.tree.heading('Weight', text='Weight')
        self.tree.heading('PetID', text='PetID')
        self.tree.heading('ManufacturerID', text='ManufacturerID')

        self.tree.pack()

    def open_dialog_pet_food(self):
        AddPetFood()

    def update_dialog_pet_food(self):
        UpdatePetFood()

class AddPetFood(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_child()
        self.view = pet_shop_table

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
        Weight = tk.Label(self, text='PostalCode:')
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
        self.btn_add.bind('<Button-1>')

class UpdatePetFood(AddPetFood):
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

class PetAccessoryDialog(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_pet_accessory()

    # self.db = db

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
                                      compound=tk.TOP, padx="15", pady="6", font="15")
        btn_delete_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='zoom_in.png')
        btn_search_dialog = tk.Button(self, text='Search', bg='#d7d8e0', bd=0, image=self.search_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15")
        btn_search_dialog.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='refresh.png')
        btn_search_dialog = tk.Button(self, text='Refresh', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15")
        btn_search_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('PetAccessoryID', 'Name', 'Size', 'Price', 'PetID', 'ManufacturerID'),
                                 height=34, show='headings')

        self.tree.column('PetAccessoryID', width=150, anchor=tk.CENTER)
        self.tree.column('Name', width=120, anchor=tk.CENTER)
        self.tree.column('Size', width=150, anchor=tk.CENTER)
        self.tree.column('Price', width=150, anchor=tk.CENTER)
        self.tree.column('PetID', width=90, anchor=tk.CENTER)
        self.tree.column('ManufacturerID', width=140, anchor=tk.CENTER)

        self.tree.heading('PetAccessoryID', text='PetAccessoryID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Size', text='Size')
        self.tree.heading('Price', text='Price')
        self.tree.heading('PetID', text='PetID')
        self.tree.heading('ManufacturerID', text='ManufacturerID')

        self.tree.pack()

    def open_dialog_pet_accessory(self):
        AddPetAccessory()

    def update_dialog_pet_accessory(self):
        UpdatePetAccessory()

class AddPetAccessory(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_child()
        self.view = pet_shop_table

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
        self.btn_add.bind('<Button-1>')

class UpdatePetAccessory(AddPetAccessory):
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

class ManufacturerDialog(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_manufacturer()

    # self.db = db

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
                                      compound=tk.TOP, padx="15", pady="6", font="15")
        btn_delete_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file='zoom_in.png')
        btn_search_dialog = tk.Button(self, text='Search', bg='#d7d8e0', bd=0, image=self.search_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15")
        btn_search_dialog.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file='refresh.png')
        btn_search_dialog = tk.Button(self, text='Refresh', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                      compound=tk.TOP, padx="15", pady="6", font="15")
        btn_search_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('ManufacturerID', 'Name', 'Adress', 'ProductsCategory'),
                                 height=34, show='headings')

        self.tree.column('ManufacturerID', width=140, anchor=tk.CENTER)
        self.tree.column('Name', width=155, anchor=tk.CENTER)
        self.tree.column('Adress', width=153, anchor=tk.CENTER)
        self.tree.column('ProductsCategory', width=200, anchor=tk.CENTER)

        self.tree.heading('ManufacturerID', text='ManufacturerID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Adress', text='Adress')
        self.tree.heading('ProductsCategory', text='ProductsCategory')

        self.tree.pack()

    def open_dialog_manufacturer(self):
        AddManufacturer()

    def update_dialog_manufacturer(self):
        UpdateManufacturer()

class AddManufacturer(tk.Toplevel):
    def __init__(self):
        super().__init__(pet_shop_dialog)
        self.init_child()
        self.view = pet_shop_table

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
        self.btn_add.bind('<Button-1>')

class UpdateManufacturer(AddManufacturer):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = pet_shop_table

    def init_edit(self):
        self.title('Edit')
        btn_edit = ttk.Button(self, text='Edit')
        btn_edit.place(x=200, y=250)
        btn_edit.bind('<Button-1>')

        self.btn_add.destroy()

class PetShopTable:
    def __init__(self):
        self.conn = sqlite3.connect("PetShop.db")
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS PetShop(PetShopID integer primary key, Name varchar(10),
         Adress varchar(10), PostalCode varchar(10), Phone int)''')
        self.conn.commit()

    def insert_values(self, Name, Adress, PostalCode, Phone):
        self.c.execute('''INSERT INTO PetShop(Name, Adress, PostalCode, Phone) VALUES(?, ?, ?, ?)''',
                       (Name, Adress, PostalCode, Phone))
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
        self.c.execute('''CREATE TABLE IF NOT EXISTS Customer(CustomerID integer primary key, 
        LastName varchar(10), FirstName varchar(10), Adress varchar(30), City varchar(15), Phone bigint, PetShopID 
        integer not null)''')
        self.conn.commit()

    def insert_values(self, LastName, FirstName, Adress, City, Phone, PetShopID):
        self.c.execute('''INSERT INTO PetShop(LastName, FirstName, Adress, City, Phone, PetShopID)
        VALUES(?, ?, ?, ?, ?, ?)''',
                       (LastName, FirstName, Adress, City, Phone, PetShopID))
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
    petshopvalues = PetShopTable()
    pet_shop_table = PetShopDialog(pet_shop_dialog)
    pet_shop_table.pack()
    customervalues = CustomerDialog()
    pet_shop_dialog.title("PetShop Table")
    pet_shop_dialog.geometry("1020x700+300+200")
    pet_shop_dialog.resizable(False, False)

    pet_shop_dialog.mainloop()