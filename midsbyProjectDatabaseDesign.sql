-- CREATE DATABASE midsbuyProject; --

--- DROP TABLE tempoplayerIds; --
USE midsbuyProject;
CREATE TABLE tempoplayerIds(
    playerID VARCHAR(255) NOT NULL PRIMARY KEY
);

-- DROP TABLE plyerIdsAndNames; --
/*
CREATE TABLE plyerIdsAndNames(
	playerID VARCHAR(255) NOT NULL PRIMARY KEY,
    playerName VARCHAR(255) NOT NULL
); */

INSERT INTO plyerIdsAndNames(playerID)
VALUES(5920206078);

DELETE FROM tempoplayerIds WHERE playerID = "1234567890";

INSERT INTO plyerIdsAndNames(playerID, playerName)
VALUES();
