while True:

    edad = int(input("Ingrese su edad: "))
    if edad >= 18:
        print("Eres mayor de edad!")

    elif 0 < edad < 18:
        print("Eres menor de edad!")

    salir = input("Deseas salir? (s/n): ").lower()
    if salir =="s":
        print("Hasta luego!")
        break