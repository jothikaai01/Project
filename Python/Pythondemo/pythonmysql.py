import mysql.connector
con=mysql.connector.connect(

    host="192.168.1.240",
    user="AIBATCH01",
    password="AI@123",
    database="j_jothika"
)

print(con)
result=con.cursor()
result.execute("select * from syst_info")
resultshow=result.fetchall()
for x in resultshow :
    print(x)