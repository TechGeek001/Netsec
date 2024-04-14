CREATE DATABASE IF NOT EXISTS eadu;
USE eadu;
CREATE TABLE IF NOT EXISTS users (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255),
	password VARCHAR(32),
	remarks VARCHAR(255)
);
INSERT INTO users (name, password, remarks) VALUES (
"Galen Erso",
"starDUST",
"Executed // Reason: Traitor to the Empire"
);
INSERT INTO users (name, password, remarks) VALUES (
"Kendal Ozzel",
"tooCLOSEtoHOTH",
"Executed // Reason: Gross Incompetence"
);
INSERT INTO users (name, password, remarks) VALUES (
"Orson Krennic",
"IamREMARKABLE",
"Deceased // Reason: Death Star Strike on Scarif"
);
INSERT INTO users (name, password, remarks) VALUES (
"Maximilian Veers",
"startYOURlanding",
"Active"
);
