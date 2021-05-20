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
    sql = 'SELECT * FROM category;'
    cursor.execute(sql)
    result = cursor.fetchall()

    #Closing connection
    cursor.close()
    connection.close()

    num = len(result)

    # Displaying results
    print('<table border="1" cellspacing="2">')
    print('<tr><td>name</td><td>Action</td></tr>')
    for row in result:
        print('<tr>')
        print('<td>{}</td><td><a href="categoryDelete.cgi?name={}">Delete category</a></td>'.format(row[0],row[0]))
        print('</tr>')
    print('</table>')


    print('<form action="categoryInsert.cgi" method="post">')
    print('<p>Simple-Category name: <input type="text" name="name"/> <input type="submit" value="Submit"/> </p>')
    print('<p><input type="hidden" name="typeCat" value="{}"/></p>'.format(0))
    print('</form>')

    print('<form action="categoryInsert.cgi" method="post">')
    print('<p>Super-Category name: <input type="text" name="name"/> <input type="submit" value="Submit"/> </p>')
    print('<p><input type="hidden" name="typeCat" value="{}"/></p>'.format(1))
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