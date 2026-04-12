#From this problem, I learned the structure of "function" in SQL.
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
#This statement is needed to avoid a syntax error in MySQL.
  DECLARE N1 INT;
  SET N1=N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT salary FROM Employee
      ORDER BY salary DESC
      LIMIT 1 OFFSET N1
  );
END