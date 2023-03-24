from enum import auto
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from analizadorLexico import automata
import webbrowser
from operaciones import programa


class Principal(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master, height=450, width=800)
        self.master = master
        self.direccionGlobal = ""
        self.pack()
        self.create_widgets()
        self.errors = []
        self.colores = {"blanco": "withe", "rojo": "red", "amarillo": "yellow",
                        "azul": "blue", "verde": "green", "negro": "black", "gris": "grays"}

    def create_widgets(self):
        # archivo
        self.buttonAnalizar = tk.Button(
            self, text="Analizar", command=self.analizar)
        self.buttonAnalizar.place(x=20, y=20)
        self.buttonErrores = tk.Button(
            self, text="Errores", command=self.errores)
        self.buttonErrores.place(x=20, y=60)
        self.textBox = tk.Text(self, height=23, width=75)
        self.textBox.place(x=160, y=20)
        self.buttonSalir = tk.Button(
            self, text="Salir", command=self.master.destroy)
        self.buttonSalir.place(x=310, y=400)
        self.buttonAbrir = tk.Button(
            self, text="Abrir", command=self.abrirArchivo)
        self.buttonAbrir.place(x=380, y=400)
        self.buttonGuardar = tk.Button(
            self, text="Guardar", command=self.guardarArchivo)
        self.buttonGuardar.place(x=460, y=400)
        self.buttonGuardarComo = tk.Button(
            self, text="Guardar como...", command=self.guardarComo)
        self.buttonGuardarComo.place(x=550, y=400)
        # ayuda
        self.label2 = tk.Label(self, text="Ayuda")
        self.label2.place(x=20, y=270)
        self.buttonManualUsuario = tk.Button(
            self, text="Manual de Usuario", command=self.manualUsuario)
        self.buttonManualUsuario.place(x=20, y=300)
        self.buttonManualTecnico = tk.Button(
            self, text="Manual Técnico", command=self.manualTecnico)
        self.buttonManualTecnico.place(x=20, y=340)
        self.buttonTemaAyuda = tk.Button(
            self, text="Tema de ayuda", command=self.temaAyuda)
        self.buttonTemaAyuda.place(x=20, y=380)

    def abrirArchivo(self):
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )
        try:
            direccion = filedialog.askopenfilename(
                initialdir="/", title="Escoge el Archivo", filetypes=filetypes)
            if direccion != "":
                self.direccionGlobal = direccion
                file = open(self.direccionGlobal, mode="r", encoding="utf-8")
                self.textBox.delete(1.0, tk.END)
                for linea in file:
                    self.textBox.insert(tk.END, linea)
                file.close()
        except:
            messagebox.showerror("Error", "Error al cargar el archivo")

    def guardarArchivo(self):
        self.guardar("w", self.direccionGlobal)

    def guardarComo(self):
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )
        direccionNueva = filedialog.asksaveasfilename(
            initialdir="/", title="Escoge la carpeta", filetypes=filetypes, defaultextension="lfp")
        if direccionNueva != "":
            self.direccionGlobal = direccionNueva
            self.guardar("x", direccionNueva)

    def guardar(self, mode="", direccion=""):
        try:
            file = open(direccion, mode=mode, encoding="utf-8")
            file.write(self.textBox.get("1.0", tk.END))
            file.close()
            messagebox.showinfo("Información", "Se ha editado correctamente")
        except:
            messagebox.showwarning("Cuidado", "No se pudo guardar el archivo")

    def analizar(self):
        if self.direccionGlobal != "":
            cadena = ""
            cadena = open(self.direccionGlobal, 'r').read()
            autom = automata(cadena)
            autom.analizar()
            self.errors = autom.errores
            cosa = programa()
            cosa.analizar_lexico(autom.token)
            cosa.leer_operaciones()
            todasOperaciones = ""
            for ope in cosa.lista_operaciones:
                todasOperaciones += ope+"<br>"
            # for error in autom.errores:
                #print("fila: "+str(error.fila)+" Columna: "+str(error.columna)+" Error:"+ error.error)

            salida = open("analisis.html", "w")
            salida.write("""<!DOCTYPE html>
                            <html lang="en">
                            <head>
                            <meta charset="UTF-8">
                            <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .titulo{
            color: """+self.colores[autom.titulo["color"].lower()]+""";
            font-size: """+autom.titulo["tamano"]+"""mm;
        }
        .descripcion{
            color: """+self.colores[autom.descripcion["color"].lower()]+""";
            font-size: """+autom.descripcion["tamano"]+"""mm;
        }
        .contenido{
            color: """+self.colores[autom.contenido["color"].lower()]+""";
            font-size: """+autom.contenido["tamano"]+"""mm;
        }
    </style>
</head>
<body>
    <p class="titulo">"""+autom.titulo["contenido"]+"""</p>
    <p class="descripcion">"""+autom.descripcion["contenido"]+"""</p>
    <p class="contenido">"""+todasOperaciones+"""</p>
</body>
</html>""")
            webbrowser.open("analisis.html")
        else:
            messagebox.showwarning("Cuidado", "Cargue un archivo primero")

    def errores(self):
        arriba = """<!DOCTYPE html>
                <html lang="en">
                    <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Document</title>
                </head>
                <body>
                    <table border="1">
                        <tr>
                        <td>NO.</td>
                        <td>Lexema</td>
                        <td>Tipo</td>
                        <td>Columna</td>
                        <td>Fila</td>
                        </tr>"""
        i = 0
        for error in self.errors:
            i += 1
            arriba += """<tr>
                    <td>"""+str(i)+"""</td>
                    <td>"""+error.error+"""</td>
                    <td>Lexico</td>
                    <td>"""+str(error.columna)+"""</td>
                 <td>"""+str(error.fila)+"""</td>
                </tr>"""
        arriba += """</table></body></html>"""
        salidaError = open("ERRORES_202111835.html", "w")
        salidaError.write(arriba)
        webbrowser.open("ERRORES_202111835.html")

    def manualTecnico(self):
        webbrowser.open("manualTecnico.pdf")

    def manualUsuario(self):
        webbrowser.open("manualUsuario.pdf")

    def temaAyuda(self):
        messagebox.showinfo(
            "Información", "Nombre: Rubén Alejandro Ralda Mejia\nCarnet: 202111835")


root = tk.Tk()
root.title("Menu")
app = Principal(master=root)
app.mainloop()
