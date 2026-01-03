# --- Conversor de Unidades (Km y Millas) ---

print("Bienvenido al Conversor de Unidades")
print("1. Convertir de Kilómetros a Millas")
print("2. Convertir de Millas a Kilómetros")

opcion = input("Elige una opción (1 o 2): ")

# Factor de conversión: 1 Km = 0.621371 millas
FACTOR_CONVERSION = 0.621371

if opcion == "1":
    km = float(input("Ingresa la cantidad en Kilometros: "))
    millas = km * FACTOR_CONVERSION
    print(f"{km} Km equivalen a {millas:.2f} millas")

elif opcion == "2":
    millas = float(input("Ingresa la cantidad en Millas: "))
    km = millas / FACTOR_CONVERSION
    print(f"{millas} millas equivalen a {km:.2f} Km")

else:
    print("Opción no válida. Por favor, reinicia el programa.")