# Chilean Fake Info

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/) ![Python Library](https://img.shields.io/badge/python-Library-yellow?logo=python&logoColor=f5da42)

![Logo](./img/IMG_3402-removebg-preview.svg)

"Chilean fake info" is a python library used to generate test information of Chilean origin

- Generation of Credit Card numbers supposedly issued in Chile from Multiple Banks
- Generation of rut numbers for both people and companies
- Random address generation

## Credit card

there are difentes ways to interact with Credits Cards, we can Generate CC's, Verify them based on the `Luhn Algorithm`, we can generate CVVs, expiration dates and a list a banks name  

### Banks name

if we need a list of bank present in Chile, we have the function `getBankList()`, this function will return a `list` with all the names in it

```python

from chileanfakeinfo import getBankList

print(getBankList())

>> ['Banco de Chile', 'Banco Internacional', 'Banco Scotiabank', 'Banco de Credito e Inversiones', 'Banco BICE', 'HSBC Bank', 'Banco Santander', 'Banco Itau', 'Banco Security', 'Banco Fallabella', 'Banco Ripley', 'Banco Consorcio', 'Banco Estado']

```

### getCreditCard() parameters

You can get a credit card from chile just using `getCreditCard()`, it will generate a CC from any bank found in the `getBankList()` function. If you requiere a Card from a specifict bank you can use the `bankName` parameter, also you can choose if you want a card be `mastercard` or `visa` using the `network` parameter

|              Bank              | visa | mastercard |
|:------------------------------:|:----:|:----------:|
|         Banco de Chile         | [x]  |    [x]     |
|      Banco Internacional       | [x]  |    [x]     |
|        Banco Scotiabank        | [x]  |    [x]     |
| Banco de Credito e Inversiones |      |    [x]     |
|           Banco BICE           | [x]  |            |
|           HSBC Bank            |      |    [x]     |
|        Banco Santander         | [x]  |    [x]     |
|           Banco Itau           |      |    [x]     |
|         Banco Security         | [x]  |    [x]     |
|        Banco Fallabella        | [x]  |            |
|          Banco Ripley          |      |    [x]     |
|        Banco Consorcio         | [x]  |            |
|          Banco Estado          | [x]  |    [x]     |

```python

from chileanfakeinfo import getCreditCard

print(getCreditCard()) # generate a CC from any bank with any network

>> 4105306670415592

print(getCreditCard(bankName="Banco de Chile", network="visa")) # generate a cc from Banco de Chile and visa Network

>> 4966702917417243

print(getCreditCard(bankName="Banco Santander", network="mastercard")) # generate a cc from Banco Santander and mastercard Network

>> 5400209517621779
```

### Credit Card Verification

Using Online resources you can verify the CC generated, as you can see the all af the cards generated are in fact from chile and match the criteria required.

<https://dnschecker.org/credit-card-validator.php>

![credit card Verification](./img/cc1.png)
![credit card Verification](./img/cc2.png)
![credit card Verification](./img/cc3.png)

If the only thing that you need to check is if that the CC is Valid or not you can use the `verifyCreditCard()` function. This function resive one parameter and return a `bool` depending if the card is valid or not

```python
from chileanfakeinfo import verifyCreditCard

print(verifyCreditCard(1234567890987654))

>> False

print(verifyCreditCard(4105306670415592))

>> True
```

### CVV and Expiration Dates

Is also posible to generate CVV numbers and expiration dates, in order to do that we have two functions `generateCVV()` and `generateExpirationDate()`

```python
from chileanfakeinfo import generateCVV
from chileanfakeinfo import generateExpirationDate

print(generateCVV())

>> 906

print(generateExpirationDate())

>> 12/31

```

## Chilean RUT

Is posible to generate ruts for Persons or Enterprises

### RUTs for Persons

In order to generate a RUT for a person you must execute the `personRutGenerator()`, it will return a `str` with the Rut generated

```python
from chileanfakeinfo import personRutGenerator as rut

print(rut())

>> 28475932k

```

### RUTs for Enterprises

In order to generate a RUT for a Enterprise you must execute the `enterpriseRutGenerator()`, it will retuen a `str` with the Rut generated

```python
from chileanfakeinfo import enterpriseRutGenerator as entRut

print(entRut())

>> 770293294
```

### Doted format

The functions `personRutGenerator` and `enterpriseRutGenerator` retuen a string with no format, but if you need you can convert this plain format into a doted format using the `dotRutFormat()`

```python
from chileanfakeinfo import dotRutFormat,personRutGenerator

rut = personRutGenerator()
print(rut)

>> 273626220

dotRut = dotRutFormat(rut)
print(dotRut)

>> 27.362.622-0
```

## Address

You can generate a random address just using `addressName()`

```python
from chileanfakeinfo import addressName

print(addressName())

>> Calle Lautaro 185, Region Arica y Parinacota, Chile
```

### Regions

If you need just the list of Regions of Chile you must use `regions()`

```python
from chileanfakeinfo import regions

print(regions())

>> {'1': {'name': 'Tarapacá'}, '2': {'name': 'Antofagasta'}, '3': {'name': 'Atacama'}, '4': {'name': 'Coquimbo'}, '5': {'name': 'Valparaíso'}, '6': {'name': "O'Higgins"}, '7': {'name': 'Maule'}, '8': {'name': 'Biobío'}, '9': {'name': 'Araucanía'}, '10': {'name': 'Los Lagos'}, '11': {'name': 'Aysén'}, '12': {'name': 'Magallanes'}, 'RM': {'name': 'Santiago'}, '14': {'name': 'Los Rios'}, '15': {'name': 'Arica y Parinacota'}}

```

## Authors

- [@MatiasTilleriasLey](https://github.com/MatiasTilleriasLey)
