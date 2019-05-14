import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(host='localhost',
                                    database='simplon',
                                    user='admin',
                                    password='password')
    if conn.is_connected():
        print('Connected to MySQL database')

except Error as e:
    print(e)

curr = conn.cursor()
curr.execute("select last_name from promo10")
list_name = []
list_name = curr.fetchall()
prenom = []
for i in list_name:
    prenom.append(str(i).replace(",","").replace("('","").replace("')","").lower())

curr.execute("select first_name from promo10")
list_fname = []
list_fname = curr.fetchall()
nom = []
for i in list_fname:
    nom.append(str(i).replace(",","").replace("('","").replace("')",""))




