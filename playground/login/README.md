# Simple Sign up and Log in System

1. Create a database first called `IT_Department`:

   ```sql
   CREATE DATABASE IT_Department;
   ```

2. Then create an `Employees` table:

   ```sql
   USE IT_Department;

   CREATE TABLE Employees
   (
       id       INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(255),
       password VARCHAR(255)
   );
   ```
