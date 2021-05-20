#!/usr/bin/python3
import cgi
import psycopg2
import login

form = cgi.FieldStorage()
name = form.getvalue('name')
typeCat = form.getvalue('typeCat')
typeCatList = ["simplecategory","supercategory"]

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Supermarket</title>')
print('</head>')
print('<body>')

connection = None
try:
    #To prevent running the query with null values
    if (name is None) or (typeCat is None):
        raise Exception("No params read")

    typeCatInt = int(typeCat)
    if (typeCatInt<0) or (typeCatInt>1):
        raise Exception("Something is wrong")

    if(name.isspace()):
        raise Exception("Not valid name")


    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()


    sql = 'INSERT INTO category(name) VALUES (%(name)s); INSERT INTO {}(name) VALUES (%(name)s);'.format(typeCatList[typeCatInt])

    data = {'name': name}

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
