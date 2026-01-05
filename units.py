# units.py
# Lógica de conversión

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