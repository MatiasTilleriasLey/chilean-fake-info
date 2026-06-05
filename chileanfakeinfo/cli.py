"""Interfaz de línea de comandos para chileanfakeinfo.

Permite usar la librería directamente desde la terminal una vez instalada,
por ejemplo:

    chilean-fake-info rut
    cfi creditcard --bank "Banco de Chile" --network visa
    cfi name --gender women -n 5
"""

import argparse
import sys

from chileanfakeinfo import (
    personRutGenerator,
    enterpriseRutGenerator,
    dotRutFormat,
    getCreditCard,
    getCreditCardFull,
    getBankList,
    verifyCreditCard,
    generateCVV,
    generateExpirationDate,
    addressName,
    regions,
    getName,
)


def _repeat(func, count):
    """Imprime el resultado de `func` un número `count` de veces."""
    for _ in range(max(1, count)):
        print(func())


def _cmd_rut(args):
    generator = enterpriseRutGenerator if args.enterprise else personRutGenerator

    def make():
        rut = generator()
        return dotRutFormat(rut) if args.dotted else rut

    _repeat(make, args.number)


def _cmd_creditcard(args):
    if args.full:
        def make():
            data = getCreditCardFull(bankName=args.bank, network=args.network)
            return (
                f"{data['credit-card']} | CVV: {data['CVV']} | "
                f"Exp: {data['expiration-date']}"
            )
    else:
        def make():
            return getCreditCard(bankName=args.bank, network=args.network)

    _repeat(make, args.number)


def _cmd_banks(args):
    for bank in getBankList():
        print(bank)


def _cmd_verify(args):
    valid = verifyCreditCard(args.number)
    print("valid" if valid else "invalid")
    sys.exit(0 if valid else 1)


def _cmd_cvv(args):
    _repeat(generateCVV, args.number)


def _cmd_expiration(args):
    _repeat(generateExpirationDate, args.number)


def _cmd_address(args):
    _repeat(addressName, args.number)


def _cmd_regions(args):
    for region in regions().values():
        print(region["name"])


def _cmd_name(args):
    _repeat(lambda: getName(args.gender).strip(), args.number)


def _add_number_arg(parser):
    parser.add_argument(
        "-n",
        "--number",
        type=int,
        default=1,
        help="Cantidad de elementos a generar (por defecto: 1).",
    )


def build_parser():
    parser = argparse.ArgumentParser(
        prog="chilean-fake-info",
        description="Generador de datos ficticios chilenos para pruebas y desarrollo.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # rut
    p_rut = subparsers.add_parser("rut", help="Genera un RUT chileno válido.")
    p_rut.add_argument(
        "-e",
        "--enterprise",
        action="store_true",
        help="Genera un RUT de empresa en lugar de uno de persona.",
    )
    p_rut.add_argument(
        "-d",
        "--dotted",
        action="store_true",
        help="Formatea el RUT con puntos y guion (ej: 12.345.678-9).",
    )
    _add_number_arg(p_rut)
    p_rut.set_defaults(func=_cmd_rut)

    # creditcard
    p_cc = subparsers.add_parser(
        "creditcard", aliases=["cc"], help="Genera un número de tarjeta de crédito."
    )
    p_cc.add_argument(
        "-b", "--bank", default="any", help='Nombre del banco (por defecto: "any").'
    )
    p_cc.add_argument(
        "-w",
        "--network",
        default="any",
        help='Red de la tarjeta: visa / mastercard (por defecto: "any").',
    )
    p_cc.add_argument(
        "-f",
        "--full",
        action="store_true",
        help="Incluye CVV y fecha de expiración.",
    )
    _add_number_arg(p_cc)
    p_cc.set_defaults(func=_cmd_creditcard)

    # banks
    p_banks = subparsers.add_parser(
        "banks", help="Lista los bancos disponibles."
    )
    p_banks.set_defaults(func=_cmd_banks)

    # verify
    p_verify = subparsers.add_parser(
        "verify", help="Valida una tarjeta de crédito con el algoritmo de Luhn."
    )
    p_verify.add_argument("number", help="Número de tarjeta a validar.")
    p_verify.set_defaults(func=_cmd_verify)

    # cvv
    p_cvv = subparsers.add_parser("cvv", help="Genera un CVV.")
    _add_number_arg(p_cvv)
    p_cvv.set_defaults(func=_cmd_cvv)

    # expiration
    p_exp = subparsers.add_parser(
        "expiration", aliases=["exp"], help="Genera una fecha de expiración."
    )
    _add_number_arg(p_exp)
    p_exp.set_defaults(func=_cmd_expiration)

    # address
    p_addr = subparsers.add_parser(
        "address", aliases=["addr"], help="Genera una dirección chilena."
    )
    _add_number_arg(p_addr)
    p_addr.set_defaults(func=_cmd_address)

    # regions
    p_reg = subparsers.add_parser("regions", help="Lista las regiones de Chile.")
    p_reg.set_defaults(func=_cmd_regions)

    # name
    p_name = subparsers.add_parser("name", help="Genera un nombre completo.")
    p_name.add_argument(
        "-g",
        "--gender",
        choices=["men", "women"],
        default="men",
        help='Género del nombre: men / women (por defecto: "men").',
    )
    _add_number_arg(p_name)
    p_name.set_defaults(func=_cmd_name)

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
