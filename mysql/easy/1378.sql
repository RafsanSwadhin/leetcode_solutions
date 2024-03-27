select eu.unique_id , e.name 
from employees e
left join EmployeeUNI eu
on e.id = eu.id

-- This SQL query retrieves data from two tables, `employees` and `EmployeeUNI`, using a left join operation. Here's a breakdown of the query:

-- 1. **SELECT Statement**:
--    - `eu.unique_id, e.name`: Specifies the columns to be selected in the result set. `eu.unique_id` refers to the unique identifier column from the `EmployeeUNI` table, and `e.name` refers to the name column from the `employees` table.

-- 2. **FROM Clause**:
--    - `employees e`: Specifies the table from which to retrieve data. `e` is an alias for the `employees` table, allowing us to reference it using a shorter name in the query.
   
-- 3. **LEFT JOIN Clause**:
--    - `LEFT JOIN EmployeeUNI eu`: Performs a left join between the `employees` table (`e`) and the `EmployeeUNI` table (`eu`). A left join returns all records from the left table (`employees`) and the matching records from the right table (`EmployeeUNI`). If there is no match in the right table, NULL values are returned.
   
-- 4. **ON Clause**:
--    - `ON e.id = eu.id`: Specifies the join condition. It indicates that the join should be performed based on the `id` column in both tables. This condition links rows from the `employees` table to corresponding rows in the `EmployeeUNI` table based on their `id` values.

-- In summary, the query retrieves the unique identifier (`unique_id`) from the `EmployeeUNI` table and the name (`name`) from the `employees` table, where there is a match based on the `id` column between the two tables. If there is no match in the `EmployeeUNI` table, NULL values will be returned for the `unique_id` column.