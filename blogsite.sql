-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 19, 2024 at 07:31 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `blogsite`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `Sr_No` int(50) NOT NULL,
  `Name` text NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Phone` varchar(50) NOT NULL,
  `msg` text NOT NULL,
  `Date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`Sr_No`, `Name`, `Email`, `Phone`, `msg`, `Date`) VALUES
(1, 'first post', 'firstpost@gmail.com', '1234566789', 'first post', '2024-09-24 19:17:02'),
(2, 'My name', 'myemail@gmail.com', '789456123', 'Hello Database!', NULL),
(3, 'javeed', 'myemail@gmail.com', '03010243916', 'I am javeed Iqbal.', NULL),
(4, 'javeed', 'myemail@gmail.com', '03010243916', 'I am javeed Iqbal.', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `Sr_No` int(11) NOT NULL,
  `Title` text NOT NULL,
  `tagline` text NOT NULL,
  `slug` varchar(25) NOT NULL,
  `Content` text NOT NULL,
  `img_file` varchar(12) NOT NULL,
  `Date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`Sr_No`, `Title`, `tagline`, `slug`, `Content`, `img_file`, `Date`) VALUES
(1, 'Lets learn about stock market', 'This blog about stock market', 'first-post', 'Stocks (also capital stock, or sometimes interchangeably, shares) consist of all the shares[a] by which ownership of a corporation or company is divided.[1] A single share of the stock means fractional ownership of the corporation in proportion to the total number of shares. This typically entitles the shareholder (stockholder) to that fraction of the company\'s earnings, proceeds from liquidation of assets (after discharge of all senior claims such as secured and unsecured debt),[3] or voting power, often dividing these up in proportion to the number of like shares each stockholder owns. Not all stock is necessarily equal, as certain classes of stock may be issued, for example, without voting rights, with enhanced voting rights, or with a certain priority to receive profits or liquidation proceeds before or after other classes of shareholders.\r\n\r\nStock can be bought and sold privately or on stock exchanges. Transactions of the former are closely overseen by governments and regulatory bodies to prevent fraud, protect investors, and benefit the larger economy. As new shares are issued by a company, the ownership and rights of existing shareholders are diluted in return for cash to sustain or grow the business. Companies can also buy back stock, which often lets investors recoup the initial investment plus capital gains from subsequent rises in stock price. Stock options issued by many companies as part of employee compensation do not represent ownership, but represent the right to buy ownership at a future time at a specified price. This would represent a windfall to the employees if the option were exercised when the market price is higher than the promised price, since if they immediately sold the stock they would keep the difference (minus taxes).\r\n\r\nStock bought and sold in private markets fall within the private equity realm of finance.', 'about-bg.jpg', '2024-10-18 19:25:00'),
(2, 'Share price', 'This is second post', 'second-post', 'A share price is the price of a single share of a number of saleable equity shares of a company. In layman\'s terms, the stock price is the highest amount someone is willing to pay for the stock, or the lowest amount that it can be bought for.\r\n\r\nIn economics and financial theory, analysts use random walk techniques to model behavior of asset prices, in particular share prices of companies publicly listed. This practice has its basis in the presumption that investors act rationally and without biases, and that at any moment they estimate the value of an asset based on future expectations. Under these conditions, all existing information affects the price, which changes only when new information comes out. By definition, new information appears randomly and influences the asset price randomly.\r\n\r\nEmpirical studies have demonstrated that prices do not completely follow random walks.[1] Low serial correlations (around 0.05) exist in the short term, and slightly stronger correlations over the longer term. Their sign and the strength depend on a variety of factors.', 'about-bg.jpg', '2024-10-16 14:53:13'),
(3, 'Behaviour of share prices', 'This is third post', 'Behaviour-of-share-prices', 'In economics and financial theory, analysts use random walk techniques to model behavior of asset prices, in particular share prices of companies publicly listed. This practice has its basis in the presumption that investors act rationally and without biases, and that at any moment they estimate the value of an asset based on future expectations. Under these conditions, all existing information affects the price, which changes only when new information comes out. By definition, new information appears randomly and influences the asset price randomly.\r\n\r\nEmpirical studies have demonstrated that prices do not completely follow random walks.[1] Low serial correlations (around 0.05) exist in the short term, and slightly stronger correlations over the longer term. Their sign and the strength depend on a variety of factors.\r\n\r\nResearchers have found that some of the biggest price deviations from random walks result from seasonal and temporal patterns. In particular, returns in January significantly exceed those in other months (January effect) and on Mondays stock prices go down more than on any other day. Observers have noted these effects in many different markets for more than half a century, but without succeeding in giving a completely satisfactory explanation for their persistence.', 'home-bg.jpg', '2024-10-16 15:14:44'),
(4, 'Share prices in the United States', 'This is forth post', 'Share-prices-in-the-Unite', 'Many U.S.-based companies seek to keep their share price (also called stock price) low, partly based on \"round lot\" trading (multiples of 100 shares). A corporation can adjust its stock price by a stock split, substituting a quantity of shares at one price for a different number of shares at an adjusted price where the value of shares x price remains equivalent. (For example, 500 shares at $32 may become 1000 shares at $16.) Many major firms like to keep their price in the $25 to $75 price range.\r\n\r\nA US share must be priced at $1 or more to be covered by NASDAQ. If the share price falls below that level, the stock is \"delisted\" and becomes an OTC (over the counter stock). A stock must have a price of $1 or more for 10 consecutive trading days during each month to remain listed.', '', '2024-10-16 15:15:59'),
(5, 'Most expensive shares', 'This is fifth post', 'Most-expensive-shares', 'The highest share prices on the NYSE have been those of Berkshire Hathaway class A, trading at over $625,000/share (in February 2024). Berkshire Hathaway has refused to split its stock and make it more affordable to retail investors, as they want to attract shareholders with a long-term vision. In 1996, Berkshire Hathaway issued the class B shares that come with 1/1000 of the value and 1/1500 of the voting rights in order to avoid the formation of mutual funds that buy class A shares.\r\n\r\nLindt & Sprüngli shares topped out at approximately $140,000 (December 2021). Like Berkshire Hathaway, the Swiss chocolate manufacturer issued so-called Partizipationsschein shares, valued at 1/100 of the original share value, and come void of voting rights.', 'home-bg.jpg', '2024-10-16 15:17:04'),
(6, 'Stock exchange', 'New Post', 'Stock-exchange', 'A stock exchange is an exchange (or bourse) where stockbrokers and traders can buy and sell shares (equity stock), bonds, and other securities. Many large companies have their stocks listed on a stock exchange. This makes the stock more liquid and thus more attractive to many investors. The exchange may also act as a guarantor of settlement. These and other stocks may also be traded \"over the counter\" (OTC), that is, through a dealer. Some large companies will have their stock listed on more than one exchange in different countries, so as to attract international investors.[4]\r\n\r\nStock exchanges may also cover other types of securities, such as fixed-interest securities (bonds) or (less frequently) derivatives, which are more likely to be traded OTC.\r\n\r\nTrade in stock markets means the transfer (in exchange for money) of a stock or security from a seller to a buyer. This requires these two parties to agree on a price. Equities (stocks or shares) confer an ownership interest in a particular company.\r\n\r\nParticipants in the stock market range from small individual stock investors to larger investors, who can be based anywhere in the world, and may include banks, insurance companies, pension funds and hedge funds. Their buy or sell orders may be executed on their behalf by a stock exchange trader.\r\n\r\nSome exchanges are physical locations where transactions are carried out on a trading floor, by a method known as open outcry. This method is used in some stock exchanges and commodities exchanges, and involves traders shouting bid and offer prices. The other type of stock exchange has a network of computers where trades are made electronically. An example of such an exchange is the NASDAQ.', 'about-bg.jpg', '2024-10-17 21:52:02');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`Sr_No`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`Sr_No`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `Sr_No` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `Sr_No` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
