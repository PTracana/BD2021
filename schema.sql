DROP TABLE IF EXISTS Product cascade;
DROP TABLE IF EXISTS Shelf cascade;
DROP TABLE IF EXISTS Planogram cascade;
DROP TABLE IF EXISTS Corridor cascade;
DROP TABLE IF EXISTS Supermarket cascade;
DROP TABLE IF EXISTS Supplier cascade;
DROP TABLE IF EXISTS Category cascade;
DROP TABLE IF EXISTS simplecategory cascade;
DROP TABLE IF EXISTS supercategory cascade;
DROP TABLE IF EXISTS ReplenishEvent cascade;
DROP TABLE IF EXISTS Supplies_prim cascade;
DROP TABLE IF EXISTS supplies_sec cascade;
DROP TABLE IF EXISTS displayed_in cascade;
DROP TABLE IF EXISTS consists_of cascade;

CREATE TABLE Supermarket(
    NIF INTEGER,
    S_name VARCHAR(80) NOT NULL,
    addr VARCHAR(80) NOT NULL,

    PRIMARY KEY (NIF)
);

CREATE TABLE Corridor(
    nr INTEGER,
    width INTEGER,
    NIF INTEGER,
    PRIMARY KEY (nr, NIF),
    FOREIGN KEY(NIF) REFERENCES Supermarket(NIF)
);

CREATE TABLE Shelf(
    side VARCHAR(80) CONSTRAINT valid_side CHECK(side in ('left', 'right')),
    height VARCHAR(80) CONSTRAINT valid_height CHECK(height in ('floor', 'middle', 'upper')),
    nr INTEGER,
    NIF INTEGER,
    PRIMARY KEY (nr, NIF, side, height),
    FOREIGN KEY (nr, NIF) REFERENCES Corridor(nr, NIF)
);

CREATE TABLE Category (

    name VARCHAR(80) ,
    PRIMARY KEY(name)

    -- No category can exist at the same time in both the table 'simpleCategory' or in the table 'superCategory'

    -- Every category must exist either in the table 'simpleCategory' or in the table 'superCategory'

    -- Every Category must be in the table Displayed_in


);

CREATE TABLE Product(
    ean NUMERIC(13) ,
    descr VARCHAR(80) NOT NULL,
    name VARCHAR(80),
    PRIMARY KEY (ean),
    FOREIGN KEY (name) REFERENCES Category(name) ON DELETE CASCADE


    --every product must be in the supplies_prim and supplies_sec table 
); 


CREATE TABLE Planogram(
    facings INTEGER NOT NULL ,
    units INTEGER NOT NULL ,
    loc INTEGER NOT NULL,
    nr INTEGER,
    side VARCHAR(80),
    height VARCHAR(80),
    NIF INTEGER,
    ean NUMERIC(13) ,
    PRIMARY KEY (ean, side, height, nr, NIF),
    FOREIGN KEY (nr, NIF, side, height) REFERENCES Shelf(nr,NIF, side, height),
    FOREIGN KEY (ean) REFERENCES Product(ean) ON DELETE CASCADE
    
);

CREATE TABLE ReplenishEvent (
    unitsRep NUMERIC(9) NOT NULL,
    instant DATE  CONSTRAINT valid CHECK(instant < now()) ,
    side VARCHAR(80) ,
    height VARCHAR(80) ,
    nr INTEGER,
    NIF INTEGER,
    ean NUMERIC(13) ,
    PRIMARY KEY (ean, side, height, nr, NIF, instant),
    FOREIGN KEY (ean, side, height, nr, NIF) REFERENCES Planogram(ean, side, height, nr, NIF) ON DELETE CASCADE
   
);


CREATE TABLE Supplier(

    nif INTEGER,
    s_name VARCHAR(80),
    PRIMARY KEY (nif)
);

CREATE TABLE Supplies_prim(
    nif INTEGER,
    ean NUMERIC(13),
    dia DATE,
    PRIMARY KEY (dia, nif, ean),
    FOREIGN KEY (nif) REFERENCES Supplier(nif),
    FOREIGN KEY (ean) REFERENCES Product(ean) ON DELETE CASCADE
);

CREATE TABLE Supplies_sec(
    nif INTEGER,
    ean NUMERIC(13) ,
    PRIMARY KEY (nif, ean),
    FOREIGN KEY (nif) REFERENCES Supplier(nif),
    FOREIGN KEY (ean) REFERENCES Product(ean) ON DELETE CASCADE
    -- For a given Product, a supplier cannot be simultaneously a Primary and Secondary Supplier
    -- A product can only have at most 3 Secondary Suppliers
    
);

CREATE TABLE simplecategory (

    name VARCHAR(80) ,
    PRIMARY KEY(name),
    FOREIGN KEY(name) REFERENCES Category(name) ON DELETE CASCADE

);

CREATE TABLE supercategory(

    name VARCHAR(80) ,
    PRIMARY KEY(name),
    FOREIGN KEY(name) REFERENCES Category(name) ON DELETE CASCADE

    -- Every superCategory must be present in the consists:of table

);

CREATE TABLE consists_of(
    name_super VARCHAR(80),
    name_descendant VARCHAR(80) CONSTRAINT ic1 CHECK ( name_super != name_descendant ),
    FOREIGN KEY (name_super) REFERENCES supercategory(name) ON DELETE CASCADE,
    FOREIGN KEY (name_descendant) REFERENCES Category(name) ON DELETE CASCADE

    --  Categories cannot cyclically consist of one another

);

CREATE TABLE Displayed_in(
    name VARCHAR(80),
    side VARCHAR(80),
    height VARCHAR(80),
    nr INTEGER,
    NIF INTEGER,
    PRIMARY KEY(name, side, height, nr, NIF),
    FOREIGN KEY (name) REFERENCES Category(name) ON DELETE CASCADE,
    FOREIGN KEY (side, height, nr, NIF) REFERENCES Shelf(side, height, nr, NIF)

);

