# Slowly Changing Dimensions

## SCD Type 1
- Used when only the *current state* of the data is of interest.
- Upserts - the existing record is updated or overwritten.
- Ensures there are no duplicates.
### Implementation
```sql
MERGE INTO final_table USING staging_table
	ON final_table.id = staging_table.id
	WHEN MATCHED THEN UPDATE SET 
		final_field_1 = staging_field_1
		final_field_2 = staging_field_2
		final_field_3 = staging_field_3
	WHEN NOT MATCHED THEN INSERT (
		field_1,
		field_2,
		field_3
	) VALUES (
		value_1,
		value_2,
		value_3
	)
```
## SCD Type 2
- *Change history* is essential.
- Implemented using boolean flags to say whether a record is current or not.
- Using start and end dates.
### Implementation
```sql

```
## SCD Type 3
- Only the latest historical data (*previous record*) is required.
- NULL values are stored in the another column that is related to a column that we expect to be updated.
- Example - `current_address` vs `previous_address`
### Implementation
```sql

```
## SCD Type 4
- *Change history is stored in a different table*, while the current record is stored in a dimension table.
### Implementation
```sql

```
## SCD Type 0
- Dimensions *never* change.