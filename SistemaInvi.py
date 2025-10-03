#Sistema de control de inventario 

print("🛒bienvenido al sistema de control de inventario🛒".title())

while True:

    #Pidiéndole al usuario que ingrese el producto, cantidad y valor unitario

    producto = input("Ingrese los producto: ").lower()
    cantidad = int(input("Ingrese la cantidad: "))
    precio_unitario = float(input("Ingrese el precio unitario: "))

    valor_total = cantidad * precio_unitario

    print("-" * 50)

    print("\nResumen de la operación 📑")
    print(f"➡️ Los productos agregados son: {[producto.title()]}")
    print(f"➡️ Cantidad agregada: {cantidad}")
    print(f"➡️ Precio unitario: {precio_unitario}")
    print(f"💰 Valor total: {valor_total}")

    print("-" * 50)

    #Pidiendo al usuario otros productos

    producto2 = input("Otros productos: ").lower()
    cantidad2 = int(input("Ingrese la cantidad: "))
    precio_unitario2 = float(input("Ingrese el precio unitario: "))

    valor_total2 = cantidad2 * precio_unitario2

    print("-" * 50)

    print("\nResumen de la operación 📑")
    print(f"➡️ Otros productos agregados son: {[producto2.title()]}")
    print(f"➡️ Cantidad agregada: {cantidad2}")
    print(f"➡️ Precio unitario: {precio_unitario2}")
    print(f"💰 Valor total: {valor_total2}")

    print("-" * 50)

    #Saliendo del programa con el bucle while o regresando al inicio 

    salir = input("Deseas salir del programa? (s/n): ").lower()
    if salir == "s":
        print("🛒gracias por usar el sistema de gestión de inventario🛒".title())
        break