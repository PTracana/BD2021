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
    #To prevent running the query with null values
    if (name is None):
        raise Exception("No params read")
  

    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()


    sql = 'SELECT name_descendant FROM consists_of WHERE name_super LIKE %(name)s;'

    data = {'name': name}

    cursor.execute(sql, data)
    result = cursor.fetchall()
    cursor.close()

    if (len(result)==0):
        raise Exception("No sub-category associated")

    # Displaying results
    print('<table border="3" cellspacing="1">')
    print('<tr><td><b>Name</b></td></tr>')
    for row in result:
        print('<tr>')
        print('<td>', row[0],'</td>')
        print('</tr>')
    print('</table>')
   

except Exception as e:
    
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format("No sub-category associated"))

finally:
    if connection is not None:
        connection.close()

print('<p><a href="listSubcategories.cgi">Return to List of Super-Categories</a></p>')

print('</body>')
print('</html>')