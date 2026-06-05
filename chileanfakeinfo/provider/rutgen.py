import random


def dv(rut: str) -> str:
    """Calcula el dígito verificador de un RUT chileno."""
    inverseRut = rut[::-1]
    multiplicationTable = [2, 3, 4, 5, 6, 7, 2, 3]
    result = sum(
        int(inverseRut[i]) * multiplicationTable[i] for i in range(len(inverseRut))
    )
    result = 11 - abs((int(result / 11) * 11) - result)

    if result == 11:
        return "0"
    if result == 10:
        return "k"
    return f"{result}"


def personRutGenerator() -> str:
    """Genera un RUT de persona válido para pruebas.

    Returns:
        str: el RUT como str, ya que el dígito verificador puede ser la letra K.
    """
    rut = str(random.randrange(11111111, 29999999))
    return f"{rut}{dv(rut=rut)}"


def enterpriseRutGenerator() -> str:
    """Genera un RUT de empresa válido para pruebas.

    Returns:
        str: el RUT como str.
    """
    rut = str(random.randrange(71111111, 79999999))
    return f"{rut}{dv(rut=rut)}"


def dotRutFormat(rut: str) -> str:
    """Formatea un RUT con puntos y guion (ej: 12.345.678-9)."""
    return f"{int(rut[:-1]):,d}-{rut[-1]}".replace(",", ".")
