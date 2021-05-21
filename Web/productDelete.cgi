#!/usr/bin/python3
import cgi
import psycopg2
import login

form = cgi.FieldStorage()
ean = form.getvalue('ean')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Supermarket</title>')
print('</head>')
print('<body>')

connection = None
try:
    if(ean is None):
        raise Exception("Invalid ean")
    if(int(ean)<0):
        raise Exception("Invalid ean")

        
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    sql = 'DELETE FROM product WHERE ean = %(ean)s'

    data = {'ean': int(ean)}

    sql_depend1 =  'DELETE FROM Planogram WHERE ean = %(ean)s'
    sql_depend2 =  'DELETE FROM Supplies_prim WHERE ean = %(ean)s'
    sql_depend3 =  'DELETE FROM Supplies_sec WHERE ean = %(ean)s'

    cursor.execute(sql_depend1, data)
    cursor.execute(sql_depend2, data)
    cursor.execute(sql_depend3, data)

    cursor.execute(sql, data)
    connection.commit()
    cursor.close()

    print('<h1>Success</h1>')
   

except Exception as e:
    
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format(e))

finally:
    if connection is not None:
        connection.close()

print('<p><a href="newProduct.cgi">Return to Categories</a></p>')

print('</body>')
print('</html>')
