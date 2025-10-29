from datetime import datetime

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

ano_actual = datetime.now().year
edad_2050 = edad + (2050 - ano_actual)

print(f"Saludos {nombre.capitalize()}, usted tiene {edad} de edad!")
print(f"Para el ano 2050 usted tendrá: {edad_2050} wow!")