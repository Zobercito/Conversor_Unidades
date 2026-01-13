import os

def leer_flotante(prompt: str) -> float:
    """Solicita y valida entrada de número flotante."""
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Entrada inválida. Ingresa un número válido.")
        except EOFError:
            print("\nEntrada terminada por EOF. Saliendo...")
            raise SystemExit

def pause_and_clear():
    """Pausa la ejecución y limpia la pantalla."""
    try:
        input("\nPresione Enter para continuar...")
    except EOFError:
        print("\nEntrada terminada por EOF. Saliendo...")
        raise SystemExit
    os.system("cls" if os.name == "nt" else "clear")
