#Sistema de control de inventario 

print("📦=====BIENVENIDO AL SISTEMA DE CONTROL DE INVENTARIO=====📦")

while True:

    producto = input("Ingrese el producto a agregar: ").lower()
    print(f"El producto agregado es: {producto}")

    cantidad = int(input("\nIngrese la cantidad que desee almacenar: "))
    print(f"La cantidad almacenada es: {cantidad}")

    precio_unitario = float(input("\nIngrese el precio unitario del producto: "))
    print(f"El precio unitario del producto almacenado es: {precio_unitario}")

    valor_total = cantidad * precio_unitario
    print(f"\nEl precio total del producto es el siguiente: {valor_total}")

    print("\n📑=====RESUMEN DE LA OPERACIÓN=====📑") 
    print(f"El producto agregado es: {producto}")
    print(f"La cantidad almacenada es la siguiente: {cantidad}")
    print(f"Precio unitario total del producto: {precio_unitario}")
    print(f"Valor total de la compra: {valor_total}")
    print("====================================")

    salir = input("Deseas salir del programa? (s/n): ").lower()
    if salir == "s":
         print("Gracias por usar el sistema de control de inventario!")
         break