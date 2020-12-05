-- MySQL dump 10.13  Distrib 8.0.22, for macos10.15 (x86_64)
--
-- Host: 35.232.86.37    Database: wetBat
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.15-MariaDB-1:10.4.15+maria~stretch

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `airport`
--

DROP TABLE IF EXISTS `airport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `airport` (
  `Id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `airport` varchar(100) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `airport`
--

LOCK TABLES `airport` WRITE;
/*!40000 ALTER TABLE `airport` DISABLE KEYS */;
INSERT INTO `airport` VALUES (1,'Calgary'),(2,'Edmonton'),(3,'Fort Mac'),(4,'Regina'),(5,'Montreal'),(6,'Ottawa'),(7,'Red Deer'),(8,'Halifax'),(9,'Thunderbay'),(10,'Saskatoon'),(11,'Vancouver'),(12,'Victoria'),(13,'Whitehorse'),(14,'Winnipeg'),(15,'YellowKnife');
/*!40000 ALTER TABLE `airport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quotes`
--

DROP TABLE IF EXISTS `quotes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quotes` (
  `Id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `departure` date NOT NULL,
  `arrival` date NOT NULL,
  `destination` varchar(100) NOT NULL,
  `travellers` int(10) unsigned NOT NULL,
  `transportation` varchar(100) NOT NULL,
  `name` varchar(150) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phoneNumber` text NOT NULL,
  `finalprice` int(10) unsigned NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quotes`
--

LOCK TABLES `quotes` WRITE;
/*!40000 ALTER TABLE `quotes` DISABLE KEYS */;
INSERT INTO `quotes` VALUES (1,'2020-12-01','2020-12-09','Toronto',4,'Enterprise','John abbot','test123@gmail.com','444555543',3445),(3,'2020-12-01','2020-12-09','Toronto',4,'Enterprise','John abbot','test123@gmail.com','444555543',3445),(4,'2020-12-01','2020-12-09','Toronto',4,'Enterprise','John abbot','test123@gmail.com','444555543',3445),(5,'2020-12-01','2020-12-09','Toronto',4,'Enterprise','John abbot','test123@gmail.com','444555543',3445),(6,'2020-12-01','2020-12-09','Toronto',4,'Enterprise','John abbot','test123@gmail.com','444555543',3445),(7,'2020-12-10','2020-12-11','Montreal',3,'Hertz','Bilal Abdurahman','billa.abdu@gmail.com','4036902348',4534),(8,'2020-12-05','2020-12-17','Ottawa',4,'Hertz','Bilal Abdurahman','billa.abdu@gmail.com','4036902348',4354),(9,'2020-12-19','2020-12-30','Red Deer',3,'Avis','Billy Bob','test23@gmail.com','403-696-4221',4555);
/*!40000 ALTER TABLE `quotes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transportation`
--

DROP TABLE IF EXISTS `transportation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transportation` (
  `Id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `company` varchar(100) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transportation`
--

LOCK TABLES `transportation` WRITE;
/*!40000 ALTER TABLE `transportation` DISABLE KEYS */;
INSERT INTO `transportation` VALUES (1,'Enterprise'),(2,'National'),(3,'Alamo'),(4,'Hertz'),(5,'Avis'),(6,'Budget'),(7,'Dollar'),(8,'Thrifty');
/*!40000 ALTER TABLE `transportation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'wetBat'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-05 16:39:43
