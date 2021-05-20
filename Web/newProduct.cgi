#!/usr/bin/python3
import psycopg2

import login

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Supermarket</title>')
print('</head>')
print('<body>')
print('<div style="flex:1;  display:flex;  flex-direction:row;">')

connection = None
try:
    #----------------------------------------FIRST TABLE _ PRODUCTS-----------------------------------------
    # Creating connection
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    # Making query
    sql = 'SELECT * FROM product;'
    cursor.execute(sql)
    result = cursor.fetchall()

    #Closing connection
    cursor.close()
    connection.close()

    num = len(result)

    print('<div style="width: 30%; float:left">')
    print('<h3>Product table</h3>')
    # Displaying results
    print('<table border="5" cellspacing="5">')
    print('<tr><td><b>Ean</b></td><td><b>Descr</b></td><td><b>Name</b></td><td><b>Action</b></td></tr>')
    for row in result:
        print('<tr>')
        print('<td>', row[0], '</td><td>', row[1], '</td><td>', row[2], '</td><td>', '<a href="productDelete.cgi?ean={}">Delete product</a>'.format(row[0]),'</td>')
        print('</tr>')
    print('</table>')
    print('</div>')
    #----------------------------------------SECOND TABLE _ SUPPLIERS-----------------------------------------
    # Creating connection
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    # Making query
    sql = 'SELECT * FROM supplier;'
    cursor.execute(sql)
    result = cursor.fetchall()

    #Closing connection
    cursor.close()
    connection.close()

    num = len(result)

    print('<div style="padding-left:10px; width: 20%; float:left">')
    print('<h3>Supplier table</h3>')
    # Displaying results
    print('<table border="2" cellspacing="3" style="width:100%;">')
    print('<tr><td><b>nif</b></td><td><b>Supplier name </b></td></tr>')
    for row in result:
        print('<tr>')
        print('<td>', row[0], '</td><td>', row[1], '</td>')
        print('</tr>')
    print('</table>')
    print('</div>')

        #----------------------------------------THIRD TABLE _ CATEGORIES-----------------------------------------
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

    print('<div style="padding-left:10px; width: 30%; float:left">')
    print('<h3>Categories table</h3>')
    # Displaying results
    print('<table border="1" cellspacing="2">')
    print('<tr><td><b>name</b></td></tr>')
    for row in result:
        print('<tr>')
        print('<td>', row[0], '</td>')
        print('</tr>')
    print('</table>')
    print('</div>')

    print('</div>') #closes outside div

    print('<div>')
    print('<form action="newProductInsert.cgi" method="post">')
    print('<p>Product ean: <input type="number" name="ean"/></p>')
    print('<p>Product designation: <input type="text" name="descr"/></p>')
    print('<p>Product category: <input type="text" name="name"/></p>')
    print('<p>Primary supllier NIF: <input type="number" name="nif_p"/></p>')
    print('<p>Primary supllier date: <input type="date" name="date"/></p>')
    print('<p>Secondary supllier NIF: <input type="number" name="nif_s"/></p>')
    print('<p><input type="submit" value="Submit"/></p>')
    print('</form>')
    print('</div>')


except Exception as e:
    print('</div>') # outside div
    print('<h1>An error occurred.</h1>')
    print('<p>', e, '</p>')
finally:
    if connection is not None:
        connection.close()

print('<p><a href="frontPage.cgi">Return to Main Page</a></p>')
print('</body>')
print('</html>')