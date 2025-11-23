
print("*Primer ejercicio* \n ========================================")


class usuario:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def mostar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

user = usuario("Sonry", 29)
user.mostar()       


print("\n *Segundo ejercicio* \n ========================================")

class Rectangulo:
     
     def __init__(self, base,altura):
         self.base = base
         self.altura = altura

     def Calcular_area(self):
        return self.base * self.altura
     
are = Rectangulo(15,10)
print("El area del rectangulo es: ", are.Calcular_area())

print("\n *Tercer ejercicio* \n ========================================")

class Carro:
    def __init__(self, marca, velocidad):
        self.marca = marca
        self.velocidad = velocidad

    def acelerar(self,cantidad):
      self.velocidad += cantidad

      print(f"velocidad aumentada.  Nueva velocidad: {self.velocidad} Km/h")


car = Carro("honda", 30)
car.acelerar(20)

print("\n *Cuarto ejercicio* \n ========================================")

class CuentaBancaria:
     def __init__(self,titular,balance):
         self.titular = titular
         self.balance = balance

     def depositar(self, deposito):
    
        self.balance += deposito
        print(f"Deposito exitoso su nuevo balance es: {self.balance}")

     def retirar(self,retiro):
         self.balance -= retiro
         print(f"Retiro exitoso su nuevo balance es: {self.balance}")

         
             

cuenta = CuentaBancaria("Sonry ",4000)
cuenta.depositar(30)
cuenta.retirar(10)


print("\n *Quinto ejercicio* \n ========================================")  

class Estudiante:
    def __init__(self,nombre,calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones

    def Promedio(self):
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)
    
alumno = Estudiante("Sonry ", [90,85,90,98])
print("Promedio : ", alumno.Promedio())