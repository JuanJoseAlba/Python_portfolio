palabras = ["aire", "ojos", "piel", "anteojos", "joven", "viejo", "alto", "bajo", "pequeño", "gordo", "delgado", "bella", "azul", "verde", "negro", "sombrero", "guantes", "corbata", "gemelos", "paraguas", "plata", "oro", "perla", "diamante", "esmeralda", "anillo", "pulsera", "reloj", "elegante", "sencillo", "chaqueta", "traje", "camisa", "zapatos", "pelo", "maquillaje", "peine", "dedo", "hueso", "cara", "ojo", "calor", "ambulancia", "enfermera", "farmacia", "vitaminas", "pastillas", "dentista", "ciego", "correr", "caminar", "regresar", "saltar", "fin", "cerrar", "nombre", "mujer", "hombre", "soltero", "novio", "nacer", "vivir", "edad", "anciana","trabajar", "cobrar", "azafata", "artista", "panadero", "carpintero", "cocinero", "maestro", "bombero", "juez", "modelo", "monje", "pintor", "piloto", "secretaria", "taxista", "escritor", "jefe", "aprendiz", "jubilado", "empleo", "industria", "taller", "tienda", "vacaciones", "sueldo", "impuesto", "huelga", "obedecer", "locura", "humor", "inteligencia", "orgullo", "timidez", "valiente", "aburrido", "loco", "divertido", "bueno", "feliz", "amable", "pobre", "serio", "extraño", "gritar", "llorar", "suspirar", "preocupado", "risa", "amor", "suerte", "enamorado", "ver", "apagar", "luz", "color", "lupa", "microscopio", "claro", "cantar", "silbar", "voz", "eco", "trueno", "altavoz", "radio", "auricular", "liso", "comer", "dulce", "salado", "perfume", "despertarse", "vestirse", "desayunar", "leer", "dormirse", "toalla", "cobija", "almuerzo", "sopa", "agua", "leche", "jugo", "sal", "pimienta", "vinagre", "ajo", "perejil", "menta", "canela", "mayonesa", "pan", "mantequilla", "miel", "manzana", "pera", "durazno", "cereza", "papa", "lechuga", "arroz", "pollo", "pavo", "hamburguesa", "camarones", "tortilla", "espagueti", "sopa", "helado", "chocolate", "galletas", "bombones", "limpiar", "cortar", "hervir", "planchar", "aspiradora", "plancha", "horno", "abrelatas", "vajilla", "vaso", "cafetera", "azucarera", "comprar", "gastar", "vender", "barato", "caro", "gratis", "cliente", "bolsa", "precio", "recibo", "ascensor", "esquiar", "ciclismo", "golf", "pelota", "tenis", "bicicleta", "estadio", "gol", "torneo", "leer", "dibujar", "cantar", "bailar", "libro", "revista", "clavo", "cine", "pala", "cocina", "hielo", "coro", "piano", "cartas", "pesca", "radio", "noticias", "televisor", "documental", "anuncio", "aplaudir", "teatro", "circo", "mago", "disco", "portero", "propina", "regalo", "fiesta", "vela", "alfombra", "puerta", "ventana", "cortina", "escritorio", "cuadro", "juguete", "alquiler", "mudanza", "casa", "pared", "chimenea", "comedor", "plaza", "calle", "estacionamiento", "parque", "puente", "puerto", "edificio", "escuela", "museo", "estatua", "fuente", "turista", "mendigo", "manejar", "acelerar", "frenar", "cruzar", "reparar", "conductor", "multa", "atasco", "carretera", "peaje", "curva", "florecer", "campo", "bosque", "huerto", "selva", "tronco", "rama", "flor", "hoja", "musgo", "cedro", "roble", "pino", "nogal", "naranjo", "tallo", "clavel", "margarita", "amapola", "rosa", "girasol", "violeta", "gato", "perro", "vaca", "pato", "oveja", "conejo", "pez", "oso", "jirafa", "erizo", "mariposa", "foca", "tigre", "cobra", "almeja", "paloma", "cisne", "mosquito", "hormiga", "llover", "nevar", "nublado", "soleado", "clima", "rayo", "nieve", "sol", "viento", "padre", "madre", "hijo", "abuela", "estudioso", "aula", "tiza", "regla", "computadora", "diccionario"]

words = ["air", "eyes", "skin", "glasses", "young", "old", "tall", "short", "small", "fat", "thin", "beautiful", "blue ", "green", "black", "hat", "gloves", "tie", "cufflinks", "umbrella", "silver", "gold", "pearl", "diamond", "emerald", "ring", "bracelet", "watch", "elegant", "simple", "jacket", "suit", "shirt", "shoes", "hair", "makeup", "comb", "finger ", "bone", "face", "eye", "heat", "ambulance", "nurse", "pharmacy", "vitamins", "pills", "dentist", "blind", "run", "walk", "return", "jump", "end", "close", "name", "woman", "man", "single", "boyfriend", "born", "live", "age ", "old woman", "work", "get paid", "stewardess", "artist", "baker", "carpenter", "cook", "teacher", "fireman", "judge", "model", "monk", "painter", "pilot", "secretary", "taxi driver", "writer", "boss", "apprentice", "retired", "employment", "industry", "workshop", "shop ", "vacation", "salary", "tax", "strike", "obey", "madness", "humor", "intelligence", "pride", "shyness", "brave", "boring", "crazy", "funny", "good", "happy", "kind", "poor", "serious", "strange", "yell", "cry", "sigh", "worried", "laugh ", "love", "luck", "in love", "see", "turn off", "light", "color", "magnifying glass", "microscope", "clear", "sing", "whistle", "voice", "echo", "thunder", "speaker", "radio", "earphone", "smooth", "eat", "sweet", "salty", "perfume", "wake up", "dress ", "breakfast", "read", "fall asleep", "towel", "blanket", "lunch", "soup", "water", "milk", "juice", "salt", "pepper", "vinegar", "garlic", "parsley", "mint", "cinnamon", "mayonnaise", "bread", "butter", "honey", "apple", "pear", "peach", "cherry ", "potato", "lettuce", "rice", "chicken", "turkey", "hamburger", "shrimp", "omelette", "spaghetti", "soup", "ice cream", "chocolate", "biscuits", "chocolate", "clean", "cut", "boil", "iron", "vacuum", "iron", "oven", "can opener", "dishes", "glass", "coffee maker ", "sugar bowl", "buy", "spend", "sell", "cheap", "expensive", "free", "customer", "bag", "price", "receipt", "elevator", "skiing", "cycling", "golf", "ball", "tennis", "bicycle", "stadium", "goal", "tournament", "reading", "drawing", "singing", "dancing ", "book", "magazine", "nail", "cinema", "shovel", "kitchen", "ice", "choir", "piano", "letters", "fishing", "radio", "news", "tv", "documentary", "advertisement", "applaud", "theater", "circus", "magician", "disco", "janitor", "tip", "gift", "party ", "candle", "carpet", "door", "window", "curtain", "desk", "picture", "toy", "rental", "moving", "house", "wall", "chimney", "dining room", "square", "street", "parking", "park", "bridge", "harbor", "building", "school", "museum", "statue", "fountain" , "tourist", "beggar", "drive", "accelerate", "slow down", "cross", "repair", "driver", "fine", "traffic jam", "road", "toll", "curve", "bloom", "field", "forest", "orchard", "jungle", "trunk", "branch", "flower", "leaf", "moss", "cedar", "oak" , "pine", "walnut", "orange", "stem", "carnation", "daisy", "poppy", "rose", "sunflower", "violet", "cat", "dog", "cow", "duck", "sheep", "rabbit", "fish", "bear", "giraffe", "hedgehog", "butterfly", "seal", "tiger", "cobra", "clam" , "pigeon", "swan", "mosquito", "ant", "rain", "snow", "cloudy", "sunny", "weather", "lightning", "snow", "sun", "wind", "father", "mother", "son", "grandmother", "scholar", "classroom", "chalk", "ruler", "computer", "dictionary"]