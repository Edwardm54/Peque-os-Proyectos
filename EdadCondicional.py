print("AQUÍ PUEDE COMPROBAR SU ES MAYOR O MENOR DE EDAD!")

while True:

    edad = int(input("Ingrese su edad: "))

    if edad >= 18:
        print("Usted es mayor de edad!")

    elif 0 < edad < 18:
        print("Usted es menor de edad!")

    salir = input("Deseas salir del programa? (s/n): ")
    if salir == "s":
        print("Hasta luego!")
        break