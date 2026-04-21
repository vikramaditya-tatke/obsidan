## On-demand Backups
- Tables can be backed-up on-demand and are retain until removed.
- Restore table with or without indexes.
- Encryption settings can be adjusted upon restore.
- Can be used to restore backups across regions and is a good option to migrate data across regions.

## PITR
- Point In Time recovery allows to record a stream of changes to the table over a 35 day window at 1 second granularity.
- Can be restored to a new table.
> Must be explicitly enabled on each table.

