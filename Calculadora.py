#Calculadora 

print("🧮=====calculadora=====🧮".upper())

while True:

    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))

    print("-" * 50)

    #Operaciones aritmeticos disponibles

    print("operaciones disponibles👇".title())
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Modulo")

    print("-" * 50)

    #Pidiendo al usuario que escoja una de las 4 opciones

    opcion = input("Seleccione una opcion del 1-4: ")

    if opcion == "1":
        print(f"El resultado de la suma es: {a + b}")

    elif opcion == "2":
        print(f"El resultado de la resta es: {a - b}")

    elif opcion == "3":
        print(f"El resultado de la multiplicación es: {a * b:.2f}")

    elif opcion == "4":
        if b != 0:
            print(f"El resultado de la division es: {a / b:.2f}")
        else:
            print("No se puede dividir por 0")

    elif opcion == "5":
        print(f"El resultado del modulo es: {a % b}")

    else:
        print("Error operación incorrecta ❌")

    #Saliendo del programa

    salir = input("Deseas salir del programa (s/n): ").lower()
    if salir == "s":
        print("🧮gracias por usar la calculadora🧮".title())
        break