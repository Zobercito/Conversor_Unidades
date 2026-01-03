# cli.py
# Interfaz en terminal (menú) — llama directamente a km_to_mi y mi_to_km

from units import km_to_mi, mi_to_km

def leer_flotante(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Entrada inválida. Ingresa un número válido.")

def menu():
    print("\nBienvenido al Conversor de Unidades")
    print("1. Convertir de Kilómetros a Millas")
    print("2. Convertir de Millas a Kilómetros")
    print("3. Salir")

def main():
    while True:
        menu()
        opcion = input("Elige una opción (1, 2 o 3): ").strip()
        if opcion == "1":
            km = leer_flotante("Ingresa la cantidad en Kilómetros: ")
            millas = km_to_mi(km)
            print(f"{km} Km equivalen a {millas:.4f} millas")
        elif opcion == "2":
            millas = leer_flotante("Ingresa la cantidad en Millas: ")
            km = mi_to_km(millas)
            print(f"{millas} millas equivalen a {km:.4f} Km")
        elif opcion == "3":
            print("Adiós")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
