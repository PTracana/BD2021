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
	print('<tr><td>ean</td><td>descr</td><td>name</td><td></td></tr>')
	for row in result:
		print('<tr>')
		print('<td>', row[0], '</td><td>', row[1], '</td><td>', row[2], '</td><td>', '<a href="descrPoduct.cgi?ean={}">Change designation</a>'.format(row[0]),'</td>')
		print('</tr>')
	print('</table>')

	#Closing connection
	cursor.close()
	connection.close()

	print('<p>Connection closed.</p>')
	print('<p>Test completed successfully.</p>')
except Exception as e:
	print('<h1>An error occurred.</h1>')
	print('<p>', e, '</p>')

print('</body>')
print('</html>')
