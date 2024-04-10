-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1:3306
-- Thời gian đã tạo: Th4 10, 2024 lúc 10:59 AM
-- Phiên bản máy phục vụ: 10.4.28-MariaDB
-- Phiên bản PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `diemdanhsv`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `buoihoc`
--

CREATE TABLE `buoihoc` (
  `maBH` int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
  `maMH` int(11) NOT NULL,
  `gioBD` int(11) NOT NULL,
  `gioKT` int(11) NOT NULL,
  `ngay` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `diemdanh`
--

CREATE TABLE `diemdanh` (
  `maDD` int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
  `maSV` int(11) NOT NULL,
  `gioVao` int(11) NOT NULL,
  `gioRa` int(11) NOT NULL,
  `maBH` int(11) NOT NULL,
  `hinhAnh` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `giangvien`
--

CREATE TABLE `giangvien` (
  `maGV` int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
  `hoTen` varchar(100) NOT NULL,
  `SDT` varchar(11) NOT NULL,
  `maTK` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `hinhsv`
--

CREATE TABLE `hinhsv` (
  `maSV` int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
  `hinhAnh` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `lop`
--

CREATE TABLE `lop` (
  `maLop` int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
  `tenLop` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `monhoc`
--

CREATE TABLE `monhoc` (
  `maMH` int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
  `tenMH` varchar(100) NOT NULL,
  `maLop` int(11) NOT NULL,
  `maGV` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `sinhvien`
--

CREATE TABLE `sinhvien` (
  `maSV` int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
  `hoTen` varchar(100) NOT NULL,
  `maLop` int(11) NOT NULL,
  `cmnd` int(11) NOT NULL,
  `gioiTinh` int(11) NOT NULL,
  `ngaySinh` date NOT NULL,
  `email` varchar(100) NOT NULL,
  `SDT` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `taikhoan`
--

CREATE TABLE `taikhoan` (
  `maTK` int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
  `email` text NOT NULL,
  `matKhau` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `buoihoc`
--
ALTER TABLE `buoihoc`
  ADD KEY `fk_maMH` (`maMH`);

--
-- Chỉ mục cho bảng `diemdanh`
--
ALTER TABLE `diemdanh`
  ADD KEY `fk_maSV` (`maSV`),
  ADD KEY `fk_maBH` (`maBH`);

--
-- Chỉ mục cho bảng `giangvien`
--
ALTER TABLE `giangvien`
  ADD KEY `fk_maTK` (`maTK`);

--
-- Chỉ mục cho bảng `hinhsv`
--
ALTER TABLE `hinhsv`
  ADD KEY `fk_maSV_1` (`maSV`);

--
-- Chỉ mục cho bảng `lop`
--


--
-- Chỉ mục cho bảng `monhoc`
--
ALTER TABLE `monhoc`
  ADD KEY `fk_maLop_2` (`maLop`),
  ADD KEY `fk_maGV` (`maGV`);

--
-- Chỉ mục cho bảng `sinhvien`
--
ALTER TABLE `sinhvien`
  ADD KEY `fk_maLop_1` (`maLop`);

--
-- Chỉ mục cho bảng `taikhoan`
--

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `buoihoc`
--
ALTER TABLE `buoihoc`
  ADD CONSTRAINT `fk_maMH` FOREIGN KEY (`maMH`) REFERENCES `monhoc` (`maMH`);

--
-- Các ràng buộc cho bảng `diemdanh`
--
ALTER TABLE `diemdanh`
  ADD CONSTRAINT `fk_maBH` FOREIGN KEY (`maBH`) REFERENCES `buoihoc` (`maBH`),
  ADD CONSTRAINT `fk_maSV` FOREIGN KEY (`maSV`) REFERENCES `sinhvien` (`maSV`);

--
-- Các ràng buộc cho bảng `giangvien`
--
ALTER TABLE `giangvien`
  ADD CONSTRAINT `fk_maTK` FOREIGN KEY (`maTK`) REFERENCES `taikhoan` (`maTK`);

--
-- Các ràng buộc cho bảng `hinhsv`
--
ALTER TABLE `hinhsv`
  ADD CONSTRAINT `fk_maSV_1` FOREIGN KEY (`maSV`) REFERENCES `sinhvien` (`maSV`);

--
-- Các ràng buộc cho bảng `monhoc`
--
ALTER TABLE `monhoc`
  ADD CONSTRAINT `fk_maGV` FOREIGN KEY (`maGV`) REFERENCES `giangvien` (`maGV`),
  ADD CONSTRAINT `fk_maLop_2` FOREIGN KEY (`maLop`) REFERENCES `lop` (`maLop`);

--
-- Các ràng buộc cho bảng `sinhvien`
--
ALTER TABLE `sinhvien`
  ADD CONSTRAINT `fk_maLop_1` FOREIGN KEY (`maLop`) REFERENCES `lop` (`maLop`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- Chèn dữ liệu vào bảng `lop`
INSERT INTO `lop` (`tenLop`) VALUES
('Lớp A'),
('Lớp B'),
('Lớp C');

-- Chèn dữ liệu vào bảng `taikhoan`
INSERT INTO `taikhoan` (`email`, `matKhau`) VALUES
('gv1@example.com', 'gv1_password'),
('gv2@example.com', 'gv2_password');

-- Chèn dữ liệu vào bảng `giangvien`
INSERT INTO `giangvien` (`hoTen`, `SDT`, `maTK`) VALUES
('Nguyễn Văn Giáo Viên', '0123456789', 1),
('Trần Thị Giảng Viên', '0987654321', 2);



-- Chèn dữ liệu vào bảng `monhoc`
INSERT INTO `monhoc` (`tenMH`, `maLop`, `maGV`) VALUES
('Toán', 1, 1),
('Văn', 2, 2);

-- Chèn dữ liệu vào bảng `sinhvien`
INSERT INTO `sinhvien` (`hoTen`, `maLop`, `cmnd`, `gioiTinh`, `ngaySinh`, `email`, `SDT`) VALUES
('Nguyễn Thị Sinh Viên', 1, 123456789, 1, '2000-01-01', 'sv1@example.com', '0123456789'),
('Trần Văn Sinh Viên', 2, 987654321, 0, '2001-02-02', 'sv2@example.com', '0987654321');

-- Chèn dữ liệu vào bảng `buoihoc`
INSERT INTO `buoihoc` (`maMH`, `gioBD`, `gioKT`, `ngay`) VALUES
(1, 8, 10, '2024-04-10'),
(2, 10, 12, '2024-04-11');

-- Chèn dữ liệu vào bảng `diemdanh`
INSERT INTO `diemdanh` (`maSV`, `gioVao`, `gioRa`, `maBH`, `hinhAnh`) VALUES
(1, 8, 10, 1, 'image1.jpg'),
(2, 9, 11, 2, 'image2.jpg');

-- Chèn dữ liệu vào bảng `hinhsv`
INSERT INTO `hinhsv` (`hinhAnh`) VALUES
('image1.jpg'),
('image2.jpg');

