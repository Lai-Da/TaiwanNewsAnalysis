-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2022-12-16 09:23:39
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
-- 資料庫： `1216data`
--

-- --------------------------------------------------------

--
-- 資料表結構 `bert_3_prec_training_samples`
--

CREATE TABLE `bert_3_prec_training_samples` (
  `title` text DEFAULT NULL,
  `category` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `bert_3_prec_training_samples`
--

INSERT INTO `bert_3_prec_training_samples` (`title`, `category`) VALUES
('〈張忠謀開講〉談英特爾現任CEO 「對台積電很不客氣」 - cnyes.com', 'Unchanged'),
('台積電子公司JASM：建廠進度順利 明春迎百名應屆畢業生 - cnyes.com', 'Unchanged'),
('台積電扮矽盾張忠謀：保護台灣免於被中國攻擊| Anue鉅亨- 台股新聞 - cnyes.com', 'Down'),
('台積電攻略重要關鍵價| Anue鉅亨- 台股 - cnyes.com', 'Unchanged'),
('台積電1奈米廠傳落腳桃園 經部：最先進製程會在台灣投資 - cnyes.com', 'Up'),
('盤中速報- 台積電(2330)股價大漲至442.0元，漲幅達8.47% | Anue鉅亨- 台股盤中 - cnyes.com', 'Unchanged'),
('台積電攻略重要關鍵價| Anue鉅亨- 台股 - 鉅亨', 'Unchanged'),
('為解決台積電子公司員工住居需求 日本熊本釋出公有地 - 鉅亨', 'Down'),
('無畏「積」弱不振 台積電9位副總級主管9月共加碼自家持股逾70張 - 鉅亨', 'Down'),
('外資回補台積電、金融股大砍聯電3.1萬餘張| Anue鉅亨- 台股新聞 - 鉅亨', 'Unchanged'),
('台積電1奈米廠傳落腳桃園 經部：最先進製程會在台灣投資 - 鉅亨', 'Up'),
('盤中速報- 台積電(2330)股價大漲至442.0元，漲幅達8.47% | Anue鉅亨- 台股盤中 - 鉅亨', 'Unchanged'),
('〈台版晶片法案〉行政院會明討論 台積電：樂觀其成 - 鉅亨', 'Unchanged'),
('台積電供應鏈旺到年底| Anue鉅亨- 專家觀點 - 鉅亨', 'Unchanged'),
('【台股龍捲風】選前內資股獲利回吐！2330台積電、1605華新續漲| Anue鉅亨- 台股新聞 - 鉅亨', 'Unchanged'),
('台積電的魅力巴菲特也擋不住，投資人怎麼找對時機加碼？ - 鉅亨', 'Unchanged'),
('台積電有股神罩，留意低基期『台積大聯盟』 - 鉅亨', 'Unchanged'),
('盤後速報- 台積電(2330)下週(12月15日)除息2.75元，預估參考價468.75元| Anue鉅亨- 台股盤後 - 鉅亨', 'Up'),
('美股盤前：台積電營收創高!微軟收購動視暴雪最快今日將遭美國FTC起訴! | Anue鉅亨- 美股 - 鉅亨', 'Unchanged'),
('〈孫又文開講〉有閒錢就會進場加碼 台積電股價上600元是「遲來的正義」 - Anue鉅亨', 'Unchanged'),
('台積電南科再生水廠3月完成主建 首開先例將工業再生水導入製程 - Anue鉅亨', 'Up');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
