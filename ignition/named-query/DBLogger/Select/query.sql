SELECT * FROM {table_name}
WHERE logger LIKE :logger
AND level_ LIKE :level
AND project LIKE :project
ORDER BY time_stamp DESC