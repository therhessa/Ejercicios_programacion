import datetime
class Coche:
    def __init__( self, modelo, cilindrada, combustible, potencia, matricula, fecha, kilometros):
        self.modelo=modelo
        self.cilindrada=cilindrada
        self.combustible=combustible
        self.potencia=potencia
        self.matricula=matricula
        self.fecha=fecha
        self.kilometros=kilometros

    def __str__(self):
        return f"{self.modelo }, {self.cilindrada} ,{self.combustible}, {self.potencia } , {self.matricula} , {self.fecha} , {self.kilometros}"

class Marca:
    def __init__(self, marca,nacionalidad, coches):
        self.marca=marca
        self.nacionalidad=nacionalidad
        self.coches=coches
     
    def __str__(self):
        return  f"{self.marca }, {self.nacionalidad} ,{self.coches}"   
    
class Busqueda:
    def __init__(self,marca,modelo,combustible,min_potencia,max_potencia,min_ano):
        self.marca=marca
        self.modelo=modelo
        self.combustible=combustible
        self.min_potencia=min_potencia
        self.max_potencia=max_potencia
        self.min_ano=min_ano
    def __str__(self):
        return f"{self.marca},{self.modelo } ,{self.combustible}, {self.min_potencia } , {self.max_potencia}  , {self.min_ano}"
class Concesionario:
    def __init__(self, nombre,marcas):
        self.nombre= nombre
        self.marcas=marcas
        
    def __str__(self):
    
        return f"{self.nombre }, {self.marcas}"
"""
 no se como implementar la funcion busqueda
    def buscar(self,Busqueda):
        busqueda=() 
        return busqueda
         
"""         
      
if __name__ == "__main__":
    coches1 = [Coche("V40", 2.0, "Diesel", 120, "", datetime.date.today(), 0),
               Coche("S90", 2.0, "Diesel", 150, "", datetime.date.today(), 23435)]
    coches2 = [ Coche("A3", 1.0, "Gasolina", 115, "", datetime.date.today(), 1453),
                Coche("A4", 2.0, "Gasolina", 125, "", datetime.date.today(), 0) ]
    coches3 = [ Coche("Corolla", 1.5, "Híbrido", 115, "", datetime.date.today(), 7564),
                Coche("C-HR", 1.8, "Híbrido", 125, "", datetime.date.today(), 0) ]
    

    marcas = [ Marca("Volvo", "Suecia", coches1),
               Marca("Audi", "Alemania", coches2),
               Marca("Toyota", "Japón", coches3) ]
    
    concesionario = Concesionario("Rafael Multimotor", marcas)

    print(concesionario)
    print(concesionario)
    for coche in concesionario.buscar(Busqueda("","","",0,345,0)):
        for marca in concesionario.marcas:
            if coche in marca.coches:
                print(marca.marca, end=" ") 
        print(coche)


        
        
        