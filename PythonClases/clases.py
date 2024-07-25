class Tarifa():
    def __init__(self, id, categoria, frecuencia, tarifa):
        self.id = id
        self.categoria = categoria
        self.frecuencia = frecuencia
        self.tarifa = tarifa

    def __str__(self):
        return (f"{self.categoria}, {self.frecuencia}, ${self.tarifa}")
    

class Vehiculo():
    def __init__(self, id, marca, modelo, tarifa_id) -> None:
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.antiguedad = 0
        self.tipo = ''
        self.estado = ''
        self.tarifa_id = tarifa_id

    def __str__(self):
        return (f"{self.marca}, {self.modelo}")


class RTO():
    def __init__(self) -> None:
        self.vehiculos = []
        self.tarifas = []
        self.cargarTarifas()
        self.cargarVehiculos()
        self.menu()

    def buscarTarifa(self):
        print("Buscando tarifas....*utilice mayusculas y minusculas*")
        s_marca = input("Marca: ")
        s_modelo = input("Modelo: ")
        resultado = []

        for vehiculo in self.vehiculos:
            if vehiculo.marca == s_marca and vehiculo.modelo == s_modelo:
                resultado = [vehiculo]
        
        if resultado != []:
            for tarifa in self.tarifas:
                if tarifa.id == resultado[0].tarifa_id:
                    resultado.append(tarifa)

        if resultado == []:
            print("No se hallaron resultados para esa marca y modelo")
        else: 
            print("--------------------------------")
            print(f"Vehiculo: {resultado[0]}")
            print(f"Tarifa: {resultado[1]}")
            print("--------------------------------")

    def cargarTarifas(self):
        categorias = ['baja', 'media', 'alta']
        frecuencias = ['bianual', 'anual', 'oblea de DNRPA']
        cont = 1

        for j in range(3):
            for k in range(3):
                new_tarifa = Tarifa(cont, categorias[j], frecuencias[k], (j+k+(j*k)+10)*1000)
                self.tarifas.append(new_tarifa)
                cont += 1

    def cargarVehiculos(self):
        cont = 1
        cont2 = 1
        m_m = [['Alfa Romeo', 'Giulietta', 'MiTo'],['BMW', 'Serie 3', 'Serie 5', 'Serie 4'], ['Chevrolet', 'Cruze', 'Aveo', 'Trax', 'Orlando'], ['Citroen', 'C4', 'C3', 'C5', 'C3 Picasso', 'C4 Picasso', 'Grand C4 Picasso'], ['Ferrari', '488', 'GTC4', 'California']]

        for i in range(len(m_m)):
            for j in range(len(m_m[i])-1):
                new_vehiculo = Vehiculo(cont, m_m[i][0], m_m[i][j+1], cont2)
                self.vehiculos.append(new_vehiculo)

                if cont2>=9:
                    cont2 = 0

                cont2 += 1
                cont += 1

    def verTarifas(self):

        print("Mostrando tarifas")
        print("Categoria, frecuencia, tarifa")
        for tarifa in self.tarifas:
            print(tarifa)

    def verVehiculos(self):

        print("Mostrando vehiculos")
        print("Marca, modelo")
        for vehiculo in self.vehiculos:
            print(vehiculo)

    def menu(self):
        rta = 0

        while rta != 5:
            print("++++++++++++++++++++++++++")
            print("+   Bienvenido a RTO     +")
            print("++++++++++++++++++++++++++")
            print("1. Buscar tarifa")
            print("2. Ver todas las tarifas (no implementada)")
            print("3. Ver tarifas")
            print("4. Ver vehiculos")
            print("5. Salir")
            rta = int(input("Elija un número: "))

            if rta==1:
                self.buscarTarifa()
            elif rta==2:
                pass
            elif rta==3:
                self.verTarifas()
            elif rta==4:
                self.verVehiculos()


rto = RTO()
