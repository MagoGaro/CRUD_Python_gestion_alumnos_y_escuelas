from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
#from tkinter import scrolledtext as st
from ttkthemes import themed_tk
from PIL import ImageTk,Image
import consultas

class GestionAlumnos:
    def __init__(self):
            
            self.consultitas=consultas.consultas_db()
            self.win = themed_tk.ThemedTk(theme="black")
            self.win.title("Control de Gastos")
            self.win.geometry("1070x500")
            self.win.resizable(False,False)
            self.win.config(bg="gray")
            self.cuaderno1 = ttk.Notebook(self.win)
            self.gestionAlumno()
            self.gestionEscuela()
            self.gestionLocalidad()
            self.gestionProvincia()
            self.cuaderno1.grid(row=0,column=0,padx=20,pady=20)
            self.botonlicencia=ttk.Button(self.win, text="Licencia", command=self.licencia)
            self.botonlicencia.place(x=400, y=450)
            self.botonacercade=ttk.Button(self.win, text="Acerca De..", command=self.acercaDe)
            self.botonacercade.place(x=550, y=450)
            self.labelegajo=Label(self.win,bg="gray", fg="darkslateblue" ,text="©(2023) por Gabriel S. Roman para CaC 4.0 - Big Data")
            self.labelegajo.grid(row=2,column=0,padx=20,pady=5)
            
            
            self.win.mainloop()
    
    
    def gestionAlumno(self):
                #global imagen
                self.pagina0 = ttk.Frame(self.cuaderno1)
                self.cuaderno1.add(self.pagina0, text="Gestion Alumno")
                self.labelframe1 =LabelFrame(self.pagina0, text="Datos Alumno",fg="white",bg="slategray",font=("Arial"),bd=5)
                self.labelframe1.grid(row=0,column=0,padx=100,pady=30)
                self.labelegajo=Label(self.labelframe1, text="N° Legajo:")
                self.labelegajo.grid(row=0,column=0,padx=20,pady=5,sticky="e")
                self.labelegajo.config(fg="white",bg="slategray")
                self.botonbuscar=ttk.Button(self.labelframe1, text="Buscar" ,command=self.buscarAlumno)
                self.botonbuscar.grid(row=0,column=2,padx=5,pady=5)
                self.botonlimpiar=ttk.Button(self.labelframe1, text="Limpiar", command=self.limpiar)
                self.botonlimpiar.grid(row=0,column=3,padx=5,pady=5)
                self.n_legajo=StringVar()
                self.entrylegajo=Entry(self.labelframe1,highlightcolor= "deepskyblue", highlightthickness=2, textvariable=self.n_legajo)
                self.entrylegajo.focus()
                self.entrylegajo.grid(row=0,column=1,padx=10,pady=5)
                self.labelnom=Label(self.labelframe1, text="Nombre:")
                self.labelnom.grid(row=1,column=0,padx=20,pady=5,sticky="e")
                self.labelnom.config(fg="white",bg="slategray")
                self.nom_alumno=StringVar()
                self.entrynom=Entry(self.labelframe1,highlightcolor= "deepskyblue", highlightthickness=2, textvariable=self.nom_alumno)
                self.entrynom.grid(row=1,column=1,padx=10,pady=5)
                self.labelape=Label(self.labelframe1, text="Apellido:")
                self.labelape.grid(row=1,column=2,padx=20,pady=5,sticky="e")
                self.labelape.config(fg="white",bg="slategray")
                self.ape_alumno=StringVar()
                self.entryape=Entry(self.labelframe1,highlightcolor= "deepskyblue", highlightthickness=2, textvariable=self.ape_alumno)
                self.entryape.grid(row=1,column=3,padx=10,pady=5)
                self.labelemail=Label(self.labelframe1, text="Email:")
                self.labelemail.grid(row=2,column=0,padx=20,pady=5,sticky="e")
                self.labelemail.config(fg="white",bg="slategray")
                self.email_alumno=StringVar()
                self.entryemail=Entry(self.labelframe1,highlightcolor= "deepskyblue", highlightthickness=2, textvariable=self.email_alumno)
                self.entryemail.grid(row=2,column=1,padx=10,pady=5)
                self.labelgenero=Label(self.labelframe1, text="Genero:")
                self.labelgenero.grid(row=2,column=2,padx=20,pady=5,sticky="e")
                self.labelgenero.config(fg="white",bg="slategray")
                self.gene_alumno=StringVar()
                self.entrygene=ttk.Combobox(self.labelframe1,foreground="black",background="white",state="readonly",values=["Selecicone uno","Masculino", "Femenino"],textvariable=self.gene_alumno)
                self.entrygene.current(0)
                self.entrygene.grid(row=2,column=3,padx=10,pady=5)
                self.labelgrado=Label(self.labelframe1, text="Grado:")
                self.labelgrado.grid(row=3,column=0,padx=20,pady=5,sticky="e")
                self.labelgrado.config(fg="white",bg="slategray")
                self.grado_alumno=IntVar()
                self.entrygrado=Entry(self.labelframe1,highlightcolor= "deepskyblue", highlightthickness=2, textvariable=self.grado_alumno)
                self.entrygrado.grid(row=3,column=1,padx=10,pady=5)
                self.labelprom=Label(self.labelframe1,text="Promedio:")
                self.labelprom.grid(row=3,column=2,padx=20,pady=5,sticky="e")
                self.labelprom.config(fg="white",bg="slategray")
                self.prom_alumno=DoubleVar()
                self.entryprom=Entry(self.labelframe1,highlightcolor= "deepskyblue", highlightthickness=2,textvariable=self.prom_alumno)
                self.entryprom.grid(row=3,column=3,padx=10,pady=5)
                self.labelesc=Label(self.labelframe1,text="Escuela:")
                self.labelesc.grid(row=4,column=0,padx=20,pady=5,sticky="e")
                self.labelesc.config(fg="white",bg="slategray")
                escuelas = self.consultitas.buscar_escuelas()
                self.escuela_alumno = StringVar()
                self.escuela_alumno.set("Seleccione una Opción")
                self.opcionesc = OptionMenu(self.labelframe1, self.escuela_alumno, *escuelas)
                self.opcionesc.grid(row=4, column=1,padx=20,pady=5, columnspan=10)
                self.opcionesc.config(width=50)
                self.labelprov=Label(self.labelframe1,text="Provincia:")
                self.labelprov.grid(row=5,column=0,padx=20,pady=5,sticky="e")
                self.labelprov.config(fg="white",bg="slategray")
                provincias = self.consultitas.buscar_provincias()
                self.provincia_alumno = StringVar()
                self.provincia_alumno.set("Seleccione una Opción")
                self.opcionprov = OptionMenu(self.labelframe1, self.provincia_alumno, *provincias)
                self.opcionprov.grid(row=5, column=1,padx=20,pady=5, columnspan=10)
                self.opcionprov.config(width=50)
                self.botonagregar=ttk.Button(self.labelframe1, text="Agregar", command=self.cargarAlumno)
                self.botonagregar.grid(row=6,column=1,padx=10,pady=5)
                self.botonactualizar=ttk.Button(self.labelframe1, text="Actualizar", command=self.actualizarAlumno)
                self.botonactualizar.grid(row=6,column=2,padx=10,pady=5)
                self.botoneliminar=ttk.Button(self.labelframe1, text="Eliminar", command=self.borrarAlumno)
                self.botoneliminar.grid(row=6,column=3,padx=10,pady=5)
    
    def limpiar(self):
        self.nom_alumno.set("")
        self.ape_alumno.set("")
        self.prom_alumno.set("")
        self.email_alumno.set("")
        self.grado_alumno.set("")
        self.escuela_alumno.set("Seleccione una Opción")
        self.provincia_alumno.set("Seleccione una Opción")
        self.entrygene.current(0)
        self.entrylegajo.config(state=NORMAL)
        
    def buscarAlumno(self):
        
        if self.n_legajo.get() != "":
            if self.n_legajo.get().isnumeric():
                datos = self.n_legajo.get()
                int(datos)
                respuesta = self.consultitas.buscar_alumno(datos)
                if respuesta != []:
                #print(respuesta)
                    self.nom_alumno.set(respuesta[0][1])
                    self.ape_alumno.set(respuesta[0][2])
                    self.prom_alumno.set(respuesta[0][3])
                    self.email_alumno.set(respuesta[0][4])
                    self.grado_alumno.set(respuesta[0][5])
                    self.escuela_alumno.set(respuesta[0][6])
                    self.provincia_alumno.set(respuesta[0][7])
                    self.gene_alumno.set(respuesta[0][8])
                    self.entrylegajo.config(state=DISABLED)
                else:
                    mb.showerror("Error","El N° Legajo no existe")
            else:
                mb.showerror("Error","Inserte N° Legajo valido")
                
        else:
            mb.showerror("Error","El N° Legajo no puede quedar vacio")


    def cargarAlumno(self):
        
        if self.n_legajo != 0:
            datos = (self.escuela_alumno.get(),self.n_legajo.get(),self.nom_alumno.get(),self.ape_alumno.get(),self.prom_alumno.get(),self.grado_alumno.get(),self.email_alumno.get(),self.gene_alumno.get(),self.provincia_alumno.get())
            
            self.consultitas.alta_alumno(datos)
            mb.showinfo("Informacion","Alumno cargado exitosamente")
            self.limpiar()
        else:
            mb.showerror("Informacion","Es obligatorio rellenar todos los campos ")

    def actualizarAlumno(self):
        try:
            datos = (self.escuela_alumno.get(),self.n_legajo.get(),self.nom_alumno.get(),self.ape_alumno.get(),self.prom_alumno.get(),self.grado_alumno.get(),self.email_alumno.get(),self.gene_alumno.get(),self.provincia_alumno.get())
            
            self.consultitas.actualizar_alumno(datos)
            mb.showinfo("Informacion","Alumno actualizado exitosamente")
        except:
            mb.showerror("Error","Hubo un problema al procesar la solicitud")
    
    def borrarAlumno(self):
        valor = mb.askquestion("Sesión", "¿Desea eliminar el registro?")
        if valor == "yes":
            try:
                datos = self.n_legajo.get()
                int(datos)
                self.consultitas.baja_alumno(datos)
                mb.showinfo("Informacion","Alumno eliminado exitosamente")
                self.limpiar()
            except:
                mb.showerror("Error","Hubo un problema al procesar la solicitud")

    def gestionEscuela(self):
                #global imagen
                self.pagina2 = ttk.Frame(self.cuaderno1)
                self.cuaderno1.add(self.pagina2, text="Gestion Escuela")
                self.labelframe1 =LabelFrame(self.pagina2, text="Datos Escuela",fg="white",bg="slategray",font=("Arial"),bd=5)
                self.labelframe1.grid(row=0,column=0,padx=100,pady=30)
                self.esc_nombre=Label(self.labelframe1, text="Escuela:")
                self.esc_nombre.grid(row=0,column=0,padx=20,pady=5,sticky="e")
                self.esc_nombre.config(fg="white",bg="slategray")
                escuelas2 = self.consultitas.buscar_escuelas()
                self.escuela_nom = StringVar()
                self.opcionesc2 = OptionMenu(self.labelframe1, self.escuela_nom, *escuelas2)
                self.opcionesc2.grid(row=0, column=1,padx=20,pady=5, columnspan=10)
                self.opcionesc2.config(width=50)
                self.botonbuscar2=ttk.Button(self.labelframe1, text="Buscar" ,command=self.buscarAlumno)
                self.botonbuscar2.grid(row=0,column=11,padx=5,pady=5)
                self.botonlimpiar2=ttk.Button(self.labelframe1, text="Limpiar", command=self.limpiar)
                self.botonlimpiar2.grid(row=0,column=13,padx=5,pady=5)
                self.esc_nombre2=Label(self.labelframe1, text="Nombre:")
                self.esc_nombre2.grid(row=1,column=0,padx=20,pady=5,sticky="e")
                self.esc_nombre2.config(fg="white",bg="slategray")
                self.nom_esc2=StringVar()
                self.entrynom2=Entry(self.labelframe1,highlightcolor= "deepskyblue", highlightthickness=2, textvariable=self.nom_esc2)
                self.entrynom2.grid(row=1,column=2,padx=10,pady=5)
                self.esc_capa=Label(self.labelframe1, text="Capacidad:")
                self.esc_capa.grid(row=1,column=4,padx=20,pady=5,sticky="e")
                self.esc_capa.config(fg="white",bg="slategray")
                self.esc_capa2=IntVar()
                self.entrynom2=Entry(self.labelframe1,highlightcolor= "deepskyblue", highlightthickness=2, textvariable=self.esc_capa2)
                self.entrynom2.grid(row=1,column=5,padx=10,pady=5)
                self.esc_localidad=Label(self.labelframe1, text="Localidad:")
                self.esc_localidad.grid(row=2,column=0,padx=20,pady=5,sticky="e")
                self.esc_localidad.config(fg="white",bg="slategray")
                localidad2 = self.consultitas.buscar_localidades()
                self.esc_localidad2 = StringVar()
                self.opcionesc3 = OptionMenu(self.labelframe1, self.esc_localidad2, *localidad2)
                self.opcionesc3.grid(row=2, column=1,padx=20,pady=5, columnspan=10)
                self.opcionesc3.config(width=50)
                self.botonagregar2=ttk.Button(self.labelframe1, text="Agregar")
                self.botonagregar2.grid(row=3,column=1,padx=10,pady=5, columnspan=2)
                self.botonactualizar2=ttk.Button(self.labelframe1, text="Actualizar")
                self.botonactualizar2.grid(row=3,column=3,padx=10,pady=5, columnspan=2)
                self.botoneliminar2=ttk.Button(self.labelframe1, text="Eliminar")
                self.botoneliminar2.grid(row=3,column=5,padx=10,pady=5, columnspan=2)
    
    def gestionLocalidad(self):
                #global imagen
                self.pagina3 = ttk.Frame(self.cuaderno1)
                self.cuaderno1.add(self.pagina3, text="Gestion Localidad")
                self.labelframe1 =LabelFrame(self.pagina3, text="Datos Localidad",fg="white",bg="slategray",font=("Arial"),bd=5)
                self.labelframe1.grid(row=0,column=3,padx=100,pady=30)
                self.labenlocalidad=Label(self.labelframe1, text="Localidad:")
                self.labenlocalidad.grid(row=0,column=0,padx=20,pady=5,sticky="e")
                self.labenlocalidad.config(fg="white",bg="slategray")
                loca2 = self.consultitas.buscar_localidades()
                self.loca_nom = StringVar()
                self.opcionesloca = OptionMenu(self.labelframe1, self.loca_nom, *loca2)
                self.opcionesloca.grid(row=0, column=1,padx=20,pady=5, columnspan=10)
                self.opcionesloca.config(width=50)
                self.botonbuscar3=ttk.Button(self.labelframe1, text="Buscar")
                self.botonbuscar3.grid(row=0,column=11,padx=5,pady=5)
                self.botonlimpiar3=ttk.Button(self.labelframe1, text="Limpiar")
                self.botonlimpiar3.grid(row=0,column=13,padx=5,pady=5)
                self.labenlocalidad2=Label(self.labelframe1, text="Nombre:")
                self.labenlocalidad2.grid(row=1,column=0,padx=20,pady=5,sticky="e")
                self.labenlocalidad2.config(fg="white",bg="slategray")
                self.loca_nom2=StringVar()
                self.entrynom2=Entry(self.labelframe1,highlightcolor= "deepskyblue", highlightthickness=2, textvariable=self.loca_nom2)
                self.entrynom2.grid(row=1,column=1,padx=10,pady=5, columnspan=2)
                self.labelprov2=Label(self.labelframe1,text="Provincia:")
                self.labelprov2.grid(row=5,column=0,padx=20,pady=5,sticky="e")
                self.labelprov2.config(fg="white",bg="slategray")
                provincias = self.consultitas.buscar_provincias()
                self.provincia_loca = StringVar()
                self.opcionprov3= OptionMenu(self.labelframe1, self.provincia_loca, *provincias)
                self.opcionprov3.grid(row=5, column=1,padx=20,pady=5, columnspan=10)
                self.opcionprov3.config(width=50)
                self.botonagregar3=ttk.Button(self.labelframe1, text="Agregar")
                self.botonagregar3.grid(row=6,column=1,padx=10,pady=5)
                self.botonactualizar3=ttk.Button(self.labelframe1, text="Actualizar")
                self.botonactualizar3.grid(row=6,column=2,padx=10,pady=5)
                self.botoneliminar3=ttk.Button(self.labelframe1, text="Eliminar")
                self.botoneliminar3.grid(row=6,column=3,padx=10,pady=5)
    
    def gestionProvincia(self):
                #global imagen
                self.pagina4 = ttk.Frame(self.cuaderno1)
                self.cuaderno1.add(self.pagina4, text="Gestion Provincia")
                self.labelframe1 =LabelFrame(self.pagina4, text="Datos Provincia",fg="white",bg="slategray",font=("Arial"),bd=5)
                self.labelframe1.grid(row=0,column=2,padx=100,pady=30)
                self.labelprov2=Label(self.labelframe1, text="Provincia:")
                self.labelprov2.grid(row=0,column=0,padx=20,pady=5,sticky="e")
                self.labelprov2.config(fg="white",bg="slategray")
                provincias4 = self.consultitas.buscar_provincias()
                self.provincia_n = StringVar()
                self.opcionprov = OptionMenu(self.labelframe1, self.provincia_n, *provincias4)
                self.opcionprov.grid(row=0, column=1,padx=20,pady=5, columnspan=10)
                self.opcionprov.config(width=50)
                self.botonbuscar4=ttk.Button(self.labelframe1, text="Buscar")
                self.botonbuscar4.grid(row=0,column=11,padx=5,pady=5)
                self.botonlimpiar4=ttk.Button(self.labelframe1, text="Limpiar")
                self.botonlimpiar4.grid(row=0,column=13,padx=5,pady=5)
                self.labenprovnom=Label(self.labelframe1, text="Nombre:")
                self.labenprovnom.grid(row=1,column=0,padx=20,pady=5,sticky="e")
                self.labenprovnom.config(fg="white",bg="slategray")
                self.provnom2=StringVar()
                self.entrynom4=Entry(self.labelframe1,highlightcolor= "deepskyblue", highlightthickness=2, textvariable=self.provnom2)
                self.entrynom4.grid(row=1,column=1,padx=10,pady=5, columnspan=2)
                self.botonagregar4=ttk.Button(self.labelframe1, text="Agregar")
                self.botonagregar4.grid(row=2,column=1,padx=10,pady=5)
                self.botonactualizar4=ttk.Button(self.labelframe1, text="Actualizar")
                self.botonactualizar4.grid(row=2,column=2,padx=10,pady=5)
                self.botoneliminar4=ttk.Button(self.labelframe1, text="Eliminar")
                self.botoneliminar4.grid(row=2,column=3,padx=10,pady=5)
    
    def licencia(self):
        self.win2 = themed_tk.ThemedTk(theme="black")
        self.win2.geometry("540x310")
        self.win2.title("Licencia")
        self.win2.config(bg="gray")
        self.win2.resizable(False,False)
        Label(self.win2, background="gray", foreground="white",text= '''Demo de un sistema CRUD en Python para gestión de alumnos
    Copyright (C) 2023 - Gabriel S. Roman
    Basado en el sistema de
    Regina Noemí Molares
    Email: regina.molares@bue.edu.ar
    =======================================
    This program is free software: you can redistribute it 
    and/or modify it under the terms of the GNU General Public 
    License as published by the Free Software Foundation, 
    either version 3 of the License, or (at your option) any 
    later version. This program is distributed in the hope that it will be 
    useful, but WITHOUT ANY WARRANTY; without even the 
    implied warranty of MERCHANTABILITY or FITNESS FOR A 
    PARTICULAR PURPOSE. See the GNU General Public License 
    for more details.
    You should have received a copy of the GNU General Public 
    License along with this program.  
    If not, see <https://www.gnu.org/licenses/>.''', font=('Mistral 10 bold')).place(x=0,y=0)
        
    def acercaDe(self):
        self.win3 = themed_tk.ThemedTk(theme="black")
        self.win3.geometry("400x150")
        self.win3.title("Acerca De")
        self.win3.config(bg="gray")
        self.win3.resizable(False,False)
        Label(self.win3,background="gray", foreground="white", text= "Creado por \n Gabriel S. Roman\npara \n Codo a Codo 4.0 - Big Data\nNoviembre, 2023\nEmail: gabriel.magogaro@gmail.com", font=('Mistral 14 bold')).place(x=0,y=0)
                
if __name__ == '__main__':
    app=GestionAlumnos()