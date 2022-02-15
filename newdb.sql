-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 15, 2022 at 12:01 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.0.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `newdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(50) NOT NULL,
  `Name` varchar(50) CHARACTER SET latin1 NOT NULL,
  `Phone_No` varchar(10) CHARACTER SET latin1 NOT NULL,
  `Message` text CHARACTER SET latin1 NOT NULL,
  `Email` varchar(50) CHARACTER SET latin1 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `Name`, `Phone_No`, `Message`, `Email`) VALUES
(1, 'first post', '2147483647', 'Hello this is my first post of newly created database', 'firstpost@gmail.com'),
(0, 'hi', '', '', ''),
(0, 'TOOLS', '', '', ''),
(0, 'TOOLS', '', '', ''),
(0, 'TOOLS', '', '', ''),
(0, 'yes ', '', '', ''),
(0, 'yes ', '', '', ''),
(0, 'yes ', '', '', ''),
(0, 'it is me', '', '', ''),
(0, 'hhiihi', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(25) NOT NULL,
  `title` varchar(50) NOT NULL,
  `tagline` varchar(50) NOT NULL,
  `slug` varchar(29) NOT NULL,
  `Content` varchar(250) NOT NULL,
  `date` datetime NOT NULL,
  `img_file` varchar(77) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `tagline`, `slug`, `Content`, `date`, `img_file`) VALUES
(1, 'First Post', 'Early Flask', 'first-post', 'Flask-Blogging is a Flask extension for adding Markdown based blog support to your site. It provides a flexible mechanism to store the data in the database of your choice. It is meant to work with the authentication provided by packages such as Flask', '2022-01-31 10:24:17', 'cool-view.jpg'),
(2, 'This is my 2nd post', 'More about flask and how it works', 'second-post', 'For fun, I thought I\'d write a post describing how to build a blog using Flask, a Python web-framework. Building a blog seems like, along with writing a Twitter-clone, a quintessential experience when learning a new web framework.', '2022-02-08 12:22:04', 'post-bg.jpg'),
(3, 'This is my 3rd post', 'What Flask is actually', 'third-post', 'What is flask used for?\r\nFlask is used for developing web applications using python, implemented on Werkzeug and Jinja2. Advantages of using Flask framework are: There is a built-in development server and a fast debugger provided.', '2022-02-09 11:26:18', 'photo.jpg'),
(4, 'This is my last post', 'Conclusion', 'fourth-post', 'As of now we can concluded that you use flask with the help of python to built a static website and make it functional. Hope to add more post in future.......', '2022-02-09 11:28:51', 'beautiful.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
