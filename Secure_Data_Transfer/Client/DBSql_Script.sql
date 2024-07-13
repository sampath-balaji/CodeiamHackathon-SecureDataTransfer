CREATE DATABASE `HackathonCodeiam`;
USE `HackathonCodeiam`;
 

CREATE TABLE `ProblemStatements` (
  `SerialNumber` int NOT NULL AUTO_INCREMENT,
  `Issue` varchar(100) NOT NULL,
  `Rating` decimal(9,2) DEFAULT NULL,
  `Description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`SerialNumber`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='This table contains confidential data.';


INSERT INTO `ProblemStatements` (`Issue`, `Rating`, `Description`)
VALUES
('Network latency issues in remote locations', 4.5, 'Delays in network performance in rural areas.'),
('Frequent software crashes', 3.8, 'Unexpected crashes in the main application.'),
('Data inconsistency in the database', 4.0, 'Mismatch in user data across different tables.'),
('Security vulnerabilities in the application', 4.7, 'Potential exploits found in the authentication module.'),
('Poor user interface design', 3.5, 'Feedback indicates UI is not user-friendly.'),
('High memory usage in background processes', 4.2, 'Background processes consuming excessive memory.'),
('Inadequate error handling', 3.9, 'Errors are not handled gracefully leading to poor UX.'),
('Slow response times for API calls', 4.3, 'API calls taking longer than expected to respond.'),
('Lack of documentation for new features', 3.7, 'Insufficient documentation for newly added features.'),
('Compatibility issues with older hardware', 4.1, 'Software not functioning properly on older hardware.'),
('Frequent password reset requests', 3.6, 'Users are often required to reset their passwords.'),
('Inconsistent data backup schedules', 4.4, 'Data backups are not being performed consistently.'),
('Complexity in navigation', 3.8, 'Users find it difficult to navigate through the system.'),
('Limited support for internationalization', 4.0, 'Application lacks adequate support for multiple languages.'),
('Issues with session management', 4.5, 'Sessions are not managed properly, leading to unexpected logouts.');
