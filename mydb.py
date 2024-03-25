import mysql.connector 

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'G4rf13ld!'
)

# prepare a cursor object 
cursorObject = dataBase.cursor()

# Create a database 
cursorObject.execute("CREATE DATABASE lukman_db")

print ("All DONE!")