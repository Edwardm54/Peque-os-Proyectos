#Calculadora 

print("🧮=====calculadora=====🧮".upper())

while True: 

    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))

    #Operadores aritméticos disponibles

    print("="* 30)

    print("\noperaciones disponibles 👇".title())
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")

    print("="* 30)

    #Pidiendo al usuario que escoja una de las 4 opciones
    opcion = input("\nEncoje una opcion del 1 al 4: ")

    if opcion == "1":
        print("El resultado de la suma es: {}".format(num1 + num2))

    elif opcion == "2":
        print("El resultado de la resta es: {}".format(num1 + num2))

    elif opcion == "3":
        print("El resultado de la multiplicacion es: {}".format(num1 + num2))

    elif opcion == "4":
        if num2 != 0:
            print("El resultado de la division es: {}".format(num1 + num2))
        else:
            print("Error no se puede dividir entre 0")

    else:
        print("Error operación incorrecta ❌")

    print("="* 30)

    #Saliendo del programa 

    salir = input("\nDeseas salir del programa? (s/n): ").lower()
    if salir == "s":
        print("🧮Gracias por usar la calculadora! 🧮".title())
        break