#!/usr/bin/python3
import cgi
import psycopg2
import login

form = cgi.FieldStorage()
name = form.getvalue('name')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Supermarket</title>')
print('</head>')
print('<body>')

connection = None
try:
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()


    


    sql = 'DELETE FROM category WHERE name LIKE %(name)s'

    data = {'name': name}

    
    sql_depend1 = 'DELETE FROM product WHERE name LIKE %(name)s'
    sql_depend2 = 'DELETE FROM simplecategory WHERE name LIKE %(name)s'
    sql_depend3 = 'DELETE FROM supercategory WHERE name LIKE %(name)s'
    sql_depend4 = 'DELETE FROM consist_of WHERE name LIKE %(name)s'
    sql_depend5 = 'DELETE FROM Displayed_in WHERE name LIKE %(name)s'

    cursor.execute(sql_depend1, data)
    cursor.execute(sql_depend2, data)
    cursor.execute(sql_depend3, data)
    cursor.execute(sql_depend4, data)
    cursor.execute(sql_depend5, data)

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

print('<p><a href="categories.cgi">Return to Categories</a></p>')

print('</body>')
print('</html>')
