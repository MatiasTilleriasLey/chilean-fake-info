import random
menName = [
    "Mateo", "Liam", "Lucas", "Santiago", "Gaspar", "Facundo", "Thiago", "Benjamín", "Vicente", "Gael",
    "Agustín", "Máximo", "Noah", "Tomás", "Maximiliano", "Emiliano", "Bruno", "Alonso", "Santino", "Matías",
    "Martín", "Gabriel", "Luciano", "Joaquín", "Dante", "Julián", "Ian", "Clemente", "León", "Valentino",
    "Eithan", "José", "Matteo", "Sebastián", "Nicolás", "Dylan", "Juan", "Amaro", "Cristóbal", "Rafael",
    "Diego", "Valentín", "Samuel", "Simón", "Oliver", "Pedro", "Borja", "Damián", "Daniel", "Bastián",
    "Felipe", "Andrés", "Pablo", "Rodrigo", "Ignacio", "Esteban", "Fernando", "Hernán", "Jorge", "Luis",
    "Manuel", "Ricardo", "Eduardo", "Francisco", "Alejandro", "Carlos", "Raúl", "Sergio", "Víctor", "Álvaro",
    "Hugo", "Mario", "Oscar", "Patricio", "Ramón", "Roberto", "Rubén", "Salvador", "Teodoro", "Ulises",
    "Vladimir", "Walter", "Xavier", "Yago", "Zacarías", "Abel", "Adán", "Adrián", "Alan", "Albert",
    "Alberto", "Aldo", "Alejo", "Alfonso", "Alfredo", "Amador", "Américo", "Aníbal", "Antonio", "Armando",
    "Arnaldo", "Arturo", "Baltasar", "Bartolomé", "Bautista", "Beltrán", "Bernardo", "Blas", "Brayan", "Camilo",
    "César", "Claudio", "Clemente", "Conrado", "Cristian", "Damián", "Danilo", "David", "Demetrio", "Diego",
    "Domingo", "Donato", "Edgardo", "Efraín", "Elías", "Emilio", "Enrique", "Ernesto", "Eugenio", "Eusebio",
    "Evaristo", "Fabián", "Facundo", "Federico", "Félix", "Fermín", "Flavio", "Florencio", "Fortunato", "Froilán",
    "Gaspar", "Gerardo", "Germán", "Gilberto", "Gonzalo", "Gregorio", "Guido", "Guillermo", "Gustavo", "Héctor",
    "Homero", "Horacio", "Humberto", "Iker", "Isaac", "Ismael", "Iván", "Jacinto", "Jaime", "Javier",
    "Jeremías", "Jesús", "Joaquín", "Jonás", "Jonathan", "Jorge", "José", "Josué", "Juan", "Julián",
    "Julio", "Justo", "Kevin", "Lautaro", "Leandro", "Leonardo", "Leopoldo", "Lorenzo", "Lucas", "Luciano",
    "Luis", "Manuel", "Marcos", "Mariano", "Mario", "Martín", "Mateo", "Matías", "Mauricio", "Maximiliano",
    "Miguel", "Moisés", "Narciso", "Nicolás", "Norberto", "Octavio", "Omar", "Orlando", "Oscar", "Pablo",
    "Patricio", "Pedro", "Rafael", "Ramiro", "Raúl", "Renato", "Ricardo", "Roberto", "Rodrigo", "Rogelio",
    "Román", "Rubén", "Salvador", "Samuel", "Santiago", "Sebastián", "Sergio", "Simón", "Teodoro", "Timoteo",
    "Tomás", "Ulises", "Valentín", "Vicente", "Víctor", "Wilfredo", "Xavier", "Yago", "Zacarías", "Abraham",
    "Adolfo", "Agustín", "Alcides", "Alejandro", "Alfonso", "Alfredo", "Amadeo", "Amaro", "Aníbal", "Antonio",
    "Aquiles", "Armando", "Arturo", "Augusto", "Aurelio", "Baldomero", "Baltasar", "Benjamín", "Bernardo", "Blas",
    "Bruno", "Calixto", "Camilo", "Carlos", "César", "Claudio", "Cristóbal", "Damián", "Daniel", "Dante",
    "David", "Demetrio", "Diego", "Domingo", "Donato", "Edgardo", "Eduardo", "Efraín", "Eladio", "Elías",
    "Emilio", "Enrique", "Ernesto", "Eugenio", "Fabián", "Facundo", "Federico", "Félix", "Fernando", "Fidel",
    "Flavio", "Francisco", "Gabriel", "Gaspar", "Germán", "Gerardo", "Gonzalo", "Gregorio", "Guido", "Guillermo",
    "Gustavo", "Héctor", "Horacio", "Hugo", "Humberto", "Ignacio", "Isaac", "Ismael", "Iván", "Jaime",
    "Javier", "Jesús", "Joaquín", "Jorge", "José", "Juan", "Julián", "Julio", "Kevin", "Lautaro",
    "Leandro", "Leonardo", "Lorenzo", "Lucas", "Luciano", "Luis", "Manuel", "Marcos", "Mario", "Martín",
    "Mateo", "Matías", "Mauricio", "Maximiliano", "Miguel", "Nicolás", "Omar", "Orlando", "Oscar", "Pablo",
    "Patricio", "Pedro", "Rafael", "Raúl", "Renato", "Ricardo", "Roberto", "Rodrigo", "Román", "Rubén",
    "Salvador", "Samuel", "Santiago", "Sebastián", "Sergio", "Simón", "Teodoro", "Tomás", "Ulises", "Vicente",
    "Víctor", "Xavier", "Yago", "Zacarías"
]
womenName = [
    "Isidora", "Florencia", "Emma", "Josefa", "Sofía", "Emilia", "Martina", "Antonella", "Agustina", "Catalina",
    "Valentina", "Amanda", "Maite", "Renata", "Javiera", "Mariana", "Gabriela", "Julieta", "Francisca", "Camila",
    "Fernanda", "Trinidad", "Romina", "María José", "Josefina", "Alondra", "Paula", "Carla", "Paz", "Nicole",
    "Daniela", "Alejandra", "Constanza", "Bianca", "Victoria", "Valeria", "Clara", "Rocío", "Vanessa", "Luciana",
    "Anaís", "Elena", "Ximena", "Ariana", "Alicia", "Paloma", "Belén", "Amparo", "Luisa", "Montserrat",
    "Tamara", "Carolina", "Angélica", "Melissa", "Gabriella", "Elisa", "Regina", "Delfina", "Juliana", "Macarena",
    "Aurora", "Amanda", "Celeste", "Milagros", "Felicia", "Andrea", "Lorena", "Susana", "Norma", "Luz",
    "Blanca", "René", "Soledad", "Fabiola", "Rosa", "Maribel", "Teresa", "Margarita", "Estefanía", "Beatriz",
    "Viviana", "Esperanza", "Patricia", "Silvia", "Paulina", "Erika", "Ángela", "Magdalena", "Nancy", "Olga",
    "Ruth", "Bárbara", "Lilian", "Pilar", "Cecilia", "Yolanda", "Evelyn", "Gloria", "Cristina", "Verónica",
    "Daniela", "Leonor", "Carolina", "Mónica", "Lourdes", "Esther", "Graciela", "Alejandra", "Natalia", "Martha",
    "Diana", "Adriana", "Claudia", "Marina", "Inés", "Eugenia", "Josefa", "Débora", "Marisol", "Anabel",
    "Brenda", "Carmen", "Dora", "Emilia", "Florencia", "Genoveva", "Hilda", "Irene", "Jana", "Karla",
    "Lidia", "Marcia", "Nerea", "Oriana", "Raquel", "Sandra", "Tatiana", "Ursula", "Violeta", "Zaira",
    "Abril", "Alba", "Amelia", "Antonia", "Ariadna", "Aurelia", "Azucena", "Betsabé", "Candela", "Carlota",
    "Damaris", "Ester", "Fiona", "Geraldine", "Herminia", "Isabel", "Jazmín", "Karen", "Leticia", "Maritza",
    "Nayara", "Noelia", "Ofelia", "Penélope", "Queralt", "Rafaela", "Selena", "Tamara", "Uxia", "Valentina",
    "Wendy", "Xenia", "Yadira", "Zaida", "Zulema", "Aida", "Brigitte", "Camille", "Dolores", "Elvira",
    "Frida", "Gloria", "Harumi", "Ivette", "Jenifer", "Katya", "Linda", "Malena", "Nora", "Olivia",
    "Perla", "Quintina", "Rosalía", "Susana", "Thelma", "Urbana", "Virginia", "Wilma", "Ximena", "Yesenia",
    "Yvonne", "Zenaida", "Alison", "Betania", "Cinthia", "Desirée", "Eloísa", "Felipa", "Griselda", "Hana",
    "Itzel", "Jovita", "Kendra", "Liana", "María Fernanda", "Mía", "Noemí", "Pamela", "Rebeca", "Samanta",
    "Tania", "Vania", "Wanda", "Xochitl", "Yara", "Zoraida", "Anahí", "Berta", "Celia", "Dafne",
    "Eliana", "Flor", "Georgina", "Helena", "Ileana", "Juliana", "Kiara", "Lara", "Magaly", "Nicolle",
    "Otilia", "Paola", "Ramona", "Sasha", "Tess", "Ubalda", "Valeria", "Waleska", "Xandra", "Yvette",
    "Zahira", "Amapola", "Basilia", "Concepción", "Donatella", "Estrella", "Felisa", "Giselle", "Hortensia", "Imelda",
    "Jacinta", "Katiuska", "Lucía", "Milena", "Nubia", "Ona", "Petra", "Querubina", "Rocío", "Sabina",
    "Tirsa", "Ursina", "Vega", "Wilhelmina", "Xilena", "Yudith", "Zelma", "Araceli", "Bibiana", "Clarisa",
    "Dora", "Eusebia", "Fermina", "Genara", "Hilda", "Iliana", "Jesusa", "Kenia", "Lina", "Mireya",
    "Nayeli", "Octavia", "Priscila", "Quintina", "Rosario", "Socorro", "Teodora", "Ursulina", "Vittoria", "Xaviera",
    "Yasmín", "Zenaida", "Alicia", "Beatriz", "Carmela", "Daniela", "Estefanía", "Gabriela", "Hermelinda", "Inmaculada",
    "Juana", "Karla", "Lorena", "Mercedes", "Nieves", "Olga", "Patricia", "Rosalba", "Silvia", "Tatiana",
    "Úrsula", "Vanessa", "Wendy", "Xiomara", "Yesenia", "Zaira", "Adela", "Brenda", "Clara", "Dulce",
    "Elisa", "Florencia", "Gilda", "Helena", "Isabel", "Jazmín", "Katherine", "Luz", "Margarita", "Natalia",
    "Orquídea", "Pamela", "Raquel", "Sandra", "Teresa", "Valentina", "Wilma", "Xaviera", "Ylenia", "Zulema"
]

apellidos = [
    "González", "Muñoz", "Rojas", "Díaz", "Pérez", "Soto", "Contreras", "Silva", "Martínez", "Sepúlveda",
    "Morales", "Rodríguez", "López", "Fuentes", "Hernández", "Torres", "Araya", "Flores", "Espinoza", "Valenzuela",
    "Castillo", "Ramírez", "Reyes", "Gutiérrez", "Castro", "Vargas", "Pizarro", "Carvajal", "Fernández", "Bravo",
    "Molina", "Vásquez", "Sandoval", "Jara", "Navarro", "Salazar", "Alarcón", "Garrido", "Cortés", "Tapia",
    "Gómez", "Vega", "Campos", "Ortega", "Zúñiga", "Vergara", "Olivares", "Henríquez", "Cáceres", "Aguilera",
    "Escobar", "Paredes", "San Martín", "Orellana", "Miranda", "Ortiz", "Aravena", "Aliaga", "Yáñez", "Valdés",
    "Quezada", "Godoy", "Peña", "Guerrero", "Farías", "Bustos", "Salinas", "Toledo", "Maldonado", "Neira",
    "Saavedra", "Moreno", "Medina", "Palma", "Chávez", "Riquelme", "Cárdenas", "Delgado", "Pino", "Carrasco",
    "Álvarez", "Venegas", "Villarroel", "Montoya", "Becerra", "Alvarado", "Escudero", "Arriagada", "Sanhueza", "Donoso",
    "Meza", "Lagos", "Cisternas", "Araya", "Cuevas", "Asenjo", "Beltrán", "Ríos", "Cornejo", "Bahamondes",
    "Cerda", "Padilla", "Rosales", "Poblete", "Acevedo", "Albornoz", "Mulet", "Serrano", "Madrid", "Arce",
    "Andrade", "Santibáñez", "Salcedo", "Sepúlveda", "Osorio", "Figueroa", "Barrientos", "Villanueva", "Galdames", "Benítez",
    "Ávalos", "Aróstica", "Bustamante", "Mena", "Montero", "Osses", "Troncoso", "Quezada", "León", "Véliz",
    "Catalán", "Carmona", "Almeida", "Berríos", "Cifuentes", "Rebolledo", "Iturra", "Vallejos", "Lizana", "Pavéz",
    "Ojeda", "Saéz", "Opazo", "Venegas", "Toro", "Ramón", "Campos", "Escalona", "Marín", "Suárez",
    "Valdivia", "Tapia", "Mujica", "Hidalgo", "Fierro", "Parra", "Moraga", "Godoy", "Rivas", "Santander",
    "Moya", "Baeza", "Méndez", "Carrillo", "Jofré", "Maturana", "Medel", "Ochoa", "Navarrete", "Bravo",
    "Silvestre", "Burgos", "Saavedra", "Rivera", "Andaur", "Aguilar", "Pérez", "Gallegos", "Ulloa", "Pizarro",
    "Lobos", "Sepúlveda", "Rebolledo", "Solís", "Tapia", "Morán", "Quintana", "Moncada", "Sanhueza", "Páez",
    "Valencia", "Aguirre", "Pacheco", "Benavides", "Bustamante", "Marambio", "Rifo", "Del Valle", "Vera", "San Miguel",
    "Quezada", "Vergara", "Riveros", "Arellano", "Arrieta", "Astudillo", "Cordero", "Olmedo", "Tello", "Toro",
    "Olivos", "Sepúlveda", "Vargas", "Escalante", "Tapia", "Canales", "Avendaño", "Bobadilla", "Lucero", "Peñaloza",
    "Navarrete", "Fuenzalida", "Rebolledo", "Duarte", "Parraguez", "Manríquez", "Galaz", "Villagran", "Leyton", "Obando",
    "Vallejos", "Montecinos", "Urrutia", "Lillo", "Cartes", "Améstica", "Farias", "Olea", "Méndez", "Lozano",
    "Espina", "Arismendi", "Lizama", "Santana", "Páez", "Bascur", "Tobar", "Figueroa", "Lemún", "Pinto",
    "Ibarra", "Villarreal", "Mallea", "Queupumil", "Huenchumilla", "Curihuinca", "Nahuel", "Abarca", "Panguilef", "Painemal",
    "Caniullán", "Antilef", "Catril", "Marileo", "Curiqueo", "Chihualaf", "Huaiquilaf", "Marilaf", "Lientur", "Tralcal",
    "Huenul", "Catrillanca", "Melillanca", "Loncomilla", "Nahuelcura", "Paine", "Huaiquimil", "Ancalaf", "Cariman", "Colipe",
    "Huircán", "Cayuqueo", "Cheuquepán", "Huichalaf", "Quintriqueo", "Curinao", "Antinao", "Catriao", "Huala", "Huayquil",
    "Huaiquifil", "Huichapan", "Huinca", "Huichalaf", "Coliqueo", "Caniuqueo", "Nahuelquin", "Pailamilla", "Antulef", "Calbucura",
    "Calfuqueo", "Colil", "Huenulef", "Manquilef", "Ñanco", "Paillán", "Queipul", "Reuque", "Troncozo", "Wangelen",
    "Huilipán", "Guineo", "Callupe", "Millacura", "Nahuelpán", "Calfu", "Curiqueo", "Antil", "Coloma", "Huentemilla"
]

def getName(gender: str) -> str:
    nameGenerated = ""
    for _ in range(2):
        if gender == "men":
            nameGenerated += random.choice(menName)
        if gender == "women":
            nameGenerated += random.choice(womenName)
        nameGenerated += " "
    for _ in range(2):
        nameGenerated += random.choice(apellidos)
        nameGenerated += " "
    return nameGenerated
