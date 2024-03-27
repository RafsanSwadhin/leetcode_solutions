select distinct author_id as id
from views
where author_id = viewer_id
order by id

-- The `DISTINCT` keyword in SQL is used to ensure that the result set of a query contains only unique values for the specified column(s). In the provided SQL query, the `DISTINCT` keyword is used to ensure that only unique `author_id` values are returned from the `views` table.

-- Here's a breakdown of the query:

-- 1. `SELECT DISTINCT author_id AS id`: This selects unique values of the `author_id` column from the `views` table and renames it as `id`.
  
-- 2. `FROM views`: Specifies that the data is being selected from the `views` table.

-- 3. `WHERE author_id = viewer_id`: Filters the rows where the `author_id` is equal to the `viewer_id`.

-- 4. `ORDER BY id`: Orders the result set by the `id` column in ascending order.

-- So, the query retrieves distinct `author_id` values from the `views` table where `author_id` is equal to `viewer_id`, ensuring that each `author_id` appears only once in the result set.