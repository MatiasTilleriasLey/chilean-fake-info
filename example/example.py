from chileanfakeinfo import *

rutPerson = personRutGenerator()
rutEnterprise = enterpriseRutGenerator()

print(f"[*] Person rut Generated: ")
print(rutPerson)

print("[*] Doted rut Person")
print(dotRutFormat(rutPerson))

print(f"[*] Enterprise rut Generated: ")
print(rutEnterprise)

print("[*] Doted rut Enterprise")
print(dotRutFormat(rut=rutEnterprise))


print("[*] Chilean Credit Card -> any bank any network")
print(getCreditCard())

print("[*] Chilean Credit Card -> Banco de Chile Visa Network")
print(getCreditCard(bankName="Banco de Chile", network="visa"))

print("[*] Chilean Credit Card -> Banco Santander Mastercard Network")
print(getCreditCard(bankName="Banco Santander", network="mastercard"))

print("[*] CVV")
print(generateCVV())

print("[*] Expiration date")
print(generateExpirationDate())

print("[*] Generate Credit Card Full")
print(getCreditCardFull())


print("[*] Credit Card Verification -> True")
print(verifyCreditCard(getCreditCard()))

print("[*] Credit Card Verification -> False")
print(verifyCreditCard("4564323456797657"))

print("[*] List of Chileans Banks")
print(getBankList())

print("[*] Random Address")
print(addressName())

print("[*] Regions of Chile")
print(regions())

