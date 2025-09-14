# Temperatura

while True:
    temperatura = int(input("Ingrese la temperatura: "))
    if temperatura >= 30:
        print("Hace mucho calor!🥵")

    elif 0 <= temperatura < 30:
        print("Hace un clima frio!🥶")

    salir = input("Deseas salir? (s/n): ").lower()

    if salir == "s":
        print("Hasta luego!")
        break
