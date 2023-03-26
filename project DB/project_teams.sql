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
-- Table structure for table `teams`
--

DROP TABLE IF EXISTS `teams`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teams` (
  `team_id` int NOT NULL AUTO_INCREMENT,
  `a_id1` int NOT NULL,
  `a_name1` varchar(20) NOT NULL,
  `a_id2` int NOT NULL,
  `a_name2` varchar(20) NOT NULL,
  `a_id3` int NOT NULL,
  `a_name3` varchar(20) NOT NULL,
  PRIMARY KEY (`team_id`),
  CONSTRAINT `teams_ibfk_1` FOREIGN KEY (`team_id`) REFERENCES `missions` (`team_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teams`
--

LOCK TABLES `teams` WRITE;
/*!40000 ALTER TABLE `teams` DISABLE KEYS */;
INSERT INTO `teams` VALUES (1,1,'Abhimanyu R',2,'Smithi Chauhan',3,'Harry Styles'),(2,4,'Sahil M',5,'Charlotte S',6,'Susan Jim'),(3,7,'Abhigna R',8,'Niall Horan',9,'Liam T'),(4,10,'Ranveer M',11,'Suhail Khan',12,'Theodora N '),(5,13,'Faizan F',14,'Hajira Z',15,'Deeksha G'),(6,16,'Bharath ',17,'Bhuvan K',18,'Susan'),(7,19,'Manoj H',20,'Shashi K',21,'Samanth'),(8,22,'Gabriel',23,'Natasha',24,'Tom Holland'),(9,25,'Hajira',26,'Sam ',27,'Harold'),(10,28,'Faisal ',29,'Nihan',30,'Charlie'),(11,31,'Maya Hart',32,'Riley Matthews',33,'Lucas J'),(12,34,'Henry',35,'Rupert',36,'Granger V'),(13,37,'Jerry',38,'Camilla',39,'Salvatore'),(14,40,'Henry',41,'Richard',42,'Williams'),(15,43,'Smith',44,'Abhay',45,'Kokila'),(16,46,'Kepler',47,'Jonathan',48,'Daniel'),(17,49,'Jhonny',50,'James',51,'Mark'),(18,52,'Hariet',53,'Morris',54,'Kirthi'),(19,55,'Kate',56,'Middleton',57,'Elizabeth'),(20,58,'Juliet',59,'Hagrid',60,'Vasanth');
/*!40000 ALTER TABLE `teams` ENABLE KEYS */;
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
