CREATE USER 'orson.krennic'@'%' IDENTIFIED BY 'kyberTHIEF1';
GRANT ALL PRIVILEGES ON *.* TO 'orson.krennic'@'%';
CREATE USER 'maximilian.veers'@'%' IDENTIFIED BY 'startYOURlanding';
GRANT ALL PRIVILEGES ON scarif.* To 'maximilian.veers'@'%';
CREATE USER 'galen.erso'@'%' IDENTIFIED BY 'starDUST';
GRANT ALL PRIVILEGES ON eadu.* To 'galen.erso'@'%';
CREATE USER 'kendal.ozzel'@'%' IDENTIFIED BY 'tooCLOSEtoHOTH';
FLUSH PRIVILEGES;