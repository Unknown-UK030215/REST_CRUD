-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: enrollment
-- ------------------------------------------------------
-- Server version	5.7.44-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `middle_initial` char(1) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `postal_code` varchar(20) DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `registration_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'mark123','b79ea17b7c5ca8fe9cccd8cdba6e8f8ed0b3c948f9f709ed0f47d2fd47fcba82','giovanni@gmail.com','John','E','Ishikawa','2003-02-15','brgy. tiniguiban','Puerto Prinsesa City','Phillippines','5300','09451281802','2024-05-26 01:23:02'),(2,'yukikawa','15e2b0d3c33891ebb0f1ef609ec419420c20e320ce94c65fbc8c3312448eb225','vince@gmail.com','Mark Vincent','E','Santos','2003-12-02','brgy. tiniguiban','Puerto Prinsesa City','Phillippines','5300','09451281802','2024-05-26 09:53:29'),(3,'dulce','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92','dulce@gmail.com','Dulce','E','Santos','2005-02-20','Brgy. Maligaya','Puerto Prinsesa City','Phillippines','5300','09934748324','2024-05-26 10:43:35'),(4,'rodri','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92','lanuza@gmail.com','Rodrigo','M','Lanuza','1998-05-15','Brgy. San Jose','Puerto Prinsesa City','Phillippines','5300','09453423568','2024-05-26 10:44:49'),(5,'Junnie','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92','jun@gmail.com','Junnie','D','Boy','2001-03-31','Brgy. San Manuel','Puerto Prinsesa City','Phillippines','5300','09452387671','2024-05-26 10:46:49'),(6,'Henry','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92','henry@gmail.com','Henry','M','San Jose','2003-09-24','Brgy. Manalo','Manila','Phillippines','1000','09125426843','2024-05-26 10:48:13'),(7,'Giovanni','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92','gov@gmail.com','Giana','D','Giovanni','2004-05-08','Brgy. San Manuel','Puerto Prinsesa City','Phillippines','5300','0918645238','2024-05-26 10:49:35'),(8,'Kenji','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92','ishikawa@gmail.com','Kenji','J','Ishikawa','2005-04-05','Brgy. Maligaya','El nido','Phillippines','5300','0945852524','2024-05-26 10:50:38'),(9,'Xyril','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92','nalica@gmail.com','Xyril','T','Nalica','1995-02-21','Brgy. Iwanan','Manila','Phillippines','1000','09674532657','2024-05-26 10:51:52'),(10,'andrew','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92','delacruz@gmail.com','Andrew','C','Dreo','2012-05-08','Brgy. Maligaya','El nido','Phillippines','5300','09452368125','2024-05-26 10:55:01'),(11,'Michael','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92','mike@gmail.com','Michael','U','Ulanday','1994-05-06','Brgy. Walang Awa','Manila','Phillippines','5300','09452387169','2024-05-26 10:56:07'),(12,'joshua','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92','josh@gmail.com','Joshua','L','Dela Torre','1999-03-07','Brgy. San Manuel','Puerto Prinsesa City','Phillippines','5300','09234556789','2024-05-26 10:57:37'),(13,'amor','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92','amor123@gmail.com','Dulce Amor','E','Santos','2006-05-20','Brgy. San Jose','Puerto Prinsesa City','Phillippines','5300','09458723515','2024-05-26 10:58:46'),(14,'May','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92','gianamay@gmail.com','Giana May Cherish','D','Juanzo','2004-05-08','Brgy. Pretty','Puerto Prinsesa City','Phillippines','5300','09458732546','2024-05-26 11:00:18'),(15,'yuki123','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92','yukikawa@gmail.com','yuki','D','Ishikawa','2003-02-15','Brgy. Maligaya','El nido','Phillippines','5300','09451281802','2024-05-26 11:01:09'),(16,'John','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92','john@gmail.com','John','L','Relova','2004-12-06','Brgy. Iwanan','Puerto Prinsesa City','Phillippines','5300','09865482153','2024-05-26 11:02:22'),(17,'Franz','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92','chang@gmail.com','Franz','N','Chang','2004-03-16','Brgy. Manlalic','El nido','Phillippines','5300','09861462348','2024-05-26 11:03:36'),(18,'kanzaki','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92','kanzaki@gmail.com','Kanzaki','T','Kenzawa','2002-02-05','Brgy. San Manuel','Puerto Prinsesa City','Phillippines','5300','09865231548','2024-05-26 11:05:12'),(19,'Yawa','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92','yawa@gmail.com','Yawazaki','D','Denjiro','2010-02-06','Brgy. San Manuel','Puerto Prinsesa City','Phillippines','5300','0965113548','2024-05-26 11:06:06'),(20,'denji','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92','denji@gmail.com','Denji','K','Yamazaki','2001-04-07','Brgy. Iwanan','Puerto Prinsesa City','Phillippines','5300','09668547312','2024-05-26 11:07:46'),(21,'Franzine','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92','franzine@gmail.com','Princess Franzine','J','Diaz','2006-02-08','Brgy. San Jose','Puerto Prinsesa City','Phillippines','5300','09786543215','2024-05-26 11:09:47');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-26 19:11:54
