# Pseccion de importacion de bibliotecas
import conexion
from tkinter import *
from tkinter import messagebox

# Seccion de instacimiento del objeto tipo TKinter
app = Tk()

app.title("SisCOL CR")  # Titulo de la ventana
# Seccion para la definicion de la dimension de la venta
app.geometry('700x250')

# Color de Fondo de Pantalla
app['background'] = '#ddecfc'

# Crear una tupla que contenga, las especificaciones del font.
# Tipo de letra para el titulo de Pantalla
Font_tuple = ("Britannic Bold", 16)

# Crear una tupla que contenga, las especificaciones del font.
# Tipo de letra para los de Labels
Font_tuplelbl = ("MS UI Gothic", 12, "bold")


# ********************************* INICIO VENTANAS *********************************
# function to open a "Groups Window" on a button click
def openGroups():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(app)

    # sets the title of the
    # Toplevel widget
    newWindow.title("Grupos: Verduras, Frutas y Hortalizas")

    # sets the geometry of toplevel
    newWindow.geometry("800x450")

    # Color de Fondo de Pantalla
    newWindow['background'] = '#ddecfc'

    # Agregar un textbox para capturar el nombre del grupo
    txtbox_grupo = StringVar()
    lbl_nom_grupo = Label(newWindow, text='Nombre del Grupo:',
                          font=Font_tuplelbl, pady=20)
    lbl_nom_grupo.grid(row=0, column=0, sticky=W)
    lbl_nom_grupo['background'] = '#ddecfc'
    Entrada = Entry(newWindow, textvariable=txtbox_grupo)
    Entrada.grid(row=0, column=1)
    # Fin del textbox

    # Caja de texto / Listado de Grupos de la Verduleria(ListBox)
    grupos_list_grupo = Listbox(newWindow, height=15, width=50, border=0)
    grupos_list_grupo.grid(row=2, column=0, columnspan=3,
                           rowspan=6, pady=20, padx=20)
    sentencia= 'SELECT * FROM grupos  '
    conexion.cursor.execute(sentencia)
    registro= conexion.cursor.fetchall()
    n=0
    for x in registro:
        print(x)
        n1=n+1
        grupos_list_grupo.insert(n1,x)
    # Creacion de la barra scroll
    scrollbar_grupo = Scrollbar(newWindow)
    scrollbar_grupo.grid(row=2, column=4)


##################################### FIN DE VENTANA GRUPOS ##############################

#  PRODUCTOS
# function to open a "Products" on a button click
def openProducts():
    def getdate():
        a =  txtbox_nom_producto.get()
        b = txtbox_precio_producto.get()
        c =  txtbox_id_grupo.get()
        conexion.addP(a, c, b)
        conexion.seeP()
        
    def deletePr():
        print()
        a=txtbox_id_producto.get()
        conexion.deleteP(a)
    def editP():
        name =  txtbox_nom_producto .get()
        precio = txtbox_precio_producto.get()
        idG =  txtbox_id_grupo.get()
        idP=txtbox_id_producto.get()
        conexion.updateP(name,idG, precio,idP)
    # Toplevel object which will be treated as a new window
    newWindow = Toplevel(app)

    # sets the title of the Toplevel widget
    newWindow.title("Ventana de Productos")

    # sets the geometry of toplevel
    newWindow.geometry("710x450")

    # Color de Fondo de Pantalla
    newWindow['background'] = '#ddecfc'

  
    
# Agregar un textbox para capturar el id del producto
    txtbox_id_producto = IntVar()
    lbl_id_producto = Label(newWindow, text='Id Producto:',
font=Font_tuplelbl, pady=20)
    lbl_id_producto.grid(row=0, column=0, sticky=W)
    lbl_id_producto['background'] = '#ddecfc'
    Entrada = Entry(newWindow, textvariable=txtbox_id_producto)
    Entrada.grid(row=0, column=1)
# Fin del textbox para capturar el id del producto
# Agregar un textbox para capturar el Nombre del Producto
    txtbox_nom_producto = StringVar()
    lbl_nom_producto = Label(newWindow, text='Nombre del Producto:',
font=Font_tuplelbl, pady=20)
    lbl_nom_producto.grid(row=1, column=0, sticky=W)
    lbl_nom_producto['background'] = '#ddecfc'
    Entrada = Entry(newWindow, textvariable=txtbox_nom_producto)
    Entrada.grid(row=1, column=1)
# Fin del textbox para capturar el Id del Grupo
# Agregar un textbox para capturar el Id Grupo
    txtbox_id_grupo=  IntVar()
    lbl_id_grupo = Label(newWindow, text='Id Grupo:',
font=Font_tuplelbl, pady=20)
    lbl_id_grupo.grid(row=0, column=2, sticky=W)
    lbl_id_grupo['background'] = '#ddecfc'
    Entrada = Entry(newWindow, textvariable=txtbox_id_grupo)
    Entrada.grid(row=0, column=3)
# Fin del textbox para capturar el Precio del Producto
# Agregar un textbox para el Precio del Producto
    txtbox_precio_producto =  IntVar()
    lbl_precio_producto = Label(newWindow, text='Precio:',
font=Font_tuplelbl, pady=20)
    lbl_precio_producto.grid(row=1, column=2, sticky=W)
    lbl_precio_producto['background'] = '#ddecfc'
    Entrada = Entry(newWindow, textvariable=txtbox_precio_producto)
    Entrada.grid(row=1, column=3)


    
    # ***SECCION DE BOTONES ****************
    # Boton de Agregar un Grupo de Productos
    add_btn_producto = Button(newWindow, text='Agregar Producto', width=15, command= getdate) #command=add_item)
    add_btn_producto.grid(row=2, column=1, pady=5)
    
    # Boton de eliminar un Grupo de Productos
    remove_btn_producto= Button(newWindow, text='Eliminar Producto', width=15, command= deletePr ) #command=remove_item)
    remove_btn_producto.grid(row=2, column=2)
    
    # Boton de Actualizar un Grupo de Productos
    update_btn_producto = Button(newWindow, text='Actulizar Producto', width=15,command=editP) #command=update_item)
    update_btn_producto.grid(row=2, column=3)
    
    # Boton para Limpiar el textbox de nombre de grupo

    
    # Caja de texto / Listado de Productos de la Verduleria(ListBox)
    grupos_list_producto = Listbox(newWindow, height=15, width=50, border=0 ,)
    grupos_list_producto.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
    sentencia= 'SELECT * FROM productos '
    conexion.cursor.execute(sentencia)
    registro= conexion.cursor.fetchall()
    n=0
    for x in registro:
        print(x)
        n1=n+1
        grupos_list_producto.insert(n1,x)
    # Creacion de la barra scroll
    scrollbar_producto = Scrollbar(newWindow)
    scrollbar_producto.grid(row=4, column=4)
    

##################################### FIN DE VENTANA PRODUCTOS ##############################  


# function to open a "Vendors" on a button click
def openVendors():
    def getdV():   
        a =  txtbox_vendedores.get()    
        b =  txtbox_fecha_alta.get()
        c = txtbox_fecha_naci.get()
        d =  txtbox_direccion.get()
        conexion.addV(a, b, c,d)
        conexion.seeV() 
    def deleteVe():
        print()
        a= txtbox_id_vendedor.get()
        conexion.deleteV(a)
    def editV():
        name =txtbox_vendedores.get()
        fecA = txtbox_fecha_alta.get()
        fecN = txtbox_fecha_naci.get()
        dirr=txtbox_direccion.get()
        idV=txtbox_id_vendedor.get()
        conexion.updateV(name,fecA,fecN,dirr, idV)
    # Toplevel object which will be treated as a new window
    newWindow = Toplevel(app)

    # sets the title of the Toplevel widget
    newWindow.title("Ventana de Vendedores")

    # sets the geometry of toplevel
    newWindow.geometry("750x450")
    
    # Color de Fondo de Pantalla
    newWindow['background'] = '#ddecfc'
    
    # Agregar un textbox para capturar el nombre del Vendedor
    txtbox_vendedores = StringVar()
    lbl_nom_vendedores = Label(newWindow, text='Nombre del Vendedor:',
                          font=Font_tuplelbl, pady=20)
    lbl_nom_vendedores.grid(row=0, column=0, sticky=W)
    lbl_nom_vendedores['background'] = '#ddecfc'
    Entrada = Entry(newWindow, textvariable=txtbox_vendedores)
    Entrada.grid(row=0, column=1)
    # Fin del textbox para capturar el nombre del Vendedor
    
    # Agregar un textbox para capturar la Fecha de Alta
    txtbox_fecha_alta = StringVar()
    lbl_fecha_alta = Label(newWindow, text='Fecha de Alta:',
                          font=Font_tuplelbl, pady=20)
    lbl_fecha_alta.grid(row=1, column=0, sticky=W)
    lbl_fecha_alta['background'] = '#ddecfc'
    Entrada = Entry(newWindow, textvariable=txtbox_fecha_alta)
    Entrada.grid(row=1, column=1)
    # Fin del textbox para capturar la Fecha de Alta
    
    # Agregar un textbox para capturar la Fecha de Nacimiento
    txtbox_fecha_naci = StringVar()
    lbl_nom_fecha_naci = Label(newWindow, text='Fecha de Nacimiento:',
                          font=Font_tuplelbl, pady=20)
    lbl_nom_fecha_naci.grid(row=0, column=2, sticky=W)
    lbl_nom_fecha_naci['background'] = '#ddecfc'
    Entrada = Entry(newWindow, textvariable=txtbox_fecha_naci)
    Entrada.grid(row=0, column=3)
    # Fin del textbox para capturar la Fecha de Nacimiento
    
    # Agregar un textbox para capturar la Direccion
    txtbox_direccion = StringVar()
    lbl_direccion = Label(newWindow, text='Direccion:',
                          font=Font_tuplelbl, pady=20)
    lbl_direccion.grid(row=1, column=2, sticky=W)
    lbl_direccion['background'] = '#ddecfc'
    Entrada = Entry(newWindow, textvariable=txtbox_direccion)
    Entrada.grid(row=1, column=3)
    # Fin del textbox para capturar la Direccion
 # Agregar un textbox para capturar el Id Vendedor
    txtbox_id_vendedor = IntVar()
    lbl_id_vendedor = Label(newWindow, text='Id Vendedor:',
                          font=Font_tuplelbl, pady=20)
    lbl_id_vendedor.grid(row=2, column=0, sticky=W)
    lbl_id_vendedor['background'] = '#ddecfc'
    Entrada = Entry(newWindow, textvariable=txtbox_id_vendedor)
    Entrada.grid(row=2, column=1)
    # Fin del textbox para capturar el Id Vendedor
    
    
# ***SECCION DE BOTONES ****************
#Boton de Agregar un Vendedor
    add_btn_vendedor = Button(newWindow, text='Agregar Vendedor', width=15,command= getdV) #command=add_item)
    add_btn_vendedor.grid(row=3, column=1, pady=5)
#Boton de eliminar un Grupo de Vendedor
    remove_btn_vendedor= Button(newWindow, text='Eliminar Vendedor', width=15,command= deleteVe) #command=remove_item)
    remove_btn_vendedor.grid(row=3, column=2)
#Boton de Actualizar un Grupo de Vendedor
    update_btn_vendedor = Button(newWindow, text='Actulizar Vendedor', width=15,command=editV) #command=update_item)
    update_btn_vendedor.grid(row=3, column=3)
#Boton para Limpiar los textboxs 

# Caja de texto / Listado de Grupos de Vendedores Verduleria(ListBox)
    grupos_list_vendedor = Listbox(newWindow, height=20, width=110, border=0)
    grupos_list_vendedor.grid(row=4, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
    sentencia= 'SELECT * FROM vendedores '
    conexion.cursor.execute(sentencia)
    registro= conexion.cursor.fetchall()
    n=0
    for x in registro:
        print(x)
        n1=n+1
        grupos_list_vendedor.insert(n1,x)
    scrollbar_vendedor = Scrollbar(newWindow)
    scrollbar_vendedor.grid(row=4, column=4)
    

##################################### FIN DE VENTANA VENDEDORES ############################## 
    
    
# function to open a "Groups Sales" on a button click
def openSales():
    def getdS():   
        a =  txtbox_id_vendedor.get()    
        b =  txtbox_id_producto.get()
        c =  txtbox_fecha_venta.get()
        d =  txtbox_kilos_vendidos.get()
        conexion.addS(a, b, c,d)
        conexion.seeS() 
    # Toplevel object which will be treated as a new window
    newWindow = Toplevel(app)

    # sets the title of the Toplevel widget
    newWindow.title("Ventana de Ventas")

    # sets the geometry of toplevel
    newWindow.geometry("750x450")
    
    # Color de Fondo de Pantalla
    newWindow['background'] = '#ddecfc'
    
    # Agregar un textbox para capturar el Id Vendedor
    txtbox_id_vendedor = IntVar()
    lbl_nom_id_vendedor = Label(newWindow, text='Id Vendedor:',
                          font=Font_tuplelbl, pady=20)
    lbl_nom_id_vendedor.grid(row=0, column=0, sticky=W)
    lbl_nom_id_vendedor['background'] = '#ddecfc'
    Entrada = Entry(newWindow, textvariable=txtbox_id_vendedor)
    Entrada.grid(row=0, column=1)
    # Fin del textbox para capturar el Id Vendedor
    
    # Agregar un textbox para capturar Id Producto
    txtbox_id_producto = IntVar()
    lbl_id_producto = Label(newWindow, text='Id Producto:',
                          font=Font_tuplelbl, pady=20)
    lbl_id_producto.grid(row=1, column=0, sticky=W)
    lbl_id_producto['background'] = '#ddecfc'
    Entrada = Entry(newWindow, textvariable=txtbox_id_producto)
    Entrada.grid(row=1, column=1)
    # Fin del textbox para capturar Id Producto
    
    # Agregar un textbox para capturar la Fecha de la Venta
    txtbox_fecha_venta = StringVar()
    lbl_nom_fecha_venta = Label(newWindow, text='Fecha de Venta:',
                          font=Font_tuplelbl, pady=20)
    lbl_nom_fecha_venta.grid(row=0, column=2, sticky=W)
    lbl_nom_fecha_venta['background'] = '#ddecfc'
    Entrada = Entry(newWindow, textvariable=txtbox_fecha_venta)
    Entrada.grid(row=0, column=3)
    # Fin del textbox para capturar la Fecha de la Venta
    
    # Agregar un textbox para capturar los Kilos Vendidos
    txtbox_kilos_vendidos =IntVar()
    lbl_kilos_vendidos = Label(newWindow, text='Kilos Vendidos:',
                          font=Font_tuplelbl, pady=20)
    lbl_kilos_vendidos.grid(row=1, column=2, sticky=W)
    lbl_kilos_vendidos['background'] = '#ddecfc'
    Entrada = Entry(newWindow, textvariable=txtbox_kilos_vendidos)
    Entrada.grid(row=1, column=3)

    # ***SECCION DE BOTONES ****************
    # Boton de Agregar una Venta
    add_btn_venta = Button(newWindow, text='Agregar Venta', width=15, command=getdS) #command=add_item)
    add_btn_venta.grid(row=2, column=1, pady=5)
    
 
    
    # Caja de texto / Listado de Grupos de Ventas Verduleria(ListBox)
    grupos_list_venta = Listbox(newWindow, height=15, width=50, border=0)
    grupos_list_venta.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
    sentencia= 'SELECT * FROM ventas '
    conexion.cursor.execute(sentencia)
    registro= conexion.cursor.fetchall()
    n=0
    for x in registro:
        print(x)
        n1=n+1
        grupos_list_venta.insert(n1,x)
    # Creacion de la barra scroll
    scrollbar_venta = Scrollbar(newWindow)
    scrollbar_venta.grid(row=4, column=4)

    
# ********************************* FINAL VENTANA VENTAS *********************************

# **************************Funcion de la VENTA PRINCIPAL (MAIN)*****
# Declaracion de la funcion cerrarVentana
def cerrarVentana():
    messagebox.showinfo('Saliendo de la Administracion:',
                        'Se procedera a cerrar este programa.')
    if messagebox.askokcancel('Mensaje', '¿Esta seguro que desea Continuar?'):
        messagebox.showinfo('Mensaje', 'Hasta luego lo esperamos pronto')
    else:
        messagebox.showinfo('Mensaje', 'Regresando a la venta principal')
        app.mainloop()
    app.destroy()
# Fin de la funcion cerrarVentana


# Agregar un label a la pantalla
Etiqueta1 = Label(app, text='Administracion de Verduleria', font=Font_tuple)
Etiqueta1.grid(row=4, column=4, sticky=W)
Etiqueta1['background'] = '#ddecfc'

# Agregar un boton en la pantalla
boton_salir = Button(app, text='Salir', bg="#ff0000", width=4,
                     font=('bold', 12), command=cerrarVentana)
boton_salir.grid(row=8, column=8)

# Agregar Boton para creacion de Grupos
boton_grupos = Button(app, text='Grupos', bg="#ddecfc",
                      width=12, font=('bold', 12), command=openGroups)
boton_grupos.grid(row=10, column=1)

# Agregar Boton para creacion de Productos
boton_productos = Button(app, text='Productos', bg="#ddecfc", width=12, font=(
    'bold', 12), command=openProducts)
boton_productos.grid(row=11, column=1)

# Agregar Boton para creacion de Vendedores
boton_vendedores = Button(app, text='Vendedores', bg="#ddecfc",
                          width=12, font=('bold', 12), command=openVendors)
boton_vendedores.grid(row=12, column=1)

# Agregar Boton para creacion de Ventas
boton_ventas = Button(app, text='Ventas', bg="#ddecfc",
                      width=12, font=('bold', 12), command=openSales)
boton_ventas.grid(row=13, column=1)

# Seccion de presentacion de la interface grafica
app.mainloop()
