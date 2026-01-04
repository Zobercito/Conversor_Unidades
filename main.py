# main.py
# Interfaz en terminal (menu)

import os
from units import km_to_mi, mi_to_km

def leer_flotante(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Entrada invalida. Ingresa un numero valido.")

def pause_and_clear(message: str = "Presione Enter para continuar..."):
    input(message)
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    print("\nBienvenido al Conversor de Unidades")
    print("1. Convertir de Kilometros a Millas")
    print("2. Convertir de Millas a Kilometros")
    print("3. Salir")

def main():
    while True:
        menu()
        opcion = input("Elige una opcion (1, 2 o 3): ").strip()
        if opcion == "1":
            km = leer_flotante("Ingresa la cantidad en Kilometros: ")
            millas = km_to_mi(km)
            print(f"{km} Km equivalen a {millas:.4f} millas")
            pause_and_clear()
        elif opcion == "2":
            millas = leer_flotante("Ingresa la cantidad en Millas: ")
            km = mi_to_km(millas)
            print(f"{millas} millas equivalen a {km:.4f} Km")
            pause_and_clear()
        elif opcion == "3":
            print("Adios")
            break
        else:
            print("Opcion no valida. Por favor, intenta de nuevo.")
            pause_and_clear()

if __name__ == "__main__":
    main()
