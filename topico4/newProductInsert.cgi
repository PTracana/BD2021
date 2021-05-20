#!/usr/bin/python3
import cgi
import psycopg2
import login

form = cgi.FieldStorage()
ean = form.getvalue('ean')
descr = form.getvalue('descr')
name = form.getvalue('name')
nif_p = form.getvalue('nif_p')
date = form.getvalue('date')
nif_s = form.getvalue('nif_s')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Supermarket</title>')
print('</head>')
print('<body>')

connection = None
try:
    if (ean is None) or (descr is None) or (name is None) or ((nif_p is None or date is None) and (nif_s is None)):
        raise Exception("No params read")

    eanValue = int(ean)
    if (eanValue<0):
        raise Exception("Invalid Ean")

    if(name.isspace()):
        raise Exception("Invalid category")

    #To prevent a supplier from being secondary and primary at the same time
    if (nif_p == nif_s):
        raise Exception("Something is wrong")


    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()


    sql = 'INSERT INTO product(ean,descr,name) VALUES (%(ean)s,%(descr)s,%(name)s);'

    data = {'ean': eanValue,'descr': descr,'name': name}

    cursor.execute(sql, data)

    if(nif_p is not None and date is not None):
        sql = 'INSERT INTO supplies_prim(nif,ean,dia) VALUES (%(nif_p)s,%(ean)s,%(dia)s);'
        data = {'nif_p': nif_p,'ean': eanValue,'dia':date}
        cursor.execute(sql, data)

    if(nif_s is not None):
        sql = 'INSERT INTO supplies_sec(nif,ean) VALUES (%(nif_s)s,%(ean)s);'
        data = {'nif_s': nif_s,'ean': eanValue}
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

print('<p><a href="newProduct.cgi">Return to new Product</a></p>')

print('</body>')
print('</html>')
