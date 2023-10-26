import psycopg2
conn= psycopg2.connect(dbname='python', user='postgres', password='postgres')

cur= conn.cursor()

contacts_dict ={
    "Father": '353452345',
    "Sister": '243234',

}

sql_command = "INSERT INTO Mynames VALUES"

for key, value in contacts_dict.items():
    sql_command +=f"('{key}', '{value}'),"

sql_command = sql_command[:-2] + ";"

# Execute a query
#cur.execute(f"INSERT INTO Myname VALUES('test2', '3243246245'), ('Test3', '22);")
# sql_command = SELECT * FROM Student
#print(sql_command)
cur.execute(sql_command)
conn.commit()
cur.close()
conn.close()

#Retrive query results
#records = cur.fetchal()
#print(records)
