-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 07, 2024 at 07:59 PM
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
-- Database: `db_nhom7_python`
--

-- --------------------------------------------------------

--
-- Table structure for table `chitiethoadon`
--

CREATE DATABASE db_nhom7_python;
USE db_nhom7_python;

CREATE TABLE `chitiethoadon` (
  `cthd_id` int(11) NOT NULL,
  `cthd_hdb_id` varchar(255) NOT NULL,
  `cthd_s_id` varchar(255) DEFAULT NULL,
  `cthd_dongia` decimal(19,2) NOT NULL,
  `cthd_soluong` int(11) NOT NULL,
  `cthd_thanhtien` decimal(19,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `hoadonban`
--

CREATE TABLE `hoadonban` (
  `hdb_id` varchar(255) NOT NULL,
  `hdb_nv_id` varchar(255) DEFAULT NULL,
  `hdb_kh_sdt_id` varchar(255) DEFAULT NULL,
  `hdb_ngayxuat` datetime NOT NULL,
  `hdb_tongtien` decimal(19,2) NOT NULL,
  `hdb_trangthai` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Triggers `hoadonban`
--
DELIMITER $$
CREATE TRIGGER `tr_hdb_before_insert` BEFORE INSERT ON `hoadonban` FOR EACH ROW BEGIN
    DECLARE max_id INT;
    DECLARE new_id VARCHAR(255);

    SELECT IFNULL(MAX(CAST(SUBSTRING(hdb_id, 4) AS UNSIGNED)), 0) INTO max_id FROM hoadonban;
    SET new_id = CONCAT('hdb', LPAD(max_id + 1, 3, '0'));
    SET NEW.hdb_id = new_id;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `tr_update_hoadonban_before_update` BEFORE UPDATE ON `hoadonban` FOR EACH ROW BEGIN
    IF NEW.hdb_trangthai <> OLD.hdb_trangthai THEN
        IF DATEDIFF(NOW(), OLD.hdb_ngayxuat) > 15 THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Khong the cap nhat trang thai hoa don ban sau 15 ngay!';
        END IF;
    END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `hoadonchothue`
--

CREATE TABLE `hoadonchothue` (
  `hdct_id` varchar(255) NOT NULL,
  `hdct_kh_sdt_id` varchar(255) DEFAULT NULL,
  `hdct_nv_id` varchar(255) DEFAULT NULL,
  `hdct_ngaythue` datetime NOT NULL,
  `hdct_ngayhethan` date NOT NULL,
  `hdct_tongtien` decimal(19,2) NOT NULL,
  `hdct_trangthai` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Triggers `hoadonchothue`
--
DELIMITER $$
CREATE TRIGGER `tr_hdct_before_insert` BEFORE INSERT ON `hoadonchothue` FOR EACH ROW BEGIN
    DECLARE max_id INT;
    DECLARE new_id VARCHAR(255);

    SELECT IFNULL(MAX(CAST(SUBSTRING(hdct_id, 5) AS UNSIGNED)), 0) INTO max_id FROM hoadonchothue;
    SET new_id = CONCAT('hdct', LPAD(max_id + 1, 3, '0'));
    SET NEW.hdct_id = new_id;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `hoadonnhap`
--

CREATE TABLE `hoadonnhap` (
  `hdn_id` varchar(255) NOT NULL,
  `hdn_ls_id` varchar(255) DEFAULT NULL,
  `hdn_ngayxuat` datetime NOT NULL,
  `hdn_dongia` decimal(19,2) NOT NULL,
  `hdn_soluong` int(11) NOT NULL,
  `hdn_thanhtien` decimal(19,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Triggers `hoadonnhap`
--
DELIMITER $$
CREATE TRIGGER `tr_hdn_before_insert` BEFORE INSERT ON `hoadonnhap` FOR EACH ROW BEGIN
    DECLARE max_id INT;
    DECLARE new_id VARCHAR(255);

    SELECT IFNULL(MAX(CAST(SUBSTRING(hdn_id, 4) AS UNSIGNED)), 0) INTO max_id FROM hoadonnhap;
    SET new_id = CONCAT('hdn', LPAD(max_id + 1, 3, '0'));
    SET NEW.hdn_id = new_id;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `hoadontrahang`
--

CREATE TABLE `hoadontrahang` (
  `hdth_id` varchar(255) NOT NULL,
  `hdth_hdb_id` varchar(255) DEFAULT NULL,
  `hdth_nv_id` varchar(255) DEFAULT NULL,
  `hdth_ngaytrahang` datetime NOT NULL,
  `hdth_tongtienhoantra` decimal(19,2) NOT NULL,
  `hdth_trangthai` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Triggers `hoadontrahang`
--
DELIMITER $$
CREATE TRIGGER `tr_hdth_before_insert` BEFORE INSERT ON `hoadontrahang` FOR EACH ROW BEGIN
    DECLARE max_id INT;
    DECLARE new_id VARCHAR(255);

    SELECT IFNULL(MAX(CAST(SUBSTRING(hdth_id, 5) AS UNSIGNED)), 0) INTO max_id FROM hoadontrahang;
    SET new_id = CONCAT('hdth', LPAD(max_id + 1, 3, '0'));
    SET NEW.hdth_id = new_id;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `khachhang`
--

CREATE TABLE `khachhang` (
  `STT` int(11) DEFAULT NULL,
  `kh_sdt_id` varchar(255) NOT NULL,
  `kh_ten` varchar(255) NOT NULL,
  `kh_gioitinh` varchar(255) NOT NULL,
  `kh_ngaysinh` date NOT NULL,
  `kh_cccd` varchar(255) NOT NULL,
  `kh_email` varchar(255) NOT NULL,
  `kh_diachi` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `khachhang`
--

INSERT INTO `khachhang` (`STT`, `kh_sdt_id`, `kh_ten`, `kh_gioitinh`, `kh_ngaysinh`, `kh_cccd`, `kh_email`, `kh_diachi`) VALUES
(1, '0901234567', 'Trần Thị B', 'Nữ', '1985-08-20', '987654321', 'thib@example.com', '456 Đường DEF, Quận UVW'),
(2, '0912345678', 'Phạm Thị D', 'Nữ', '1988-12-25', '654321098', 'thid@example.com', '012 Đường JKL, Quận PQR'),
(3, '0921098765', 'Phan Văn I', 'Nam', '1987-11-02', '321098765', 'vani@example.com', '567 Đường UVW, Quận EFG'),
(4, '0932109876', 'Trần Văn G', 'Nam', '1991-06-12', '543210987', 'vang@example.com', '901 Đường OPQ, Quận CDE'),
(5, '0943210987', 'Nguyễn Thị F', 'Nữ', '1993-09-05', '210987654', 'thif@example.com', '678 Đường XYZ, Quận HIJ'),
(6, '0956789012', 'Lê Thị H', 'Nữ', '1994-03-18', '432109876', 'thih@example.com', '234 Đường RST, Quận BCD'),
(7, '0965432109', 'Hoàng Văn E', 'Nam', '1992-04-30', '789012345', 'vane@example.com', '345 Đường MNO, Quận STU'),
(8, '0978123456', 'Lê Văn C', 'Nam', '1995-01-10', '456789012', 'vanc@example.com', '789 Đường GHI, Quận KLM'),
(9, '0987654321', 'Nguyễn Văn A', 'Nam', '1990-05-15', '123456789', 'vana@example.com', '123 Đường ABC, Quận XYZ'),
(10, '0998765432', 'Trần Văn K', 'Nam', '1998-07-20', '987654321', 'vank@example.com', '890 Đường HIJ, Quận LMN');

--
-- Triggers `khachhang`
--
DELIMITER $$
CREATE TRIGGER `tr_insert_khachhang` BEFORE INSERT ON `khachhang` FOR EACH ROW BEGIN
    SET NEW.STT := (SELECT MAX(STT) + 1 FROM khachhang);
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `losach`
--

CREATE TABLE `losach` (
  `ls_id` varchar(255) NOT NULL,
  `ls_s_id` varchar(255) DEFAULT NULL,
  `ls_ncc_id` varchar(255) DEFAULT NULL,
  `ls_tensach` varchar(255) NOT NULL,
  `ls_theloaisach` varchar(255) NOT NULL,
  `ls_nhaxuatban` varchar(255) NOT NULL,
  `ls_ngaynhap` datetime NOT NULL,
  `ls_dongia` decimal(19,2) NOT NULL,
  `ls_soluong` int(11) NOT NULL,
  `ls_thanhtien` decimal(19,2) NOT NULL,
  `ls_giabanle` decimal(19,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Triggers `losach`
--
DELIMITER $$
CREATE TRIGGER `tr_ls_before_insert` BEFORE INSERT ON `losach` FOR EACH ROW BEGIN
    DECLARE max_id INT;
    DECLARE new_id VARCHAR(255);

    SELECT IFNULL(MAX(CAST(SUBSTRING(ls_id, 3) AS UNSIGNED)), 0) INTO max_id FROM losach;
    SET new_id = CONCAT('ls', LPAD(max_id + 1, 3, '0'));
    SET NEW.ls_id = new_id;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `nhacungcap`
--

CREATE TABLE `nhacungcap` (
  `ncc_id` varchar(255) NOT NULL,
  `ncc_ten` varchar(255) NOT NULL,
  `ncc_sdt` varchar(255) NOT NULL,
  `ncc_email` varchar(255) NOT NULL,
  `ncc_diachi` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `nhacungcap`
--

INSERT INTO `nhacungcap` (`ncc_id`, `ncc_ten`, `ncc_sdt`, `ncc_email`, `ncc_diachi`) VALUES
('ncc001', 'Nhà cung cấp A', '123456789', 'nccA@example.com', '123 Đường ABC'),
('ncc002', 'Nhà cung cấp B', '987654321', 'nccB@example.com', '456 Đường XYZ'),
('ncc003', 'Nhà cung cấp C', '456123789', 'nccC@example.com', '789 Đường KLM'),
('ncc004', 'Nhà cung cấp D', '789123456', 'nccD@example.com', '101 Đường UVW'),
('ncc005', 'Nhà cung cấp E', '321654987', 'nccE@example.com', '111 Đường PQRS');

--
-- Triggers `nhacungcap`
--
DELIMITER $$
CREATE TRIGGER `tr_ncc_before_insert` BEFORE INSERT ON `nhacungcap` FOR EACH ROW BEGIN
    DECLARE max_id INT;
    DECLARE new_id VARCHAR(255);

    SELECT IFNULL(MAX(CAST(SUBSTRING(ncc_id, 4) AS UNSIGNED)), 0) INTO max_id FROM nhacungcap;
    SET new_id = CONCAT('ncc', LPAD(max_id + 1, 3, '0'));
    SET NEW.ncc_id = new_id;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `nhanvien`
--

CREATE TABLE `nhanvien` (
  `nv_id` varchar(255) NOT NULL,
  `nv_tk_id` int(11) NOT NULL,
  `nv_ten` varchar(255) NOT NULL,
  `nv_gioitinh` varchar(255) NOT NULL,
  `nv_ngaysinh` date NOT NULL,
  `nv_sdt` varchar(255) NOT NULL,
  `nv_email` varchar(255) NOT NULL,
  `nv_diachi` varchar(255) NOT NULL,
  `nv_luong` decimal(19,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `nhanvien`
--

INSERT INTO `nhanvien` (`nv_id`, `nv_tk_id`, `nv_ten`, `nv_gioitinh`, `nv_ngaysinh`, `nv_sdt`, `nv_email`, `nv_diachi`, `nv_luong`) VALUES
('nv001', 1, 'Nguyễn Văn Admin', 'Nam', '2000-06-01', '0123456789', 'admin@gmail.com', 'Hải Dương', 10000000.00),
('nv002', 2, 'Nhân viên 1', 'Nữ', '2000-07-18', '0987654321', 'nhanvien@gmail.com', 'Hà Nội', 5000000.00);

--
-- Triggers `nhanvien`
--
DELIMITER $$
CREATE TRIGGER `tr_nv_before_insert` BEFORE INSERT ON `nhanvien` FOR EACH ROW BEGIN
    DECLARE max_id INT;
    DECLARE new_id VARCHAR(255);

    SELECT IFNULL(MAX(CAST(SUBSTRING(nv_id, 3) AS UNSIGNED)), 0) INTO max_id FROM nhanvien;
    SET new_id = CONCAT('nv', LPAD(max_id + 1, 3, '0'));
    SET NEW.nv_id = new_id;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `phieuchothue`
--

CREATE TABLE `phieuchothue` (
  `pct_id` int(11) NOT NULL,
  `pct_hdct_id` varchar(255) DEFAULT NULL,
  `pct_s_id` varchar(255) DEFAULT NULL,
  `pct_dongia` decimal(19,2) NOT NULL,
  `pct_soluong` int(11) NOT NULL,
  `pct_thanhtien` decimal(19,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `sach`
--

CREATE TABLE `sach` (
  `s_id` varchar(255) NOT NULL,
  `s_tensach` varchar(255) NOT NULL,
  `s_theloaisach` varchar(255) NOT NULL,
  `s_nhaxuatban` varchar(255) NOT NULL,
  `s_gia` decimal(19,2) NOT NULL,
  `s_soluong` int(11) NOT NULL,
  `s_trangthai` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sach`
--

INSERT INTO `sach` (`s_id`, `s_tensach`, `s_theloaisach`, `s_nhaxuatban`, `s_gia`, `s_soluong`, `s_trangthai`) VALUES
('sach001', 'Cuộc Phiêu Lưu Của TinTin', 'Sách thiếu nhi', 'Nhà xuất bản Kim Đồng', 50000.00, 100, 1),
('sach002', 'Đắc Nhân Tâm', 'Sách tâm lý, tình cảm', 'Nhà xuất bản Trẻ', 80000.00, 200, 1),
('sach003', 'Bí Mật Tư Duy Phản Biện', 'Sách tôn giáo', 'Nhà xuất bản giáo dục Việt Nam', 90000.00, 0, 0),
('sach004', 'Lịch Sử Việt Nam', 'Sách lịch sử', 'Nhà xuất bản chính trị quốc gia sự thật', 120000.00, 75, 1),
('sach005', 'Harry Potter và Hòn Đá Phù Thủy', 'Sách văn học viễn tưởng', 'Nhà xuất bản Trẻ', 150000.00, 300, 1),
('sach006', 'Steve Jobs - Hành Trình Đến Thành Công', 'Sách tiểu sử, tự truyện', 'Nhà xuất bản lao động', 170000.00, 120, 1),
('sach007', 'Nhà Giả Kim', 'Sách kinh dị, bí ẩn', 'Nhà xuất bản Hội Nhà văn', 100000.00, 90, 1),
('sach008', 'Tự Học IELTS', 'Sách khoa học công nghệ', 'Nhà xuất bản Tổng hợp thành phố Hồ Chí Minh', 250000.00, 110, 1),
('sach009', 'Hạt Giống Tâm Hồn', 'Sách truyền cảm hứng', 'Nhà xuất bản Trẻ', 130000.00, 200, 1),
('sach010', 'Kỹ Năng Sống Cho Trẻ', 'Sách thiếu nhi', 'Nhà xuất bản Kim Đồng', 60000.00, 180, 1),
('sach011', 'Tình Yêu Không Có Lỗi, Lỗi Ở Bạn Thân', 'Sách tâm lý, tình cảm', 'Nhà xuất bản Tư pháp', 75000.00, 150, 1),
('sach012', 'Tâm Linh Và Sự Sống Sau Khi Chết', 'Sách tôn giáo', 'Nhà xuất bản giáo dục Việt Nam', 90000.00, 100, 1),
('sach013', 'Văn Hoá Việt Nam', 'Sách văn hoá xã hội', 'Nhà xuất bản chính trị quốc gia sự thật', 115000.00, 130, 1),
('sach014', 'The Lord of The Rings', 'Sách văn học viễn tưởng', 'Nhà xuất bản Trẻ', 180000.00, 90, 1),
('sach015', 'Nguyễn Ái Quốc - Hồ Chí Minh', 'Sách tiểu sử, tự truyện', 'Nhà xuất bản lao động', 160000.00, 80, 1);

--
-- Triggers `sach`
--
DELIMITER $$
CREATE TRIGGER `tr_sach_before_insert` BEFORE INSERT ON `sach` FOR EACH ROW BEGIN
    DECLARE max_id INT;
    DECLARE new_id VARCHAR(255);

    SELECT IFNULL(MAX(CAST(SUBSTRING(s_id, 5) AS UNSIGNED)), 0) INTO max_id FROM sach;
    SET new_id = CONCAT('sach', LPAD(max_id + 1, 3, '0'));
    SET NEW.s_id = new_id;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `tr_update_sach_trangthai` BEFORE UPDATE ON `sach` FOR EACH ROW BEGIN
    IF NEW.s_soluong > 0 THEN
        SET NEW.s_trangthai = TRUE;
    ELSE
        SET NEW.s_trangthai = FALSE;
    END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `taikhoan`
--

CREATE TABLE `taikhoan` (
  `tk_id` int(11) NOT NULL,
  `tk_username` varchar(255) NOT NULL,
  `tk_password` varchar(255) NOT NULL,
  `tk_role` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `taikhoan`
--

INSERT INTO `taikhoan` (`tk_id`, `tk_username`, `tk_password`, `tk_role`) VALUES
(1, 'admin', '1234', 'admin'),
(2, 'nhanvien1', '1234', 'nhanvien');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `chitiethoadon`
--
ALTER TABLE `chitiethoadon`
  ADD PRIMARY KEY (`cthd_id`),
  ADD KEY `fk_cthd_hdb` (`cthd_hdb_id`),
  ADD KEY `fk_cthd_s` (`cthd_s_id`);

--
-- Indexes for table `hoadonban`
--
ALTER TABLE `hoadonban`
  ADD PRIMARY KEY (`hdb_id`),
  ADD KEY `fk_hdb_kh` (`hdb_kh_sdt_id`),
  ADD KEY `fk_hdb_nv` (`hdb_nv_id`);

--
-- Indexes for table `hoadonchothue`
--
ALTER TABLE `hoadonchothue`
  ADD PRIMARY KEY (`hdct_id`),
  ADD KEY `fk_hdct_kh` (`hdct_kh_sdt_id`),
  ADD KEY `fk_hdct_nv` (`hdct_nv_id`);

--
-- Indexes for table `hoadonnhap`
--
ALTER TABLE `hoadonnhap`
  ADD PRIMARY KEY (`hdn_id`),
  ADD KEY `fk_hdn_ls` (`hdn_ls_id`);

--
-- Indexes for table `hoadontrahang`
--
ALTER TABLE `hoadontrahang`
  ADD PRIMARY KEY (`hdth_id`),
  ADD KEY `fk_hdth_hdb` (`hdth_hdb_id`),
  ADD KEY `fk_hdth_nv` (`hdth_nv_id`);

--
-- Indexes for table `khachhang`
--
ALTER TABLE `khachhang`
  ADD PRIMARY KEY (`kh_sdt_id`);

--
-- Indexes for table `losach`
--
ALTER TABLE `losach`
  ADD PRIMARY KEY (`ls_id`),
  ADD KEY `fk_ls_ncc` (`ls_ncc_id`),
  ADD KEY `fk_ls_s` (`ls_s_id`);

--
-- Indexes for table `nhacungcap`
--
ALTER TABLE `nhacungcap`
  ADD PRIMARY KEY (`ncc_id`);

--
-- Indexes for table `nhanvien`
--
ALTER TABLE `nhanvien`
  ADD PRIMARY KEY (`nv_id`),
  ADD KEY `fk_nv_tk` (`nv_tk_id`);

--
-- Indexes for table `phieuchothue`
--
ALTER TABLE `phieuchothue`
  ADD PRIMARY KEY (`pct_id`),
  ADD KEY `fk_pct_hdct` (`pct_hdct_id`),
  ADD KEY `fk_pct_s` (`pct_s_id`);

--
-- Indexes for table `sach`
--
ALTER TABLE `sach`
  ADD PRIMARY KEY (`s_id`);

--
-- Indexes for table `taikhoan`
--
ALTER TABLE `taikhoan`
  ADD PRIMARY KEY (`tk_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `chitiethoadon`
--
ALTER TABLE `chitiethoadon`
  MODIFY `cthd_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `phieuchothue`
--
ALTER TABLE `phieuchothue`
  MODIFY `pct_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `taikhoan`
--
ALTER TABLE `taikhoan`
  MODIFY `tk_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `chitiethoadon`
--
ALTER TABLE `chitiethoadon`
  ADD CONSTRAINT `fk_cthd_hdb` FOREIGN KEY (`cthd_hdb_id`) REFERENCES `hoadonban` (`hdb_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_cthd_s` FOREIGN KEY (`cthd_s_id`) REFERENCES `sach` (`s_id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `hoadonban`
--
ALTER TABLE `hoadonban`
  ADD CONSTRAINT `fk_hdb_kh` FOREIGN KEY (`hdb_kh_sdt_id`) REFERENCES `khachhang` (`kh_sdt_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_hdb_nv` FOREIGN KEY (`hdb_nv_id`) REFERENCES `nhanvien` (`nv_id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `hoadonchothue`
--
ALTER TABLE `hoadonchothue`
  ADD CONSTRAINT `fk_hdct_kh` FOREIGN KEY (`hdct_kh_sdt_id`) REFERENCES `khachhang` (`kh_sdt_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_hdct_nv` FOREIGN KEY (`hdct_nv_id`) REFERENCES `nhanvien` (`nv_id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `hoadonnhap`
--
ALTER TABLE `hoadonnhap`
  ADD CONSTRAINT `fk_hdn_ls` FOREIGN KEY (`hdn_ls_id`) REFERENCES `losach` (`ls_id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `hoadontrahang`
--
ALTER TABLE `hoadontrahang`
  ADD CONSTRAINT `fk_hdth_hdb` FOREIGN KEY (`hdth_hdb_id`) REFERENCES `hoadonban` (`hdb_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_hdth_nv` FOREIGN KEY (`hdth_nv_id`) REFERENCES `nhanvien` (`nv_id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `losach`
--
ALTER TABLE `losach`
  ADD CONSTRAINT `fk_ls_ncc` FOREIGN KEY (`ls_ncc_id`) REFERENCES `nhacungcap` (`ncc_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_ls_s` FOREIGN KEY (`ls_s_id`) REFERENCES `sach` (`s_id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `nhanvien`
--
ALTER TABLE `nhanvien`
  ADD CONSTRAINT `fk_nv_tk` FOREIGN KEY (`nv_tk_id`) REFERENCES `taikhoan` (`tk_id`) ON UPDATE CASCADE;

--
-- Constraints for table `phieuchothue`
--
ALTER TABLE `phieuchothue`
  ADD CONSTRAINT `fk_pct_hdct` FOREIGN KEY (`pct_hdct_id`) REFERENCES `hoadonchothue` (`hdct_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_pct_s` FOREIGN KEY (`pct_s_id`) REFERENCES `sach` (`s_id`) ON DELETE SET NULL ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
