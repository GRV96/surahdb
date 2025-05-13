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
