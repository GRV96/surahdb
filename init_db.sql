CREATE DATABASE IF NOT EXISTS surahdb;
USE surahdb;

CREATE TABLE IF NOT EXISTS surahs(
    id INT PRIMARY KEY UNIQUE, -- The surah's number in the Quran
    chronology INT,
    titlefr VARCHAR(40),
	-- 0: Meccan period
	-- 1: Medinan period
    period INT CHECK (period = 0 OR period = 1),
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

CREATE OR REPLACE VIEW v_surah_chronology_trad_order AS
SELECT chronology
FROM surahs
ORDER BY id;

CREATE OR REPLACE VIEW v_surah_ids_chron_order AS
SELECT id
FROM surahs
ORDER BY chronology;

CREATE OR REPLACE VIEW v_surah_length_chron_order AS
SELECT id, nbverses
FROM surahs
ORDER BY chronology;

CREATE OR REPLACE VIEW v_surah_length_trad_order AS
SELECT id, nbverses
FROM surahs
ORDER BY id;
