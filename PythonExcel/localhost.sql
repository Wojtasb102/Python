-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Czas generowania: 08 Lis 2021, 09:44
-- Wersja serwera: 5.7.33-36
-- Wersja PHP: 7.4.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `34017600_wykaz`
--
CREATE DATABASE IF NOT EXISTS `34017600_wykaz` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `34017600_wykaz`;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `odejscia`
--

CREATE TABLE `odejscia` (
  `ID` int(11) NOT NULL,
  `IMIE` varchar(30) DEFAULT NULL,
  `DATA` date DEFAULT NULL,
  `DZIAL` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `odejscia`
--

INSERT INTO `odejscia` (`ID`, `IMIE`, `DATA`, `DZIAL`) VALUES
(1, 'MARCIN BAK', '2009-01-07', 'P1'),
(2, 'ADAM NOWAK', '2009-01-16', 'P2'),
(3, 'JAN KOWALSKI', '2009-01-17', 'P2'),
(4, 'MATEUSZ RUJ', '2009-01-18', 'P1'),
(5, 'JANUSZ TRACZ', '2009-01-29', 'P1'),
(6, 'STANISŁAW KRÓL', '2009-01-02', 'P2'),
(7, 'MIROSŁAW CUGOWSKI', '2009-01-17', 'P2'),
(8, 'JAN NOWAK', '2009-01-18', 'P1'),
(9, 'GRZEGORZ LATO', '2009-01-12', 'P2'),
(10, 'ZBYSZEK BONIEK', '2009-01-18', 'P1'),
(11, 'ROBERT LEWANDOWSKI', '2009-01-20', 'P2');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `przeniesienia`
--

CREATE TABLE `przeniesienia` (
  `ID` int(11) NOT NULL,
  `IMIE` varchar(30) DEFAULT NULL,
  `DATA` date DEFAULT NULL,
  `DZIALDO` varchar(10) DEFAULT NULL,
  `DZIALZ` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `przeniesienia`
--

INSERT INTO `przeniesienia` (`ID`, `IMIE`, `DATA`, `DZIALDO`, `DZIALZ`) VALUES
(1, 'MARCIN BAK', '2009-01-17', 'P1', 'P2'),
(2, 'ADAM NOWAK', '2009-01-12', 'P2', 'P1'),
(3, 'JAN KOWALSKI', '2009-01-13', 'P2', 'P1'),
(4, 'MATEUSZ RUJ', '2009-01-28', 'P1', 'P2'),
(5, 'MATEUSZ RUJ', '2009-01-01', 'P1', 'P2');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `przyjecia`
--

CREATE TABLE `przyjecia` (
  `ID` int(11) NOT NULL,
  `IMIE` varchar(30) DEFAULT NULL,
  `DATA` date DEFAULT NULL,
  `DZIAL` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `przyjecia`
--

INSERT INTO `przyjecia` (`ID`, `IMIE`, `DATA`, `DZIAL`) VALUES
(1, 'MARCIN BAK', '2009-05-05', 'P1'),
(2, 'ADAM NOWAK', '2009-05-06', 'P2'),
(3, 'JAN KOWALSKI', '2009-05-07', 'P2'),
(4, 'MATEUSZ RUJ', '2009-05-08', 'P1'),
(5, 'JANUSZ TRACZ', '2009-05-09', 'P1'),
(6, 'STANISŁAW KRÓL', '2009-01-02', 'P2'),
(7, 'MIROSŁAW CUGOWSKI', '2009-01-07', 'P2'),
(8, 'JAN NOWAK', '2009-01-18', 'P1'),
(9, 'GRZEGORZ LATO', '2009-01-18', 'P2'),
(10, 'ZBYSZEK BONIEK', '2009-01-18', 'P1'),
(11, 'ROBERT LEWANDOWSKI', '2009-01-30', 'P2');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `wykaz`
--

CREATE TABLE `wykaz` (
  `ID` int(11) NOT NULL,
  `Imie` varchar(50) DEFAULT NULL,
  `Dział` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `wykaz`
--

INSERT INTO `wykaz` (`ID`, `Imie`, `Dział`) VALUES
(1, 'Jan Nowak', 'P1'),
(2, 'Jan Szyc', 'P2');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `odejscia`
--
ALTER TABLE `odejscia`
  ADD PRIMARY KEY (`ID`);

--
-- Indeksy dla tabeli `przeniesienia`
--
ALTER TABLE `przeniesienia`
  ADD PRIMARY KEY (`ID`);

--
-- Indeksy dla tabeli `przyjecia`
--
ALTER TABLE `przyjecia`
  ADD PRIMARY KEY (`ID`);

--
-- Indeksy dla tabeli `wykaz`
--
ALTER TABLE `wykaz`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT dla zrzuconych tabel
--

--
-- AUTO_INCREMENT dla tabeli `odejscia`
--
ALTER TABLE `odejscia`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT dla tabeli `przeniesienia`
--
ALTER TABLE `przeniesienia`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT dla tabeli `przyjecia`
--
ALTER TABLE `przyjecia`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT dla tabeli `wykaz`
--
ALTER TABLE `wykaz`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
