BEGIN TRANSACTION;
CREATE TABLE "items" (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`itemName`	TEXT NOT NULL,
	`ItemPrice`	INTEGER NOT NULL,
	`Weight`	NUMERIC,
	`Image `	TEXT
);
INSERT INTO `items` VALUES (1,'Tv',300,10,'tv.png');
INSERT INTO `items` VALUES (2,'Laptop',450,5,'laptop.png');
INSERT INTO `items` VALUES (3,'Desk',100,20,'desk.png');
INSERT INTO `items` VALUES (4,'Pc',500,15,'pc.png');
INSERT INTO `items` VALUES (5,'Book',20,2,'book.png');
INSERT INTO `items` VALUES (6,'Pen',5,1,'pen.png');
INSERT INTO `items` VALUES (7,'Ps',350,7,'ps.png');
INSERT INTO `items` VALUES (8,'Xbox one ',320,6,'xboxone.png');
INSERT INTO `items` VALUES (9,'Phone',600,3,'phone.png');
INSERT INTO `items` VALUES (10,'Chair',40,13,'chair.png');
COMMIT;
