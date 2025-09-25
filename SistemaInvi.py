#Sistema de control de inventario 

print("📦bienvenido al sistema de control de inventario📦".upper())

#Pidiéndole al usuario que ingrese el producto, cantidad y valor unitario

while True:

    print("=" * 50)

    producto = input("Ingrese los productos: ").lower()
    cantidad = int(input("Ingrese la cantidad: "))
    precio_unitario = float(input("Ingrese el valor unitario: "))

    #Valor total del producto
    valor_total = cantidad * precio_unitario

    print("=" * 50)

    #Resumen de la operación

    print("📑\nresumen de la operación📑".upper())
    print("=" * 50)
    print(f"➡️ Los productos agregados son: {producto.title()}")
    print(f"➡️ Cantidad agregada: {cantidad}")
    print(f"➡️ Precio unitario del producto: ${precio_unitario:.2f}")
    print(f"💰 Valor total: ${valor_total:.2f}")

    print("=" * 50)

    #Pidiéndole al usuario que ingrese otro producto

    producto = input("Ingrese los productos: ").lower().strip().title()
    cantidad = int(input("Ingrese la cantidad: "))
    precio_unitario = float(input("Ingrese el valor unitario: "))

    #Valor total del producto
    valor_total = cantidad * precio_unitario

    #Resumen de la operación

    print("📑\nresumen de la operación📑".upper())
    print("=" * 50)
    print(f"Los productos agregados son: ${producto}")
    print(f"Cantidad agregada: ${cantidad}")
    print(f"Precio unitario de los productos: ${precio_unitario}")
    print(f"Valor total de la operación: ${valor_total}")
    print("=" * 50)

    #Saliendo del programa con el bucle while o regresando al inicio 

    salir = input("Deseas salir del programa? (s/n): ").lower()
    if salir == "s":
        print("🛒 Gracias por usar el sistema de control de inventario 🛒".upper())
        break