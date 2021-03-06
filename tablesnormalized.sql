DROP TABLE IF EXISTS Accounts;

CREATE TABLE AccountLogin (
    UserID INT NOT NULL AUTO_INCREMENT,
    Username VARCHAR(45) NOT NULL,
    Firstname VARCHAR(45) NOT NULL,
    Lastname VARCHAR(45) NOT NULL,

CREATE TABLE AccountsInfo (
    UserID INT NOT NULL AUTO_INCREMENT,
    Email Address VARCHAR(45) NOT NULL,
    Home Address VARCHAR(45) NOT NULL,
    ZIP INT(5) NOT NULL,
    Phonenum int(10)NOT NULL,
    Gender VARCHAR(45) NOT NULL,
    Role VARCHAR(45) NOT NULL,
    PRIMARY KEY (UserID)
);

CREATE TABLE AccountCity (
    ZIP INT(5) NOT NULL,
    City VARCHAR(45) NOT NULL,
    Role VARCHAR(45) NOT NULL,
    PRIMARY KEY (UserID)
);


CREATE TABLE Generalization(
    FOREIGN KEY (UserID),
    Primary Key(UserID)
);
CREATE TABLE Managers
    FOREIGN KEY (UserID),
    Primary Key(UserID)
);
CREATE TABLE Vendors (
    VendorID INT NOT NULL AUTO_INCREMENT,
    VenName VARCHAR(45) NOT NULL,
    MinOrdQuantity INT NOT NULL,
    DatePurchased DATE NOT NULL,
    ItemsPurchased INT NOT NULL,
    Quality VARCHAR(45) NOT NULL,
    EmailAddress VARCHAR(45) NOT NULL,
    Phonenum INT(10)NOT NULL,
    PRIMARY KEY (VENDERID)
);
CREATE TABLE PurchaseOrder (
    PurchID INT NOT NULL AUTO_INCREMENT,
    PurchQuantity INT NOT NULL,
    ShippingAddress VARCHAR(45),
    Payment VARCHAR(45),
    PhoneNum INT NOT NULL,
    SupplierID_1 INT NOT NULL,
    Email Address VARCHAR(45),
    PRIMARY KEY (PurchID),
    FOREIGN KEY (VenderID),
    FOREIGN KEY (UserID),
    FOREIGN KEY (RequestID),
    FOREIGN KEY (ItemID),
    FOREIGN KEY (SupplierID)
);

CREATE TABLE OrderReciept (
    ReceiptID INT NOT NULL AUTO_INCREMENT,
    OrderDate date NOT NULL,
    TotalOrdered INT NOT NULL,
    OrderStatus VARCHAR(45)
    ItemName VARCHAR(45),
    Price INT NOT NULL,
    BillingAddress VARCHAR(45),
    Payment VARCHAR(45)
    OrderSum INT,
    PRIMARY KEY (ReceiptID),
    FOREIGN KEY (PurchID),
    FOREIGN KEY (VenderID),
    FOREIGN KEY (UserID),
    FOREIGN KEY (RequestID),
    FOREIGN KEY (ItemID),
    FOREIGN KEY (SupplierID),
);
CREATE TABLE MaterialRequests (
    RequestID INT NOT NULL AUTO_INCREMENT,
    Quantity INT not null
    PRIMARY KEY INT NOT NULL AUTO_INCREMENT,
    FOREIGN KEY (ItemID),
    FOREIGN KEY (SupplierID),
    FOREIGN KEY (UserID)
);
CREATE TABLE Items (
    ItemID INT NOT NULL AUTO_INCREMENT,
    ItemCode INT NOT NULL,
    ItemName VARCHAR(45),
    Quantity INT NOT NULL,
    itemDesc VARCHAR(45)NULL,
    Price INT NOT NULL,
    ManufacDate VARCHAR(45) NOT NULL,
    ExpireDate date NOT NULL
    Manufacturer VARCHAR(45) NOT NULL,
    ItemImage VARCHAR(45) NULL,
    Supplier VARCHAR(45) NULL,
    Alternative Item VARCHAR(45) NULL,
    PRIMARY KEY (ItemID),
    FOREIGN KEY (SupplierID),
    FOREIGN KEY (UserID)
);
CREATE TABLE Supplier(
    SupplierID INT NOT NULL AUTO_INCREMENT,
    Address VARCHAR(45) NOT NULL,
    Name VARCHAR(45)NOT NULL,
	--AltItemShould be  Checkmark
    Alt Item VARCHAR(45)NULL,
    PRIMARY KEY (SupplierID(
    )
