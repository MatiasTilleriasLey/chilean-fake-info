import random

from chileanfakeinfo.provider.numGen import numberGen
from chileanfakeinfo.provider.bank import bankBinList
from chileanfakeinfo.provider.dates import month, year

# source: https://es.wikipedia.org/wiki/Algoritmo_de_Luhn#C%C3%A1lculo_del_d%C3%ADgito_de_chequeo


def calculate_luhn(cc) -> int:
    """Calcula el dígito de chequeo de Luhn para un número de tarjeta."""
    nums = [int(x) for x in str(cc)]
    check_digit = 10 - sum(
        nums[-2::-2] + [sum(divmod(d * 2, 10)) for d in nums[::-2]]
    ) % 10
    return check_digit % 10


def getCreditCard(bankName: str = "any", network: str = "any") -> str:
    """Genera un número de tarjeta de crédito.

    Puedes elegir el banco y la red (visa/mastercard). La lista completa de
    bancos disponibles se obtiene con la función getBankList().

    Args:
        bankName (str): Nombre del banco emisor de la tarjeta.
        network (str): Red utilizada por la tarjeta (visa/mastercard).

    Returns:
        str: La tarjeta como str.
    """
    if bankName == "any":
        bankName = random.choice(list(bankBinList().keys()))
    if network == "any":
        network = random.choice(list(bankBinList()[bankName].keys()))
    PAN = numberGen(9)
    binNumber = random.choice(bankBinList()[bankName][network])
    cc = f"{binNumber}{PAN}"
    return f"{cc}{calculate_luhn(cc)}"


def generateCVV() -> int:
    """Genera un CVV (un número aleatorio de 3 dígitos).

    Returns:
        int: el CVV generado.
    """
    return numberGen(3)


def generateExpirationDate() -> str:
    """Genera una fecha de expiración con el formato MM/YY.

    Returns:
        str: la fecha de expiración.
    """
    m = random.choice(list(month().keys()))
    return f"{m}/{int(year()[2:]) + numberGen(1)}"


def verifyCreditCard(cc: str) -> bool:
    """Valida una tarjeta de crédito usando el algoritmo de Luhn."""
    return str(calculate_luhn(cc[:-1])) == cc[-1]


def getCreditCardFull(bankName: str = "any", network: str = "any") -> dict:
    """Genera una tarjeta completa: número, CVV y fecha de expiración."""
    return {
        "credit-card": getCreditCard(bankName=bankName, network=network),
        "CVV": generateCVV(),
        "expiration-date": generateExpirationDate(),
    }


def getBankList() -> list:
    """Devuelve la lista de bancos disponibles."""
    return list(bankBinList().keys())
