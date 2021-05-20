#!/usr/bin/python3
import psycopg2
import cgi
import login

form = cgi.FieldStorage()

ean = form.getvalue('ean')
descr = form.getvalue('descr')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Supermarket</title>')
print('</head>')
print('<body>')

connection = None
try:
    #To prevent running the query with null values
    if (descr is None) or (ean is None):
        raise Exception("No params read")

          
    if(int(ean)<0):
        raise Exception("Invalid ean")

    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    sql = 'UPDATE product SET descr = %(descr)s WHERE ean = %(ean)s;'

    data = {'descr': descr, 'ean': int(ean)}

    

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

print('<p><a href="products.cgi">Return to Products</a></p>')
print('</body>')
print('</html>')