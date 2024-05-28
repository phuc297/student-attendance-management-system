-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema diemdanhsinhvien
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema diemdanhsinhvien
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `diemdanhsinhvien` DEFAULT CHARACTER SET utf8 ;
USE `diemdanhsinhvien` ;

-- -----------------------------------------------------
-- Table `diemdanhsinhvien`.`taikhoan`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `diemdanhsinhvien`.`taikhoan` (
  `maTK` INT NOT NULL AUTO_INCREMENT,
  `tenTK` VARCHAR(45) NOT NULL,
  `matKhau` VARCHAR(45) NOT NULL,
  `loaiTK` INT NOT NULL,
  PRIMARY KEY (`maTK`, `tenTK`),
  UNIQUE INDEX `tenTK_UNIQUE` (`tenTK` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `diemdanhsinhvien`.`giangvien`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `diemdanhsinhvien`.`giangvien` (
  `maGV` INT NOT NULL AUTO_INCREMENT,
  `hoTen` VARCHAR(45) NOT NULL,
  `gioitinh` ENUM('Nam', 'Nữ') NOT NULL,
  `ngaysinh` DATE NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `sdt` VARCHAR(45) NOT NULL,
  `maTK` INT NOT NULL,
  PRIMARY KEY (`maGV`),
  INDEX `maTK_idx` (`maTK` ASC) VISIBLE,
  CONSTRAINT `giangvien_taikhoan`
    FOREIGN KEY (`maTK`)
    REFERENCES `diemdanhsinhvien`.`taikhoan` (`maTK`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `diemdanhsinhvien`.`lop`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `diemdanhsinhvien`.`lop` (
  `maLop` INT NOT NULL AUTO_INCREMENT,
  `tenLop` VARCHAR(45) NULL,
  PRIMARY KEY (`maLop`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `diemdanhsinhvien`.`sinhvien`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `diemdanhsinhvien`.`sinhvien` (
  `maSV` INT NOT NULL AUTO_INCREMENT,
  `hoTen` VARCHAR(45) NOT NULL,
  `gioitinh` ENUM('Nam', 'Nữ') NOT NULL,
  `ngaysinh` DATE NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `sdt` VARCHAR(45) NOT NULL,
  `maLop` INT NULL,
  PRIMARY KEY (`maSV`),
  INDEX `sinhvien_lopsinhvien_idx` (`maLop` ASC) VISIBLE,
  CONSTRAINT `sinhvien_lophoc`
    FOREIGN KEY (`maLop`)
    REFERENCES `diemdanhsinhvien`.`lop` (`maLop`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `diemdanhsinhvien`.`monhoc`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `diemdanhsinhvien`.`monhoc` (
  `maMH` INT NOT NULL AUTO_INCREMENT,
  `tenMH` VARCHAR(45) NOT NULL,
  `maGV` INT NOT NULL,
  `maLop` INT NOT NULL,
  PRIMARY KEY (`maMH`),
  INDEX `monhoc_giangvien_idx` (`maGV` ASC) VISIBLE,
  INDEX `monhoc_lophoc_idx` (`maLop` ASC) VISIBLE,
  CONSTRAINT `monhoc_giangvien`
    FOREIGN KEY (`maGV`)
    REFERENCES `diemdanhsinhvien`.`giangvien` (`maGV`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `monhoc_lophoc`
    FOREIGN KEY (`maLop`)
    REFERENCES `diemdanhsinhvien`.`lop` (`maLop`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `diemdanhsinhvien`.`buoihoc`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `diemdanhsinhvien`.`buoihoc` (
  `maBH` INT NOT NULL AUTO_INCREMENT,
  `maLH` INT NOT NULL,
  `tuan` INT NOT NULL,
  `tietbatdau` INT NOT NULL,
  `tietketthuc` INT NOT NULL,
  `ngay` DATE NULL,
  PRIMARY KEY (`maBH`),
  INDEX `buoihoc_monhoc_idx` (`maLH` ASC) VISIBLE,
  CONSTRAINT `buoihoc_monhoc`
    FOREIGN KEY (`maLH`)
    REFERENCES `diemdanhsinhvien`.`monhoc` (`maLop`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `diemdanhsinhvien`.`diemdanh`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `diemdanhsinhvien`.`diemdanh` (
  `maDD` INT NOT NULL AUTO_INCREMENT,
  `maBH` INT NOT NULL,
  `maSV` INT NOT NULL,
  `giovao` DATETIME NOT NULL,
  `giora` DATETIME NOT NULL,
  `trangthai` INT NULL,
  `ghichu` NVARCHAR(500) NULL,
  PRIMARY KEY (`maDD`),
  INDEX `diemdanh_buoihoc_idx` (`maBH` ASC) VISIBLE,
  INDEX `diemdanh_sinhvien_idx` (`maSV` ASC) VISIBLE,
  UNIQUE INDEX `buoihoc_sinhvien_idx` (`maBH` ASC, `maSV` ASC) VISIBLE,
  CONSTRAINT `diemdanh_buoihoc`
    FOREIGN KEY (`maBH`)
    REFERENCES `diemdanhsinhvien`.`buoihoc` (`maBH`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `diemdanh_sinhvien`
    FOREIGN KEY (`maSV`)
    REFERENCES `diemdanhsinhvien`.`sinhvien` (`maSV`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
