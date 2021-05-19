#!/usr/bin/python3
import cgi

form = cgi.FieldStorage()
ean = form.getvalue('ean')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Supermarket</title>')
print('</head>')
print('<body>')

print('<h3>Change designation for product {}</h3>'.format(ean))

print('<form action="updateProducts.cgi" method="post">')
print('<p><input type="hidden" name="ean" value="{}"/></p>'.format(ean))
print('<p>New designation: <input type="text" name="descr"/></p>')
print('<p><input type="submit" value="Submit"/></p>')
print('</form>')

print('</body>')
print('</html>')
