import random
from chileanfakeinfo.provider.numGen import numberGen
from chileanfakeinfo.provider.bank import bankBinList
from chileanfakeinfo.provider.dates import *

# Intente escribir el algoritmo basado en varios articulos que leí
# pero supongo que soy idiota para escribirlo
# source: https://es.wikipedia.org/wiki/Algoritmo_de_Luhn#C%C3%A1lculo_del_d%C3%ADgito_de_chequeo
def calculate_luhn(cc):
    nums = [int(x) for x in str(cc)]
    check_digit = 10 - sum(nums[-2::-2] + [sum(divmod(d * 2, 10)) for d in nums[::-2]]) % 10
    return check_digit % 10

def getCreditCard(bankName:str = "any", network:str = "any") -> str:
    if bankName == "any":
        bankName = random.choice(list(bankBinList().keys()))
    if network == "any":
        network = random.choice(list(bankBinList()[bankName].keys()))
    PAN = numberGen(9)    
    binNumber = random.choice(bankBinList()[bankName][network])
    cc = f"{binNumber}{PAN}"
    return f"{cc}{calculate_luhn(cc)}"    

def generateCVV() -> int:
    return numberGen(3)


def generateExpirationDate():
    m = random.choice(list(month().keys()))
    return f"{m}/{int(year()[2:])+numberGen(1) }"

    pass

def verifyCreditCard(cc:str) -> bool:
    return str(calculate_luhn(cc[:-1])) == cc[-1]

def getCreditCardFull(bankName:str="any", network:str="any") -> dict:
    return {
        "credit-card": getCreditCard(),
        "CVV" : generateCVV(),
        "expiration-date": generateExpirationDate()
    }

def getBankList() -> list:
    return list(bankBinList().keys())