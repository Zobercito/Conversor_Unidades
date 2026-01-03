# Contenido de units.py
# Lógica de conversión

FACTOR_KM_MI = 0.621371

def km_to_mi(km: float) -> float:
    """Convierte kilometros a millas."""
    return km * FACTOR_KM_MI

def mi_to_km(mi: float) -> float:
    """Convierte millas a kilometros."""
    return mi / FACTOR_KM_MI
