use diemdanhsv

select * from taikhoan
insert into taikhoan(email, matKhau, maGV) VALUES ('concac','1234', 2)
delete from taikhoan where maTK=
select * from sinhvien
insert into sinhvien(hoTen, maLop, cmnd, gioiTinh, ngaySinh, email, SDT) value ('Nguyễn Thị Sinh Viên', 1, 123456789, 1, '2000-01-01', 'sv1@example.com', '0123456789')
delete from sinhvien where maSV=6

UPDATE table_name SET hoTen ='', maLop=, cmnd=, gioiTinh=, ngaySinh='', email=, SDT= WHERE maSV=6

select diemdanh.maBH, diemdanh.maSV, sinhvien.hoTen, diemdanh.gioVao from diemdanh
join sinhvien on diemdanh.maSV = sinhvien.maSV 
where maBH = 1

select * from diemdanh where maBH = 1
delete from diemdanh where maBH  =1

insert into sinhvien(maSV, hoTen, maLop, cmnd, gioiTinh, ngaySinh, email, SDT) value (6, 'Do Hoang Phuc', 1, 123456789, 1, '2000-01-01', 'sv1@example.com', '0123456789taikhoan')
insert into sinhvien(maSV, hoTen, maLop, cmnd, gioiTinh, ngaySinh, email, SDT) value (7, 'To Minh triet', 1, 123456789, 1, '2000-01-01', 'sv1@example.com', '0123456789')
insert into sinhvien(maSV, hoTen, maLop, cmnd, gioiTinh, ngaySinh, email, SDT) value (8, 'Hieu', 1, 123456789, 1, '2000-01-01', 'sv1@example.com', '0123456789')

select * from die
INSERT INTO `diemdanh` (`maSV`, `gioVao`, `gioRa`, `maBH`, `hinhAnh`) VALUES (1, 8, 10, 1, 'image1.jpg'),

INSERT INTO `diemdanh` (`maSV`, `gioVao`, `gioRa`, `maBH`, `hinhAnh`) VALUES (6, 3, 100, 1, 'image1.jpg')



