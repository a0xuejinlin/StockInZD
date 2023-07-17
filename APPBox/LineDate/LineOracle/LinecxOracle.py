import cx_Oracle

# 59.110.240.182

connection = cx_Oracle.connect('root', '12345WSXqaz!', '59.110.240.182/orcl')

cursor = connection.cursor()
cursor.execute('SELECT * FROM mytable')
results = cursor.fetchall()
for r in results:
    print(r)

cursor.close()
connection.close()