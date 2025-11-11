class Persona :
    def __init__(self,Nombre,Edad,Altura,Peso):
        self.nombre = Nombre
        self.edad = Edad
        self.altura = Altura
        self.peso = Peso
        

    def imprimir(self):
            print(f"Nombre: {self.nombre}")
            print(f"Edad: {self.edad}")
            print(f"Altura: {self.altura}")
            print(f"Peso: {self.peso}")

persona1 = Persona("Juan", 30,6.2,222)
persona1.imprimir()
