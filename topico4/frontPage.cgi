#!/usr/bin/python3

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Supermarket</title>')
print('</head>')
print('<body>')


# Displaying results
print('<table border="2" cellspacing="1">')
print('<tr><td>Options</td></tr>')

result = [("Insert/Remove categories and sub-categories","categories.cgi"),\
("Insert/Remove a new product and its respective suppliers",""),\
("List replenishment events","replenishEvent.cgi"),\
("Change designation of a product","products.cgi"),\
("List all the sub-categories of a super-category","listSubcategories.cgi")]

for row in result:
    print('<tr>')
    print('<td><a href="{}">{}</a></td>'.format(row[1],row[0]))
    print('</tr>')
print('</table>')
print('</body>')
print('</html>')

