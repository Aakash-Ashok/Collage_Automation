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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `attendence` */

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `course` */

/*Table structure for table `department` */

DROP TABLE IF EXISTS `department`;

CREATE TABLE `department` (
  `DEPARTMENT_ID` int(11) NOT NULL AUTO_INCREMENT,
  `DEPARTMENT_NAME` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`DEPARTMENT_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `department` */

insert  into `department`(`DEPARTMENT_ID`,`DEPARTMENT_NAME`) values (1,'cs');

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `event` */

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

insert  into `leave`(`LEAVE_ID`,`LEAVE_REASON`,`TEACHER_ID`,`REPLY`,`REPLY_DATE`,`DEPARTMENT_ID`) values (1,'d',1,'pending','4',NULL);

/*Table structure for table `leave_student` */

DROP TABLE IF EXISTS `leave_student`;

CREATE TABLE `leave_student` (
  `LEAVE_ID` int(11) NOT NULL AUTO_INCREMENT,
  `STUDENT_ID` int(11) DEFAULT NULL,
  `DATE` varchar(50) DEFAULT NULL,
  `LEAVE_REASON` varchar(250) DEFAULT NULL,
  `REPLY` varchar(250) DEFAULT NULL,
  `REPLY-DATE` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`LEAVE_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `leave_student` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `LOGIN_ID` int(11) NOT NULL,
  `USERNAME` varchar(50) DEFAULT NULL,
  `PASSWORD` varchar(50) DEFAULT NULL,
  `USERTYPE` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`LOGIN_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`LOGIN_ID`,`USERNAME`,`PASSWORD`,`USERTYPE`) values (1,'admin','admin','admin');

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `mark` */

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `NOTIFICATION_ID` int(11) NOT NULL AUTO_INCREMENT,
  `NOTIFICATION_NAME` varchar(50) DEFAULT NULL,
  `NOTIFICATION_DEATILES` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`NOTIFICATION_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `STUDENT_ID` int(11) NOT NULL AUTO_INCREMENT,
  `STUDENT_NAME` varchar(50) DEFAULT NULL,
  `DEPARTMENT_ID` int(11) DEFAULT NULL,
  `COURSE_ID` int(11) DEFAULT NULL,
  `REGISTER_NO` int(11) DEFAULT NULL,
  `DOB` varchar(50) DEFAULT NULL,
  `SEM` int(11) DEFAULT NULL,
  `BLOOD_GROUP` varchar(50) DEFAULT NULL,
  `PLACE` varchar(50) DEFAULT NULL,
  `POST` varchar(50) DEFAULT NULL,
  `PIN` int(11) DEFAULT NULL,
  `IMAGE` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`STUDENT_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `student` */

insert  into `student`(`STUDENT_ID`,`STUDENT_NAME`,`DEPARTMENT_ID`,`COURSE_ID`,`REGISTER_NO`,`DOB`,`SEM`,`BLOOD_GROUP`,`PLACE`,`POST`,`PIN`,`IMAGE`) values (1,'A',1,1,8,'12',3,'E','S','SD',0,'SD');

/*Table structure for table `study_material` */

DROP TABLE IF EXISTS `study_material`;

CREATE TABLE `study_material` (
  `MATERIAL_ID` int(11) DEFAULT NULL,
  `SUBJECT-ID` int(11) DEFAULT NULL,
  `DATE` varchar(50) DEFAULT NULL,
  `MATERIAL` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `study_material` */

/*Table structure for table `subject` */

DROP TABLE IF EXISTS `subject`;

CREATE TABLE `subject` (
  `SUBJECT_ID` int(11) NOT NULL AUTO_INCREMENT,
  `SUBJECT_NAME` varchar(50) DEFAULT NULL,
  `COURSE_ID` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`SUBJECT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `subject` */

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
  PRIMARY KEY (`TEACHER_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `teacher` */

insert  into `teacher`(`TEACHER_ID`,`DEPARTMENT_ID`,`TEACHER_NAME`,`DOB`,`QUALIFICATION`,`PLACE`,`PIN`,`POST`,`IMAGE`,`CONTACT`) values (1,1,'a','5','s','f','8','b','h',7);

/*Table structure for table `timetable` */

DROP TABLE IF EXISTS `timetable`;

CREATE TABLE `timetable` (
  `TIMETABLE_ID` int(11) NOT NULL AUTO_INCREMENT,
  `DATE` varchar(50) DEFAULT NULL,
  `SUBJECT_ID` int(11) DEFAULT NULL,
  `TIMETABLE` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`TIMETABLE_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `timetable` */

/*Table structure for table `tutor` */

DROP TABLE IF EXISTS `tutor`;

CREATE TABLE `tutor` (
  `TUTOR_ID` int(11) NOT NULL AUTO_INCREMENT,
  `TEACHER_ID` int(11) DEFAULT NULL,
  `COURSE_ID` int(11) DEFAULT NULL,
  `SEM` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`TUTOR_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `tutor` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
