DELETE FROM ReplenishEvent ;
DELETE FROM Planogram ;
DELETE FROM Supplies_prim ;
DELETE FROM supplies_sec ;
DELETE FROM Product ;
DELETE FROM displayed_in ;
DELETE FROM Shelf ;
DELETE FROM Corridor ;
DELETE FROM Supermarket ;
DELETE FROM consists_of ;
DELETE FROM simplecategory ;
DELETE FROM supercategory ;
DELETE FROM Category ;

DELETE FROM Supplier ;

--populate supermarket

INSERT INTO supermarket(nif, s_name, addr) VALUES (93610, 'Auchan', 'Rua alberto');


-- corridor

INSERT INTO corridor(nr, width, nif) VALUES (1,10,93610);
INSERT INTO corridor(nr, width, nif) VALUES (2,15,93610);
INSERT INTO corridor(nr, width, nif) VALUES (3,22,93610);
INSERT INTO corridor(nr, width, nif) VALUES (4,10,93610);
INSERT INTO corridor(nr, width, nif) VALUES (5,10,93610);
INSERT INTO corridor(nr, width, nif) VALUES (6,10,93610);




--populate shelfs

INSERT INTO shelf(side, height, nr, nif) VALUES ('left', 'floor', 1, 93610);
INSERT INTO shelf(side, height, nr, nif) VALUES ('right', 'middle', 2, 93610);
INSERT INTO shelf(side, height, nr, nif) VALUES ('left', 'upper', 3, 93610);
INSERT INTO shelf(side, height, nr, nif) VALUES ('left', 'upper', 1, 93610);
INSERT INTO shelf(side, height, nr, nif) VALUES ('right', 'floor',3, 93610);




--populate categories

INSERT INTO category(name) VALUES ('Milk');
INSERT INTO category(name) VALUES ('Condensed Milk');
INSERT INTO category(name) VALUES ('Whole Milk');
INSERT INTO category(name) VALUES ('Coconut Milk');
INSERT INTO category(name) VALUES ('Meat');
INSERT INTO category(name) VALUES ('Cow Meat');
INSERT INTO category(name) VALUES ('Fish');
INSERT INTO category(name) VALUES ('River Fish');


--Populate Products
INSERT INTO product(ean, descr, name) VALUES (7854123690546,'leite gordo', 'Whole Milk');
INSERT INTO product(ean, descr, name) VALUES (7842651395888,'bife','Cow Meat');
INSERT INTO product(ean, descr, name) VALUES (9125436740551,'carpa','River Fish');
INSERT INTO product(ean, descr, name) VALUES (1024356875915,'leite condensado', 'Condensed Milk');
INSERT INTO product(ean, descr, name) VALUES (7842365196001,'leite de coco','Coconut Milk');

--populate the planogram for every product
INSERT INTO planogram(facings, units, loc, side, height, nr, nif, ean) VALUES (15,25,1,'left', 'floor', 1, 93610,7854123690546);
INSERT INTO planogram(facings, units, loc, side, height, nr, nif, ean) VALUES (42,59,3,'right', 'floor',3, 93610,1024356875915);
INSERT INTO planogram(facings, units, loc, side, height, nr, nif, ean) VALUES(21,29,2,'right', 'middle', 2, 93610,9125436740551);
INSERT INTO planogram(facings, units, loc, side, height, nr, nif, ean) VALUES(61,93,4,'left', 'upper', 1, 93610,7842651395888);
INSERT INTO planogram(facings, units, loc, side, height, nr, nif, ean) VALUES(54,55,5,'left', 'upper', 3, 93610,7842365196001);

--populate replenish event
INSERT INTO replenishevent(unitsrep, instant, side, height, nr, nif, ean)  VALUES (10,'02-02-2021','right', 'floor',3, 93610,1024356875915);
INSERT INTO replenishevent(unitsrep, instant, side, height, nr, nif, ean)  VALUES (45, '12-04-2021','left', 'floor', 1, 93610,7854123690546);
INSERT INTO replenishevent(unitsrep, instant, side, height, nr, nif, ean)  VALUES (16,'25-03-2021','left', 'upper', 1, 93610,7842651395888);
INSERT INTO replenishevent(unitsrep, instant, side, height, nr, nif, ean)  VALUES (14, '13-04-2021','left', 'upper', 3, 93610,7842365196001);
INSERT INTO replenishevent(unitsrep, instant, side, height, nr, nif, ean)  VALUES (22,'29-03-2021','right', 'middle', 2, 93610,9125436740551);


--populate super categories
INSERT INTO supercategory(name) VALUES ('Milk');
INSERT INTO supercategory(name) VALUES ('Meat');
INSERT INTO supercategory(name) VALUES ('Fish');

--populate simple categories
INSERT INTO simplecategory(name) VALUES ('Condensed Milk');
INSERT INTO simplecategory(name) VALUES ('Whole Milk');
INSERT INTO simplecategory(name) VALUES ('Coconut Milk');
INSERT INTO simplecategory(name) VALUES ('Cow Meat');
INSERT INTO simplecategory(name) VALUES ('River Fish');

--populate consists_of
INSERT INTO consists_of(name_super, name_descendant) VALUES ('Milk', 'Condensed Milk');
INSERT INTO consists_of(name_super, name_descendant) VALUES ('Milk', 'Whole Milk');
INSERT INTO consists_of(name_super, name_descendant) VALUES ('Milk', 'Coconut Milk');
INSERT INTO consists_of(name_super, name_descendant) VALUES ('Meat', 'Cow Meat');
INSERT INTO consists_of(name_super, name_descendant) VALUES ('Fish', 'River Fish');


--populate displayed_in
INSERT INTO displayed_in(name, side, height, nr, nif) VALUES ('Milk', 'left', 'floor', 1, 93610);
INSERT INTO displayed_in(name, side, height, nr, nif) VALUES ('Meat', 'right', 'middle', 2, 93610);
INSERT INTO displayed_in(name, side, height, nr, nif) VALUES ('Fish', 'left', 'upper', 3, 93610);

--populating suppliers
INSERT INTO supplier(nif, s_name) VALUES (954861,'John');
INSERT INTO supplier(nif, s_name) VALUES (5846215, 'Stephanie');
INSERT INTO supplier(nif, s_name) VALUES (57487120, 'Alexander');
INSERT INTO supplier(nif, s_name) VALUES (45648186, 'Paul');
INSERT INTO supplier(nif, s_name) VALUES (31367208,'Richard');
INSERT INTO supplier(nif, s_name) VALUES(1234612, 'Jane');

-- Populating prim supplier
INSERT INTO supplies_prim(nif, ean, dia) VALUES (954861,7842651395888,'12-05-2022');
INSERT INTO supplies_prim(nif, ean, dia) VALUES (5846215,7854123690546,'06-12-2020');
INSERT INTO supplies_prim(nif, ean, dia) VALUES (57487120,9125436740551,'15-03-2021');
INSERT INTO supplies_prim(nif, ean, dia) VALUES (45648186,1024356875915,'28-03-2021');
INSERT INTO supplies_prim(nif, ean, dia) VALUES (31367208,7842365196001, '14-02-2021');


-- populating secondary supplier
INSERT INTO supplies_sec(nif, ean) VALUES (31367208,7842651395888);
INSERT INTO supplies_sec(nif, ean) VALUES (31367208,7854123690546);
INSERT INTO supplies_sec(nif, ean) VALUES (31367208,9125436740551);
INSERT INTO supplies_sec(nif, ean) VALUES (31367208,1024356875915);
INSERT INTO supplies_sec(nif, ean) VALUES (5846215,7842651395888);
INSERT INTO supplies_sec(nif, ean) VALUES (57487120,1024356875915);
INSERT INTO supplies_sec(nif, ean) VALUES (57487120,7842651395888);


