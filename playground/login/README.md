# Simple Sign up and Log in Window

1. Create a database:

   ```sql
   CREATE DATABASE IT_Department;
   ```

2. Create a table:

   ```sql
   USE IT_Department;

   CREATE TABLE Employees
   (
       id       INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(255),
       password VARCHAR(255)
   );
   ```
