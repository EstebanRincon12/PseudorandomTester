# Librerias
import math
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import filedialog

from NumbersTest import MeanTest as MT
from NumbersTest import VarianceTest as VT
from NumbersTest import KSTest as KST
from NumbersTest import ChiTest as CT
from NumbersTest import PokerTest as PT

import csv


class meanTestFrame(ttk.Frame):
    # pestaña Prueba de medias
    def __init__(self,parent_file_upload, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent_file_upload = parent_file_upload
        print(self.parent_file_upload.csvPatch)
        self.gInit = ttk.Button(self, text="Iniciar Prueba", command=self.meanFrame)
        self.gInit.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
        
    def meanFrame(self):
        meanResult = MT.verifyMean(self.parent_file_upload.csvPatch)
        meansLabel = tk.Label(self, justify="left")
        meansLabel2 = tk.Label(self, justify="left")
        meansLabel["text"] = "Prueba de medios:" + (" Paso" if meanResult[0] else " No paso")
        meansLabel2["text"] = "Media: {}\nMedia máxima: {}".format(meanResult[2], meanResult[1])
       
        meansLabel.grid(row=1, column=0, padx=10, pady=8, sticky="w")
        meansLabel2.grid(row=2, column=0, padx=10, pady=8)

        

class VarianceTestFrame(ttk.Frame):
    # pestaña Prueba de Varianza
    def __init__(self, parent_file_upload, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent_file_upload = parent_file_upload
        print(self.parent_file_upload.csvPatch)
        self.gInit = ttk.Button(self, text="Iniciar Prueba", command=self.varianceFrame)
        self.gInit.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
        

    def varianceFrame(self):
        varianceResult =  VT.verifyVariance(self.parent_file_upload.csvPatch)
        varianceLabel = tk.Label(self, justify="left")
        varianceLabel2 = tk.Label(self, justify="left")
        varianceLabel["text"] = "Prueba de varianza:" + (" Paso" if varianceResult[0] else " No paso")
        
        varianceLabel2["text"] ="Limite inferior: {} \nLimite Superior: {} \nVarianza: {}".format(varianceResult[1] ,varianceResult[2], varianceResult[3])
        varianceLabel.grid(row=1, column=0, padx=10, pady=8, sticky="w")
        varianceLabel2.grid(row=2, column=0, padx=10, pady=8, sticky="w")


class ChiSquareTestFrame(ttk.Frame):
    # pestaña Prueba de chi2
    def __init__(self, parent_file_upload, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent_file_upload = parent_file_upload
        self.gInit = ttk.Button(self, text="Iniciar Prueba", command=self.chiSquareFrame)
        self.gInit.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        self.table = ttk.Treeview(self, columns=("col0", "col1", "col2", "col3", "col4"), show="headings")
        self.table.heading("col0", text="i")
        self.table.column("col0", width=15)
        self.table.heading("col1", text="Inicial")
        self.table.column("col1", width=120)
        self.table.heading("col2", text="Final")
        self.table.column("col2", width=120)
        self.table.heading("col3", text="F Esp")
        self.table.column("col3", width=120)
        self.table.heading("col4", text="F obt")
        self.table.column("col4", width=40)

        self.totalFrequencyLabel = tk.Label(self)

    def chiSquareFrame(self):
        chiResult = CT.verifyChiTest(self.parent_file_upload.csvPatch)
        chiLabel = tk.Label(self)
        chiLabel["text"] = "Prueba chi cuadrado: " + ("Pasó" if chiResult[0] else "No paso")
        chiLabel.grid(row=1, column=0, padx=10, pady=8, sticky="w")

        self.table.delete(*self.table.get_children())  # Limpia la tabla antes de llenarla con datos nuevos

        for i in range(chiResult[3]):
            self.table.insert("", "end", values=(i, chiResult[1] + (i * chiResult[2]), chiResult[1] + ((i + 1) * chiResult[2]), (i + 1) * chiResult[3], chiResult[4][i]))

        self.table.column("col0", anchor="center")
        self.table.column("col1", anchor="center")
        self.table.column("col2", anchor="center")
        self.table.column("col3", anchor="center")
        self.table.column("col4", anchor="center")

        # Ajustar el tamaño de las columnas según tus preferencias
        self.table.column("#1", width=15)
        self.table.column("#2", width=125)
        self.table.column("#3", width=125)
        self.table.column("#4", width=40)
        self.table.column("#5", width=40)

        self.table.grid(row=2, column=0, padx=10, pady=8, sticky="w")

        # Permitir que la tabla se expanda verticalmente
        self.table.grid_rowconfigure(0, weight=1)
        self.table.grid_rowconfigure(1, weight=1)

        self.totalFrequencyLabel["text"] = "Frecuencia acumulada obtenida: {} \nValor maximo que puede tener la frecuencia acumulada: {}".format(chiResult[5], chiResult[6])
        self.totalFrequencyLabel.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        
class KSTestFrame(ttk.Frame):
    # pestaña Prueba de KS
    def __init__(self, parent_file_upload, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent_file_upload = parent_file_upload
        self.gInit = ttk.Button(self, text="Iniciar Prueba", command=self.ksFrame)
        self.gInit.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        self.table = ttk.Treeview(self, columns=("col0", "col1", "col2", "col3", "col4", "col5"), show="headings")
        self.table.heading("col0", text="i")
        self.table.column("col0", width=15)
        self.table.heading("col1", text="Inicial")
        self.table.column("col1", width=120)
        self.table.heading("col2", text="Final")
        self.table.column("col2", width=120)
        self.table.heading("col3", text="F Esp")
        self.table.column("col3", width=120)
        self.table.heading("col4", text="F obt")
        self.table.column("col4", width=40)
        self.table.heading("col5", text="Dif")
        self.table.column("col5", width=120)

        self.totalFrequencyLabel = tk.Label(self, justify="left")

    def ksFrame(self):
        ksResult = KST.verifyKSTest(self.parent_file_upload.csvPatch)
        ksLabel = tk.Label(self, justify="left")
        ksLabel["text"] = "Prueba ks:" + ("Paso" if ksResult[0] else "No paso")
        ksLabel.grid(row=1, column=0, padx=10, pady=8, sticky="w")

        self.table.delete(*self.table.get_children())  # Limpia la tabla antes de llenarla con datos nuevos

        for i in range(len(ksResult[3])):
            self.table.insert("", "end", values=(i, ksResult[1] + (i * ksResult[2]), ksResult[1] + ((i + 1) * ksResult[2]), ksResult[4] * i, (ksResult[3][i]), ksResult[5][i]))

        self.table.column("col0", anchor="center")
        self.table.column("col1", anchor="center")
        self.table.column("col2", anchor="center")
        self.table.column("col3", anchor="center")
        self.table.column("col4", anchor="center")
        self.table.column("col5", anchor="center")

        self.table.grid(row=2, column=0, padx=10, pady=8, sticky="w")  # Cambio a grid

        self.totalFrequencyLabel["text"] = ("Frecuencia acumulada maxima obtenida: {}\nValor maximo que puede tener la frecuencia acumulada: {}"  ).format(max(ksResult[5]), KST.findValueKs(ksResult[6]))
        self.totalFrequencyLabel.grid(row=3, column=0, padx=10, pady=5, sticky="w")  # Cambio a grid



class fileUpload(ttk.Frame):
    # pestaña para subir archivo
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.verifyLabel = tk.Label(self)
        self.verifyLabel["text"] = "ultimo guardado"
        self.verifyLabel.config(bg="blue")
        self.csvPatch = "RiList.csv"
        self.verifyLabel.grid(row=0, column=3, padx=12, pady=10)
        # Boton encontrar archivo
        self.gAd = ttk.Button(self, text="Abrir archivo", command=self.openCsvFile)
        self.gAd.grid(row=0, column=1, padx=10, pady=10)
        self.csvPatchLabel = tk.Label(self)
        self.csvPatchLabel["text"] = "Ruta del archivo csv"
        self.csvPatchLabel.grid(row=0, column=0, padx=10, pady=10)
    
    def openCsvFile(self):
        self.csvPatch = filedialog.askopenfilename(title="abrir", initialdir="C:/",
                                                   filetypes=(("Archivo CSV", "*.csv"), ("Todos los Archivos", "*.*")))

        self.verifyLabel = tk.Label(self)
        if self.csvPatch.split(".")[1] == "csv":
            self.verifyLabel["text"] = ("csv Encontrado")
            self.verifyLabel.config(bg="green")
        else:
            mb.showerror("Error", "el csv seleccionado es invalido, se usara el por csv por defecto")
            self.verifyLabel["text"] = ("Csv invalido")
            self.verifyLabel.config(bg="red")
            self.csvPatch = "RiList.csv"
        self.verifyLabel.grid(row=0, column=3, padx=10, pady=10)

class pokerFrame(ttk.Frame):
    # pestaña Prueba de Poker
    def __init__(self,parent_file_upload ,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent_file_upload = parent_file_upload
        self.gInit = ttk.Button(self, text="Iniciar Prueba", command=self.pokerFrame)
        self.gInit.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        self.table = ttk.Treeview(self, columns=("col0", "col1", "col2", "col3"), show="headings")
        self.table["columns"] = ("col0", "col1", "col2", "col3")
        self.table.heading("col0", text="Mano")
        self.table.column("col0", width=40)
        self.table.heading("col1", text="Frecuencia obtenida")
        self.table.column("col1", width=60)
        self.table.heading("col2", text="Probabilidad esperada")
        self.table.column("col2", width=60)
        self.table.heading("col3", text="Estadistico chi 2")
        self.table.column("col3", width=60)

        self.totalFrequencyLabel = tk.Label(self, justify="left")

    def pokerFrame(self):
        pokerResult = PT.verifyPoker(self.parent_file_upload.csvPatch)

        pokerLabel = tk.Label(self)
        pokerLabel["text"] = "Prueba_poker:"+ ("Paso" if pokerResult[0] else "No paso")
        pokerLabel.grid(row=1, column=0, padx=10, pady=8, sticky="w")

        self.table.delete(*self.table.get_children())  # Limpia la tabla antes de llenarla con datos nuevos

        letterList = ["D", "O", "T", "K", "P", "Q"]
        for i in letterList:
            self.table.insert("", "end", values=(i, pokerResult[1][i], pokerResult[2][i], pokerResult[5][letterList.index(i)]))

        self.table.column("col0", anchor="center")
        self.table.column("col1", anchor="center")
        self.table.column("col2", anchor="center")

        # Ajustar el tamaño de las columnas según tus preferencias
        self.table.column("#1", width=40)
        self.table.column("#2", width=60)
        self.table.column("#3", width=120)

        self.table.grid(row=2, column=0, padx=10, pady=8, sticky="w")

        # Permitir que la tabla se expanda verticalmente
        self.table.grid_rowconfigure(0, weight=1)
        self.table.grid_rowconfigure(1, weight=1)

        self.totalFrequencyLabel["text"] = "Frecuencia acumulada obtenida: {}\nValor maximo que puede tener la frecuencia acumulada: {}".format(pokerResult[4],pokerResult[3]) 
        self.totalFrequencyLabel.grid(row=3, column=0, padx=10, pady=5, sticky="w")

# Configuracion de pestañas
class Interface(ttk.Frame):
    
    def __init__(self, principalV):
        super().__init__(principalV)
        # título principal de la ventana
        principalV.title("Prueba de números aleatorios")
        
        # Crear el Notebook
        self.notebook = ttk.Notebook(self, width=600, height=500)
        
        # Crear una instancia de fileUpload y pasarla a meanTestFrame
        
        self.file_upload = fileUpload(self.notebook)
        mean_frame = meanTestFrame(self.file_upload,self.notebook)
        variance_frame = VarianceTestFrame(self.file_upload, self.notebook)
        chi_square_frame = ChiSquareTestFrame(self.file_upload,self.notebook)
        ks_frame = KSTestFrame(self.file_upload,self.notebook)
        poker_frame = pokerFrame(self.file_upload,self.notebook)
        
        # Agregar pestañas al Notebook
        self.notebook.add(self.file_upload, text="Subir Archivo", padding=8)
        self.notebook.add(mean_frame, text="Prueba de Medios", padding=8)
        self.notebook.add(variance_frame, text="Prueba de Varianza", padding=8)
        self.notebook.add(chi_square_frame, text="Prueba de Chi Cuadrado", padding=8)
        self.notebook.add(ks_frame, text="Prueba de KS", padding=8)
        self.notebook.add(poker_frame, text="Prueba de poker", padding=8)
        
        self.notebook.pack(padx=10, pady=10)
        self.pack()


##############
try:
    principalV = tk.Tk()
    principalV.geometry('600x500')
    principalV.resizable(width=False, height=False)
    app = Interface(principalV)
    app.mainloop()
except Exception as e:
    print("Ocurrió un error:", str(e))
    sys.exit(0)

