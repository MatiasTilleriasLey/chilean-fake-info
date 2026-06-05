# Chilean Fake Info

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/) ![Python Library](https://img.shields.io/badge/python-Library-yellow?logo=python&logoColor=f5da42)

![Logo](https://raw.githubusercontent.com/MatiasTilleriasLey/chilean-fake-info/main/img/IMG_3402-removebg-preview.svg)

**Chilean Fake Info** is a Python library designed to generate test data of Chilean origin. This library is useful for developers and testers who need to generate fake but structured information.

## Features

- **Credit Card Generation:** Generates valid credit card numbers from multiple Chilean banks.
- **RUT Generation:** Creates valid RUTs for both individuals and companies.
- **Random Address Generation:** Generates addresses with valid region names.
- **Random Name Generation:** Creates full names with realistic first names and last names.
- **Date Utility Functions:** Provides helper functions for generating month and year values.

---

## Installation

To install the library, simply use `pip`:

```bash
pip install chileanfakeinfo
```

---

## Command Line Interface (CLI)

After installing the library, two terminal commands become available:
`chilean-fake-info` and its short alias `cfi`. They let you generate data
directly from your terminal without writing any Python.

```bash
# RUT
cfi rut                       # Person RUT          -> 285313732
cfi rut -e                    # Enterprise RUT      -> 717534115
cfi rut -d                    # Dotted format       -> 23.678.860-1
cfi rut -e -d -n 3            # 3 dotted enterprise RUTs

# Credit cards
cfi banks                     # List available banks
cfi creditcard                # Random credit card number
cfi cc -b "Banco de Chile" -w visa     # Specific bank and network (cc = alias)
cfi creditcard -f             # Full card: number | CVV | expiration date
cfi verify 5222102881454263   # Validate a card (exit code 0 = valid, 1 = invalid)
cfi cvv                       # Generate a CVV
cfi exp                       # Generate an expiration date

# Addresses and regions
cfi address                   # Random Chilean address
cfi regions                   # List Chilean regions

# Names
cfi name -g men               # Male full name
cfi name -g women -n 5        # 5 female full names
```

Most subcommands accept `-n / --number` to generate several items at once.
Run `cfi --help` or `cfi <command> --help` for the full list of options.

---

## Usage

### Generating a Chilean RUT

You can generate RUTs for individuals and enterprises:

```python
from chileanfakeinfo import personRutGenerator, enterpriseRutGenerator, dotRutFormat

# Generate a RUT for a person
person_rut = personRutGenerator()
print(person_rut)  # Example: 28475932k

# Generate a RUT for an enterprise
enterprise_rut = enterpriseRutGenerator()
print(enterprise_rut)  # Example: 770293294

# Format a RUT to the dot notation
formatted_rut = dotRutFormat(person_rut)
print(formatted_rut)  # Example: 28.475.932-K
```

---

### Generating Credit Card Numbers

You can generate random credit card numbers and validate them using the Luhn Algorithm.

```python
from chileanfakeinfo import getCreditCard, verifyCreditCard, generateCVV, generateExpirationDate, getBankList

# Get a list of banks available in Chile
print(getBankList())

# Generate a credit card number from any bank
credit_card = getCreditCard()
print(credit_card)

# Generate a credit card from a specific bank and network
specific_cc = getCreditCard(bankName="Banco de Chile", network="visa")
print(specific_cc)

# Validate a generated credit card number
print(verifyCreditCard(credit_card))  # Returns True if valid

# Generate CVV and Expiration Date
cvv = generateCVV()
exp_date = generateExpirationDate()
print(f"CVV: {cvv}, Expiration Date: {exp_date}")
```

#### Available Banks and Networks

| Bank Name | Visa | Mastercard |
|-----------|------|------------|
| Banco de Chile | ✅ | ✅ |
| Banco Internacional | ✅ | ✅ |
| Banco Scotiabank | ✅ | ✅ |
| Banco de Credito e Inversiones | ❌ | ✅ |
| Banco BICE | ✅ | ❌ |
| HSBC Bank | ❌ | ✅ |
| Banco Santander | ✅ | ✅ |
| Banco Itau | ❌ | ✅ |
| Banco Security | ✅ | ✅ |
| Banco Falabella | ✅ | ❌ |
| Banco Ripley | ❌ | ✅ |
| Banco Consorcio | ✅ | ❌ |
| Banco Estado | ✅ | ✅ |

---

### Generating Random Addresses

```python
from chileanfakeinfo import addressName, regions

# Generate a random Chilean address
print(addressName())  # Example: Calle Lautaro 185, Región de Coquimbo, Chile

# Get a list of Chilean regions
print(regions())
```

---

### Generating Random Names

You can generate a random full name by specifying the gender (`"men"` or `"women"`).

```python
from chileanfakeinfo import getName

# Generate a male name
print(getName("men"))  # Example: Mateo Alonso González Silva

# Generate a female name
print(getName("women"))  # Example: Isidora Fernanda Rojas Martínez
```

---

## Contribution

Contributions are welcome! If you'd like to improve this library, feel free to fork the repository, submit issues, or create pull requests.

---

## License

This project is licensed under the **GPL v3** License - see the [LICENSE](https://opensource.org/licenses/GPL-3.0) file for details.

---

## Author

- **[@MatiasTilleriasLey](https://github.com/MatiasTilleriasLey)**

