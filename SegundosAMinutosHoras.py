#De segundos a minutos, horas

segundos = int(input("Ingrese la cantidad de segundos: "))

horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60

print(f"\n{segundos} segundos equivalen a {horas} hora, {minutos} minutos y {segundos_restantes} segundos.")

print("Hasta luego!")