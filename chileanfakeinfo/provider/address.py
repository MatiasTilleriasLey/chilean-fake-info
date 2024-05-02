import random
from chileanfakeinfo.provider.numGen import numberGen

def regions() -> dict:
    return {
        "1":{
            "name": "Tarapacá"
        },
        "2":{
            "name": "Antofagasta"
        },
        "3":{
            "name": "Atacama"
        },
        "4":{
            "name":"Coquimbo"
        },
        "5":{
            "name":"Valparaíso"
        },
        "6":{
            "name":"O'Higgins"
        },
        "7":{
            "name":"Maule"
        },
        "8":{
            "name":"Biobío"
        },
        "9":{
            "name":"Araucanía"
        },
        "10":{
            "name":"Los Lagos"
        },
        "11":{
            "name":"Aysén"
        },
        "12":{
            "name":"Magallanes"
        },
        "RM":{
            "name":"Santiago"
        },
        "14":{
            "name":"Los Rios"
        },
        "15":{
            "name": "Arica y Parinacota"
        }
    }

def addressName()->str:
    streetNames = (
        "Arturo Prat",
        "Esmeralda",
        "Gabriela Mistral",
        "Manuel Rodriguez",
        "Las Rosas",
        "Caupolican",
        "Lautaro",
        "Los Alercecs",
        "Los Copihues",
        "Los Aromos",
        "Balmaceda",
        "Victoria",
        "Portugal",
        "San Sebastian",
        "Presidente Riesco",
        "Luz",
        "Magdalena",
        "Argentina",
        "Holanda",
        "Napoleon",
        "Callao",
        "El Bosque",
        "Presidente Errazuriz",
        "Cristobal Colon",
        "La Pinta",
        "la niña",
        "Santa Maria",
        "Marco Polo"
    )

    streetType = [
        "Avenida",
        "Calle",
        "Pasaje",
        "Camino",
        "Callejon",
    ]
    return f"{random.choice(streetType)} {random.choice(streetNames)} {numberGen(3)}, Region {regions()[random.choice(list(regions().keys()))]['name']}, Chile"    


