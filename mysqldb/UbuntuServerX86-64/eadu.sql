CREATE DATABASE IF NOT EXISTS eadu;
USE eadu;
CREATE TABLE IF NOT EXISTS users (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255),
	password VARCHAR(32)
);
INSERT INTO users (name, password) VALUES (
"Galen Erso",
"starDUST"
);
INSERT INTO users (name, password) VALUES (
"Kendal Ozzel",
"tooCLOSEtoHOTH"
);
INSERT INTO users (name, password) VALUES (
"Orson Krennic",
"IamREMARKABLE"
);
INSERT INTO users (name, password) VALUES (
"Maximilian Veers",
"startYOURlanding"
);
