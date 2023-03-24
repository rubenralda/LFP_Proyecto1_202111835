import math

class programa():
    def __init__(self):
        self.lista_operaciones=[]
        self.aux = []
        self.texto = ""

    def analizar_lexico(self,token=[]):
        self.tokens = token
        self.tokens.append("asdfasd")
        

    def expresion(self):
        if self.tokens[0]=="Numero":
            self.aux.append(self.tokens.pop(0))
            numero = self.tokens[0]
            self.aux.append(self.tokens.pop(0))
            self.aux.append(self.tokens.pop(0))
            return str(numero)
        if self.tokens[0]=="SUMA":
            self.aux.append(self.tokens.pop(0))
            return "("+str(self.expresion())+")+("+ str(self.expresion())+")"
        if self.tokens[0]=="RESTA":
            self.aux.append(self.tokens.pop(0))
            return "("+str(self.expresion())+")-("+ str(self.expresion())+")"
        if self.tokens[0]=="MULTIPLICACION":
            self.aux.append(self.tokens.pop(0))
            return "("+str(self.expresion())+")*("+ str(self.expresion())+")"
        if self.tokens[0]=="DIVISION":
            self.aux.append(self.tokens.pop(0))
            return "("+str(self.expresion())+")/("+ str(self.expresion())+")"
        if self.tokens[0]=="POTENCIA":
            self.aux.append(self.tokens.pop(0))
            return "("+str(self.expresion())+")^("+ str(self.expresion())+")"
        if self.tokens[0]=="RAIZ":
            self.aux.append(self.tokens.pop(0))
            return "("+str(self.expresion())+")^(1/"+ str(self.expresion())+")"
        if self.tokens[0]=="INVERSO":
            self.aux.append(self.tokens.pop(0))
            return "(1/"+str(self.expresion())+")"
        if self.tokens[0]=="SENO":
            self.aux.append(self.tokens.pop(0))
            return "SENO("+str(self.expresion())+")"
        if self.tokens[0]=="COSENO":
            self.aux.append(self.tokens.pop(0))
            return "COSENO("+str(self.expresion())+")"
        if self.tokens[0]=="TANGENTE":
            self.aux.append(self.tokens.pop(0))
            return "TAN("+str(self.expresion())+")"
        if self.tokens[0]=="MOD":
            self.aux.append(self.tokens.pop(0))
            return "("+str(self.expresion())+"%"+ str(self.expresion())+")"
        return None

    def operacion(self):
        if self.aux[0]=="Numero":
            self.aux.pop(0)
            numero = self.aux[0]
            self.aux.pop(0)
            self.aux.pop(0)
            return float(numero)
        if self.aux[0]=="SUMA":
            self.aux.pop(0)
            return self.operacion() + self.operacion()
        if self.aux[0]=="RESTA":
            self.aux.pop(0)
            return self.operacion() - self.operacion()
        if self.aux[0]=="MULTIPLICACION":
            self.aux.pop(0)
            return self.operacion() * self.operacion()
        if self.aux[0]=="DIVISION":
            self.aux.pop(0)
            return self.operacion() / self.operacion()
        if self.aux[0]=="POTENCIA":
            self.aux.pop(0)
            return self.operacion()**self.operacion()
        if self.aux[0]=="RAIZ":
            self.aux.pop(0)
            return self.operacion()**(1/self.operacion())
        if self.aux[0]=="INVERSO":
            self.aux.pop(0)
            return 1/self.operacion()
        if self.aux[0]=="SENO":
            self.aux.pop(0)
            return math.sin(self.operacion())
        if self.aux[0]=="COSENO":
            self.aux.pop(0)
            return math.cos(self.operacion())
        if self.aux[0]=="TANGENTE":
            self.aux.pop(0)
            return math.tan(self.operacion())
        if self.aux[0]=="MOD":
            self.aux.pop(0)
            return self.operacion() % self.operacion()

    def leer_operaciones(self):
        expresion = self.expresion()
        while expresion != None:
            self.lista_operaciones.append(expresion+"="+str(self.operacion()))
            expresion = self.expresion()


