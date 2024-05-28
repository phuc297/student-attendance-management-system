-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1:3306
-- Thời gian đã tạo: Th4 22, 2024 lúc 12:38 PM
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
  `maBH` int(11) NOT NULL,
  `maMH` int(11) NOT NULL,
  `tuan` int(11) NOT NULL,
  `tietBD` int(11) NOT NULL,
  `tietKT` int(11) NOT NULL,
  `ngay` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `buoihoc`
--

INSERT INTO `buoihoc` (`maBH`, `maMH`, `tuan`, `tietBD`, `tietKT`, `ngay`) VALUES
(1, 1, 1, 1, 2, '2024-04-22'),
(2, 2, 1, 3, 4, '2024-04-22');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `diemdanh`
--

CREATE TABLE `diemdanh` (
  `maDD` int(11) NOT NULL,
  `maSV` int(11) NOT NULL,
  `gioVao` int(11) NOT NULL,
  `gioRa` int(11) NOT NULL,
  `maBH` int(11) NOT NULL,
  `chitiet` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `diemdanh`
--

INSERT INTO `diemdanh` (`maDD`, `maSV`, `gioVao`, `gioRa`, `maBH`, `chitiet`) VALUES
(1, 1, 8, 12, 1, 'Điểm danh vào buổi học 1'),
(2, 2, 8, 12, 1, 'Điểm danh vào buổi học 1');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `giangvien`
--

CREATE TABLE `giangvien` (
  `maGV` int(11) NOT NULL,
  `hoTen` varchar(100) NOT NULL,
  `SDT` varchar(11) NOT NULL,
  `gioitinh` varchar(10) NOT NULL,
  `email` int(11) NOT NULL,
  `ngaysinh` int(11) NOT NULL,
  `maTK` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `giangvien`
--

INSERT INTO `giangvien` (`maGV`, `hoTen`, `SDT`, `gioitinh`, `email`, `ngaysinh`, `maTK`) VALUES
(1, 'Nguyen Van A', '0123456789', 'Nam', 0, 1990, 1),
(2, 'Tran Thi B', '0987654321', 'Nữ', 0, 1995, 2);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `lop`
--

CREATE TABLE `lop` (
  `maLop` int(11) NOT NULL,
  `tenLop` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `lop`
--

INSERT INTO `lop` (`maLop`, `tenLop`) VALUES
(1, 'Lớp A'),
(2, 'Lớp B'),
(3, 'Lớp C');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `monhoc`
--

CREATE TABLE `monhoc` (
  `maMH` int(11) NOT NULL,
  `tenMH` varchar(100) NOT NULL,
  `maGV` int(11) NOT NULL,
  `maLop` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `monhoc`
--

INSERT INTO `monhoc` (`maMH`, `tenMH`, `maGV`, `maLop`) VALUES
(1, 'Toán', 1, 1),
(2, 'Văn', 2, 1);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `sinhvien`
--

CREATE TABLE `sinhvien` (
  `maSV` int(11) NOT NULL,
  `hoTen` varchar(100) NOT NULL,
  `maLop` int(11) NOT NULL,
  `gioiTinh` int(11) NOT NULL,
  `ngaySinh` date NOT NULL,
  `email` varchar(100) NOT NULL,
  `SDT` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `sinhvien`
--

INSERT INTO `sinhvien` (`maSV`, `hoTen`, `maLop`, `gioiTinh`, `ngaySinh`, `email`, `SDT`) VALUES
(1, 'Nguyen Van An', 1, 1, '1998-01-15', 'nguyenvanan@example.com', '0123456789'),
(2, 'Tran Thi Linh', 1, 0, '1999-02-20', 'tranthilinh@example.com', '0987654321');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `taikhoan`
--

CREATE TABLE `taikhoan` (
  `maTK` int(11) NOT NULL,
  `matKhau` varchar(100) NOT NULL,
  `loaiTK` varchar(50) NOT NULL,
  `tenTK` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `taikhoan`
--

INSERT INTO `taikhoan` (`maTK`, `matKhau`, `loaiTK`, `tenTK`) VALUES
(1, 'password1', 'giangvien', 'nguyenvana'),
(2, 'password2', 'giangvien', 'tranthib'),
(3, 'password3', 'sinhvien', 'nguyenvanan'),
(4, 'password4', 'sinhvien', 'tranthilinh');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `buoihoc`
--
ALTER TABLE `buoihoc`
  ADD PRIMARY KEY (`maBH`),
  ADD KEY `fk_maMH` (`maMH`);

--
-- Chỉ mục cho bảng `diemdanh`
--
ALTER TABLE `diemdanh`
  ADD PRIMARY KEY (`maDD`),
  ADD KEY `fk_maSV` (`maSV`),
  ADD KEY `fk_maBH` (`maBH`);

--
-- Chỉ mục cho bảng `giangvien`
--
ALTER TABLE `giangvien`
  ADD PRIMARY KEY (`maGV`),
  ADD KEY `fk_TK` (`maTK`);

--
-- Chỉ mục cho bảng `lop`
--
ALTER TABLE `lop`
  ADD PRIMARY KEY (`maLop`);

--
-- Chỉ mục cho bảng `monhoc`
--
ALTER TABLE `monhoc`
  ADD PRIMARY KEY (`maMH`),
  ADD KEY `fk_maGV` (`maGV`),
  ADD KEY `fk_maLop` (`maLop`);

--
-- Chỉ mục cho bảng `sinhvien`
--
ALTER TABLE `sinhvien`
  ADD PRIMARY KEY (`maSV`),
  ADD KEY `fk_maLop_1` (`maLop`);

--
-- Chỉ mục cho bảng `taikhoan`
--
ALTER TABLE `taikhoan`
  ADD PRIMARY KEY (`maTK`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `buoihoc`
--
ALTER TABLE `buoihoc`
  MODIFY `maBH` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT cho bảng `diemdanh`
--
ALTER TABLE `diemdanh`
  MODIFY `maDD` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT cho bảng `giangvien`
--
ALTER TABLE `giangvien`
  MODIFY `maGV` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT cho bảng `lop`
--
ALTER TABLE `lop`
  MODIFY `maLop` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT cho bảng `monhoc`
--
ALTER TABLE `monhoc`
  MODIFY `maMH` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT cho bảng `sinhvien`
--
ALTER TABLE `sinhvien`
  MODIFY `maSV` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT cho bảng `taikhoan`
--
ALTER TABLE `taikhoan`
  MODIFY `maTK` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

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
  ADD CONSTRAINT `fk_TK` FOREIGN KEY (`maTK`) REFERENCES `taikhoan` (`maTK`);

--
-- Các ràng buộc cho bảng `monhoc`
--
ALTER TABLE `monhoc`
  ADD CONSTRAINT `fk_maGV` FOREIGN KEY (`maGV`) REFERENCES `giangvien` (`maGV`),
  ADD CONSTRAINT `fk_maLop` FOREIGN KEY (`maLop`) REFERENCES `lop` (`maLop`);

--
-- Các ràng buộc cho bảng `sinhvien`
--
ALTER TABLE `sinhvien`
  ADD CONSTRAINT `fk_maLop_1` FOREIGN KEY (`maLop`) REFERENCES `lop` (`maLop`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
