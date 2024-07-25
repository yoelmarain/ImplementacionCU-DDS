import mysql.connector

conexion = mysql.connector.connect(user='root', password='celeste', host='localhost',
                                   database='diseño', port='3306')

# print(conexion)

cursor = conexion.cursor(buffered=True)

def cargarTarifas():
    categorias = ['baja', 'media', 'alta']
    frecuencias = ['bianual', 'anual', 'oblea de DNRPA']
    cont = 1

    for j in range(3):
        for k in range(3):
            add_tarifa = (f"INSERT INTO tarifas (id, categoria, frecuencia, tarifa) VALUES ({cont}, '{categorias[j]}', '{frecuencias[k]}', {(j+k+(j*k)+10)*1000});")
            cursor.execute(add_tarifa)
            cont += 1

    conexion.commit()

def cargarVehiculos():
    cont = 1
    cont2 = 1
    m_m = [['Alfa Romeo', 'Giulietta', 'MiTo'],['BMW', 'Serie 3', 'Serie 5', 'Serie 4'], ['Chevrolet', 'Cruze', 'Aveo', 'Trax', 'Orlando'], ['Citroen', 'C4', 'C3', 'C5', 'C3 Picasso', 'C4 Picasso', 'Grand C4 Picasso'], ['Ferrari', '488', 'GTC4', 'California']]

    for i in range(len(m_m)):
        for j in range(len(m_m[i])-1):
            add_vehiculo = (f"INSERT INTO vehiculo (id, marca, modelo, tarifa_id) VALUES ({cont}, '{m_m[i][0]}', '{m_m[i][j+1]}', {cont2});")
            cursor.execute(add_vehiculo)

            if cont2>=9:
                cont2 = 0

            cont2 += 1
            cont += 1

    conexion.commit()

def buscarTarifa():
    print("Buscando tarifas....")
    s_marca = input("Marca: ")
    s_modelo = input("Modelo: ")

    query = ("select v.marca,v.modelo,t.categoria,t.frecuencia,t.tarifa "
    "from tarifas t join vehiculo v on t.id=v.tarifa_id "
    f"where v.marca='{s_marca}' " 
    f"and v.modelo='{s_modelo}' ")

    cursor.execute(query)

    for (marca, modelo, categoria, frecuencia, tarifa) in cursor:
      print(f"{marca}, {modelo}, {categoria}, {frecuencia}, ${tarifa}")

def verTarifas():
    query_tarifas = ("SELECT categoria, frecuencia, tarifa FROM tarifas")

    cursor.execute(query_tarifas)

    print("Mostrando tarifas")
    print("Categoria, frecuencia, tarifa")
    for (categoria, frecuencia, tarifa) in cursor:
        print(f"{categoria} {frecuencia} {tarifa}")

def verVehiculos():
    query_vehiculo = ("SELECT modelo, marca FROM vehiculo")
    
    cursor.execute(query_vehiculo)

    print("Mostrando vehiculos")
    print("Marca, modelo")
    for (marca, modelo) in cursor:
      print(f"{marca}, {modelo}")


cargarTarifas()
cargarVehiculos()

verTarifas()
verVehiculos()

buscarTarifa()

cursor.close()
conexion.close()

