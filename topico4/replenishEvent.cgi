#!/usr/bin/python3
import psycopg2

import login

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Supermarket</title>')
print('</head>')
print('<body>')

connection = None
try:
    # Creating connection
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    # Making query
    sql = 'SELECT ean, descr, name FROM product;'
    cursor.execute(sql)
    result = cursor.fetchall()
    num = len(result)

    # Displaying results
    print('<table border="5" cellspacing="5">')
    print('<tr><td>ean</td><td>descr</td><td>name</td></tr>')
    for row in result:
        print('<tr>')
        print('<td>', row[0], '</td><td>', row[1], '</td><td>', row[2], '</td>')
        print('</tr>')
    print('</table>')

    #Closing connection
    cursor.close()
    connection.close()


    print('<form action="replenishList.cgi" method="post">')
    print('<p>Product ean: <input type="text" name="ean"/> <input type="submit" value="Submit"/> </p>')
    print('</form>')



except Exception as e:
    print('<h1>An error occurred.</h1>')
    print('<p>', e, '</p>')
finally:
    if connection is not None:
        connection.close()

print('<p><a href="frontPage.cgi">Return to Main Page</a></p>')
print('</body>')
print('</html>')
