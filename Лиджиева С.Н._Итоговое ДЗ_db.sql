CREATE DATABASE IF NOT EXISTS db;
USE db;

CREATE TABLE Students (
    StudentID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    BirthDate DATE,
    ContactNumber VARCHAR(20),
    UNIQUE KEY unique_student (FirstName, LastName, BirthDate)
);

CREATE TABLE Teachers (
    TeacherID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    BirthDate DATE,
    ContactNumber VARCHAR(20),
    UNIQUE KEY unique_teacher (FirstName, LastName, BirthDate)
);

CREATE TABLE Subjects (
    SubjectID INT PRIMARY KEY AUTO_INCREMENT,
    SubjectName VARCHAR(50) NOT NULL,
    UNIQUE KEY unique_subject (SubjectName)
);

CREATE TABLE Courses (
    CourseID INT PRIMARY KEY AUTO_INCREMENT,
    CourseName VARCHAR(100) NOT NULL,
    SubjectID INT,
    TeacherID INT, 
    CourseDate DATE,
    FOREIGN KEY (SubjectID) REFERENCES Subjects(SubjectID),
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID), 
    UNIQUE KEY unique_course (CourseName, SubjectID)
);

CREATE TABLE Grades (
    GradeID INT PRIMARY KEY AUTO_INCREMENT,
    StudentID INT,
    CourseID INT,
    Grade INT CHECK (Grade BETWEEN 1 AND 5),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
    UNIQUE KEY unique_grade (StudentID, CourseID)
    );