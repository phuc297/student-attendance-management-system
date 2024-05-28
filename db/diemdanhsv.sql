-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 10, 2024 at 05:58 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `diemdanhsv`
--

-- --------------------------------------------------------

--
-- Table structure for table `buoihoc`
--

CREATE TABLE `buoihoc` (
  `maBH` int(11) NOT NULL,
  `maMH` int(11) NOT NULL,
  `maLop` int(11) NOT NULL,
  `gioBD` int(11) NOT NULL,
  `gioKT` int(11) NOT NULL,
  `ngay` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `buoihoc`
--

INSERT INTO `buoihoc` (`maBH`, `maMH`, `maLop`, `gioBD`, `gioKT`, `ngay`) VALUES
(1, 1, 1, 8, 10, '2024-04-10'),
(2, 2, 2, 10, 12, '2024-04-11');

-- --------------------------------------------------------

--
-- Table structure for table `diemdanh`
--

CREATE TABLE `diemdanh` (
  `maDD` int(11) NOT NULL,
  `maSV` int(11) NOT NULL,
  `gioVao` int(11) NOT NULL,
  `gioRa` int(11) NOT NULL,
  `maBH` int(11) NOT NULL,
  `hinhAnh` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `diemdanh`
--

INSERT INTO `diemdanh` (`maDD`, `maSV`, `gioVao`, `gioRa`, `maBH`, `hinhAnh`) VALUES
(1, 1, 8, 10, 1, 'image1.jpg'),
(2, 2, 9, 11, 2, 'image2.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `giangvien`
--

CREATE TABLE `giangvien` (
  `maGV` int(11) NOT NULL,
  `hoTen` varchar(100) NOT NULL,
  `SDT` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `giangvien`
--

INSERT INTO `giangvien` (`maGV`, `hoTen`, `SDT`) VALUES
(1, 'Nguyễn Văn Giáo Viên', '0123456789'),
(2, 'Trần Thị Giảng Viên', '0987654321'),
(3, 'Nguyễn Văn A', '0123456789');

-- --------------------------------------------------------

--
-- Table structure for table `hinhsv`
--

CREATE TABLE `hinhsv` (
  `maSV` int(11) NOT NULL,
  `hinhAnh` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `hinhsv`
--

INSERT INTO `hinhsv` (`maSV`, `hinhAnh`) VALUES
(1, 'image1.jpg'),
(2, 'image2.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `lop`
--

CREATE TABLE `lop` (
  `maLop` int(11) NOT NULL,
  `tenLop` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `lop`
--

INSERT INTO `lop` (`maLop`, `tenLop`) VALUES
(1, 'Lớp A'),
(2, 'Lớp B'),
(3, 'Lớp C');

-- --------------------------------------------------------

--
-- Table structure for table `monhoc`
--

CREATE TABLE `monhoc` (
  `maMH` int(11) NOT NULL,
  `tenMH` varchar(100) NOT NULL,
  `maGV` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `monhoc`
--

INSERT INTO `monhoc` (`maMH`, `tenMH`, `maGV`) VALUES
(1, 'Toán', 1),
(2, 'Văn', 2);

-- --------------------------------------------------------

--
-- Table structure for table `sinhvien`
--

CREATE TABLE `sinhvien` (
  `maSV` int(11) NOT NULL,
  `hoTen` varchar(100) NOT NULL,
  `maLop` int(11) NOT NULL,
  `cmnd` int(11) NOT NULL,
  `gioiTinh` int(11) NOT NULL,
  `ngaySinh` date NOT NULL,
  `email` varchar(100) NOT NULL,
  `SDT` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sinhvien`
--

INSERT INTO `sinhvien` (`maSV`, `hoTen`, `maLop`, `cmnd`, `gioiTinh`, `ngaySinh`, `email`, `SDT`) VALUES
(1, 'Nguyễn Thị Sinh Viên', 1, 123456789, 1, '2000-01-01', 'sv1@example.com', '0123456789'),
(2, 'Trần Văn Sinh Viên', 2, 987654321, 0, '2001-02-02', 'sv2@example.com', '0987654321');

-- --------------------------------------------------------

--
-- Table structure for table `taikhoan`
--

CREATE TABLE `taikhoan` (
  `maTK` int(11) NOT NULL,
  `email` text NOT NULL,
  `matKhau` varchar(100) NOT NULL,
  `maGV` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `buoihoc`
--
ALTER TABLE `buoihoc`
  ADD PRIMARY KEY (`maBH`),
  ADD KEY `fk_maMH` (`maMH`),
  ADD KEY `fk_maLop_2` (`maLop`);

--
-- Indexes for table `diemdanh`
--
ALTER TABLE `diemdanh`
  ADD PRIMARY KEY (`maDD`),
  ADD KEY `fk_maSV` (`maSV`),
  ADD KEY `fk_maBH` (`maBH`);

--
-- Indexes for table `giangvien`
--
ALTER TABLE `giangvien`
  ADD PRIMARY KEY (`maGV`);

--
-- Indexes for table `hinhsv`
--
ALTER TABLE `hinhsv`
  ADD PRIMARY KEY (`maSV`),
  ADD KEY `fk_maSV_1` (`maSV`);

--
-- Indexes for table `lop`
--
ALTER TABLE `lop`
  ADD PRIMARY KEY (`maLop`);

--
-- Indexes for table `monhoc`
--
ALTER TABLE `monhoc`
  ADD PRIMARY KEY (`maMH`),
  ADD KEY `fk_maGV` (`maGV`);

--
-- Indexes for table `sinhvien`
--
ALTER TABLE `sinhvien`
  ADD PRIMARY KEY (`maSV`),
  ADD KEY `fk_maLop_1` (`maLop`);

--
-- Indexes for table `taikhoan`
--
ALTER TABLE `taikhoan`
  ADD PRIMARY KEY (`maTK`),
  ADD KEY `fk_idgiangvien` (`maGV`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `buoihoc`
--
ALTER TABLE `buoihoc`
  MODIFY `maBH` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `diemdanh`
--
ALTER TABLE `diemdanh`
  MODIFY `maDD` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `giangvien`
--
ALTER TABLE `giangvien`
  MODIFY `maGV` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `hinhsv`
--
ALTER TABLE `hinhsv`
  MODIFY `maSV` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `lop`
--
ALTER TABLE `lop`
  MODIFY `maLop` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `monhoc`
--
ALTER TABLE `monhoc`
  MODIFY `maMH` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `sinhvien`
--
ALTER TABLE `sinhvien`
  MODIFY `maSV` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `taikhoan`
--
ALTER TABLE `taikhoan`
  MODIFY `maTK` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `buoihoc`
--
ALTER TABLE `buoihoc`
  ADD CONSTRAINT `fk_maLop_2` FOREIGN KEY (`maLop`) REFERENCES `lop` (`maLop`),
  ADD CONSTRAINT `fk_maMH` FOREIGN KEY (`maMH`) REFERENCES `monhoc` (`maMH`);

--
-- Constraints for table `diemdanh`
--
ALTER TABLE `diemdanh`
  ADD CONSTRAINT `fk_maBH` FOREIGN KEY (`maBH`) REFERENCES `buoihoc` (`maBH`),
  ADD CONSTRAINT `fk_maSV` FOREIGN KEY (`maSV`) REFERENCES `sinhvien` (`maSV`);

--
-- Constraints for table `hinhsv`
--
ALTER TABLE `hinhsv`
  ADD CONSTRAINT `fk_maSV_1` FOREIGN KEY (`maSV`) REFERENCES `sinhvien` (`maSV`);

--
-- Constraints for table `monhoc`
--
ALTER TABLE `monhoc`
  ADD CONSTRAINT `fk_maGV` FOREIGN KEY (`maGV`) REFERENCES `giangvien` (`maGV`);

--
-- Constraints for table `sinhvien`
--
ALTER TABLE `sinhvien`
  ADD CONSTRAINT `fk_maLop_1` FOREIGN KEY (`maLop`) REFERENCES `lop` (`maLop`);

--
-- Constraints for table `taikhoan`
--
ALTER TABLE `taikhoan`
  ADD CONSTRAINT `fk_idgiangvien` FOREIGN KEY (`maGV`) REFERENCES `giangvien` (`maGV`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
