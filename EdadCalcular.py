from datetime import datetime

nombre = input("Ingresa tu nombre: ")
edad = int(input("Tu edad es: "))

ano_actual = datetime.now().year
ano_2100 = edad + (2100 - ano_actual)

print(f"\nSaludos {nombre.capitalize()} tu edad es {edad}!")

print(f"En el ano 2100 usted tendrá: {ano_2100} wow")