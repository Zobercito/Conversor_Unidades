# units.py
# Lógica de conversión

# Tablas de unidades usadas por la interfaz
DISTANCE_UNITS = {
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

TEMP_UNITS = {
    "1": ("Celsius", "C"),
    "2": ("Fahrenheit", "F"),
    "3": ("Kelvin", "K"),
    "0": ("Volver al menú principal", None),
}

# Factores de conversión a metros (unidad base)
FACTORES = {
    "km": 1000,        # Kilómetros a metros
    "m": 1,            # Metros (base)
    "cm": 0.01,        # Centímetros a metros
    "mm": 0.001,       # Milímetros a metros
    "mi": 1609.344,    # Millas a metros
    "yd": 0.9144,      # Yardas a metros
    "ft": 0.3048,      # Pies a metros
    "in": 0.0254,      # Pulgadas a metros
    "nm": 1852,        # Millas náuticas a metros
}

def convertir_distancia(valor: float, unidad_origen: str, unidad_destino: str) -> float:
    """Convierte entre cualquier unidad de distancia usando metros como base."""
    # Validar que las unidades existan
    if unidad_origen not in FACTORES or unidad_destino not in FACTORES:
        raise ValueError(f"Unidad no soportada. Use: {list(FACTORES.keys())}")
    
    # Convertir a metros primero, luego a la unidad destino
    valor_en_metros = valor * FACTORES[unidad_origen]
    return valor_en_metros / FACTORES[unidad_destino]


def convertir_temperatura(valor: float, unidad_origen: str, unidad_destino: str) -> float:
    """Convierte entre Celsius (C), Fahrenheit (F) y Kelvin (K).

    La conversión se realiza normalizando primero a Celsius y luego a la unidad destino.
    """
    origen = unidad_origen.upper()
    destino = unidad_destino.upper()

    # Convertir origen -> Celsius
    if origen == "C":
        c = valor
    elif origen == "F":
        c = (valor - 32) * 5.0 / 9.0
    elif origen == "K":
        c = valor - 273.15
    else:
        raise ValueError("Unidad de temperatura no soportada. Use: C, F, K")

    # Convertir Celsius -> destino
    if destino == "C":
        return c
    if destino == "F":
        return c * 9.0 / 5.0 + 32
    if destino == "K":
        return c + 273.15

    raise ValueError("Unidad de temperatura no soportada. Use: C, F, K")