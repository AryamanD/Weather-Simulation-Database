-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `satellites`
--

DROP TABLE IF EXISTS `satellites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `satellites` (
  `s_id` int NOT NULL AUTO_INCREMENT,
  `s_name` varchar(20) NOT NULL,
  `s_location` varchar(20) NOT NULL,
  PRIMARY KEY (`s_id`),
  CONSTRAINT `satellites_ibfk_1` FOREIGN KEY (`s_id`) REFERENCES `missions` (`s_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `satellites`
--

LOCK TABLES `satellites` WRITE;
/*!40000 ALTER TABLE `satellites` DISABLE KEYS */;
INSERT INTO `satellites` VALUES (1,'Sputnik 3','Bangalore'),(2,'Kalpana-4','Delhi'),(3,'Sputnik 3','Bangalore'),(4,'YouthSat','California'),(5,'RISAT-9','California'),(6,'SARAL','Boston'),(7,'IENSS-I','Hawaii'),(8,'Apollo-13','London'),(9,'Europa','Mexico'),(10,'HAMSAT','New Zealand'),(11,'RISAT-17','Los Angeles'),(12,'GSAT-151','Mississauga'),(13,'Aryabhatta','Berlington'),(14,'Explorer-01','Hyderabad'),(15,'GSAT-II','Montrael'),(16,'Astrosat','Berlin'),(17,'INSAT-1B','Ice-land'),(18,'INSAT-22','Greenland'),(19,'IRNSS-II','Toronto'),(20,'Carosat','New York');
/*!40000 ALTER TABLE `satellites` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-21 19:44:39
