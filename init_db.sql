CREATE DATABASE IF NOT EXISTS surahdb;
USE surahdb;

CREATE TABLE IF NOT EXISTS surahs(
    id INT PRIMARY KEY UNIQUE, -- The surah's number in the Quran
    chronology INT,
    titlefr VARCHAR(40),
    period INT,
    nbverses INT
);

CREATE OR REPLACE VIEW v_chron_order AS
SELECT *
FROM surahs
ORDER BY chronology;

CREATE OR REPLACE VIEW v_trad_order AS
SELECT *
FROM surahs
ORDER BY id;
