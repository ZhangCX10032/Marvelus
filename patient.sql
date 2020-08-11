DROP DATABASE IF EXISTS entrytask;
DROP DATABASE IF EXISTS clin;

CREATE DATABASE entrytask;
CREATE DATABASE clin;

USE clin;

DROP TABLE IF EXISTS Users CASCADE;
DROP TABLE IF EXISTS Doctors CASCADE;
DROP TABLE IF EXISTS Admins CASCADE;
DROP TABLE IF EXISTS Patients CASCADE;
DROP TABLE IF EXISTS Medicine CASCADE;
DROP TABLE IF EXISTS Bills CASCADE;
DROP TABLE IF EXISTS Prescriptions CASCADE;
DROP TABLE IF EXISTS Has_Medicine CASCADE;
DROP TABLE IF EXISTS BP_Records CASCADE;

create table Users (
uname varchar(50),
password varchar(256) not null,
name varchar(50) not null,
email varchar(256) not null,
last_login datetime(6),
PRIMARY KEY (uname)
);

create table Doctors (
uname varchar(50),

FOREIGN KEY (uname) references Users(uname) ON DELETE CASCADE,
PRIMARY KEY (uname)
);

create table Admins (
uname varchar(50),
FOREIGN KEY (uname) references Users(uname) ON DELETE CASCADE,
PRIMARY KEY (uname)
);

create table Patients (
patient_id bigint unsigned AUTO_INCREMENT,
birthdate date not null,
name varchar(256) not null,
gender varchar(10) not null,
phone_number varchar(256) not null,
PRIMARY KEY (patient_id)
);

create table Medicines (
med_name varchar(127) not null,
med_manufacturer varchar(127) not null,
brand varchar(127) not null,
spec varchar(127) not null,
amount integer unsigned not null,
default_price decimal(19,4) not null,
PRIMARY KEY (med_name, med_manufacturer, brand, spec)
);

create table Prescriptions (
prescription_id bigint unsigned AUTO_INCREMENT,
create_time datetime not null,
uname varchar(50),
patient_id bigint unsigned,
FOREIGN KEY (uname) references Doctors(uname) ON DELETE CASCADE,
FOREIGN KEY (patient_id) references Patients(patient_id) ON DELETE CASCADE,
PRIMARY KEY (prescription_id)
);

create table Has_Medicine(
prescription_id bigint unsigned not null,
med_name varchar(127) not null,
med_manufacturer varchar(127) not null,
brand varchar(127) not null,
spec varchar(127) not null,
amount integer unsigned not null,
FOREIGN KEY (prescription_id) references Prescriptions(prescription_id) ON DELETE CASCADE,
FOREIGN KEY (med_name, med_manufacturer, brand, spec) references Medicines(med_name, med_manufacturer, brand, spec) ON DELETE CASCADE,
PRIMARY KEY (prescription_id, med_name, med_manufacturer, brand, spec)
);

create table Bills(
bill_id bigint unsigned AUTO_INCREMENT,
create_time datetime not null,
paid_time datetime,
deal_price decimal(19,4) not null,
paid bit(1) not null,
patient_id bigint unsigned not null,
uname varchar(50) not null,
FOREIGN KEY (patient_id) references Patients(patient_id) ON DELETE CASCADE,
FOREIGN KEY (uname) references Doctors(uname) ON DELETE CASCADE,
PRIMARY KEY (bill_id)
);

create table BP_Records( /* BP=Blood pressure血压,sbp(收缩压),dbp(舒张压),cuff单位(mmHg)*/
bp_record_id bigint unsigned AUTO_INCREMENT,
create_time datetime not null,
sbp integer not null,
dbp integer not null,
cuff_pressure integer not null,
patient_id bigint unsigned not null,
FOREIGN KEY (patient_id) references Patients(patient_id) ON DELETE CASCADE,
PRIMARY KEY (bp_record_id)
);

insert into Users values ('doc1', 'e10adc3949ba59abbe56e057f20f883e', '张医生', 'doc1@gmail.com',null);

insert into Doctors values ('doc1');

insert into Patients values (null, '1999-05-20', '患者1', '女', '12345678');
insert into Patients values (null, '1949-10-01', '患者0', '男', '10033334444');
insert into Patients values (null, '1996-02-29', '患者', '女', '22993322');

insert into Medicines values ('板蓝根', '哈药', '好牌', '袋', '10', '1.4');
insert into Medicines values ('罗红霉素', '哈药', '好牌', '瓶', '90', '15.0');
insert into Medicines values ('阿司匹林', '华药', '东方牌', '片', '400', '0.3');
