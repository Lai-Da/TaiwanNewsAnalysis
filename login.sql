-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2022-12-13 09:36:16
-- 伺服器版本： 10.4.25-MariaDB
-- PHP 版本： 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `login`
--

-- --------------------------------------------------------

--
-- 資料表結構 `users`
--

CREATE TABLE `users` (
  `id` int(100) NOT NULL,
  `Username` varchar(200) NOT NULL,
  `Email` varchar(200) NOT NULL,
  `Password` varchar(200) NOT NULL,
  `created_time` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_time` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `users`
--

INSERT INTO `users` (`id`, `Username`, `Email`, `Password`, `created_time`, `updated_time`) VALUES
(39, 'sa', 'asa', 'as', '2022-12-05 15:49:18', '2022-12-05 15:49:18'),
(40, 'a', 'v', 'v', '2022-12-05 15:54:48', '2022-12-05 15:54:48'),
(41, 'af', 'af', 's', '2022-12-05 15:57:22', '2022-12-05 15:57:22'),
(42, 'asadad', 'adaf', 'adaa', '2022-12-05 16:00:47', '2022-12-05 16:00:47'),
(43, 'asasa', 'asasas', 'asas', '2022-12-05 16:06:15', '2022-12-05 16:06:15'),
(45, 'aasas', 'asaas', 'asasd', '2022-12-05 16:07:08', '2022-12-05 16:07:08'),
(46, 'ian94305', '', 'a5BX8avVENPaz4Z', '2022-12-13 14:45:20', '2022-12-13 14:45:20'),
(47, '121212', '13131', '31313131', '2022-12-13 14:56:13', '2022-12-13 14:56:13');

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Email` (`Email`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `users`
--
ALTER TABLE `users`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
