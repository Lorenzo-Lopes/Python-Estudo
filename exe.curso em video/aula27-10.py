import sqlite3
conector = sqlite3.connect('academia.db')
cursor= conector.cursor()
sql = 'select * from cadastro'
cursor.execute(sql)
dados = cursor.fetchall()
cursor.close()
conector.close()
print('\n consulta banco')
print('dados da tabela')
print('-'*35)
print('{:7}{:20}{:>6}'.format("codigo","nome","idade"))
print('-'*35)
for d in dados:
    print('{:7} {:20}{:>6}'.format(d[0],d[1],d[2]))
print('-'*35)
print('encontrador {} registros'.format(len(dados)))
print('fim')
