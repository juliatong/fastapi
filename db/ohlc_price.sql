-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: db:3306
-- Generation Time: Jul 24, 2023 at 10:32 AM
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
-- Table structure for table `ohlc_price`
--

CREATE TABLE `ohlc_price` (
  `UNIX` datetime NOT NULL,
  `SYMBOL` varchar(255) NOT NULL,
  `OPEN` decimal(65,9) NOT NULL,
  `CLOSE` decimal(65,9) NOT NULL,
  `HIGH` decimal(65,9) NOT NULL,
  `LOW` decimal(65,9) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Historical OHLC Price Data';

--
-- Dumping data for table `ohlc_price`
--

INSERT INTO `ohlc_price` (`UNIX`, `SYMBOL`, `OPEN`, `CLOSE`, `HIGH`, `LOW`) VALUES
('2022-02-16 00:21:40', 'BTCUSDT', 42123.290000000, 42146.060000000, 42148.320000000, 42120.820000000),
('2023-02-15 18:26:00', 'BTCUSDT', 42113.080000000, 42123.300000000, 42126.320000000, 42113.070000000);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ohlc_price`
--
ALTER TABLE `ohlc_price`
  ADD PRIMARY KEY (`UNIX`,`SYMBOL`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
