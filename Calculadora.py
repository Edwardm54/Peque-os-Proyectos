#Calculadora 

while True:

    print("🧮======CALCULADORA======🧮")

    num1 = float(input("Ingrese el primer valor: "))
    num2 = float(input("Ingrese el segundo valor: "))

    print("Operaciones disponibles 👇")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")

    opcion = input("Elija una opcion del 1-4: ")

    if opcion == "1":
        print(f"El resultado de la suma es: {num1 + num2}")

    elif opcion == "2":
            print(f"El resultado de la resta es: {num1 - num2}")

    elif opcion == "3":
        print(f"El resultado de la multiplicacion es: {num1 * num2}")

    elif opcion == "4":
        if num2 != 0:
         print(f"El resultado de la division es: {num1 / num2}")
        else:
         print("Error no se puede dividir entre '0' ")

    else:
        print("Opción no valida, intente de nuevo")

    salir = input("\nDeseas salir del programa? (s/n): ")
    if salir == "s":
        print("Hasta luego!")
        break