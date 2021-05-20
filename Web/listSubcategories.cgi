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
	sql = 'SELECT name FROM supercategory;'
	cursor.execute(sql)
	result = cursor.fetchall()
	num = len(result)

	# Displaying results
	print('<table border="3" cellspacing="3">')
	print('<tr><td><b>Name</b></td><td><b>Action</b></td></tr>')
	for row in result:
		print('<tr>')
		print('<td>', row[0],'</td><td>', '<a href="subCategories.cgi?name={}">List sub-categories</a>'.format(row[0]),'</td>')
		print('</tr>')
	print('</table>')

	#Closing connection
	cursor.close()
	connection.close()

except Exception as e:
	print('<h1>An error occurred.</h1>')
	print('<p>', e, '</p>')
finally:
    if connection is not None:
        connection.close()

print('<p><a href="frontPage.cgi">Return to Main Page</a></p>')
print('</body>')
print('</html>')