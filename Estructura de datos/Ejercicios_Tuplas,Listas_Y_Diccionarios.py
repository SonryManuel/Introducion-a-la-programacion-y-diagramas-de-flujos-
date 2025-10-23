#Ejercicio 1: Tuplas

print("Ejercicio 1: Tuplas")
print("===================================")

Vulnerabilidades = ('SQL Injection', 'Cross-Site Scripting', 'Buffer Overflow', 'Denegación de Servicio')

print(Vulnerabilidades[0])
print(Vulnerabilidades)



#Ejercicio 2: Listas
print("\n \n Ejercicio 2: Listas")
print("===================================")

Puertos_abiertos = [22,80,8080]
Puertos_abiertos.append(21)

print(Puertos_abiertos)

Puertos_abiertos.remove(8080)
Puertos_abiertos.sort()

print(Puertos_abiertos)

print("\n Ejercicio 3: Diccionarios")
print("===================================")

dispositivo_red = {'ip': '192.168.1.10', 
                   'Hostname': 'Firewall-corp',
                   'Estado': 'Activo'}

print(dispositivo_red['Hostname'])
dispositivo_red['Ubicacion'] = 'Centro de Datos'
dispositivo_red['Estado'] = 'Inactivo'
print(dispositivo_red)