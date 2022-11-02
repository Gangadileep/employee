import mysql.connector

mydb = mysql.connector.connect(

    host = "localhost",

    user = "root",

    password = "",

    database = "aut"

)
mydb_Create_Table_Query = """CREATE TABLE employe
( emp_id numeric(10) not null,
  emp_name varchar(50) not null,
  emp_age varchar(50) not null,
  account  varchar(50) not null,
  position varchar(50) not null,
  CONSTRAINT employe_pk PRIMARY KEY (emp_id)
)"""



mydb_Create_Table_Query= """CREATE TABLE projects
( project_id numeric(10) not null,
  emp_id numeric(10) not null,
  project_name varchar(50) not null,
   CONSTRAINT fk_employe
    FOREIGN KEY (emp_id)
    REFERENCES employe(emp_id)
   )"""






cursor = mydb.cursor()

result = cursor.execute(mydb_Create_Table_Query)

print(" Table created successfully ")
