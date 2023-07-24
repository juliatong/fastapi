-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: db:3306
-- Generation Time: Jul 24, 2023 at 05:34 AM
-- Server version: 8.0.19
-- PHP Version: 8.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `example`
--

-- --------------------------------------------------------

--
-- Table structure for table `ohlc price`
--

CREATE TABLE `ohlc price` (
  `UNIX` datetime NOT NULL,
  `SYMBOL` varchar(255) NOT NULL,
  `OPEN` decimal(10,0) NOT NULL,
  `CLOSE` decimal(10,0) NOT NULL,
  `HIGH` decimal(10,0) NOT NULL,
  `LOW` decimal(10,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='historical OHLC price data';

--
-- Dumping data for table `ohlc price`
--

INSERT INTO `ohlc price` (`UNIX`, `SYMBOL`, `OPEN`, `CLOSE`, `HIGH`, `LOW`) VALUES
('2022-02-16 00:21:40', 'BTCUSDT', 42123, 42146, 2148, 2121),
('2023-02-15 23:54:00', 'BTCUSDT', 42113, 42123, 42126, 42113);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ohlc price`
--
ALTER TABLE `ohlc price`
  ADD PRIMARY KEY (`UNIX`,`SYMBOL`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
