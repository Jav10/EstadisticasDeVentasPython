from tkinter import *
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

conexion = sqlite3.connect('productos.sqlite3')
consulta = conexion.cursor()

sql = """CREATE TABLE IF NOT EXISTS producto(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
nombre VARCHAR(30) NOT NULL, precio FLOAT NOT NULL, m1 FLOAT, m2 FLOAT,
frecuencia INT, ganancias FLOAT)"""

sql1 = """CREATE TABLE IF NOT EXISTS usuario(
clave INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
nombre VARCHAR(30), apellido VARCHAR(40), correo VARCHAR(30) NOT NULL, contrasena VARCHAR(8) NOT NULL)"""
#Ejecutar la consulta
if(consulta.execute(sql)):
    uno=3
else:
    messagebox.showerror("Error DB","Hubo un error al ejecutar la consulta")
#Ejecutar la consulta
if(consulta.execute(sql1)):
    uno=3
else:
    messagebox.showerror("Error DB","Hubo un error al ejecutar la consulta")

#terminar la consulta
consulta.close()
#guardar cambios en bd
conexion.commit()
#cerramos la conexion
conexion.close()

#crear ventana
ventana=Tk()
#Asignar tamaño a la ventana
#geometry("ancho x altro +/- posX +/- posY")
#ventana.config(bg="green") # Le da color al fondo
ventana.geometry("500x500+400+300")
#nombre ventana
ventana.title("CEPY")
#creamos etiquetas
bv1=Label(ventana,text="Bienvenido",font=("Agency FB",30)).place(x=160,y=5)

def datosUser():
    datosUsuario=Toplevel()
    datosUsuario.geometry("500x500+500+400")
    bv=Label(datosUsuario,text="Registro Usuario",font=("Agency FB",30)).place(x=120,y=10)
    nombre=StringVar()
    apellido=StringVar()
    correo=StringVar()
    contrasena=StringVar()
    #Label's
    user=Label(datosUsuario,text="Nombre:",fg="yellow",background="gray",font=("Agency FB",12)).place(x=120,y=110)
    apuser=Label(datosUsuario,text="Apellido:",fg="yellow",background="gray",font=("Agency FB",12)).place(x=120,y=140)
    correouser=Label(datosUsuario,text="Correo:",fg="yellow",background="gray",font=("Agency FB",12)).place(x=120,y=170)
    contrasenauser=Label(datosUsuario,text="Contraseña:",fg="yellow",background="gray",font=("Agency FB",12)).place(x=120,y=200)
    #Entry's
    txtNombre=Entry(datosUsuario,textvariable=nombre)
    txtNombre.place(x=200,y=110)
    txtApellido=Entry(datosUsuario,textvariable=apellido)
    txtApellido.place(x=200,y=140)
    txtCorreo=Entry(datosUsuario,textvariable=correo)
    txtCorreo.place(x=200,y=170)
    txtContrasena=Entry(datosUsuario,textvariable=contrasena,show="*")
    txtContrasena.place(x=230,y=200)
    #Botones
    def insertar():
        conexion = sqlite3.connect('productos.sqlite3')
        consulta = conexion.cursor()
        #Excepciones checar
        uno=txtNombre.get()
        dos=txtApellido.get()
        tres=txtCorreo.get()
        cuatro=txtContrasena.get()
        if '@' in tres:
            seguro=1
        else:
            seguro=0
        if(uno==""):
            seguro2=0
        else:
            seguro2=1
        if(dos==""):
            seguro3=0
        else:
            seguro3=1
        if(cuatro==""):
            seguro4=0
        else:
            seguro4=1
        if(tres==""):
            seguro5=0
        else:
            seguro5=1
        if(len(cuatro)==8):
            seguro6=1
        else:
            seguro6=0
        if(seguro==1 and seguro2==1 and seguro3==1 and seguro4==1 and seguro5==1 and seguro6==1):
            consulta.execute("INSERT INTO usuario (nombre,apellido,correo,contrasena) VALUES (?,?,?,?)",(uno,dos,tres,cuatro))
            conexion.commit()
            consulta.close()
            conexion.close()
            messagebox.showinfo("Mensaje","Registro usuario satisfactorio")
        else:
            txtNombre.delete(0,100)
            txtApellido.delete(0,100)
            txtCorreo.delete(0,100)
            txtContrasena.delete(0,100)
            if(seguro2!=1 or seguro3!=1 or seguro4!=1 or seguro5!=1):
                messagebox.showerror("ERROR","Rellene todos los campos")
            if(seguro!=1):
                messagebox.showerror("ERROR","Correo invalido intente nuevamente")
            if(seguro6!=1):
                messagebox.showerror("ERROR","La contraseña solo puede contener 8 caracteres")

    botonRegistro=Button(datosUsuario,text="Guardar",font=("Agency FB",15),comman=insertar).place(x=230,y=250)
    
def altaProducto():
    altaProducto=Toplevel()
    altaProducto.geometry("500x500+500+400")
    nombre=StringVar()
    precio=DoubleVar()
    pMayoreo1=DoubleVar()
    pMayoreo2=DoubleVar()
    #Label's
    bv=Label(altaProducto,text="Alta Producto",font=("Agency FB",30)).place(x=130,y=10)
    nom=Label(altaProducto,text="Nombre:",fg="yellow",background="gray",font=("Agency FB",12)).place(x=120,y=110)
    p=Label(altaProducto,text="Precio:",fg="yellow",background="gray",font=("Agency FB",12)).place(x=120,y=140)
    m1=Label(altaProducto,text="Mayoreo1:",fg="yellow",background="gray",font=("Agency FB",12)).place(x=120,y=170)
    m2=Label(altaProducto,text="Mayoreo2:",fg="yellow",background="gray",font=("Agency FB",12)).place(x=120,y=200)
    #Entry's
    txtNombre=Entry(altaProducto,textvariable=nombre)
    txtNombre.place(x=200,y=110)
    txtPrecio=Entry(altaProducto,textvariable=precio)
    txtPrecio.place(x=200,y=140)
    txtM1=Entry(altaProducto,textvariable=pMayoreo1)
    txtM1.place(x=200,y=170)
    txtM2=Entry(altaProducto,textvariable=pMayoreo2)
    txtM2.place(x=230,y=200)
    #Botones
    def insertar():
        conexion = sqlite3.connect('productos.sqlite3')
        consulta = conexion.cursor()
        #excepciones
        uno=txtNombre.get()
        while True:
            try:
                dos=txtPrecio.get()
                float(dos)
                break
            except ValueError:
                messagebox.showerror("ERROR","Solo se aceptan valores numéricos en precio intente otra vez")
                txtPrecio.delete(0,50)
                txtPrecio.insert(0,0.0)
        while True:
            try:
                tres=txtM1.get()
                float(tres)
                break
            except ValueError:
                messagebox.showerror("ERROR","Solo se aceptan valores numéricos en Mayoreo1 intente otra vez")
                txtM1.delete(0,50)
                txtM1.insert(0,0.0)
        while True:
            try:
                cuatro=txtM2.get()
                float(cuatro)
                break
            except ValueError:
                messagebox.showerror("ERROR","Solo se aceptan valores numéricos en Mayoreo1 intente otra vez")
                txtM2.delete(0,50)
                txtM2.insert(0,0.0)
        if(uno=="" and dos==""):
            messagebox.showerror("ERROR","El nombre del producto y el precio no puede estar vacios")
        else:
            consulta.execute("INSERT INTO producto (nombre,precio,m1,m2) VALUES (?,?,?,?)",(uno,dos,tres,cuatro))
            conexion.commit()
            consulta.close()
            conexion.close()
            messagebox.showinfo("Mensaje","Alta de producto satisfactoria")

    botonRegistro=Button(altaProducto,text="Insertar",font=("Agency FB",15),command=insertar).place(x=230,y=250)

def modificar():
    modificar=Toplevel()
    modificar.geometry("500x500+500+400")
    nombre=StringVar()
    precio=DoubleVar()
    pMayoreo1=DoubleVar()
    pMayoreo2=DoubleVar()
    V=IntVar()
    #ListBox
    lista=Listbox(modificar)
    conexion = sqlite3.connect('productos.sqlite3')
    consulta = conexion.cursor()
    consulta.execute("SELECT * FROM producto")
    resultado=consulta.fetchall()
    for i in resultado:
        listado=[]
        listado.append(i[0])
        listado.append(i[1])
        lista.insert(END,listado)
    lista.place(x=50,y=150)
    conexion.commit()
    consulta.close()
    conexion.close()
    #Label's
    bv=Label(modificar,text="Modificar Producto",font=("Agency FB",30)).place(x=80,y=10)
    mod=Label(modificar,text="Lista Productos",fg="yellow",background="gray",font=("Agency FB",12)).place(x=52,y=95)
    clave=Label(modificar,text="Clave -- Producto",fg="yellow",background="gray",font=("Agency FB",12)).place(x=52,y=120)
    nom=Label(modificar,text="Nombre:",fg="yellow",background="gray",font=("Agency FB",12)).place(x=220,y=110)
    p=Label(modificar,text="Precio:",fg="yellow",background="gray",font=("Agency FB",12)).place(x=220,y=140)
    m1=Label(modificar,text="Mayoreo1:",fg="yellow",background="gray",font=("Agency FB",12)).place(x=220,y=170)
    m2=Label(modificar,text="Mayoreo2:",fg="yellow",background="gray",font=("Agency FB",12)).place(x=220,y=200)
    v1=Label(modificar,text="Clave Elemento a Modificar",fg="yellow",background="gray",font=("Agency FB",12)).place(x=50,y=320)
    #Entry's
    txtNombre=Entry(modificar,textvariable=nombre)
    txtNombre.place(x=300,y=110)
    txtPrecio=Entry(modificar,textvariable=precio)
    txtPrecio.place(x=300,y=140)
    txtM1=Entry(modificar,textvariable=pMayoreo1)
    txtM1.place(x=300,y=170)
    txtM2=Entry(modificar,textvariable=pMayoreo2)
    txtM2.place(x=330,y=200)
    txtV=Entry(modificar,textvariable=V)
    txtV.place(x=50,y=350)
        
    #Botones
    def seleccionar():
        nombre=txtNombre.get()
        while True:
            try:
                precio=txtPrecio.get()
                float(precio)
                break
            except ValueError:
                messagebox.showerror("ERROR","Solo se aceptan valores numéricos en Precio intente otra vez")
                txtPrecio.delete(0,50)
                txtPrecio.insert(0,0.0)
        while True:
            try:
                m1=txtM1.get()
                float(m1)
                break
            except ValueError:
                messagebox.showerror("ERROR","Solo se aceptan valores numéricos en Mayoreo1 intente otra vez")
                txtM1.delete(0,50)
                txtM1.insert(0,0.0)
        while True:
            try:
                m2=txtM2.get()
                float(m2)
                break
            except ValueError:
                messagebox.showerror("ERROR","Solo se aceptan valores numéricos en Mayoreo1 intente otra vez")
                txtM2.delete(0,50)
                txtM2.insert(0,0.0)
        while True:
            try:
                var1=V.get()
                int(var1)
                break
            except ValueError:
                messagebox.showerror("ERROR","Solo se aceptan valores numéricos enteros en seleccion intente otra vez")
                V.set(0)
        conexion = sqlite3.connect('productos.sqlite3')
        consulta = conexion.cursor()
        consulta.execute("SELECT * FROM producto WHERE id=?",(var1,))
        rest=consulta.fetchall()
        if not rest:
           messagebox.showerror("ERROR","La clave seleccionada no existe en la base de datos")
        else:
            #Configurar
            str(precio)
            if(nombre!="" and precio!="0.0"):
                str(m1)
                str(m2)
                if(m1!="0.0" and m2!="0.0"):
                    float(precio)
                    float(m1)
                    float(m2)
                    consulta.execute("UPDATE producto SET nombre=?, precio=?, m1=?, m2=? WHERE id=?",(nombre,precio,m1,m2,var1,))
                    conexion.commit()
                    consulta.close()
                    conexion.close()
                    messagebox.showinfo("Mensaje","Actualización Satisfactoria")
                if(m1!="0.0" and m2=="0.0"):
                    float(precio)
                    float(m1)
                    float(m2)
                    consulta.execute("UPDATE producto SET nombre=?, precio=?, m1=? WHERE id=?",(nombre,precio,m1,var1,))
                    conexion.commit()
                    consulta.close()
                    conexion.close()
                    messagebox.showinfo("Mensaje","Actualización Satisfactoria")
                if(m1=="0.0" and m2=="0.0"):
                    float(precio)
                    float(m1)
                    float(m2)
                    consulta.execute("UPDATE producto SET nombre=?, precio=? WHERE id=?",(nombre,precio,var1,))
                    conexion.commit()
                    consulta.close()
                    conexion.close()
                    messagebox.showinfo("Mensaje","Actualización Satisfactoria")
            if(nombre!="" and precio=="0.0"):
                float(precio)
                consulta.execute("UPDATE producto SET nombre=? WHERE id=?",(nombre,var1,))
                conexion.commit()
                consulta.close()
                conexion.close()
                messagebox.showinfo("Mensaje","Actualización Satisfactoria")
            if(nombre=="" and precio!="0.0"):
                float(precio)
                consulta.execute("UPDATE producto SET precio=? WHERE id=?",(precio,var1,))
                conexion.commit()
                consulta.close()
                conexion.close()
                messagebox.showinfo("Mensaje","Actualización Satisfactoria")
                
    botonSeleccionar=Button(modificar,text="Modificar",font=("Agency FB",15),command=seleccionar).place(x=50,y=370)
    

def baja():
    baja=Toplevel()
    baja.geometry("500x500+500+400")
    #ListBox
    V=IntVar()
    lista=Listbox(baja)
    conexion = sqlite3.connect('productos.sqlite3')
    consulta = conexion.cursor()
    consulta.execute("SELECT * FROM producto")
    resultado=consulta.fetchall()
    for i in resultado:
        listado=[]
        listado.append(i[0])
        listado.append(i[1])
        lista.insert(END,listado)
    lista.place(x=180,y=130)
    #Label's
    bv=Label(baja,text="Baja Producto",font=("Agency FB",30)).place(x=130,y=10)
    mod=Label(baja,text="Lista Productos",fg="yellow",background="gray",font=("Agency FB",12)).place(x=183,y=70)
    v1=Label(baja,text="Clave Elemento a Eliminar",fg="yellow",background="gray",font=("Agency FB",12)).place(x=183,y=300)
    clave=Label(baja,text="Clave -- Producto",fg="yellow",background="gray",font=("Agency FB",12)).place(x=183,y=100)
    #Entry
    txtV=Entry(baja,textvariable=V).place(x=183,y=330)
    #Botones
    def seleccionar():
        while True:
            try:
                var1=V.get()
                int(var1)
                break
            except ValueError:
                messagebox.showerror("ERROR","Solo se aceptan valores enteros intente otra vez")
        consulta.execute("DELETE FROM producto WHERE id=?",(var1,))
        conexion.commit()
        consulta.close()
        conexion.close()
        messagebox.showinfo("Mensaje","Actualización Satisfactoria, cierre la ventana para actualizar")
        
    botonRegistro=Button(baja,text="Eliminar",font=("Agency FB",15),comman=seleccionar).place(x=200,y=350)

def costo():
    costo=Toplevel()
    costo.geometry("500x500+500+400")
    nombre=StringVar()
    sel=IntVar()
    precio=DoubleVar()
    pMayoreo1=DoubleVar()
    pMayoreo2=DoubleVar()
    cantidad=IntVar()
    total=DoubleVar()
    V=IntVar()
    #ListBox
    lista=Listbox(costo)
    lista.place(x=30,y=130)
    conexion = sqlite3.connect('productos.sqlite3')
    consulta = conexion.cursor()
    consulta.execute("SELECT * FROM producto")
    resultado=consulta.fetchall()
    for i in resultado:
        listado=[]
        listado.append(i[0])
        listado.append(i[1])
        lista.insert(END,listado)
        
    def seleccionar():
        while True:
            try:
                var1=txtV.get()
                int(var1)
                break
            except ValueError:
                messagebox.showerror("ERROR","Solo se aceptan valores enteros intente otra vez")
                txtV.delete(0,50)
                txtV.insert(0,0)
        if(var1!=0):
            conexion = sqlite3.connect('productos.sqlite3')
            consulta = conexion.cursor()
            consulta.execute("SELECT * FROM producto WHERE id=?",(var1,))
            rest=consulta.fetchone()
            if(not rest and cantidad.get()<=0):
                messagebox.showerror("ERROR","Elige una clave de un producto existente")
            if(cantidad.get()>=1 and sel.get()>=1 and sel.get()<=3):
                nombre.set(rest[1])
                precio.set(rest[2])
                pMayoreo1.set(rest[3])
                pMayoreo2.set(rest[4])
                
                txtNombre=Label(costo,textvariable=nombre)
                txtNombre.place(x=300,y=110)
                txtPrecio=Label(costo,textvariable=precio)
                txtPrecio.place(x=300,y=140)
                txtM1=Label(costo,textvariable=pMayoreo1)
                txtM1.place(x=305,y=170)
                txtM2=Label(costo,textvariable=pMayoreo2)
                txtM2.place(x=305,y=200)
                p1=Label(costo,text="Precio: "+str(cantidad.get()*rest[2]))
                p1.place(x=295,y=300)
                p2=Label(costo,text="M1: "+str(cantidad.get()*rest[3]))
                p2.place(x=375,y=300)
                p3=Label(costo,text="M1: "+str(cantidad.get()*rest[4]))
                p3.place(x=430,y=300)
                consulta.execute("UPDATE producto SET frecuencia=? WHERE id=?",(cantidad.get(),var1,))
                conexion.commit()
                
                if(sel.get()==1):
                    n1=(cantidad.get()*rest[2])
                    print(n1)
                    consulta.execute("UPDATE producto SET ganancias=? WHERE id=?",(n1,var1,))
                    conexion.commit()
                    
                if(sel.get()==2):
                    n2=(cantidad.get()*rest[3])
                    consulta.execute("UPDATE producto SET ganancias=? WHERE id=?",(n2,var1,))
                    conexion.commit()
                    
                if(sel.get()==3):
                    n3=(cantidad.get()*rest[4])
                    consulta.execute("UPDATE producto SET ganancias=? WHERE id=?",(n3,var1,))
                    conexion.commit()
                    
            else:
                messagebox.showerror("ERROR","Rellena cantidad y Tipo de precio")
        
    #Label's
    clave=Label(costo,text="Clave -- Producto",fg="yellow",background="gray",font=("Agency FB",12)).place(x=30,y=100)
    bv=Label(costo,text="Costo Producto",font=("Agency FB",30)).place(x=130,y=10)
    mod=Label(costo,text="Lista Productos",fg="yellow",background="gray",font=("Agency FB",12)).place(x=35,y=70)
    nom=Label(costo,text="Nombre:",fg="yellow",background="gray",font=("Agency FB",12)).place(x=220,y=110)
    p=Label(costo,text="Precio:",fg="yellow",background="gray",font=("Agency FB",12)).place(x=220,y=140)
    m1=Label(costo,text="Mayoreo1:",fg="yellow",background="gray",font=("Agency FB",12)).place(x=220,y=170)
    m2=Label(costo,text="Mayoreo2:",fg="yellow",background="gray",font=("Agency FB",12)).place(x=220,y=200)
    cant=Label(costo,text="Cantidad:",fg="yellow",background="gray",font=("Agency FB",12)).place(x=220,y=230)
    tot=Label(costo,text="Precio Total:",fg="yellow",background="gray",font=("Agency FB",12)).place(x=200,y=300)
    v1=Label(costo,text="Clave Elemento a Usar",fg="yellow",background="gray",font=("Agency FB",12)).place(x=30,y=300)
    Sel=Label(costo,text="Precio: 1 - Mayoreo1: 2 - Mayoreo2: 3",fg="yellow",background="gray",font=("Agency FB",12)).place(x=30,y=400)
    
    #Entry's
    txtSel=Entry(costo,textvariable=sel)
    txtSel.place(x=30,y=430)
    txtCantidad=Entry(costo,textvariable=cantidad)
    txtCantidad.place(x=305,y=230)
    txtV=Entry(costo,textvariable=V)
    txtV.place(x=30,y=330)
    #Botones
    btn=Button(costo,text="Seleccionar",font=("Agency FB",10),command=seleccionar).place(x=30,y=360)

def reporte():
    reporte=Toplevel()
    reporte.geometry("500x500+500+400")
    #Label's
    bv=Label(reporte,text="Reportes Producto",font=("Agency FB",30)).place(x=100,y=10)
    #Botones
    def producto():
        conexion = sqlite3.connect('productos.sqlite3')
        consulta = conexion.cursor()
        consulta.execute("SELECT * FROM producto")
        resultado=consulta.fetchall()
        listaF=[]
        listaN=[]
        for i in resultado:
            listaF.append(i[5])
            listaN.append(i[1])

        posicion_y=np.arange(len(listaN))
        plt.bar(posicion_y,listaF, align="center")
        plt.xticks(posicion_y,listaN)
        plt.title("Frecuencia de Productos")
        plt.plot(listaF)
        plt.show()
        
    def ganancia():
        conexion = sqlite3.connect('productos.sqlite3')
        consulta = conexion.cursor()
        consulta.execute("SELECT * FROM producto")
        resultado=consulta.fetchall()
        listaF=[]
        listaN=[]
        for i in resultado:
            listaF.append(i[6])
            listaN.append(i[1])
        print(listaF)
        print(listaN)
        plt.figure()
        plt.title("Frecuencia Productos")
        plt.xlabel("Productos")
        plt.ylabel("Frecuencia")
        indice=np.arange(len(listaN))
        plt.xticks(indice,listaN[0:])
        plt.yticks(np.arange(0,5001,200))
        plt.plot(listaF,marker='x', linestyle=':', color='b')
        plt.show()
        
    botonRegistro=Button(reporte,text="Ganancia",font=("Agency FB",25), command=ganancia).place(x=50,y=100)
    botonRegistro1=Button(reporte,text="Producto",font=("Agency FB",25), command=producto).place(x=300,y=100)
    
    

boton=Button(ventana,text="Registro Usuario",font=("Agency FB",20),command=datosUser).place(x=150,y=50)
boton1=Button(ventana,text="Alta Producto",font=("Agency FB",15),command=altaProducto).place(x=50,y=150)
boton2=Button(ventana,text="Modificar",font=("Agency FB",15),command=modificar).place(x=200,y=150)
boton3=Button(ventana,text="Baja Producto",font=("Agency FB",15),command=baja).place(x=310,y=150)
boton4=Button(ventana,text="Costo Producto",font=("Agency FB",15),command=costo).place(x=50,y=200)
boton5=Button(ventana,text="Reporte Producto",font=("Agency FB",15),command=reporte).place(x=278,y=200)

ventana.mainloop()


