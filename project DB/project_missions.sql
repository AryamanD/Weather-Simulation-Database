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
-- Table structure for table `missions`
--

DROP TABLE IF EXISTS `missions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `missions` (
  `m_id` int NOT NULL AUTO_INCREMENT,
  `m_name` varchar(20) NOT NULL,
  `m_type` varchar(20) NOT NULL,
  `launch_date` varchar(20) NOT NULL,
  `done_date` varchar(20) NOT NULL,
  `cost` int NOT NULL,
  `t_id` int NOT NULL,
  `s_id` int NOT NULL,
  `team_id` int NOT NULL,
  `code` int NOT NULL,
  PRIMARY KEY (`m_id`),
  UNIQUE KEY `s_id` (`s_id`),
  UNIQUE KEY `team_id` (`team_id`),
  UNIQUE KEY `code` (`code`),
  KEY `t_id` (`t_id`),
  CONSTRAINT `missions_ibfk_1` FOREIGN KEY (`t_id`) REFERENCES `temperatures` (`t_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `missions`
--

LOCK TABLES `missions` WRITE;
/*!40000 ALTER TABLE `missions` DISABLE KEYS */;
INSERT INTO `missions` VALUES (1,'Shuttle-Mir Program','Launch Satellite','01-01-5012','27-03-5013',50000,3,1,1,101),(2,'Dawn','Launch Satellite','03-02-5031','03-02-5041',43000,2,2,2,102),(3,'T-RES','Repair Satellite','01-04-5033','01-06-5033',40050,3,3,3,103),(4,'Galileo','Launch Satellite','01-05-5033','01-05-5034',39220,5,4,4,104),(5,'Apollo-3','Launch Satellite','20-04-5034','23-03-5035',23400,3,5,5,105),(6,'Pioneer-10','Launch Satellite','17-09-5033','23-08-5034',76000,4,6,6,106),(7,'Magellan','Dismantle Satellite','06-01-5036','09-08-5037',30000,6,7,7,107),(8,'LSAT-9','Launch Satellite','15-07-5036','13-06-5037',23900,3,8,8,108),(9,'Juno','Launch Satellite','09-10-5037','25-08-5038',20000,2,9,9,109),(10,'OSIRISS','Launch Satellite','09-07-5041','10-09-5042',20990,7,10,10,110),(11,'Viking Program','Launch Satellite','09-09-5043','10-09-5044',45000,3,11,11,111),(12,'Huygens','Launch Satellite','09-08-5044','11-08-5045',30200,4,12,12,112),(13,'Surveyor','Repair Satellite','14-05-5045','13-06-5046',50000,3,13,13,113),(14,'DIPWW','Dismantle Satellite','12-04-5046','10-09-5046',23990,1,14,14,114),(15,'Cassini','Launch Satellite','18-04-5048','19-08-5049',39002,5,15,15,115),(16,'Hubble Mission','Repair Satellite','22-07-5048','23-08-5049',40590,6,16,16,116),(17,'Apollo-13','Launch Satellite','16-04-5049','18-02-5050',34003,3,17,17,117),(18,'Voyager 2','Launch Satellite','24-09-5051','15-08-5052',23000,3,18,18,118),(19,'Horizon','Launch Satellite','17-09-5051','18-09-5052',50040,7,19,19,199),(20,'Mariner','Repair Satellite','20-03-5052','21-09-5053',30300,4,20,20,200);
/*!40000 ALTER TABLE `missions` ENABLE KEYS */;
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
