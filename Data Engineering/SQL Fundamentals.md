# Types of Joins in SQL

![[Excalidraw/System Design.md#^frame=oFEbaGxioWUfiiTcD2LGj]]

1. **Inner Join**: Only returns the matched records on a specific field from both the tables.
2. **Outer Join**: Returns all records from both the tables, insert `NULLs` where data is not present. Examples include *Left Join* and *Right Join* 
3. **Cross Join**: Retrns all possible combination of rows from both the tables. It amps every row on the left table to every row on the right table resulting in a cartesian product.
