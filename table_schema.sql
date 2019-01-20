CREATE DATABASE pipes;
USE pipes;

CREATE TABLE `sensorData` (
	`rowID` INT NOT NULL AUTO_INCREMENT,
	`deviceID` INT NOT NULL,
	`time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
	`soilHumidity` DOUBLE,
	`soilTemperature` DOUBLE,
	`pipeSurfaceTemperature` DOUBLE,
	`gasPressure` DOUBLE,
	`ultrasoundDistance` DOUBLE,
	`batteryCharge` DOUBLE,
	PRIMARY KEY (`rowID`)
);


CREATE TABLE `sensorMeta` (
	`rowID` INT NOT NULL AUTO_INCREMENT,
	`deviceID` INT NOT NULL,
	`time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
	`latitude` DOUBLE,
	`longitude` DOUBLE,
	`sensorInstallDate` DATETIME,
	`pipeInstallDate` DATETIME,
	`severityLevel` INT NOT NULL,
	`labels` TEXT,
	PRIMARY KEY (`rowID`)
);