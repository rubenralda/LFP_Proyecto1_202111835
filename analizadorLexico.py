class errores:
    def __init__(self, fila, columna, error):
        self.fila = fila
        self.columna = columna
        self.error = error


class automata:

    def __init__(self, cadena=""):
        self.cadena = cadena
        self.columna = 1
        self.fila = 1
        self.letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                       "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        self.palabras_clave = ["SUMA", "MULTIPLICACION", "Numero", "DIVISION", "RESTA",
                               "POTENCIA", "RAIZ", "TANGENTE", "INVERSO", "SENO", "COSENO"]
        self.token = []
        self.token2 = []
        self.errores = []
        self.colores = ["blanco", "rojo", "amarillo",
                        "azul", "verde", "negro", "gris"]
        self.titulo = {"contenido": "", "color": "", "tamano": 0}
        self.descripcion = {"contenido": "", "color": "", "tamano": 0}
        self.contenido = {"contenido": "", "color": "", "tamano": 0}
        self.estado_actual = 0

    def analizar(self):
        lexema = ""
        while (len(self.cadena) > 0):
            char = self.cadena[0]
            # ignorar espacios en blanco o saltos de linea
            if char == '\n':
                self.fila += 1
                self.columna = 0
                self.cadena = self.cadena[1:]
                continue
            elif char == ' ':
                self.columna += 1
                self.cadena = self.cadena[1:]
                continue

            if self.estado_actual == 0:

                if char.lower() in self.letras:
                    lexema += char
                elif char in self.numeros:
                    self.token2.append(
                        errores(self.fila, self.columna, lexema))
                    lexema = char
                    self.estado_actual = 1
                    primerPunto = True
                elif char == '>':
                    if lexema.lower() == "texto":
                        self.token2.append(lexema)
                        lexema = ""
                        self.estado_actual = 3
                    elif lexema.lower() == "titulo":
                        self.token2.append(lexema)
                        lexema = ""
                        self.estado_actual = 4
                    elif lexema.lower() == "descripcion":
                        self.token2.append(lexema)
                        lexema = ""
                        self.estado_actual = 5
                    elif lexema.lower() == "contenido":
                        self.token2.append(lexema)
                        lexema = ""
                        self.estado_actual = 6
                    elif lexema.lower() == "estilo":
                        self.token2.append(lexema)
                        lexema = ""
                        self.estado_actual = 7
                    elif lexema in self.palabras_clave:
                        self.token.append(lexema)
                elif char == '<' or char == "=" or char == "/":
                    if lexema != "":
                        self.token2.append(lexema)
                        lexema = ""
                else:
                    self.errores.append(errores(self.fila, self.columna, char))

            elif self.estado_actual == 1:
                if char in self.numeros:
                    lexema += char
                elif char == "<" or char == "=" or char == "/" or char == ">":
                    self.token.append(lexema)
                    lexema = ""
                    self.estado_actual = 0
                elif char == "." and primerPunto == True:
                    lexema += char
                    primerPunto = False
                else:
                    self.errores.append(errores(self.fila, self.columna, char))

            elif self.estado_actual == 2:
                if char in self.numeros:
                    primerPunto == False
                    lexema += char
                    self.estado_actual == 1
                else:
                    self.errores.append(errores(self.fila, self.columna, char))

            elif self.estado_actual == 3:
                if char != "<":
                    self.descripcion["contenido"] += char
                else:
                    self.estado_actual = 0
            elif self.estado_actual == 4:
                if char != "<":
                    self.titulo["contenido"] += char
                else:
                    self.estado_actual = 0
            elif self.estado_actual == 5:
                if char == "<":
                    self.estado_actual = 0
            elif self.estado_actual == 6:
                if char == "<":
                    self.estado_actual = 0
            # estado de Estilo
            elif self.estado_actual == 7:
                if char.lower() in self.letras:
                    lexema += char
                    if lexema.lower() == "titulo":
                        self.token2.append(lexema)
                        lexema = ""
                        self.estado_actual = 8
                    elif lexema.lower() == "descripcion":
                        self.token2.append(lexema)
                        lexema = ""
                        self.estado_actual = 9
                    elif lexema.lower() == "contenido":
                        self.token2.append(lexema)
                        lexema = ""
                        self.estado_actual = 10
                elif char != '<' and char != "=" and char != "/" and char != ">":
                    self.errores.append(errores(self.fila, self.columna, char))
            elif self.estado_actual == 8:
                if char.lower() in self.letras:
                    lexema += char
                    if lexema.lower() in self.colores:
                        self.titulo["color"] = lexema
                        lexema = ""
                elif char == "=":
                    if lexema.lower() == "color":
                        self.token2.append(lexema)
                        lexema = ""
                    elif lexema.lower() == "tamanio":
                        self.token2.append(lexema)
                        lexema = ""
                elif char in self.numeros:
                    lexema += char
                elif char == "/" or char == ">":
                    self.titulo["tamano"] = lexema
                    lexema = ""
                    self.estado_actual = 7
                else:
                    self.errores.append(errores(self.fila, self.columna, char))
            elif self.estado_actual == 9:
                if char.lower() in self.letras:
                    lexema += char
                    if lexema.lower() in self.colores:
                        self.descripcion["color"] = lexema
                        lexema = ""
                elif char == "=":
                    if lexema.lower() == "color":
                        self.token2.append(lexema)
                        lexema = ""
                    elif lexema.lower() == "tamanio":
                        self.token2.append(lexema)
                        lexema = ""
                elif char in self.numeros:
                    lexema += char
                elif char == "/" or char == ">":
                    self.descripcion["tamano"] = lexema
                    lexema = ""
                    self.estado_actual = 7
                else:
                    self.errores.append(errores(self.fila, self.columna, char))
            elif self.estado_actual == 10:
                if char.lower() in self.letras:
                    lexema += char
                    if lexema.lower() in self.colores:
                        self.contenido["color"] = lexema
                        lexema = ""
                elif char == "=":
                    if lexema.lower() == "color":
                        self.token2.append(lexema)
                        lexema = ""
                    elif lexema.lower() == "tamanio":
                        self.token2.append(lexema)
                        lexema = ""
                elif char in self.numeros:
                    lexema += char
                elif char == "/" or char == ">":
                    self.contenido["tamano"] = lexema
                    lexema = ""
                    self.estado_actual = 7
                else:
                    self.errores.append(errores(self.fila, self.columna, char))
            self.columna += 1
            self.cadena = self.cadena[1:]
