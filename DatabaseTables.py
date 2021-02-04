import sqlite3


class PetShopTable:
    def __init__(self):
        self.conn = sqlite3.connect("ZooShop.db")
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS PetShop(PetShopID integer not null primary key, Name varchar(10) not null,
         Adress varchar(30) unique not null, PostalCode varchar(10) not null, City varchar(15) not null,
          Phone bigint unique not null)''')
        self.conn.commit()

    def insert_values(self, Name, Adress, PostalCode, City, Phone):
        self.c.execute('''INSERT INTO PetShop(Name, Adress, PostalCode, City, Phone) VALUES(?, ?, ?, ?, ?)''',
                       (Name, Adress, PostalCode, City, Phone))
        self.conn.commit()


class EmployeeTable:
    def __init__(self):
        self.conn = sqlite3.connect("ZooShop.db")
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS Employee(EmployeeID integer primary key,
         LastName varchar(10) not null, FirstName varchar(10) not null,
          TitleOfCourtesy varchar(5) not null, HireDate datetime not null, Adress varchar(30) not null,
           City varchar(15) not null, Phone bigint unique not null, Salary int not null, PetShopID int not null)''')
        self.conn.commit()

    def insert_values(self, LastName, FirstName, TitleOfCourtesy, HireDate, Adress, City, Phone, Salary, PetShopID):
        self.c.execute('''INSERT INTO Employee(LastName, FirstName, TitleOfCourtesy, HireDate, Adress, City,
         Phone, Salary, PetShopID) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (LastName, FirstName, TitleOfCourtesy, HireDate, Adress, City, Phone, Salary, PetShopID))
        self.conn.commit()


class OrderTable:
    def __init__(self):
        self.conn = sqlite3.connect("ZooShop.db")
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS OrderTable(OrderID integer primary key, DateOfSale datetime not null,
         Discount int not null, PetShopID int not null, EmployeeID int not null, CustomerID int not null,
          PetID int, PetAccessoryID int, PetFoodID int)''')
        self.conn.commit()

    def insert_values(self, DateOfSale, Discount, PetShopID, EmployeeID, CustomerID, PetID, PetAccessoryID, PetFoodID):
        self.c.execute('''INSERT INTO OrderTable(DateOfSale, Discount, PetShopID, EmployeeID, CustomerID, PetID,
        PetAccessoryID, PetFoodID)
         VALUES(?, ?, ?, ?, ?, ?, ?, ?)''',
                       (DateOfSale, Discount, PetShopID, EmployeeID, CustomerID, PetID, PetAccessoryID, PetFoodID))
        self.conn.commit()


class PetTable:
    def __init__(self):
        self.conn = sqlite3.connect("ZooShop.db")
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS Pet(PetID integer primary key, Specie varchar(10) not null,
         Color varchar(10) not null, Gender varchar(10) not null, Age int not null, Description text not null)''')
        self.conn.commit()

    def insert_values(self, Specie, Color, Gender, Age, Description):
        self.c.execute('''INSERT INTO Pet(Specie, Color, Gender, Age, Description) VALUES(?, ?, ?, ?, ?)''',
                       (Specie, Color, Gender, Age, Description))
        self.conn.commit()


class PetAccessoryTable:
    def __init__(self):
        self.conn = sqlite3.connect("ZooShop.db")
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS PetAccessoryTable(PetAccessoryID integer primary key,
         Name varchar(10) not null, Size varchar(10) not null, Price int not null,
          PetID int not null, ManufacturerID int not null)''')
        self.conn.commit()

    def insert_values(self, Name, Size, Price, PetID, ManufacturerID):
        self.c.execute('''INSERT INTO PetAccessoryTable(Name, Size, Price, PetID, ManufacturerID)
         VALUES(?, ?, ?, ?, ?)''',
                       (Name, Size, Price, PetID, ManufacturerID))
        self.conn.commit()


class PetFoodTable:
    def __init__(self):
        self.conn = sqlite3.connect("ZooShop.db")
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS PetFood(PetFoodID integer primary key, Name varchar(10) not null, 
        Price int not null, PackageType varchar(10) not null, Weight varchar(10), 
        PetID int not null, ManufacturerID int not null)''')
        self.conn.commit()

    def insert_values(self, Name, Price, PackageType, Weight, PetID, ManufacturerID):
        self.c.execute('''INSERT INTO PetFood(Name, Price, PackageType, Weight, PetID, ManufacturerID)
         VALUES(?, ?, ?, ?, ?, ?)''',
                       (Name, Price, PackageType, Weight, PetID, ManufacturerID))
        self.conn.commit()


class CustomerTable:
    def __init__(self):
        self.conn = sqlite3.connect("ZooShop.db")
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS Customer(CustomerID integer primary key, 
        LastName varchar(10) not null, FirstName varchar(10) not null,
         Adress varchar(30) not null, City varchar(15) not null, Phone bigint unique not null, 
         PetShopID int not null)''')
        self.conn.commit()

    def insert_values(self, LastName, FirstName, Adress, City, Phone, PetShopID):
        self.c.execute('''INSERT INTO Customer(LastName, FirstName, Adress, City, Phone, PetShopId)
         VALUES(?, ?, ?, ?, ?, ?)''',
                       (LastName, FirstName, Adress, City, Phone, PetShopID))
        self.conn.commit()


class ManufacturerTable:
    def __init__(self):
        self.conn = sqlite3.connect("ZooShop.db")
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS Manufacturer(ManufacturerID integer primary key, 
        Name varchar(10) not null, Adress varchar(10) not null, ProductsCategory varchar(10) not null)''')
        self.conn.commit()

    def insert_values(self, Name, Adress, ProductCategory):
        self.c.execute('''INSERT INTO Manufacturer(Name, Adress, ProductsCategory) VALUES(?, ?, ?)''',
                       (Name, Adress, ProductCategory))
        self.conn.commit()
