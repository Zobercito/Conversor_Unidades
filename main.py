import os
from units import convertir_distancia

def leer_flotante(prompt: str) -> float:
    """Solicita y valida entrada de número flotante."""
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Entrada inválida. Ingresa un número válido.")

def pause_and_clear():
    """Pausa la ejecución y limpia la pantalla."""
    input("\nPresione Enter para continuar...")
    os.system("cls" if os.name == "nt" else "clear")

def menu_principal():
    """Muestra el menú principal del conversor."""
    print("\n" + "="*40)
    print("      CONVERSOR DE UNIDADES")
    print("="*40)
    print("1. Conversor de Distancia")
    print("2. Conversor de Temperatura (próximamente)")
    print("3. Conversor de Peso/Masa (próximamente)")
    print("4. Conversor de Volumen (próximamente)")
    print("5. Salir")
    print("="*40)

def menu_distancia():
    """Muestra el menú específico para conversiones de distancia."""
    unidades = {
        "1": ("Kilómetros", "km"),
        "2": ("Metros", "m"),
        "3": ("Centímetros", "cm"),
        "4": ("Milímetros", "mm"),
        "5": ("Millas", "mi"),
        "6": ("Yardas", "yd"),
        "7": ("Pies", "ft"),
        "8": ("Pulgadas", "in"),
        "9": ("Millas náuticas", "nm"),
        "0": ("Volver al menú principal", None)
    }
    
    while True:
        print("\n" + "-"*40)
        print("      CONVERSOR DE DISTANCIA")
        print("-"*40)
        print("Selecciona la unidad de ORIGEN:")
        
        # Mostrar unidades disponibles
        for key, (nombre, abrev) in unidades.items():
            if key != "0":
                print(f"{key}. {nombre} ({abrev})")
        print("0. Volver al menú principal")
        
        # Selección de unidad de origen
        op_origen = input("\nOpción: ").strip()
        if op_origen == "0":
            return
        
        if op_origen not in unidades or op_origen == "0":
            print("Opción no válida.")
            continue
            
        nombre_origen, abrev_origen = unidades[op_origen]
        
        # Selección de unidad de destino
        print(f"\nConvertir {nombre_origen} a:")
        for key, (nombre, abrev) in unidades.items():
            if key != op_origen and key != "0":  # No mostrar la misma unidad ni volver
                print(f"{key}. {nombre} ({abrev})")
        
        op_destino = input("\nOpción: ").strip()
        if op_destino not in unidades or op_destino == "0" or op_destino == op_origen:
            if op_destino == op_origen:
                print("¡Debes seleccionar unidades diferentes!")
            else:
                print("Opción no válida.")
            continue
            
        nombre_destino, abrev_destino = unidades[op_destino]
        
        # Ingreso del valor a convertir
        print(f"\nConversión: {nombre_origen} → {nombre_destino}")
        valor = leer_flotante(f"Ingresa la cantidad en {nombre_origen}: ")
        
        try:
            # Realizar conversión usando la función general
            resultado = convertir_distancia(valor, abrev_origen, abrev_destino)
        except ValueError as e:
            print(f"Error: {e}")
            continue
        
        # Mostrar resultado
        print(f"\n{'='*40}")
        print(f"RESULTADO: {valor} {abrev_origen} = {resultado:.6f} {abrev_destino}")
        print("="*40)
        
        # Preguntar si quiere hacer otra conversión
        otra = input("\n¿Deseas hacer otra conversión de distancia? (s/n): ").strip().lower()
        if otra != 's':
            break
            
        pause_and_clear()

def main():
    """Función principal del programa."""
    while True:
        menu_principal()
        opcion = input("\nElige una opción (1-5): ").strip()
        
        if opcion == "1":
            menu_distancia()
        elif opcion == "2":
            print("\nConversor de Temperatura - Disponible próximamente")
            pause_and_clear()
        elif opcion == "3":
            print("\nConversor de Peso/Masa - Disponible próximamente")
            pause_and_clear()
        elif opcion == "4":
            print("\nConversor de Volumen - Disponible próximamente")
            pause_and_clear()
        elif opcion == "5":
            print("\n¡Gracias por usar el Conversor de Unidades!")
            break
        else:
            print("\nOpción no válida. Por favor, intenta de nuevo.")
            pause_and_clear()

if __name__ == "__main__":
    main()