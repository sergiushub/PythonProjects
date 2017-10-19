import sqlite3

def crear_bd():

    conexion = sqlite3.connect('restaurante.db')
    cursor = conexion.cursor()

    try:
        cursor.execute("CREATE TABLE categoria(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(100) UNIQUE NOT NULL)")
    except sqlite3.OperationalError:
        print("ERROR: Table 'CATEGORIA' already exist")

    try:
        cursor.execute("CREATE TABLE plato( id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(100) UNIQUE NOT NULL, categoria_id INTEGER NOT NULL, FOREIGN KEY(categoria_id) REFERENCES categoria(id))")
    except sqlite3.OperationalError:
        print("ERROR: Table 'PLATO' already exist")

    conexion.commit()
    conexion.close()

def agregar_categoria():
    conexion = sqlite3.connect('restaurante.db')
    cursor = conexion.cursor()

    nombre_categoria = input("Introduce el nombre de la categoria: ")

    try:
        cursor.execute("INSERT INTO categoria (nombre) VALUES (?)",(nombre_categoria,))
    except sqlite3.OperationalError:
        print("ERROR: Category '%s' already exist"%nombre_categoria)

    conexion.commit()
    conexion.close()

def agregar_plato():
    conexion = sqlite3.connect('restaurante.db')
    cursor = conexion.cursor()

    print("Selecciona una categoria: ");

    for i,row in enumerate(cursor.execute('SELECT * FROM categoria')):
        print("{0}) {1}".format(i+1,row[1]))
        category_dic[i]=row[1]

    input()

    category_dic.

    conexion.commit()
    conexion.close()

def menu():
	end = 0
	while(end==0):
		print("Elige opcion: ")
		print("1) Agregar Categoria")
		print("2) Salir")

		menuop = input()

		if menuop=='1':
			agregar_categoria()
		elif menuop=='2':
			end=1
		else:
			print("La opcion %s no es una opcion correcta")

agregar_plato()