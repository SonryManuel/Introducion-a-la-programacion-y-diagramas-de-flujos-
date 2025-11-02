import re
import json
import getpass
import os
import hashlib

usuarios = []
contraseñas = []

def passwordverificacion(password):
    longitud = len(password) >= 8
    mayuscula = re.search(r"[A-Z]", password)
    minuscula = re.search(r"[a-z]",password)
    simbolos = re.search(r"[@$!%*?$]",password)
    numero = re.search(r"[0-9]",password)

    return all ([longitud,mayuscula,minuscula,numero,simbolos])

def Alerta(password):
    if not passwordverificacion(password):
        print("La contrasela no es segura, la contrasela debe de tener 8 caracteres,numeros letras mayuscula, minuscula y simbolos")
    else:
        print("La contraseña es segura.")

def Registro():
    user = input("Usuarios: ")
    pwd = getpass.getpass("contraseña: ")
    Alerta(pwd)

    hashed = hashlib.sha256(pwd.encode()).hexdigest()

    guardarDatos()
    print(f"Usuario '{user}' registrado con éxito.")

def guardarDatos():
    data = {"usuarios": usuarios, "contraseñas": contraseñas}
    with open("usuarios.json", "w") as f:
        json.dump(data, f, indent=4)

def cargarDatos():
    global usuarios, contraseñas
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as f:
            data = json.load(f)
            usuarios = data["usuarios"]
            contraseñas = data["contraseñas"]

if __name__ == "__main__":
    cargarDatos()
    while True:
        print("\n--- Gestor de Contraseñas Seguras ---")
        print("1. Registrar nuevo usuario")
        print("2. Salir")
        op = input("Selecciona una opción: ")
        if op == "1":
            Registro()
        elif op == "2":
            break
        else:
            print("Opción no válida.")
