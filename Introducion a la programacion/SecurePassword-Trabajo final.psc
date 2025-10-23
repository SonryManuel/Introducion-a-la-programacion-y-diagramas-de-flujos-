SubProceso Registrar
	Dimension users[10], password[10]
    Definir total, option, i, pos Como Entero
    total <- 0
	Si total < 10 Entonces
		pos <- total + 1
		Escribir "Ingrese nombre de usuario:"
		Leer users[pos]
		Escribir "Ingrese contrase�a:"
		Leer password[pos]
		total <- total + 1
		Escribir "Usuario registrado correctamente."
	SiNo
		Escribir "L�mite de usuarios alcanzado."
	FinSi
FinSubProceso

SubProceso ComprobarPassword
	Definir pass Como Cadena
	Definir long, contieneMayus, contieneNumero, j Como Entero
	Definir c Como Cadena
	contieneMayus <- 0
	contieneNumero <- 0
	
	Escribir "Ingrese la contrase�a a verificar:"
	Leer pass
	long <- Longitud(pass)
	
	Para j <- 1 Hasta long Con Paso 1 Hacer
		c <- SubCadena(pass, j, j)
		Si c >= "A" Y c <= "Z" Entonces
			contieneMayus <- 1
		FinSi
		Si c >= "0" Y c <= "9" Entonces
			contieneNumero <- 1
		FinSi
	FinPara
	
	Si long >= 8 Y contieneMayus = 1 Y contieneNumero = 1 Entonces
		Escribir "La contrase�a es FUERTE."
	SiNo
		Escribir "La contrase�a es D�BIL."
	FinSi
FinSubProceso





Algoritmo SecurePassword
	
	Repetir
        Escribir ""
        Escribir "=== MEN� DE OPCIONES ==="
        Escribir "1. Registrar usuario"
        Escribir "2. Comprobar contrase�a"
        Escribir "3. Salir"
        Escribir "Seleccione una opci�n:"
        Leer option
		
        Segun option Hacer
            1:
                Registrar
            2:
                ComprobarPassword
            3:
                Escribir "Saliendo..."
            De Otro Modo:
                Escribir "Opci�n no v�lida."
        FinSegun
    Hasta Que option = 3
	
	
FinAlgoritmo
