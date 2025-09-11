import random

def adivinar_el_numero():
    print("🎲 Bienvenido al juego de adivinar el numero 🎲")

    while True:

        numero_secreto = random.randint(1, 50)
        intentos = 0

        while True:
            intento = input("Adivina un numero del 1 al 50 (O escribe 'salir' para terminar): ")

            if intento.lower() == "salir":
                print("Gracias por jugar, hasta luego!")
                return

            if not intento.isdigit():
                print("⚠️  Por favor, ingresa un numero valido.")
                continue

            intento = int(intento)
            intentos += 1

            if intento <  numero_secreto:
                print("Muy bajo. Intenta un numero mas grande.")
            elif intento > numero_secreto:
              print("Muy alto. Intenta un numero mas pequeño.")

            else:
                print(f"Felicidades! 🎉 Adivinaste el numero {numero_secreto} en {intentos} intentos.")
                print(f"Lo lograste en {intentos} intentos.")
                print("Eres muy bueno adivinando! 😎")
                break

        seguir = input("Ahora... quieres jugar de nuevo? (s/n:) ").lower()
        if seguir != "s":
            print("Gracias por jugar, hasta luego!")
            break


adivinar_el_numero()