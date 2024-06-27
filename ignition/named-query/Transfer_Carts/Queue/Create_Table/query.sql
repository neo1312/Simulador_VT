
CREATE TABLE VT_TC_TRANSFERS(
   Id INTEGER PRIMARY KEY   AUTOINCREMENT,
   SOURCE varchar(250),
   DESTINATION varchar(250),
   SOURCE_IS_AUTO bit,
   DEST_IS_AUTO bit,
   SOURCE_X int,
   DESTINATION_X int,
   DESTINATION_Y int,
   SOURCE_Y int,
   S_PATH varchar(250),
   D_PATH varchar(250),
   TimeStamp TimeStamp
);