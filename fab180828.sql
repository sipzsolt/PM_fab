-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Aug 29, 2018 at 01:24 PM
-- Server version: 10.1.19-MariaDB
-- PHP Version: 5.6.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fab`
--

-- --------------------------------------------------------

--
-- Table structure for table `ab_permission`
--

CREATE TABLE `ab_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ab_permission`
--

INSERT INTO `ab_permission` (`id`, `name`) VALUES
(9, 'can_add'),
(15, 'can_chart'),
(3, 'can_delete'),
(6, 'can_download'),
(8, 'can_edit'),
(7, 'can_list'),
(17, 'can_method1'),
(16, 'can_method2'),
(18, 'can_method3'),
(4, 'can_show'),
(2, 'can_this_form_get'),
(1, 'can_this_form_post'),
(5, 'can_userinfo'),
(14, 'Copy Role'),
(13, 'menu_access'),
(20, 'mulbid'),
(19, 'muldelete'),
(10, 'resetmypassword'),
(11, 'resetpasswords'),
(12, 'userinfoedit');

-- --------------------------------------------------------

--
-- Table structure for table `ab_permission_view`
--

CREATE TABLE `ab_permission_view` (
  `id` int(11) NOT NULL,
  `permission_id` int(11) DEFAULT NULL,
  `view_menu_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ab_permission_view`
--

INSERT INTO `ab_permission_view` (`id`, `permission_id`, `view_menu_id`) VALUES
(1, 1, 4),
(2, 2, 4),
(3, 1, 5),
(4, 2, 5),
(5, 1, 6),
(6, 2, 6),
(7, 3, 8),
(8, 4, 8),
(9, 5, 8),
(10, 6, 8),
(11, 7, 8),
(12, 8, 8),
(13, 9, 8),
(14, 10, 8),
(15, 11, 8),
(16, 12, 8),
(17, 13, 9),
(18, 13, 10),
(19, 3, 11),
(20, 4, 11),
(21, 6, 11),
(22, 7, 11),
(23, 8, 11),
(24, 9, 11),
(25, 14, 11),
(26, 13, 12),
(27, 15, 13),
(28, 13, 14),
(29, 7, 15),
(30, 13, 16),
(31, 7, 17),
(32, 13, 18),
(33, 7, 19),
(34, 13, 20),
(35, 13, 22),
(36, 13, 23),
(37, 13, 24),
(40, 18, 21),
(41, 13, 25),
(42, 17, 21),
(43, 16, 21),
(44, 13, 26),
(45, 13, 27),
(46, 9, 28),
(47, 7, 28),
(48, 8, 28),
(49, 3, 28),
(50, 4, 28),
(51, 6, 28),
(52, 13, 29),
(53, 13, 30),
(54, 6, 31),
(55, 8, 31),
(56, 3, 31),
(57, 9, 31),
(58, 7, 31),
(59, 4, 31),
(60, 9, 32),
(61, 8, 32),
(62, 7, 32),
(63, 3, 32),
(64, 6, 32),
(65, 4, 32),
(66, 13, 33),
(67, 9, 34),
(68, 6, 34),
(69, 8, 34),
(70, 7, 34),
(71, 3, 34),
(72, 4, 34),
(73, 13, 35),
(74, 4, 36),
(75, 3, 36),
(76, 6, 36),
(77, 9, 36),
(78, 8, 36),
(79, 7, 36),
(80, 13, 37),
(81, 3, 38),
(82, 9, 38),
(83, 8, 38),
(84, 6, 38),
(85, 4, 38),
(86, 7, 38),
(87, 13, 39),
(88, 6, 40),
(89, 7, 40),
(90, 9, 40),
(91, 8, 40),
(92, 4, 40),
(93, 3, 40),
(94, 13, 41),
(95, 1, 42),
(96, 2, 42),
(97, 13, 43),
(98, 13, 44),
(99, 1, 45),
(100, 2, 45),
(101, 13, 46),
(102, 2, 47),
(103, 1, 47),
(104, 13, 48),
(105, 2, 49),
(106, 1, 49),
(107, 13, 50),
(110, 13, 52),
(111, 13, 53),
(112, 13, 54),
(113, 1, 55),
(114, 2, 55),
(115, 13, 56),
(116, 8, 57),
(117, 3, 57),
(118, 4, 57),
(119, 6, 57),
(120, 9, 57),
(121, 7, 57),
(122, 13, 58),
(123, 1, 51),
(124, 2, 51),
(125, 13, 59),
(126, 13, 60),
(127, 13, 61),
(128, 13, 62),
(129, 13, 63),
(130, 13, 64),
(131, 13, 65),
(133, 20, 36);

-- --------------------------------------------------------

--
-- Table structure for table `ab_permission_view_role`
--

CREATE TABLE `ab_permission_view_role` (
  `id` int(11) NOT NULL,
  `permission_view_id` int(11) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ab_permission_view_role`
--

INSERT INTO `ab_permission_view_role` (`id`, `permission_view_id`, `role_id`) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 1),
(4, 4, 1),
(5, 5, 1),
(6, 6, 1),
(7, 7, 1),
(8, 8, 1),
(9, 9, 1),
(10, 10, 1),
(11, 11, 1),
(12, 12, 1),
(13, 13, 1),
(14, 14, 1),
(15, 15, 1),
(16, 16, 1),
(17, 17, 1),
(18, 18, 1),
(19, 19, 1),
(20, 20, 1),
(21, 21, 1),
(22, 22, 1),
(23, 23, 1),
(24, 24, 1),
(25, 25, 1),
(26, 26, 1),
(27, 27, 1),
(28, 28, 1),
(29, 29, 1),
(30, 30, 1),
(31, 31, 1),
(32, 32, 1),
(33, 33, 1),
(34, 34, 1),
(35, 35, 1),
(36, 36, 1),
(37, 37, 1),
(40, 40, 1),
(41, 41, 1),
(42, 42, 1),
(43, 43, 1),
(44, 44, 1),
(45, 45, 1),
(46, 46, 1),
(47, 47, 1),
(48, 48, 1),
(49, 49, 1),
(50, 50, 1),
(51, 51, 1),
(52, 52, 1),
(53, 53, 1),
(54, 54, 1),
(55, 55, 1),
(56, 56, 1),
(57, 57, 1),
(58, 58, 1),
(59, 59, 1),
(60, 60, 1),
(61, 61, 1),
(62, 62, 1),
(63, 63, 1),
(64, 64, 1),
(65, 65, 1),
(66, 66, 1),
(67, 67, 1),
(68, 68, 1),
(69, 69, 1),
(70, 70, 1),
(71, 71, 1),
(72, 72, 1),
(73, 73, 1),
(74, 74, 1),
(75, 75, 1),
(76, 76, 1),
(77, 77, 1),
(78, 78, 1),
(79, 79, 1),
(80, 80, 1),
(81, 81, 1),
(82, 82, 1),
(83, 83, 1),
(84, 84, 1),
(85, 85, 1),
(86, 86, 1),
(87, 87, 1),
(88, 88, 1),
(89, 89, 1),
(90, 90, 1),
(91, 91, 1),
(92, 92, 1),
(93, 93, 1),
(94, 94, 1),
(95, 95, 1),
(96, 96, 1),
(97, 97, 1),
(98, 98, 1),
(99, 99, 1),
(100, 100, 1),
(101, 101, 1),
(102, 102, 1),
(103, 103, 1),
(104, 104, 1),
(105, 105, 1),
(106, 106, 1),
(107, 107, 1),
(110, 110, 1),
(111, 111, 1),
(112, 112, 1),
(113, 113, 1),
(114, 114, 1),
(115, 115, 1),
(116, 116, 1),
(117, 117, 1),
(118, 118, 1),
(119, 119, 1),
(120, 120, 1),
(121, 121, 1),
(122, 122, 1),
(123, 123, 1),
(124, 124, 1),
(125, 125, 1),
(126, 126, 1),
(127, 127, 1),
(128, 128, 1),
(129, 129, 1),
(130, 130, 1),
(131, 131, 1),
(133, 133, 1);

-- --------------------------------------------------------

--
-- Table structure for table `ab_register_user`
--

CREATE TABLE `ab_register_user` (
  `id` int(11) NOT NULL,
  `first_name` varchar(64) NOT NULL,
  `last_name` varchar(64) NOT NULL,
  `username` varchar(64) NOT NULL,
  `password` varchar(256) DEFAULT NULL,
  `email` varchar(64) NOT NULL,
  `registration_date` datetime DEFAULT NULL,
  `registration_hash` varchar(256) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ab_role`
--

CREATE TABLE `ab_role` (
  `id` int(11) NOT NULL,
  `name` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ab_role`
--

INSERT INTO `ab_role` (`id`, `name`) VALUES
(1, 'Admin'),
(2, 'Public');

-- --------------------------------------------------------

--
-- Table structure for table `ab_user`
--

CREATE TABLE `ab_user` (
  `id` int(11) NOT NULL,
  `first_name` varchar(64) NOT NULL,
  `last_name` varchar(64) NOT NULL,
  `username` varchar(64) NOT NULL,
  `password` varchar(256) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `email` varchar(64) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `login_count` int(11) DEFAULT NULL,
  `fail_login_count` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `changed_on` datetime DEFAULT NULL,
  `created_by_fk` int(11) DEFAULT NULL,
  `changed_by_fk` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ab_user`
--

INSERT INTO `ab_user` (`id`, `first_name`, `last_name`, `username`, `password`, `active`, `email`, `last_login`, `login_count`, `fail_login_count`, `created_on`, `changed_on`, `created_by_fk`, `changed_by_fk`) VALUES
(1, 'admin', 'admin', 'admin', 'pbkdf2:sha256:50000$8R8si42V$5e6bbf90672de69b1bfc3a24c6025c3559bd8b524b8467f43bcc5f278306bb23', 1, 'admin', '2018-07-23 15:52:30', 11, 0, '2018-03-02 09:48:16', '2018-03-02 09:48:16', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `ab_user_role`
--

CREATE TABLE `ab_user_role` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ab_user_role`
--

INSERT INTO `ab_user_role` (`id`, `user_id`, `role_id`) VALUES
(1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `ab_view_menu`
--

CREATE TABLE `ab_view_menu` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ab_view_menu`
--

INSERT INTO `ab_view_menu` (`id`, `name`) VALUES
(50, 'Add Skills'),
(52, 'Add Skillst'),
(49, 'Add_SkillForm'),
(51, 'Add_SkilltForm'),
(65, 'Administration'),
(7, 'AuthDBView'),
(16, 'Base Permissions'),
(30, 'Contacts'),
(59, 'Customer'),
(53, 'Customer Registration'),
(46, 'Customer Registreation'),
(34, 'CustomerView'),
(28, 'GroupModelView'),
(1, 'IndexView'),
(35, 'List Customer'),
(29, 'List Groups'),
(58, 'List PM_SkilltestView'),
(37, 'List Project'),
(41, 'List ProjectQA'),
(39, 'List Rating'),
(12, 'List Roles'),
(33, 'List Suppliers'),
(9, 'List Users'),
(3, 'LocaleView'),
(22, 'Method1'),
(24, 'Method2'),
(25, 'Method3'),
(43, 'My form View'),
(44, 'My Forms'),
(23, 'My View'),
(42, 'MyFormView'),
(21, 'MyView'),
(56, 'New Project'),
(45, 'New_PM_CustomerForm'),
(55, 'New_PM_ProjectForm'),
(47, 'New_PM_SupplierForm'),
(20, 'Permission on Views/Menus'),
(15, 'PermissionModelView'),
(19, 'PermissionViewModelView'),
(57, 'PM_SkilltestView'),
(62, 'Project'),
(36, 'ProjectView'),
(40, 'Project_QAView'),
(38, 'RatingView'),
(60, 'Registration'),
(5, 'ResetMyPasswordView'),
(4, 'ResetPasswordView'),
(11, 'RoleModelView'),
(10, 'Security'),
(26, 'send_email'),
(27, 'send_email_view'),
(63, 'Skill'),
(64, 'Skillst'),
(61, 'Supplier'),
(54, 'Supplier Registration'),
(48, 'Supplier Registreation'),
(32, 'SupplierView'),
(14, 'User''s Statistics'),
(8, 'UserDBModelView'),
(6, 'UserInfoEditView'),
(13, 'UserStatsChartView'),
(31, 'UserView'),
(2, 'UtilView'),
(17, 'ViewMenuModelView'),
(18, 'Views/Menus');

-- --------------------------------------------------------

--
-- Table structure for table `pm_address`
--

CREATE TABLE `pm_address` (
  `id` int(11) NOT NULL,
  `street_address` varchar(150) DEFAULT NULL,
  `postal_nr` varchar(20) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `country` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pm_address`
--

INSERT INTO `pm_address` (`id`, `street_address`, `postal_nr`, `city`, `country`) VALUES
(1, 'Sexton Strickland Trading', 'Henson Casey LLC', 'Santana Murphy Associates', 'Lester and Benson Plc'),
(2, 'Labore delectus voluptatem neque quod provident vel reprehenderit ut labore adipisicing quia nisi natus ipsa non delectus aut nesciunt', 'Harum porro repudian', 'Fugiat ad voluptatum ut necessitatibus cumque est ', 'Aliquid do illo natus accusamu'),
(3, 'Vel nihil dolor adipisicing labore veritatis quas', 'Cumque ullamco optio', 'Magni nihil rerum est necessitatibus esse dolor ci', 'Repudiandae vitae dicta hic re'),
(4, 'Benjamin and Lang Associates', 'Gilliam and Valencia', 'Prince and Goodman Associates', 'Pratt and Potts Plc'),
(5, 'Ut voluptas modi beatae maiores illum blanditiis in dignissimos eum reiciendis ut dolorem facere eligendi sunt', 'Voluptatum obcaecati', 'Sed ut labore aperiam odit quod ut quia numquam co', 'Et et qui anim quod ea cupidit'),
(6, 'Sit expedita eos necessitatibus non', 'Est non soluta error', 'Laboris illo est aliquip veritatis exercitation la', 'Voluptatem consequatur Tenetur'),
(7, '36111a1e15191d1a54151a105438151a135435771b171d150117', '331d18181d151954151a', '2461d1a171154151a1054331b1b1019151a5435771b171d150', '246150054151a1054241b007542418'),
(8, '2105421b1814015754191b101d54161115015115419151d1b6117541d1818119541618151a101d01d1d7541d1a54101d131a1d771d191b75411119546111d171d111a101d7541054101b18', '221b18140150119541b1', '2711105410541815161b611541541161d1519541b101d05451', '3105411054511d54151a1d1954511b'),
(9, '271d05411c411101d01554111b7541a111711771d01501d1617541a1b1a', '3170541a1b1a5471b181', '3815161b61d7541d18181b5411705415181d511d45421161d0', '221b18140150111954171b1a711511'),
(10, 'Buckner and Stout Co', 'Russo Joyner Inc', 'Washington Tyler Inc', 'Jimenez and Compton Associates'),
(11, 'Earum sunt cupiditate ut facere saepe dolores non repellendus Amet vel ut veniam facilis reprehenderit id veritatis', 'Aut qui ad eos totam', 'Earum commodo perferendis iste ullamco est non dol', 'Asperiores recusandae Ut eum m'),
(12, 'Quo at modi excepturi consectetur iure commodi expedita mollit', 'Velit laborum itaque', 'Consectetur vero sequi consequatur nostrum qui eve', 'Dolorem fugiat labore velit do'),
(13, '371b1b4116542611111054241817', '3915601d1a11e54151a1', '22151131c1a54151a10542741115675420615101d1a13', '2d15011754271166151a1b54241817'),
(14, '3a1d71d5421b1814015011954171b1a711511501654717171d41d054511d541a1b161d754111a1d19', '3d18181b541d01551115', '3a1d1c1d18541510111954101d17015541a118181554611411', '2511d75411054101b181b611541915'),
(15, '2511d754101b181b61d161754118181519171b54511d101119541b12121d171d1d7541510541d105415741161d1b61175461501d1b1a115415101119541115411c1711401116', '2511d7511519541d1054', '3a117171d11a05415181d5115543510541d1a5461146111c11', '21054151054111a1d1954511d10111'),
(16, 'Watson Ingram Co', 'Jackson Mercer Tradi', 'Sykes Sherman Plc', 'Bradford and Hinton Inc'),
(17, 'Laudantium officiis sint cillum est aliqua Ut nisi eos vitae molestias doloremque dolor at qui perferendis sunt est', 'Inventore cillum eiu', 'Rem sit unde mollitia et ad', 'Magnam enim rerum eligendi eos'),
(18, 'Eum beatae aut aut ut culpa nulla eius accusantium obcaecati neque velit non libero nihil fuga', 'Architecto voluptatu', 'Consequatur proident dignissimos quo odio', 'Sed excepteur sed commodi quid'),
(19, '24611d0054151a10543518701b1a54241817', '38151916116054151a10', '3661171154151a1054391710151a1d111854241817', '391565111e54261b161d1a71b1a543'),
(20, 'Peck Pace Trading', 'Dixon and Dunn Inc', 'Bush and Witt Inc', 'Adkins and Trevino Traders'),
(21, 'Quia minim non ut eligendi ullamco ad placeat esse suscipit aliquip nulla amet officiis ipsam qui cum aliquam', 'Qui minus qui dolor ', 'Natus dolore aut illo excepteur', 'Velit enim ipsum qui est molli'),
(22, 'Et obcaecati maxime consectetur irure sapiente earum elit commodo', 'Mollit illo dolor ip', 'Nulla eligendi velit velit dolorem maxime ut minus', 'Et nisi in tempore id deleniti');

-- --------------------------------------------------------

--
-- Table structure for table `pm_attachment`
--

CREATE TABLE `pm_attachment` (
  `id` int(11) NOT NULL,
  `table_id` varchar(200) DEFAULT NULL,
  `table_name` varchar(200) DEFAULT NULL,
  `file` varchar(200) DEFAULT NULL,
  `ufilename` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `pm_banking`
--

CREATE TABLE `pm_banking` (
  `id` int(11) NOT NULL,
  `bank_name` varchar(150) DEFAULT NULL,
  `branch_name` varchar(150) DEFAULT NULL,
  `bank_account_number` varchar(150) DEFAULT NULL,
  `account_currency` varchar(50) DEFAULT NULL,
  `iban` varchar(150) DEFAULT NULL,
  `bic` varchar(150) DEFAULT NULL,
  `routing_bank_details` varchar(150) DEFAULT NULL,
  `annual_value_of_total_sales` varchar(150) DEFAULT NULL,
  `annual_value_of_export_sales` varchar(150) DEFAULT NULL,
  `audit_reports` varchar(300) DEFAULT NULL,
  `bankruptcy_legal_action` varchar(5) DEFAULT NULL,
  `attachment_ids` varchar(500) DEFAULT NULL,
  `branch_address_id` int(11) DEFAULT NULL,
  `branch_contact_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pm_banking`
--

INSERT INTO `pm_banking` (`id`, `bank_name`, `branch_name`, `bank_account_number`, `account_currency`, `iban`, `bic`, `routing_bank_details`, `annual_value_of_total_sales`, `annual_value_of_export_sales`, `audit_reports`, `bankruptcy_legal_action`, `attachment_ids`, `branch_address_id`, `branch_contact_id`) VALUES
(1, 'Haley Dorsey', 'Christopher Anderson', '26', 'Est dolore est quis quod et ea minus aliquip nulla', '246', 'Minus optio eaque voluptates repudiandae maiores alias incidunt a', 'Et perferendis iusto ut ullamco velit aut laborum Consequuntur quae sunt atque sunt ab tempore ut est', '1982', '2001', 'n', 'no', '', 3, 3),
(2, 'Shelley Pennington', 'Elmo Sanford', '262', 'Pariatur Ipsam sit eum facilis ut iure non nihil i', '229', 'Laborum quibusdam voluptas est ex id est dignissimos eos quisquam optio omnis molestias quis unde eaque voluptas facere recusandae Dolorem', 'Soluta cum vel nemo facere consectetur sint commodi id aperiam aut voluptatem est aliquam hic voluptas rem', '2007', '1999', 'n', 'no', '', 6, 6),
(3, '271c11181811d5424111a1a1d1a1301b1a', '3118191b5427151a121b610', '464246', '241561d15016543d4715195471d05411119541215171d181d7', '46464d', '3815161b611954511d16171015195421b181401575411705411c541d1054117054101d131a1d771d191b754111b754511d7511519541b401d1b541b191a1d754191b1811701d15754511d7', '271b18101554171195421118541a11191b541215171161154171b1a711170110165471d1a054171b19191b101d541d10541541161d15195415105421b1814015011195411705415181d511', '46444443', '454d4d4d', 'n', '1a1b', '', 9, 9),
(4, 'Eugenia Nunez', 'Kennan Hensley', '308', 'Eum itaque aliquam ut nisi ut ipsam enim officia n', '444', 'Minus assumenda id voluptatem officia excepteur at ea', 'Sit sint tempor ut sunt iste quam dolorem magni facere dolor ab eum aperiam', '1982', '1980', 'n', 'yes', '', 12, 12),
(5, '31e111f1d11185433111661161b', '27181510115439171d1a0d611', '414540', '221b18140150111954191b1811701d157541a1195115195417', '454545', '391b101d54101b181b611541a1d1c1d185411054101b181b61119541815161b61d7541577119111a101554151054110', '310541115541215171161154511d7541a1d1c1d18541d1a541d4711954611611954511b541d47119', '46444447', '454d4c4d', 'n', '1a1b', '', 15, 15),
(6, 'Quin Snow', 'Brett Berger', '460', 'Illo deserunt perferendis voluptatem tempora aliqu', '943', 'Harum mollit nobis nisi et sunt consequat Porro consequatur dolorem nobis ipsa saepe modi ut facere ex Nam eos', 'At assumenda dolor voluptatem vitae aut aliquip ullam molestiae delectus', '1975', '1996', 'n', 'yes', '', 18, 18),
(7, 'Alfreda Luna', 'Stacy Duffy', '91', 'Inventore quisquam vitae ut numquam modi hic labor', '997', 'Tempor omnis irure fugiat eligendi quod nesciunt in', 'Eius in soluta voluptatum sit quia assumenda excepturi', '1992', '1986', 'n', 'no', '', 22, 22);

-- --------------------------------------------------------

--
-- Table structure for table `pm_company_relations`
--

CREATE TABLE `pm_company_relations` (
  `id` int(11) NOT NULL,
  `company_name` varchar(150) NOT NULL,
  `parent_company` varchar(150) DEFAULT NULL,
  `subsidiaries` varchar(300) DEFAULT NULL,
  `associates` varchar(300) DEFAULT NULL,
  `international_offices` varchar(300) DEFAULT NULL,
  `type_of_business` varchar(150) DEFAULT NULL,
  `nature_of_business` varchar(150) DEFAULT NULL,
  `year_of_establishment` int(11) DEFAULT NULL,
  `employees` int(11) DEFAULT NULL,
  `licence_number` varchar(150) DEFAULT NULL,
  `vat_tax_id` varchar(150) DEFAULT NULL,
  `working_languages` varchar(150) DEFAULT NULL,
  `attachment_ids` varchar(500) DEFAULT NULL,
  `company_address_id` int(11) DEFAULT NULL,
  `company_contact_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pm_company_relations`
--

INSERT INTO `pm_company_relations` (`id`, `company_name`, `parent_company`, `subsidiaries`, `associates`, `international_offices`, `type_of_business`, `nature_of_business`, `year_of_establishment`, `employees`, `licence_number`, `vat_tax_id`, `working_languages`, `attachment_ids`, `company_address_id`, `company_contact_id`) VALUES
(1, 'Lane Hanson Trading', 'Kinney Jackson Associates', 'Proident sit qui doloribus quis dolore veniam reprehenderit exercitation', 'Pariatur Recusandae Eum praesentium dignissimos', 'Eos libero est inventore et exercitation sed minus consequatur provident qui nesciunt et inventore obcaecati', 'limited', 'Voluptatum eius eum est deleniti ut officia esse ut', 2006, 15, '278', 'Ullamco earum numquam repellendus Velit Nam nisi', 'en;ge', '', 1, 1),
(2, 'Burks and Fitzgerald Trading', 'Ruiz and Lowe Co', 'Excepteur ea voluptatibus id ut id ipsam quia aliquid dolore culpa laborum ea facere at vero est', 'Laborum Deleniti modi earum ut accusantium architecto velit cum atque veniam omnis ut rerum expedita nostrud', 'Voluptatum velit dolor laborum Ipsum quos sunt corporis tempore magni similique tempora', 'Iste nostrud necessitatibus neque qui quaerat veniam voluptatem ut debitis eius', 'Consequat Assumenda aliqua Qui quibusdam consectetur odit ad qui ex ducimus consequatur in qui cum possimus voluptatem', 1976, 742, '689', 'Ex pariatur Ad tempor quo aliquam ut ab itaque illo blanditiis dolores ab odio id dolores et', 'en;ge;fr', '', 4, 4),
(3, '36161f754151a1054321d0e131161518105420615101d1a13', '2611de54151a1054381b31154371b', '31c17114011165411155421b181401501d1617541d105410541d10541d47151954511d155415181d511d1054101b181b6115417118415541815161b61195411155412151711611541505421161b541170', '3815161b611954301118111a1d01d54191b101d541115611954105415171717151a01d11954156171c1d0111701b54211181d05417119541505111542111a1d1519541b191a1d754105461161195411c411101d015541a1b706110', '221b1814015011954211181d054101b181b6541815161b6119543d4711954511b754711a054171b641b61d7540111941b611541915131a1d5471d191d181d5111540111941b615', '1b01c116', '1b01c116', 454, 434046, '424c4d', '31c5441561d15016543510540111941b654511b5415181d5115195410541516541d0155111541d18181b541618151a101d01d1d754101b181b6117541516541b101d1b541d1054101b181b', '2;f;5;3;1;1;1;a;5;3;5;8;5;4;5;3;1;3;1;1;5;3;5;8;5;4;5;3;1;2;6;5;3;2;9', '', 7, 7),
(4, 'Cole Bush Traders', 'Gibson and Craig Traders', 'Est aliquam quis architecto vero consequuntur non quisquam a enim dicta dolor ut ad irure sed ipsam voluptatem Dolor', 'Doloremque officiis eos eligendi suscipit vitae nostrud aut itaque quas est aut harum Nam voluptate quia', 'Mollit irure ad dolores et velit sed consectetur ratione omnis explicabo Consectetur voluptas molestiae sit dolores aut', 'limited', 'partner', 2001, 188, '710', 'Aut laborum omnis proident deserunt iusto fugit eum quisquam reprehenderit eos laborum Laborum voluptate sunt et', 'ge', '', 10, 10),
(5, '271815011654151a1054351701d1a54241817', '36156018110054261519711d5420615101167', '3577119111a10155415181d511d10541a1b161d7541011161d01d754611611954171b1a7115115016542418151711150541d1a54711105421b181401501119541115', '221b18140150115417119546114111818111a10175421054191b1811701d1575415181d511d4541b12121d171d15542111854117054101b181b61154511d155421d0151154156171c1d0111701b54111551115421d01511541170541d1a171d101d1011a0', '271511411541011711611a054101b181b6117541d10540111941b65421d015115412151711611', '181d191d01110', '1b01c116', 454, 414, '43404d', '2711511d541a11818155410545115754171b661401d541a1b1a54101d701d1a1701d1b54371b1a711511501654151a1d191d543a15195421b18140150111954511d15', '2;f;5;3;1;c;1;5;3;2;9', '', 13, 13),
(6, 'Moss and Mccormick Co', 'Warner Lewis Trading', 'Enim mollit consequatur repellendus Nobis eu non laboriosam ullamco deserunt officia porro molestias laborum Reprehenderit atque distinctio Magni occaecat qui', 'Itaque magna quidem porro odit aspernatur nostrum consequatur odit assumenda reiciendis autem adipisicing possimus ipsam pariatur Corporis reprehenderit', 'Dolorem exercitation sit ipsum amet inventore neque ipsa laborum qui sit non', 'limited', 'Quia adipisci qui nobis dolor saepe tempora quae dolore libero', 1974, 504, '268', 'Vitae quis eiusmod recusandae Neque ut voluptatem est est harum fuga Sit ipsam blanditiis neque', 'ge;hu', '', 16, 16),
(7, 'Reynolds and Serrano Inc', 'Rivers Hamilton LLC', 'Recusandae Laboris non sint rerum sed dicta soluta', 'Porro rem omnis odio omnis cumque et veniam fugit omnis placeat et rerum iure molestias amet obcaecati vero', 'Rerum veniam eu officia eius quis iste placeat cumque placeat minima maxime veniam impedit voluptatem officia accusamus nihil officia qui', 'limited', 'In tempore nostrum illum laudantium voluptatem proident quia aliquip qui inventore ex et accusantium rerum', 1972, 93, '651', 'Illo quam dolore quia aut rerum facilis aut molestiae labore repudiandae aspernatur', 'ge;fr', '', 20, 20);

-- --------------------------------------------------------

--
-- Table structure for table `pm_contact`
--

CREATE TABLE `pm_contact` (
  `id` int(11) NOT NULL,
  `phone_mobile` varchar(30) DEFAULT NULL,
  `phone_office` varchar(30) DEFAULT NULL,
  `phone_private` varchar(30) DEFAULT NULL,
  `email` varchar(150) NOT NULL,
  `email_secondary` varchar(150) DEFAULT NULL,
  `fax` varchar(50) DEFAULT NULL,
  `website` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pm_contact`
--

INSERT INTO `pm_contact` (`id`, `phone_mobile`, `phone_office`, `phone_private`, `email`, `email_secondary`, `fax`, `website`) VALUES
(1, NULL, '366215541', NULL, 'kuqowydifa@mailinator.net', NULL, 'Rodriguez and Hale Traders', 'Austin and Rosales Trading'),
(2, NULL, '462527155484', NULL, 'civih@mailinator.net', NULL, NULL, NULL),
(3, NULL, '173401386093', NULL, 'n@n.n', NULL, 'Beasley and Finch Plc', NULL),
(4, NULL, '366215541', NULL, 'bycugodoba@mailinator.com', NULL, 'Harrison Wilkinson Trading', 'Lane and Mueller Traders'),
(5, NULL, '382888262807', NULL, 'nyhyb@mailinator.net', NULL, NULL, NULL),
(6, NULL, '724136502938', NULL, 'n@n.n', NULL, 'Pugh and Richardson Inc', NULL),
(7, NULL, '5f47425f42464541414045', NULL, '16d171131b101b16153419151d181d1a1501b65a171b19', NULL, '3c15661d71b1a54231d181f1d1a71b1a5420615101d1a13', '38151a1154151a10543911118181165420615101167'),
(8, NULL, '5f474c46594c4c594c4642464c4443', NULL, '1ad1cd163419151d181d1a1501b65a1a110', NULL, NULL, NULL),
(9, NULL, '5f43464059454759424144464d474c', NULL, 'n@n.n', NULL, '241131c54151a1054261d171c1561071b1a543d1a17', NULL),
(10, NULL, '', NULL, 'qykuzutyso@mailinator.com', NULL, 'Barnes and Huff Plc', 'Mullins Harrington Traders'),
(11, NULL, '895448509479', NULL, 'fizuwykitu@mailinator.com', NULL, NULL, NULL),
(12, NULL, '383109670298', NULL, 'n@n.n', NULL, 'Whitley and Phelps LLC', NULL),
(13, NULL, '5f47425f42464541414045', NULL, '41b181411e1b3419151d181d1a1501b65a171b19', NULL, '2015011543915601d1a11e5420615101d1a13', '361171f54361d61054241817'),
(14, NULL, '5f4645475945405941474647434546', NULL, 'c1512d17d101153419151d181d1a1501b65a171b19', NULL, NULL, NULL),
(15, NULL, '5f464645594542594740404c474741', NULL, 'n@n.n', NULL, '30151a1d1118754151a1054361166d5420615101167', NULL),
(16, NULL, '366215541', NULL, 'niwywofotu@mailinator.net', NULL, 'Buckner Franklin Plc', 'Daniel Sloan LLC'),
(17, NULL, '679202752801', NULL, 'pewir@mailinator.com', NULL, NULL, NULL),
(18, NULL, '864586782028', NULL, 'n@n.n', NULL, 'Guzman Malone Inc', NULL),
(19, NULL, '5f47425f42464541414045', NULL, 'c1101133419151d181d1a1501b65a1a110', NULL, '3917171b1a1a11181854151a10542610181110131154206151', '3361d12121d1a54371b171c6151a543d1a17'),
(20, NULL, '366215541', NULL, 'hukewolaj@mailinator.net', NULL, 'Sexton and Russell Plc', 'Brock Mann Traders'),
(21, NULL, '536533160156', NULL, 'wolawi@mailinator.net', NULL, NULL, NULL),
(22, NULL, '224297386537', NULL, 'n@n.n', NULL, 'Wilson and Leon LLC', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `pm_customer`
--

CREATE TABLE `pm_customer` (
  `id` int(11) NOT NULL,
  `introduction` varchar(1000) DEFAULT NULL,
  `ignored` varchar(1000) DEFAULT NULL,
  `consultant_name` varchar(200) DEFAULT NULL,
  `attachment_ids` varchar(500) DEFAULT NULL,
  `consultant_id` int(11) DEFAULT NULL,
  `mailing_address_id` int(11) DEFAULT NULL,
  `company_relations_id` int(11) DEFAULT NULL,
  `bank_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pm_customer`
--

INSERT INTO `pm_customer` (`id`, `introduction`, `ignored`, `consultant_name`, `attachment_ids`, `consultant_id`, `mailing_address_id`, `company_relations_id`, `bank_id`) VALUES
(1, 'Aliquid nulla dolorum ullam consequat Et mollitia accusantium facere quaerat sit', 'Illum lorem dolores quia eos odio', 'Phillip Hester', '', 2, 2, 1, 1),
(2, 'Corrupti aliquam ducimus nobis dolore labore aperiam culpa aperiam exercitationem cum', 'Neque voluptatem Tempora et ad enim et nobis culpa pariatur Est maiores consequuntur enim molestiae minus sint facere doloremque', 'Rogan Brock', '', 21, 21, 7, 7);

-- --------------------------------------------------------

--
-- Table structure for table `pm_project`
--

CREATE TABLE `pm_project` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL,
  `type` varchar(150) NOT NULL,
  `phases` varchar(1500) NOT NULL,
  `description` varchar(1500) DEFAULT NULL,
  `skill_grade` varchar(500) DEFAULT NULL,
  `budget` varchar(150) NOT NULL,
  `employees_need` int(11) DEFAULT NULL,
  `person_days` int(11) DEFAULT NULL,
  `responsible_person` varchar(150) DEFAULT NULL,
  `backup_person` varchar(150) DEFAULT NULL,
  `project_planned_start` date DEFAULT NULL,
  `project_planned_end` date DEFAULT NULL,
  `attachment_ids` varchar(500) DEFAULT NULL,
  `project_history_ids` varchar(500) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pm_project`
--

INSERT INTO `pm_project` (`id`, `name`, `type`, `phases`, `description`, `skill_grade`, `budget`, `employees_need`, `person_days`, `responsible_person`, `backup_person`, `project_planned_start`, `project_planned_end`, `attachment_ids`, `project_history_ids`, `customer_id`) VALUES
(1, 'Angelica Morris', 'asd', 'qwe', 'dsa', 'coding-medium;sap-low', '500000 VND', 10, 14, 'ewq', 'yxc', '2018-07-30', '2018-07-31', '', '3', 1),
(2, 'Portia Orr', 'Excepturi ut nobis veniam error est velit cillum vitae voluptatem quod facilis voluptatem est est non velit illum fugit est', 'Quis labore duis sint omnis minus veniam nulla', 'Ex id est sequi cupiditate tempora nihil', 'coding-high;sap-high;virtualization-high', '500000 USD', 10, 26, 'Hic magnam ea vitae proident anim anim enim quibusdam non', 'Et ut odit mollitia est inventore veniam natus quia mollitia quis incidunt', '2018-08-03', '2018-08-08', '', '3', 1);

-- --------------------------------------------------------

--
-- Table structure for table `pm_project_qa`
--

CREATE TABLE `pm_project_qa` (
  `id` int(11) NOT NULL,
  `message` varchar(1500) DEFAULT NULL,
  `attachment_ids` varchar(500) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `project_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `pm_rating`
--

CREATE TABLE `pm_rating` (
  `id` int(11) NOT NULL,
  `rate` int(11) DEFAULT NULL,
  `comment` varchar(1500) DEFAULT NULL,
  `sources` varchar(1500) DEFAULT NULL,
  `attachment_ids` varchar(500) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `project_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `pm_skillset`
--

CREATE TABLE `pm_skillset` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pm_skillset`
--

INSERT INTO `pm_skillset` (`id`, `name`) VALUES
(1, 'coding'),
(3, 'sap'),
(4, 'sap2'),
(2, 'virtualization');

-- --------------------------------------------------------

--
-- Table structure for table `pm_supplier`
--

CREATE TABLE `pm_supplier` (
  `id` int(11) NOT NULL,
  `skill_grade` varchar(500) DEFAULT NULL,
  `introduction` varchar(1000) DEFAULT NULL,
  `quality_assurance` varchar(150) DEFAULT NULL,
  `certification` varchar(300) DEFAULT NULL,
  `goods_service` varchar(150) DEFAULT NULL,
  `goods_list` varchar(150) DEFAULT NULL,
  `service_list` varchar(150) DEFAULT NULL,
  `consultant_name` varchar(200) DEFAULT NULL,
  `gdpr` tinyint(1) DEFAULT NULL,
  `attachment_ids` varchar(500) DEFAULT NULL,
  `project_ids` varchar(500) DEFAULT NULL,
  `consultant_id` int(11) DEFAULT NULL,
  `company_relations_id` int(11) DEFAULT NULL,
  `mailing_address_id` int(11) DEFAULT NULL,
  `bank_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pm_supplier`
--

INSERT INTO `pm_supplier` (`id`, `skill_grade`, `introduction`, `quality_assurance`, `certification`, `goods_service`, `goods_list`, `service_list`, `consultant_name`, `gdpr`, `attachment_ids`, `project_ids`, `consultant_id`, `company_relations_id`, `mailing_address_id`, `bank_id`) VALUES
(1, 'coding-low;sap-medium;virtualization-low', 'Qui ipsa aliquip expedita et architecto sint enim ex aperiam et temporibus molestiae facere voluptate in ex eu', 'Autem quae quo necessitatibus tempor dolorum Nam labore aliquid lorem', 'Mollitia ut quis blanditiis voluptatem eum qui rerum non sunt voluptate similique tempore eveniet ea et minim est', 'Nulla ullamco reprehenderit magna esse voluptatem Lorem rerum culpa eu pariatur Animi sed et praesentium consequat Veritatis aut laborum', 'Velit adipisicing saepe velit sit repudiandae labore aut vel et debitis consectetur quia doloremque dolore sunt et excepturi', 'Quaerat maxime ipsum deserunt nihil provident nemo facilis iste dolores aperiam maxime minim dolor quis dolores eligendi repellendus Maiores', 'Lunea Parsons', 0, '', NULL, 5, 2, 5, 2),
(2, 'virtualization-low', 'Saepe eius magna quia fugiat ducimus', 'Cupiditate ut ratione omnis necessitatibus et voluptas error at magna voluptatibus iusto tempora in expedita laborum Incididunt eos dolor consectetur', 'Odit vitae aliquip eius enim nobis sit odio corporis', 'A quaerat voluptatem ut ex sit esse qui aliqua Officia vel nostrud', 'Aut aspernatur consequat Deserunt incididunt quidem voluptatem vero culpa', 'Lorem irure voluptas velit aspernatur', 'Gregory Walker', 0, '', NULL, 11, 4, 11, 4),
(3, 'coding-low;sap-high;virtualization-medium', 'Totam incidunt labore et sed', 'Officiis voluptatibus quasi eligendi nobis voluptate rerum magna', 'Aut proident obcaecati totam velit alias esse aut praesentium corrupti nostrud inventore pariatur', 'Doloremque quidem officiis sint vel ut lorem tempor culpa corporis et consequatur Suscipit architecto est', 'Distinctio Sunt dolor possimus labore et odio vero eaque quidem accusamus rerum qui libero ullam autem voluptatem beatae debitis', 'Voluptas quidem fugit quas eos', 'Lydia Barlow', 0, '', NULL, 17, 6, 17, 6);

-- --------------------------------------------------------

--
-- Table structure for table `pm_user`
--

CREATE TABLE `pm_user` (
  `id` int(11) NOT NULL,
  `office_name` varchar(150) DEFAULT NULL,
  `position` varchar(30) DEFAULT NULL,
  `attachment_ids` varchar(500) DEFAULT NULL,
  `office_address_id` int(11) DEFAULT NULL,
  `office_contact_id` int(11) DEFAULT NULL,
  `mailing_address_id` int(11) DEFAULT NULL,
  `personal_contact_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `projskills`
--

CREATE TABLE `projskills` (
  `pm_skillset_id` int(11) DEFAULT NULL,
  `pm_project_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `projskills`
--

INSERT INTO `projskills` (`pm_skillset_id`, `pm_project_id`) VALUES
(1, 1),
(3, 1),
(1, 2),
(3, 2),
(2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `supplkills`
--

CREATE TABLE `supplkills` (
  `pm_skillset_id` int(11) DEFAULT NULL,
  `pm_supplier` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `supplkills`
--

INSERT INTO `supplkills` (`pm_skillset_id`, `pm_supplier`) VALUES
(1, 1),
(3, 1),
(2, 1),
(2, 2),
(1, 3),
(3, 3),
(2, 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ab_permission`
--
ALTER TABLE `ab_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `ab_permission_view`
--
ALTER TABLE `ab_permission_view`
  ADD PRIMARY KEY (`id`),
  ADD KEY `permission_id` (`permission_id`),
  ADD KEY `view_menu_id` (`view_menu_id`);

--
-- Indexes for table `ab_permission_view_role`
--
ALTER TABLE `ab_permission_view_role`
  ADD PRIMARY KEY (`id`),
  ADD KEY `permission_view_id` (`permission_view_id`),
  ADD KEY `role_id` (`role_id`);

--
-- Indexes for table `ab_register_user`
--
ALTER TABLE `ab_register_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `ab_role`
--
ALTER TABLE `ab_role`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `ab_user`
--
ALTER TABLE `ab_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `created_by_fk` (`created_by_fk`),
  ADD KEY `changed_by_fk` (`changed_by_fk`);

--
-- Indexes for table `ab_user_role`
--
ALTER TABLE `ab_user_role`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `role_id` (`role_id`);

--
-- Indexes for table `ab_view_menu`
--
ALTER TABLE `ab_view_menu`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `pm_address`
--
ALTER TABLE `pm_address`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pm_attachment`
--
ALTER TABLE `pm_attachment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pm_banking`
--
ALTER TABLE `pm_banking`
  ADD PRIMARY KEY (`id`),
  ADD KEY `branch_address_id` (`branch_address_id`),
  ADD KEY `branch_contact_id` (`branch_contact_id`);

--
-- Indexes for table `pm_company_relations`
--
ALTER TABLE `pm_company_relations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `company_address_id` (`company_address_id`),
  ADD KEY `company_contact_id` (`company_contact_id`);

--
-- Indexes for table `pm_contact`
--
ALTER TABLE `pm_contact`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pm_customer`
--
ALTER TABLE `pm_customer`
  ADD PRIMARY KEY (`id`),
  ADD KEY `consultant_id` (`consultant_id`),
  ADD KEY `mailing_address_id` (`mailing_address_id`),
  ADD KEY `company_relations_id` (`company_relations_id`),
  ADD KEY `bank_id` (`bank_id`);

--
-- Indexes for table `pm_project`
--
ALTER TABLE `pm_project`
  ADD PRIMARY KEY (`id`),
  ADD KEY `customer_id` (`customer_id`);

--
-- Indexes for table `pm_project_qa`
--
ALTER TABLE `pm_project_qa`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `project_id` (`project_id`);

--
-- Indexes for table `pm_rating`
--
ALTER TABLE `pm_rating`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `project_id` (`project_id`);

--
-- Indexes for table `pm_skillset`
--
ALTER TABLE `pm_skillset`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `pm_supplier`
--
ALTER TABLE `pm_supplier`
  ADD PRIMARY KEY (`id`),
  ADD KEY `consultant_id` (`consultant_id`),
  ADD KEY `company_relations_id` (`company_relations_id`),
  ADD KEY `mailing_address_id` (`mailing_address_id`),
  ADD KEY `bank_id` (`bank_id`);

--
-- Indexes for table `pm_user`
--
ALTER TABLE `pm_user`
  ADD PRIMARY KEY (`id`),
  ADD KEY `office_address_id` (`office_address_id`),
  ADD KEY `office_contact_id` (`office_contact_id`),
  ADD KEY `mailing_address_id` (`mailing_address_id`),
  ADD KEY `personal_contact_id` (`personal_contact_id`);

--
-- Indexes for table `projskills`
--
ALTER TABLE `projskills`
  ADD KEY `pm_skillset_id` (`pm_skillset_id`),
  ADD KEY `pm_project_id` (`pm_project_id`);

--
-- Indexes for table `supplkills`
--
ALTER TABLE `supplkills`
  ADD KEY `pm_skillset_id` (`pm_skillset_id`),
  ADD KEY `pm_supplier` (`pm_supplier`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `ab_permission`
--
ALTER TABLE `ab_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
--
-- AUTO_INCREMENT for table `ab_permission_view`
--
ALTER TABLE `ab_permission_view`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=134;
--
-- AUTO_INCREMENT for table `ab_permission_view_role`
--
ALTER TABLE `ab_permission_view_role`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=134;
--
-- AUTO_INCREMENT for table `ab_register_user`
--
ALTER TABLE `ab_register_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `ab_role`
--
ALTER TABLE `ab_role`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `ab_user`
--
ALTER TABLE `ab_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `ab_user_role`
--
ALTER TABLE `ab_user_role`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `ab_view_menu`
--
ALTER TABLE `ab_view_menu`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=66;
--
-- AUTO_INCREMENT for table `pm_address`
--
ALTER TABLE `pm_address`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
--
-- AUTO_INCREMENT for table `pm_attachment`
--
ALTER TABLE `pm_attachment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `pm_banking`
--
ALTER TABLE `pm_banking`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `pm_company_relations`
--
ALTER TABLE `pm_company_relations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `pm_contact`
--
ALTER TABLE `pm_contact`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
--
-- AUTO_INCREMENT for table `pm_customer`
--
ALTER TABLE `pm_customer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `pm_project`
--
ALTER TABLE `pm_project`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `pm_project_qa`
--
ALTER TABLE `pm_project_qa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `pm_rating`
--
ALTER TABLE `pm_rating`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `pm_skillset`
--
ALTER TABLE `pm_skillset`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `pm_supplier`
--
ALTER TABLE `pm_supplier`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `pm_user`
--
ALTER TABLE `pm_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `ab_permission_view`
--
ALTER TABLE `ab_permission_view`
  ADD CONSTRAINT `ab_permission_view_ibfk_1` FOREIGN KEY (`permission_id`) REFERENCES `ab_permission` (`id`),
  ADD CONSTRAINT `ab_permission_view_ibfk_2` FOREIGN KEY (`view_menu_id`) REFERENCES `ab_view_menu` (`id`);

--
-- Constraints for table `ab_permission_view_role`
--
ALTER TABLE `ab_permission_view_role`
  ADD CONSTRAINT `ab_permission_view_role_ibfk_1` FOREIGN KEY (`permission_view_id`) REFERENCES `ab_permission_view` (`id`),
  ADD CONSTRAINT `ab_permission_view_role_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `ab_role` (`id`);

--
-- Constraints for table `ab_user`
--
ALTER TABLE `ab_user`
  ADD CONSTRAINT `ab_user_ibfk_1` FOREIGN KEY (`created_by_fk`) REFERENCES `ab_user` (`id`),
  ADD CONSTRAINT `ab_user_ibfk_2` FOREIGN KEY (`changed_by_fk`) REFERENCES `ab_user` (`id`);

--
-- Constraints for table `ab_user_role`
--
ALTER TABLE `ab_user_role`
  ADD CONSTRAINT `ab_user_role_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `ab_user` (`id`),
  ADD CONSTRAINT `ab_user_role_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `ab_role` (`id`);

--
-- Constraints for table `pm_banking`
--
ALTER TABLE `pm_banking`
  ADD CONSTRAINT `pm_banking_ibfk_1` FOREIGN KEY (`branch_address_id`) REFERENCES `pm_address` (`id`),
  ADD CONSTRAINT `pm_banking_ibfk_2` FOREIGN KEY (`branch_contact_id`) REFERENCES `pm_contact` (`id`);

--
-- Constraints for table `pm_company_relations`
--
ALTER TABLE `pm_company_relations`
  ADD CONSTRAINT `pm_company_relations_ibfk_1` FOREIGN KEY (`company_address_id`) REFERENCES `pm_address` (`id`),
  ADD CONSTRAINT `pm_company_relations_ibfk_2` FOREIGN KEY (`company_contact_id`) REFERENCES `pm_contact` (`id`);

--
-- Constraints for table `pm_customer`
--
ALTER TABLE `pm_customer`
  ADD CONSTRAINT `pm_customer_ibfk_1` FOREIGN KEY (`consultant_id`) REFERENCES `pm_contact` (`id`),
  ADD CONSTRAINT `pm_customer_ibfk_2` FOREIGN KEY (`mailing_address_id`) REFERENCES `pm_address` (`id`),
  ADD CONSTRAINT `pm_customer_ibfk_3` FOREIGN KEY (`company_relations_id`) REFERENCES `pm_company_relations` (`id`),
  ADD CONSTRAINT `pm_customer_ibfk_4` FOREIGN KEY (`bank_id`) REFERENCES `pm_banking` (`id`);

--
-- Constraints for table `pm_project`
--
ALTER TABLE `pm_project`
  ADD CONSTRAINT `pm_project_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `pm_customer` (`id`);

--
-- Constraints for table `pm_project_qa`
--
ALTER TABLE `pm_project_qa`
  ADD CONSTRAINT `pm_project_qa_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `pm_user` (`id`),
  ADD CONSTRAINT `pm_project_qa_ibfk_2` FOREIGN KEY (`project_id`) REFERENCES `pm_project` (`id`);

--
-- Constraints for table `pm_rating`
--
ALTER TABLE `pm_rating`
  ADD CONSTRAINT `pm_rating_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `pm_user` (`id`),
  ADD CONSTRAINT `pm_rating_ibfk_2` FOREIGN KEY (`project_id`) REFERENCES `pm_project` (`id`);

--
-- Constraints for table `pm_supplier`
--
ALTER TABLE `pm_supplier`
  ADD CONSTRAINT `pm_supplier_ibfk_1` FOREIGN KEY (`consultant_id`) REFERENCES `pm_contact` (`id`),
  ADD CONSTRAINT `pm_supplier_ibfk_2` FOREIGN KEY (`company_relations_id`) REFERENCES `pm_company_relations` (`id`),
  ADD CONSTRAINT `pm_supplier_ibfk_3` FOREIGN KEY (`mailing_address_id`) REFERENCES `pm_address` (`id`),
  ADD CONSTRAINT `pm_supplier_ibfk_4` FOREIGN KEY (`bank_id`) REFERENCES `pm_banking` (`id`);

--
-- Constraints for table `pm_user`
--
ALTER TABLE `pm_user`
  ADD CONSTRAINT `pm_user_ibfk_1` FOREIGN KEY (`office_address_id`) REFERENCES `pm_address` (`id`),
  ADD CONSTRAINT `pm_user_ibfk_2` FOREIGN KEY (`office_contact_id`) REFERENCES `pm_contact` (`id`),
  ADD CONSTRAINT `pm_user_ibfk_3` FOREIGN KEY (`mailing_address_id`) REFERENCES `pm_address` (`id`),
  ADD CONSTRAINT `pm_user_ibfk_4` FOREIGN KEY (`personal_contact_id`) REFERENCES `pm_contact` (`id`);

--
-- Constraints for table `projskills`
--
ALTER TABLE `projskills`
  ADD CONSTRAINT `projskills_ibfk_1` FOREIGN KEY (`pm_skillset_id`) REFERENCES `pm_skillset` (`id`),
  ADD CONSTRAINT `projskills_ibfk_2` FOREIGN KEY (`pm_project_id`) REFERENCES `pm_project` (`id`);

--
-- Constraints for table `supplkills`
--
ALTER TABLE `supplkills`
  ADD CONSTRAINT `supplkills_ibfk_1` FOREIGN KEY (`pm_skillset_id`) REFERENCES `pm_skillset` (`id`),
  ADD CONSTRAINT `supplkills_ibfk_2` FOREIGN KEY (`pm_supplier`) REFERENCES `pm_supplier` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
