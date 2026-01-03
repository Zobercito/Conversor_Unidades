# units.py
# Lógica de conversión (sin I/O ni función genérica)

FACTOR_KM_MI = 0.621371

def km_to_mi(km: float) -> float:
    """Convierte kilómetros a millas."""
    return km * FACTOR_KM_MI

def mi_to_km(mi: float) -> float:
    """Convierte millas a kilómetros."""
    return mi / FACTOR_KM_MI
