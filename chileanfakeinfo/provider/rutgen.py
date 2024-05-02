import random

def dv(rut):
    inverseRut = rut[::-1]
    multiplicationTable = [2,3,4,5,6,7,2,3]
    result = sum([int(inverseRut[i]) * multiplicationTable[i] for i in range(len(inverseRut))])
    result = 11 - abs((int(result/11)*11) - result)

    if result == 11:
        return f"0"
    if result == 10:
        return f"k"
    return f"{result}"


def personRutGenerator() -> str:
    """Generate a valid rut that can be used for testing

    Returns:
        str: the rut is return as str  variable type, the rut may include the letter K, for that the function returns a str
    """
    rut = str(random.randrange(11111111,29999999))
    return f"{rut}{dv(rut=rut)}"

def enterpriseRutGenerator() -> str:
    rut = str(random.randrange(71111111,79999999))
    return f"{rut}{dv(rut=rut)}"

def dotRutFormat(rut:str) -> str:
    return f"{int(rut[:-1]):,d}-{rut[-1]}".replace(",",".")