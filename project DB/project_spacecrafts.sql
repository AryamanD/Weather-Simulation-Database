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
-- Table structure for table `spacecrafts`
--

DROP TABLE IF EXISTS `spacecrafts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `spacecrafts` (
  `code` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `class` varchar(20) NOT NULL,
  PRIMARY KEY (`code`),
  CONSTRAINT `spacecrafts_ibfk_1` FOREIGN KEY (`code`) REFERENCES `missions` (`code`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=201 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `spacecrafts`
--

LOCK TABLES `spacecrafts` WRITE;
/*!40000 ALTER TABLE `spacecrafts` DISABLE KEYS */;
INSERT INTO `spacecrafts` VALUES (101,'Apollo-12','Ion Rocket'),(102,'TARDIS','Plasma Rocket'),(103,'Elysium','Liquid Fuel'),(104,'SpaceX','Plasma Rocket'),(105,'SpaceCruiser','Solid Fuel Rocket'),(106,'SpaceX-2','Ion Rocket'),(107,'Mir','Plasma Rocket'),(108,'Reapers','Solid Fuel Rocket'),(109,'Lunar-II','Solid Fuel Rocket'),(110,'Souyuz','Solid Fuel Rocket'),(111,'Gemini','Solid Fuel Rocket'),(112,'Artemis','Ion Rocket'),(113,'XUS','Liquid Fuel Rocket'),(114,'SpaceCraft MIX','Liquid Fuel Rocket'),(115,'ISSIO','Liquid Fuel Rocket'),(116,'Path Finder','Ion Rocket'),(117,'Odyssey','Solid Fuel Rocket'),(118,'Dragon 2','Ion Rocket'),(199,'Giotto','Solid Fuel Rocket'),(200,'Colunbia','Liquid Fuel Rocket');
/*!40000 ALTER TABLE `spacecrafts` ENABLE KEYS */;
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
