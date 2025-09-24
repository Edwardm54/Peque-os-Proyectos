#Sistema de control de inventario 

bienvenida = "📦bienvenido al sistema de control de inventario📦"
print(bienvenida.upper())

while True:

    #Pidiéndole al usuario que ingrese el producto, cantidad y valor unitario

    producto = input("Ingrese los productos a agregar: ").lower()
    print("Los productos ingresados son los siguientes: {}".format(producto.split(sep=",")))
    
    cantidad = int(input("\nIngrese la cantidad a adquirir: "))
    print(f"La cantidad adquirida es: {cantidad}")

    precio_unitario = float(input("\nIngrese el valor precio unitario del producto: "))
    print(f"El precio unitario del producto es: ${precio_unitario}")

    valor_total = cantidad * precio_unitario
    print(f"\nEl valor total los productos es: ${valor_total}")

    #Total de la operación

    print("=" * 50)

    print("\n📑RESUMEN DE LA OPERACIÓN📑")
    print("➡️ Los productos agregados son: {}".format(producto.title().split(sep=",")))
    print("➡️ Cantidad agregada: {}".format(cantidad))
    print("➡️ Precio unitario de los productos: ${}".format(precio_unitario))
    print("➡️ Valor total de los productos: ${}".format(valor_total))

    print("=" * 50)

    #Saliendo del programa con el bucle while o regresando al inicio 

    salir = input("Deseas salir del programa? (s/n): ").lower()
    if salir == "s":
        print("Gracias por usar el sistema de control de inventario 😎")
        break