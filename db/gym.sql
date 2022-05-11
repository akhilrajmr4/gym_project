-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 05, 2022 at 12:21 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gym`
--

-- --------------------------------------------------------

--
-- Table structure for table `app_achievement`
--

CREATE TABLE `app_achievement` (
  `id` bigint(20) NOT NULL,
  `Achievement_title` varchar(100) DEFAULT NULL,
  `Achievement_description` longtext DEFAULT NULL,
  `Achievement_image` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_achievement`
--

INSERT INTO `app_achievement` (`id`, `Achievement_title`, `Achievement_description`, `Achievement_image`) VALUES
(1, 'Achievement1', 'Work is OK. It has its waves of enthusiasm, lots of interesting things and even some small achievements. But ultimately just a cog in a wheel, the wheel being the need to eat and pay off the debts. What I do doesn’t really make any difference. I have a young daughter, she’s a delight of course. She achieves every day but that’s not down to me it is down to her. I just play a minor supporting role as best I can.Work is OK.', 'images/4eb4894cc05dd9ca0398124be1f9f92c.gif');

-- --------------------------------------------------------

--
-- Table structure for table `app_batch`
--

CREATE TABLE `app_batch` (
  `id` bigint(20) NOT NULL,
  `batch` varchar(100) NOT NULL,
  `fromtime` time(6) DEFAULT NULL,
  `totime` time(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_batch`
--

INSERT INTO `app_batch` (`id`, `batch`, `fromtime`, `totime`) VALUES
(2, 'Morning', '07:17:00.000000', '10:17:00.000000');

-- --------------------------------------------------------

--
-- Table structure for table `app_category`
--

CREATE TABLE `app_category` (
  `id` bigint(20) NOT NULL,
  `cate_name` varchar(200) NOT NULL,
  `cate_details` varchar(200) NOT NULL,
  `cate_image` varchar(100) DEFAULT NULL,
  `cate_description` longtext NOT NULL,
  `cate_type_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_category`
--

INSERT INTO `app_category` (`id`, `cate_name`, `cate_details`, `cate_image`, `cate_description`, `cate_type_id`) VALUES
(1, 'Round dumbbell', '10kg', 'images/Dumbbell1.jpg', 'dumbbell used for biceps', 1);

-- --------------------------------------------------------

--
-- Table structure for table `app_designation`
--

CREATE TABLE `app_designation` (
  `id` bigint(20) NOT NULL,
  `designation` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_designation`
--

INSERT INTO `app_designation` (`id`, `designation`, `status`) VALUES
(1, 'Trainer', ''),
(2, 'Trainee', '');

-- --------------------------------------------------------

--
-- Table structure for table `app_expense`
--

CREATE TABLE `app_expense` (
  `id` bigint(20) NOT NULL,
  `payee` varchar(100) NOT NULL,
  `payacnt` varchar(100) NOT NULL,
  `paymethod` varchar(100) NOT NULL,
  `paydate` varchar(100) NOT NULL,
  `refno` varchar(100) NOT NULL,
  `amount` varchar(100) NOT NULL,
  `tax` varchar(100) NOT NULL,
  `total` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_expense`
--

INSERT INTO `app_expense` (`id`, `payee`, `payacnt`, `paymethod`, `paydate`, `refno`, `amount`, `tax`, `total`, `category`, `description`) VALUES
(1, '15000', '', 'online', '2022-04-06', '', '1000', '23', '1023', 'ghjb', 'nb');

-- --------------------------------------------------------

--
-- Table structure for table `app_machine`
--

CREATE TABLE `app_machine` (
  `id` bigint(20) NOT NULL,
  `machine_name` varchar(50) NOT NULL,
  `machine_details` varchar(200) NOT NULL,
  `machine_image` varchar(100) DEFAULT NULL,
  `machine_description` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_machine`
--

INSERT INTO `app_machine` (`id`, `machine_name`, `machine_details`, `machine_image`, `machine_description`) VALUES
(1, 'Dumbell', 'It is used of Biceps', 'images/dumbell.jpg', 'It is used of Biceps');

-- --------------------------------------------------------

--
-- Table structure for table `app_payment`
--

CREATE TABLE `app_payment` (
  `id` bigint(20) NOT NULL,
  `date` date DEFAULT NULL,
  `payment` varchar(240) DEFAULT NULL,
  `bank` varchar(240) DEFAULT NULL,
  `accountnumber` varchar(240) DEFAULT NULL,
  `ifse` varchar(240) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_payment`
--

INSERT INTO `app_payment` (`id`, `date`, `payment`, `bank`, `accountnumber`, `ifse`, `user_id`) VALUES
(1, '2022-04-21', '1000', 'SBI', '89547859652145', 'SBI1245', 2),
(2, '2022-04-21', '3000', 'SBI', '89547859652145', 'SBI1245', 3),
(4, '2022-04-21', '4000', 'SBI', '89547859652145', 'SBI1245', 6),
(5, '2022-04-21', '3000', 'SBI', '89547859652145', 'SBI1245', 4),
(6, '2022-04-21', '3000', 'SBI', '89547859652145', 'SBI1245', 1);

-- --------------------------------------------------------

--
-- Table structure for table `app_tutorial`
--

CREATE TABLE `app_tutorial` (
  `id` bigint(20) NOT NULL,
  `video` varchar(100) DEFAULT NULL,
  `Workout_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_tutorial`
--

INSERT INTO `app_tutorial` (`id`, `video`, `Workout_id`) VALUES
(1, 'images/Chest_workout1.mp4', 1),
(2, 'images/Chest_workout1.mp4', 1);

-- --------------------------------------------------------

--
-- Table structure for table `app_user_registration`
--

CREATE TABLE `app_user_registration` (
  `id` bigint(20) NOT NULL,
  `fullname` varchar(240) DEFAULT NULL,
  `fathername` varchar(240) DEFAULT NULL,
  `mothername` varchar(240) DEFAULT NULL,
  `dateofbirth` date DEFAULT NULL,
  `gender` varchar(240) DEFAULT NULL,
  `pincode` varchar(240) DEFAULT NULL,
  `district` varchar(240) DEFAULT NULL,
  `state` varchar(240) DEFAULT NULL,
  `country` varchar(240) DEFAULT NULL,
  `permanentaddress1` varchar(240) DEFAULT NULL,
  `permanentaddress2` varchar(240) DEFAULT NULL,
  `permanentaddress3` varchar(240) DEFAULT NULL,
  `mobile` varchar(240) DEFAULT NULL,
  `alternativeno` varchar(240) DEFAULT NULL,
  `email` varchar(240) DEFAULT NULL,
  `password` varchar(240) DEFAULT NULL,
  `idproof` varchar(100) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `joiningdate` date DEFAULT NULL,
  `startdate` date DEFAULT NULL,
  `enddate` date DEFAULT NULL,
  `status` varchar(240) DEFAULT NULL,
  `designation_id` bigint(20) DEFAULT NULL,
  `Trainer_id` int(11) DEFAULT NULL,
  `height` varchar(240) DEFAULT NULL,
  `weight` varchar(240) DEFAULT NULL,
  `rate` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_user_registration`
--

INSERT INTO `app_user_registration` (`id`, `fullname`, `fathername`, `mothername`, `dateofbirth`, `gender`, `pincode`, `district`, `state`, `country`, `permanentaddress1`, `permanentaddress2`, `permanentaddress3`, `mobile`, `alternativeno`, `email`, `password`, `idproof`, `photo`, `joiningdate`, `startdate`, `enddate`, `status`, `designation_id`, `Trainer_id`, `height`, `weight`, `rate`) VALUES
(1, 'Binil', NULL, NULL, '2022-04-06', 'Male', '688875', 'Erm', 'Kerala', 'India', 'Address1', 'Address1', 'Address1', '8579685485', '8965748956', 'binil@gmail.com', '123', 'images/face5_Hg4zDyh.jpg', 'images/face24.jpg', '2022-03-27', '2022-04-18', '2022-08-24', 'active', 1, 0, '160', '60', ''),
(2, 'hari', NULL, NULL, '2021-07-21', 'Male', '685478', 'None', 'Kerala', 'India', 'Address1', 'Address2', 'Address3', '9847596586', '887596584589', 'hari@gmail.com', '123', 'images/face12_1zQJBUh.jpg', 'images/face12_YYRzBLn.jpg', '2022-04-04', '2022-04-06', '2022-06-22', 'active', 2, 1, '150cm', '75 kg', ''),
(3, 'Nihal', NULL, NULL, '2022-04-05', NULL, NULL, NULL, NULL, NULL, 'Address1', 'Address2', 'Address3', '895645896', '8547965825', 'nihal@gmail.com', '123', '', 'images/face9_YYkYeC9.jpg', '2022-03-29', '2022-04-23', '2022-07-22', 'active', 2, 5, '167cm', '80kg', ''),
(4, 'jain', NULL, NULL, '2021-07-05', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '895645896', '8547965825', 'jain@gmail.com', '123', '', 'images/face8_265KQpj.jpg', '2021-10-14', '2022-04-22', '2022-07-28', 'resign', 2, 1, '160cm', '85kg', ''),
(5, 'haneef', NULL, NULL, '2021-08-31', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '8579685485', '8965748956', 'haneef@gmail.com', '123', '', 'images/face7.jpg', '2022-02-15', '2022-04-20', '2022-08-29', 'active', 1, 0, '162 cm', '77 kg', '2000'),
(6, 'Lijin', NULL, NULL, '2020-09-09', 'Male', '689562', 'Kottayam', 'Kerala', 'India', 'Address1', 'Address2', 'Address3', '9865789658', '8458967895', 'lijin@gmail.com', NULL, 'images/face13.jpg', 'images/face7.jpg', '2022-04-01', NULL, '2022-04-04', 'resign', 2, 5, '160 cm', '80kg', '5000'),
(7, 'mahin', NULL, NULL, '2020-09-09', 'Male', '689562', 'Kottayam', 'Kerala', 'India', 'Address1', 'Address2', 'Address3', '9865789658', '8458967895', 'mahin@gmail.com', NULL, 'images/face13_KsGq6mD.jpg', 'images/face7_tP5xTTx.jpg', '2022-04-19', NULL, NULL, 'active', 1, 0, '160 cm', '80kg', ''),
(8, 'sandeep', NULL, NULL, '2021-10-27', 'Male', '602452', 'Erklm', 'Kerala', 'India', 'Address1', 'Address2', 'Address3', '8952145927', '8254796582', 'sandeep@gmail.com', NULL, 'images/face21.jpg', 'images/face21_5h3k1kP.jpg', '2022-04-19', NULL, NULL, '', NULL, 0, '158cm', '65kg', ''),
(9, 'manu', NULL, NULL, '2021-10-27', 'Male', '602452', 'Erklm', 'Kerala', 'India', 'Address1', 'Address2', 'Address3', '8952145927', '8254796582', 'manu@gmail.com', NULL, 'images/face21_dd2ekHp.jpg', 'images/face21_h1E15Lc.jpg', '2022-04-19', NULL, NULL, '', NULL, 0, '158cm', '65kg', ''),
(10, 'vishnu', NULL, NULL, '2021-08-30', 'Male', '622201', 'Ktm', 'kerala', 'india', 'Address1', 'Address2', 'Address3', '965895624', '8957892235', 'vishnu@gmail.com', NULL, 'images/face16.jpg', 'images/face16_GlReZbo.jpg', '2022-04-19', NULL, NULL, '', NULL, 0, '160cm', '58kg', ''),
(11, 'n', NULL, NULL, '2022-03-30', 'Male', '556', 'hj,nm', 'nb', 'b n', 'h', 'n ', 'kj', '65745623', '52543', 'amalcs0006@gmail.com', '17800', 'images/face27.jpg', 'images/face27_rFw2q8N.jpg', '2022-04-20', NULL, NULL, '', NULL, 0, '160', '50', ''),
(12, 'n', NULL, NULL, '2022-03-30', 'Male', '556', 'hj,nm', 'nb', 'b n', 'h', 'n ', 'kj', '65745623', '52543', 'amalcs0006@gmail.com', '51657', 'images/face27_nD8vTGp.jpg', 'images/face27_0oVSVF7.jpg', '2022-04-20', NULL, NULL, '', NULL, 0, '160', '50', ''),
(13, 'n', NULL, NULL, '2022-03-30', 'Male', '556', 'hj,nm', 'nb', 'b n', 'h', 'n ', 'kj', '65745623', '52543', 'amalcs0006@gmail.com', '91061', 'images/face27_29TBOt3.jpg', 'images/face27_oynABLD.jpg', '2022-04-20', NULL, NULL, '', NULL, 0, '160', '50', ''),
(14, 'n', NULL, NULL, '2022-03-30', 'Male', '556', 'hj,nm', 'nb', 'b n', 'h', 'n ', 'kj', '65745623', '52543', 'amalcs0006@gmail.com', '41296', 'images/face27_xNxKYdx.jpg', 'images/face27_68VWeVa.jpg', '2022-04-20', NULL, NULL, '', NULL, 0, '160', '50', ''),
(15, 'n', NULL, NULL, '2022-03-30', 'Male', '556', 'hj,nm', 'nb', 'b n', 'h', 'n ', 'kj', '65745623', '52543', 'amalcs0006@gmail.com', '27905', 'images/face27_1CQeaVD.jpg', 'images/face27_iaHFIw9.jpg', '2022-04-20', NULL, NULL, '', NULL, 0, '160', '50', ''),
(16, 'n', NULL, NULL, '2022-03-30', 'Male', '556', 'hj,nm', 'nb', 'b n', 'h', 'n ', 'kj', '65745623', '52543', 'amalcs0006@gmail.com', '87824', 'images/face27_SQPB9Fg.jpg', 'images/face27_YheTbOB.jpg', '2022-04-20', NULL, NULL, '', NULL, 0, '160', '50', ''),
(17, 'n', NULL, NULL, '2022-03-30', 'Male', '556', 'hj,nm', 'nb', 'b n', 'h', 'n ', 'kj', '65745623', '52543', 'amalcs0006@gmail.com', '94568', 'images/face27_1U0j87o.jpg', 'images/face27_Yxk54mu.jpg', '2022-04-20', NULL, NULL, '', NULL, 0, '160', '50', ''),
(18, 'n', NULL, NULL, '2022-03-29', 'Male', '12', 'gh', 'bn', 'hgn', 'jgh', 'hjm', 'gfh', '432.', '543', 'amalcs0006@gmai.com', '30276', 'images/face10.jpg', 'images/face12_RztWmvD.jpg', '2022-04-20', NULL, NULL, '', NULL, 0, '160', '60', ''),
(19, 's', NULL, NULL, '2022-03-30', 'Male', '645', 'bv', 'fb', 'hgb', 'jh', 'ghj', 'hg', '5321', '321', 'amalcs0006@gmail.com', '99651', 'images/face9.jpg', 'images/face5_gAnNNG9.jpg', '2022-04-20', NULL, NULL, '', NULL, 0, '160', '60', ''),
(20, 's', NULL, NULL, '2022-03-30', 'Male', '645', 'bv', 'fb', 'hgb', 'jh', 'ghj', 'hg', '5321', '321', 'amalcs0006@gmail.com', '10077', 'images/face9_ECQIvLa.jpg', 'images/face5_4eS3Lcr.jpg', '2022-04-20', NULL, NULL, '', NULL, 0, '160', '60', ''),
(21, 'ashiq', NULL, NULL, '2022-03-29', 'Male', '432', 'fh', 'ggf', 'g', 'kgj,b', 'yhgv', 'hgn', '5341', '12', 'amalcs0006@gmail.com', '76794', 'images/face6_SJPkysE.jpg', 'images/face12_uaAoUN3.jpg', '2022-04-20', NULL, NULL, '', NULL, 0, '160', '90', '');

-- --------------------------------------------------------

--
-- Table structure for table `app_workout`
--

CREATE TABLE `app_workout` (
  `id` bigint(20) NOT NULL,
  `workout_name` varchar(100) NOT NULL,
  `description` varchar(225) NOT NULL,
  `image` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_workout`
--

INSERT INTO `app_workout` (`id`, `workout_name`, `description`, `image`) VALUES
(1, 'Chest', 'It is warmup excercise', 'images/chest.webp');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add designation', 7, 'add_designation'),
(26, 'Can change designation', 7, 'change_designation'),
(27, 'Can delete designation', 7, 'delete_designation'),
(28, 'Can view designation', 7, 'view_designation'),
(29, 'Can add user_registration', 8, 'add_user_registration'),
(30, 'Can change user_registration', 8, 'change_user_registration'),
(31, 'Can delete user_registration', 8, 'delete_user_registration'),
(32, 'Can view user_registration', 8, 'view_user_registration'),
(33, 'Can add achievement', 9, 'add_achievement'),
(34, 'Can change achievement', 9, 'change_achievement'),
(35, 'Can delete achievement', 9, 'delete_achievement'),
(36, 'Can view achievement', 9, 'view_achievement'),
(37, 'Can add batch', 10, 'add_batch'),
(38, 'Can change batch', 10, 'change_batch'),
(39, 'Can delete batch', 10, 'delete_batch'),
(40, 'Can view batch', 10, 'view_batch'),
(41, 'Can add expense', 11, 'add_expense'),
(42, 'Can change expense', 11, 'change_expense'),
(43, 'Can delete expense', 11, 'delete_expense'),
(44, 'Can view expense', 11, 'view_expense'),
(45, 'Can add machine', 12, 'add_machine'),
(46, 'Can change machine', 12, 'change_machine'),
(47, 'Can delete machine', 12, 'delete_machine'),
(48, 'Can view machine', 12, 'view_machine'),
(49, 'Can add workout', 13, 'add_workout'),
(50, 'Can change workout', 13, 'change_workout'),
(51, 'Can delete workout', 13, 'delete_workout'),
(52, 'Can view workout', 13, 'view_workout'),
(53, 'Can add tutorial', 14, 'add_tutorial'),
(54, 'Can change tutorial', 14, 'change_tutorial'),
(55, 'Can delete tutorial', 14, 'delete_tutorial'),
(56, 'Can view tutorial', 14, 'view_tutorial'),
(57, 'Can add payment', 15, 'add_payment'),
(58, 'Can change payment', 15, 'change_payment'),
(59, 'Can delete payment', 15, 'delete_payment'),
(60, 'Can view payment', 15, 'view_payment'),
(61, 'Can add category', 16, 'add_category'),
(62, 'Can change category', 16, 'change_category'),
(63, 'Can delete category', 16, 'delete_category'),
(64, 'Can view category', 16, 'view_category');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$320000$I0fODRqK4NWI7NiUoY05dk$/6wRJStYZuTZfDZ6//YG7j0GeXQuBoKI5P1GVyAlTC4=', '2022-04-18 09:58:56.377958', 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2022-04-18 09:58:09.803547');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(9, 'app', 'achievement'),
(10, 'app', 'batch'),
(16, 'app', 'category'),
(7, 'app', 'designation'),
(11, 'app', 'expense'),
(12, 'app', 'machine'),
(15, 'app', 'payment'),
(14, 'app', 'tutorial'),
(8, 'app', 'user_registration'),
(13, 'app', 'workout'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-04-18 09:31:00.057256'),
(2, 'auth', '0001_initial', '2022-04-18 09:31:00.944379'),
(3, 'admin', '0001_initial', '2022-04-18 09:31:01.447351'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-04-18 09:31:01.471826'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-04-18 09:31:01.489779'),
(6, 'app', '0001_initial', '2022-04-18 09:31:01.653619'),
(7, 'contenttypes', '0002_remove_content_type_name', '2022-04-18 09:31:01.763368'),
(8, 'auth', '0002_alter_permission_name_max_length', '2022-04-18 09:31:01.847293'),
(9, 'auth', '0003_alter_user_email_max_length', '2022-04-18 09:31:01.884195'),
(10, 'auth', '0004_alter_user_username_opts', '2022-04-18 09:31:01.903153'),
(11, 'auth', '0005_alter_user_last_login_null', '2022-04-18 09:31:01.982045'),
(12, 'auth', '0006_require_contenttypes_0002', '2022-04-18 09:31:01.988028'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2022-04-18 09:31:02.010969'),
(14, 'auth', '0008_alter_user_username_max_length', '2022-04-18 09:31:02.038891'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2022-04-18 09:31:02.076793'),
(16, 'auth', '0010_alter_group_name_max_length', '2022-04-18 09:31:02.114689'),
(17, 'auth', '0011_update_proxy_permissions', '2022-04-18 09:31:02.138626'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2022-04-18 09:31:02.215888'),
(19, 'sessions', '0001_initial', '2022-04-18 09:31:02.280758'),
(20, 'app', '0002_user_registration_trainer_id_and_more', '2022-04-19 05:03:02.551379'),
(21, 'app', '0003_achievement_batch_expense_machine_workout_and_more', '2022-04-21 05:14:42.376717');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('8eiw5jqmc2b485aqyae879a93qelz5xt', 'eyJUbnJfaWQiOjEsInVzZXJuYW1ldHMxIjoiQmluaWwifQ:1nhnYU:U6yjjNjiMpBuaRH5aJYPsTHuaKNm-Xp-Z03tR8OdbWI', '2022-05-06 07:18:14.755783'),
('95dhwuvtl65a2q121y39jf09fs5ezldq', 'eyJTQWRtX2lkIjoxfQ:1nhmdu:IYxETzksfebmXfcWhb8qNGVMilFM8fZwJaYlrKqb7Rg', '2022-05-06 06:19:46.545346'),
('xtrmlddlu9t0f2z3d30h19eyimv3zz4p', 'eyJUbnJfaWQiOjEsInVzZXJuYW1ldHMxIjoiQmluaWwifQ:1nhkwd:QjQYBgFaU0GmPehvjR5sbTDmlrNdPg3gaf1Dcf8yGyk', '2022-05-06 04:30:59.192022');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `app_achievement`
--
ALTER TABLE `app_achievement`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `app_batch`
--
ALTER TABLE `app_batch`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `app_category`
--
ALTER TABLE `app_category`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app_category_cate_type_id_ea868323_fk_app_machine_id` (`cate_type_id`);

--
-- Indexes for table `app_designation`
--
ALTER TABLE `app_designation`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `app_expense`
--
ALTER TABLE `app_expense`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `app_machine`
--
ALTER TABLE `app_machine`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `app_payment`
--
ALTER TABLE `app_payment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app_payment_user_id_0f781b98_fk_app_user_registration_id` (`user_id`);

--
-- Indexes for table `app_tutorial`
--
ALTER TABLE `app_tutorial`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app_tutorial_Workout_id_37d0557d_fk_app_workout_id` (`Workout_id`);

--
-- Indexes for table `app_user_registration`
--
ALTER TABLE `app_user_registration`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app_user_registratio_designation_id_be0510c1_fk_app_desig` (`designation_id`);

--
-- Indexes for table `app_workout`
--
ALTER TABLE `app_workout`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `app_achievement`
--
ALTER TABLE `app_achievement`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `app_batch`
--
ALTER TABLE `app_batch`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `app_category`
--
ALTER TABLE `app_category`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `app_designation`
--
ALTER TABLE `app_designation`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `app_expense`
--
ALTER TABLE `app_expense`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `app_machine`
--
ALTER TABLE `app_machine`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `app_payment`
--
ALTER TABLE `app_payment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `app_tutorial`
--
ALTER TABLE `app_tutorial`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `app_user_registration`
--
ALTER TABLE `app_user_registration`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `app_workout`
--
ALTER TABLE `app_workout`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `app_category`
--
ALTER TABLE `app_category`
  ADD CONSTRAINT `app_category_cate_type_id_ea868323_fk_app_machine_id` FOREIGN KEY (`cate_type_id`) REFERENCES `app_machine` (`id`);

--
-- Constraints for table `app_payment`
--
ALTER TABLE `app_payment`
  ADD CONSTRAINT `app_payment_user_id_0f781b98_fk_app_user_registration_id` FOREIGN KEY (`user_id`) REFERENCES `app_user_registration` (`id`);

--
-- Constraints for table `app_tutorial`
--
ALTER TABLE `app_tutorial`
  ADD CONSTRAINT `app_tutorial_Workout_id_37d0557d_fk_app_workout_id` FOREIGN KEY (`Workout_id`) REFERENCES `app_workout` (`id`);

--
-- Constraints for table `app_user_registration`
--
ALTER TABLE `app_user_registration`
  ADD CONSTRAINT `app_user_registratio_designation_id_be0510c1_fk_app_desig` FOREIGN KEY (`designation_id`) REFERENCES `app_designation` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
