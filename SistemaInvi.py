#Sistema de control de inventario 

while True:

    print("=====Bienvenido al sistema de control de inventario====")

    producto = input("Ingrese el nombre del producto: ").lower()
    print(f"El producto a agregado es: {producto}")

    cantidad = int(input("Ingrese la cantidad que desea agregar: "))
    print(f"Usted agrego: '{cantidad}' unidades del producto {producto}")

    precio_unitario = float(input("Ingrese el precio unitario del producto: "))
    print(f"El precio unitario del producto {producto} es: ${precio_unitario}")

    valor_total = cantidad * precio_unitario
    print(f"El valor total del producto {producto} es: ${valor_total}")

    print("=====Resumen del inventario=====")

    print("El producto agregado es:", producto)
    print("La cantidad agregada es:", cantidad)
    print(f"El precio unitario es: ${precio_unitario}")
    print(f"Valor total del inventario es: ${valor_total}")

    salir = input("Desea salir del sistema? (s/n): ").lower()
    if salir == "s":
            print("Gracias por usar el sistema de control de inventario...")
            break