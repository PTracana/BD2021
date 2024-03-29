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
    #To prevent running the query with null values
    if (ean is None):
        raise Exception("No params read")
              
    if(int(ean)<0):
        raise Exception("Invalid ean")


    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()


    sql = 'SELECT * FROM replenishevent WHERE ean = %(ean)s;'

    data = {'ean': int(ean)}

    cursor.execute(sql, data)
    result = cursor.fetchall()
    cursor.close()

    if (len(result)==0):
        raise Exception("No event for given product")

    # Displaying results
    print('<table border="3" cellspacing="7">')
    print('<tr><td><b>UnitsRep</b></td><td><b>Instant</b></td><td><b>Side</b></td><td><b>Height</b></td><td><b>Nr</b></td><td><b>NIF</b></td><td><b>Ean</b></td></tr>')
    for row in result:
        print('<tr>')
        print('<td>', row[0], '</td><td>', row[1], '</td><td>', row[2], '</td><td>', row[3], '</td><td>', row[4], '</td><td>', row[5], '</td><td>', row[6], '</td>')
        print('</tr>')
    print('</table>')
   

except Exception as e:
    
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format("No event for given product"))

finally:
    if connection is not None:
        connection.close()

print('<p><a href="replenishEvent.cgi">Return to ReplenishEvent</a></p>')

print('</body>')
print('</html>')
