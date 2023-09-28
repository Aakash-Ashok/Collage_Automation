/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - college
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`college` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `college`;

/*Table structure for table `attendence` */

DROP TABLE IF EXISTS `attendence`;

CREATE TABLE `attendence` (
  `ATTENDENCE_ID` int(11) NOT NULL AUTO_INCREMENT,
  `SUBJECT_ID` int(11) DEFAULT NULL,
  `STUDENT_ID` int(11) DEFAULT NULL,
  `DATE` varchar(50) DEFAULT NULL,
  `ATTENDENCE` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ATTENDENCE_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `attendence` */

insert  into `attendence`(`ATTENDENCE_ID`,`SUBJECT_ID`,`STUDENT_ID`,`DATE`,`ATTENDENCE`) values (1,25,33,'2023-02-04','PRESENT');

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `CHAT_ID` int(11) NOT NULL AUTO_INCREMENT,
  `FROM_ID` int(11) DEFAULT NULL,
  `TO_ID` int(11) DEFAULT NULL,
  `MESSAGE` varchar(250) DEFAULT NULL,
  `DATE` varchar(250) DEFAULT NULL,
  `IMAGE` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`CHAT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

/*Table structure for table `course` */

DROP TABLE IF EXISTS `course`;

CREATE TABLE `course` (
  `COURSE_ID` int(11) NOT NULL AUTO_INCREMENT,
  `DEPARTMENT_ID` int(11) DEFAULT NULL,
  `COURSE_NAME` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`COURSE_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `course` */

insert  into `course`(`COURSE_ID`,`DEPARTMENT_ID`,`COURSE_NAME`) values (7,11,'BCA'),(8,12,'ACCOUNTING'),(9,14,'bs'),(10,11,'sd');

/*Table structure for table `department` */

DROP TABLE IF EXISTS `department`;

CREATE TABLE `department` (
  `DEPARTMENT_ID` int(11) NOT NULL AUTO_INCREMENT,
  `DEPARTMENT_NAME` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`DEPARTMENT_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `department` */

insert  into `department`(`DEPARTMENT_ID`,`DEPARTMENT_NAME`) values (11,'chemistry'),(14,'as'),(15,'qw'),(16,'mm');

/*Table structure for table `discussion_form` */

DROP TABLE IF EXISTS `discussion_form`;

CREATE TABLE `discussion_form` (
  `DISCUSSION_ID` int(11) NOT NULL AUTO_INCREMENT,
  `FROM-ID` int(11) DEFAULT NULL,
  `MESSAGE` varchar(250) DEFAULT NULL,
  `DATE` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`DISCUSSION_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `discussion_form` */

/*Table structure for table `event` */

DROP TABLE IF EXISTS `event`;

CREATE TABLE `event` (
  `EVENT_ID` int(11) NOT NULL AUTO_INCREMENT,
  `EVENT_NAME` varchar(50) DEFAULT NULL,
  `EVENT_DEATILES` varchar(50) DEFAULT NULL,
  `EVENT_IMAGE` varchar(200) DEFAULT NULL,
  `EVENT_DATE` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`EVENT_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `event` */

insert  into `event`(`EVENT_ID`,`EVENT_NAME`,`EVENT_DEATILES`,`EVENT_IMAGE`,`EVENT_DATE`) values (3,'FRESHERS DAY','CELEBRATION CHILL','/static/IMAGE/230202-210026.jpg','2023-01-05'),(4,'rew','gfds','/static/IMAGE/230202-151428.jpg','2023-02-01'),(5,'DFDf','SDFGHGFDSA','/static/IMAGE/230203-201903.jpg','2023-02-10');

/*Table structure for table `leave` */

DROP TABLE IF EXISTS `leave`;

CREATE TABLE `leave` (
  `LEAVE_ID` int(11) NOT NULL AUTO_INCREMENT,
  `LEAVE_REASON` varchar(250) DEFAULT NULL,
  `TEACHER_ID` int(11) DEFAULT NULL,
  `REPLY` varchar(250) DEFAULT NULL,
  `REPLY_DATE` varchar(50) DEFAULT NULL,
  `DEPARTMENT_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`LEAVE_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `leave` */

insert  into `leave`(`LEAVE_ID`,`LEAVE_REASON`,`TEACHER_ID`,`REPLY`,`REPLY_DATE`,`DEPARTMENT_ID`) values (1,'sdf',14,'OK','2023-02-07',13);

/*Table structure for table `leave_student` */

DROP TABLE IF EXISTS `leave_student`;

CREATE TABLE `leave_student` (
  `LEAVE_ID` int(11) NOT NULL AUTO_INCREMENT,
  `STUDENT_ID` int(11) DEFAULT NULL,
  `DATE` varchar(50) DEFAULT NULL,
  `LEAVE_REASON` varchar(250) DEFAULT NULL,
  `REPLY` varchar(250) DEFAULT NULL,
  `REPLY_DATE` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`LEAVE_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `leave_student` */

insert  into `leave_student`(`LEAVE_ID`,`STUDENT_ID`,`DATE`,`LEAVE_REASON`,`REPLY`,`REPLY_DATE`) values (1,33,'432','GFDS','pending','pending'),(2,4,'yui','tyui','pending','pending'),(3,33,'2023-03-02','kk','pending','pending'),(4,33,'2023-03-02','df','pending','pending'),(5,33,'2023-03-02','ywk','pending','pending');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `LOGIN_ID` int(11) NOT NULL AUTO_INCREMENT,
  `USERNAME` varchar(250) DEFAULT NULL,
  `PASSWORD` varchar(250) DEFAULT NULL,
  `USERTYPE` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`LOGIN_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`LOGIN_ID`,`USERNAME`,`PASSWORD`,`USERTYPE`) values (1,'admin','admin','admin'),(32,'farzi','1111','teacher'),(33,'Akash','0000','student'),(34,'hjkl','7681','student'),(35,'OIUHGFCVBNM','6054','student'),(36,';LKJHGFDS','3364','teacher');

/*Table structure for table `mark` */

DROP TABLE IF EXISTS `mark`;

CREATE TABLE `mark` (
  `MARK_ID` int(11) NOT NULL AUTO_INCREMENT,
  `STUDENT_ID` int(11) DEFAULT NULL,
  `COURSE_ID` int(11) DEFAULT NULL,
  `SUBJECT_ID` int(11) DEFAULT NULL,
  `SCORE` int(11) DEFAULT NULL,
  `TOTAL` int(11) DEFAULT NULL,
  `GRADE` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`MARK_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `mark` */

insert  into `mark`(`MARK_ID`,`STUDENT_ID`,`COURSE_ID`,`SUBJECT_ID`,`SCORE`,`TOTAL`,`GRADE`) values (1,33,7,25,89,NULL,NULL),(2,33,7,26,78,NULL,NULL);

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `NOTIFICATION_ID` int(11) NOT NULL AUTO_INCREMENT,
  `NOTIFICATION_NAME` varchar(50) DEFAULT NULL,
  `NOTIFICATION_DEATILES` varchar(250) DEFAULT NULL,
  `NOTIFICATION_DATE` varchar(250) DEFAULT NULL,
  `USERTYPE` varchar(250) DEFAULT NULL,
  `RECIVER_TYPE` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`NOTIFICATION_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`NOTIFICATION_ID`,`NOTIFICATION_NAME`,`NOTIFICATION_DEATILES`,`NOTIFICATION_DATE`,`USERTYPE`,`RECIVER_TYPE`) values (8,'FAREWELL','NOTHING TO SAY','2023-01-31',NULL,NULL),(9,'hgfd','dfg','gfd','admin','BOTH'),(10,'tre','cvb','3456','teacher','STUDENT');

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `STUDENT_ID` int(11) NOT NULL AUTO_INCREMENT,
  `STUDENT_NAME` varchar(50) DEFAULT NULL,
  `DEPARTMENT_ID` int(11) DEFAULT NULL,
  `COURSE_ID` int(11) DEFAULT NULL,
  `REGISTER_NO` int(11) DEFAULT NULL,
  `DOB` varchar(50) DEFAULT NULL,
  `SEM` varchar(20) DEFAULT NULL,
  `BLOOD_GROUP` varchar(50) DEFAULT NULL,
  `PLACE` varchar(50) DEFAULT NULL,
  `POST` varchar(50) DEFAULT NULL,
  `PIN` varchar(50) DEFAULT NULL,
  `IMAGE` varchar(200) DEFAULT NULL,
  `EMAIL` varchar(200) DEFAULT NULL,
  `STATUS` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`STUDENT_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=latin1;

/*Data for the table `student` */

insert  into `student`(`STUDENT_ID`,`STUDENT_NAME`,`DEPARTMENT_ID`,`COURSE_ID`,`REGISTER_NO`,`DOB`,`SEM`,`BLOOD_GROUP`,`PLACE`,`POST`,`PIN`,`IMAGE`,`EMAIL`,`STATUS`) values (33,'AKASH',11,7,8956,'2023-12-3','SEMESTER 1','B','Q','E','675433','/static/IMAGE/230203-201903.jpg','akashask2012@gmail.com','APPROVED'),(34,'ghjk',13,9,789,'','SEMESTER 1','','','','','','hjkl','pending'),(35,'ASDFGHJK',13,9,789654,'','SEMESTER 1','','','','','','OIUHGFCVBNM','pending');

/*Table structure for table `study_material` */

DROP TABLE IF EXISTS `study_material`;

CREATE TABLE `study_material` (
  `MATERIAL_ID` int(11) NOT NULL AUTO_INCREMENT,
  `SUBJECT_ID` int(11) DEFAULT NULL,
  `DATE` varchar(50) DEFAULT NULL,
  `MATERIAL` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`MATERIAL_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `study_material` */

insert  into `study_material`(`MATERIAL_ID`,`SUBJECT_ID`,`DATE`,`MATERIAL`) values (1,25,'2023-03-02','/static/materials/230302-124825.pdf'),(2,25,'2023-03-02','/static/materials/230302-144916.pdf'),(3,25,'2023-03-02','C:UsersakashPycharmProjectsCOLLEGE AUTOMATIONstaticmaterials230302-145040.pdf'),(4,25,'2023-03-02','C:UsersakashPycharmProjectsCOLLEGE AUTOMATIONstaticmaterials230302-145049.pdf'),(5,25,'2023-03-02','static/materials/230302-145222.pdf'),(6,25,'2023-03-02','static/materials/230302-145231.pdf'),(7,25,'2023-03-02','static/materials/230302-145553.pdf'),(8,25,'2023-03-02','static/materials/230302-145600.pdf');

/*Table structure for table `subject` */

DROP TABLE IF EXISTS `subject`;

CREATE TABLE `subject` (
  `SUBJECT_ID` int(11) NOT NULL AUTO_INCREMENT,
  `SUBJECT_NAME` varchar(50) DEFAULT NULL,
  `COURSE_ID` varchar(50) DEFAULT NULL,
  `DEPARTMENT_ID` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`SUBJECT_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

/*Data for the table `subject` */

insert  into `subject`(`SUBJECT_ID`,`SUBJECT_NAME`,`COURSE_ID`,`DEPARTMENT_ID`) values (25,'PYTHON C','7','11'),(26,'CPP','8','12');

/*Table structure for table `teacher` */

DROP TABLE IF EXISTS `teacher`;

CREATE TABLE `teacher` (
  `TEACHER_ID` int(11) NOT NULL AUTO_INCREMENT,
  `DEPARTMENT_ID` int(11) DEFAULT NULL,
  `TEACHER_NAME` varchar(50) DEFAULT NULL,
  `DOB` varchar(50) DEFAULT NULL,
  `QUALIFICATION` varchar(50) DEFAULT NULL,
  `PLACE` varchar(50) DEFAULT NULL,
  `PIN` varchar(50) DEFAULT NULL,
  `POST` varchar(50) DEFAULT NULL,
  `IMAGE` varchar(200) DEFAULT NULL,
  `CONTACT` int(11) DEFAULT NULL,
  `EMAIL` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`TEACHER_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `teacher` */

insert  into `teacher`(`TEACHER_ID`,`DEPARTMENT_ID`,`TEACHER_NAME`,`DOB`,`QUALIFICATION`,`PLACE`,`PIN`,`POST`,`IMAGE`,`CONTACT`,`EMAIL`) values (14,14,'FARZEEN','2001-09-06','BCA','MATTOOL','670302','MATTOOL SOUTH','/static/IMAGE/230204-115204.jpg',2147483647,'farzi@gmail.com'),(15,14,'ASDFGHJK','','','','','','',0,';LKJHGFDS');

/*Table structure for table `timetable` */

DROP TABLE IF EXISTS `timetable`;

CREATE TABLE `timetable` (
  `TIMETABLE_ID` int(11) NOT NULL AUTO_INCREMENT,
  `DATE` varchar(50) DEFAULT NULL,
  `SUBJECT1` varchar(250) DEFAULT NULL,
  `SUBJECT2` varchar(250) DEFAULT NULL,
  `SUBJECT3` varchar(250) DEFAULT NULL,
  `SUBJECT4` varchar(250) DEFAULT NULL,
  `SUBJECT5` varchar(250) DEFAULT NULL,
  `DEPARTMENT_ID` int(50) DEFAULT NULL,
  `COURSE_ID` int(50) DEFAULT NULL,
  `SEM_ID` int(50) DEFAULT NULL,
  PRIMARY KEY (`TIMETABLE_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `timetable` */

insert  into `timetable`(`TIMETABLE_ID`,`DATE`,`SUBJECT1`,`SUBJECT2`,`SUBJECT3`,`SUBJECT4`,`SUBJECT5`,`DEPARTMENT_ID`,`COURSE_ID`,`SEM_ID`) values (2,'','25','25','25','25','25',11,7,0),(3,'','25','25','25','25','25',11,7,0),(4,'','25','25','25','25','25',13,7,0);

/*Table structure for table `tutor` */

DROP TABLE IF EXISTS `tutor`;

CREATE TABLE `tutor` (
  `TUTOR_ID` int(11) NOT NULL AUTO_INCREMENT,
  `TEACHER_ID` int(11) DEFAULT NULL,
  `COURSE_ID` int(11) DEFAULT NULL,
  `SEM` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`TUTOR_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `tutor` */

insert  into `tutor`(`TUTOR_ID`,`TEACHER_ID`,`COURSE_ID`,`SEM`) values (4,14,8,'SEMESTER 1');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
