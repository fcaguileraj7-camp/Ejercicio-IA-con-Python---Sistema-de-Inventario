import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

# ==============================
# BASE DE DATOS
# ==============================

def crear_db():
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        precio REAL,
        cantidad INTEGER,
        stock_minimo INTEGER
    )
    """)

    conn.commit()
    conn.close()


# ==============================
# FUNCIONES CRUD
# ==============================

def agregar_producto():

    nombre = entry_nombre.get()
    precio = entry_precio.get()
    cantidad = entry_cantidad.get()
    stock = entry_stock.get()

    if nombre == "" or precio == "" or cantidad == "" or stock == "":
        messagebox.showwarning("Campos incompletos", "Debe llenar todos los campos")
        return

    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO productos(nombre,precio,cantidad,stock_minimo)
    VALUES(?,?,?,?)
    """,(nombre,precio,cantidad,stock))

    conn.commit()
    conn.close()

    limpiar_campos()
    mostrar_productos()


def mostrar_productos():

    for row in tabla.get_children():
        tabla.delete(row)

    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM productos")

    datos = cursor.fetchall()

    for fila in datos:
        tabla.insert("",tk.END,values=(
            fila[0],
            fila[1],
            f"$ {fila[2]:,.0f}",
            fila[3],
            fila[4]
        ))

    conn.close()


def seleccionar_producto(event):

    item = tabla.focus()

    if item == "":
        return

    valores = tabla.item(item,"values")

    entry_id.config(state="normal")
    entry_id.delete(0,tk.END)
    entry_id.insert(0,valores[0])
    entry_id.config(state="readonly")

    entry_nombre.delete(0,tk.END)
    entry_nombre.insert(0,valores[1])

    entry_precio.delete(0,tk.END)
    entry_precio.insert(0,valores[2].replace("$","").replace(",",""))

    entry_cantidad.delete(0,tk.END)
    entry_cantidad.insert(0,valores[3])

    entry_stock.delete(0,tk.END)
    entry_stock.insert(0,valores[4])


def actualizar_producto():

    id_producto = entry_id.get()

    if id_producto == "":
        messagebox.showwarning("Seleccione","Seleccione un producto")
        return

    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE productos
    SET nombre=?,precio=?,cantidad=?,stock_minimo=?
    WHERE id=?
    """,(
        entry_nombre.get(),
        entry_precio.get(),
        entry_cantidad.get(),
        entry_stock.get(),
        id_producto
    ))

    conn.commit()
    conn.close()

    limpiar_campos()
    mostrar_productos()


def eliminar_producto():

    id_producto = entry_id.get()

    if id_producto == "":
        messagebox.showwarning("Seleccione","Seleccione un producto")
        return

    confirm = messagebox.askyesno("Confirmar","¿Eliminar producto?")

    if confirm:

        conn = sqlite3.connect("inventario.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM productos WHERE id=?", (id_producto,))

        conn.commit()
        conn.close()

        limpiar_campos()
        mostrar_productos()


def alerta_stock():

    for row in tabla.get_children():
        tabla.delete(row)

    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM productos
    WHERE cantidad < stock_minimo
    """)

    datos = cursor.fetchall()

    for fila in datos:
        tabla.insert("",tk.END,values=(
            fila[0],
            fila[1],
            f"$ {fila[2]:,.0f}",
            fila[3],
            fila[4]
        ))

    conn.close()

    if len(datos)==0:
        messagebox.showinfo("Stock","No hay productos en alerta")


def limpiar_campos():

    entry_id.config(state="normal")
    entry_id.delete(0,tk.END)
    entry_id.config(state="readonly")

    entry_nombre.delete(0,tk.END)
    entry_precio.delete(0,tk.END)
    entry_cantidad.delete(0,tk.END)
    entry_stock.delete(0,tk.END)


# ==============================
# INTERFAZ
# ==============================

ventana = tk.Tk()
ventana.title("Gestión de Inventario")
ventana.geometry("900x520")
ventana.configure(bg="#eef2f7")

# ======= ESTILO =======

style = ttk.Style()
style.theme_use("default")

style.configure(
    "Treeview",
    font=("Segoe UI",10),
    rowheight=25
)

style.configure(
    "Treeview.Heading",
    font=("Segoe UI",11,"bold")
)

# ======= TITULO =======

titulo = tk.Label(
    ventana,
    text="Sistema de Inventario",
    font=("Segoe UI",20,"bold"),
    bg="#eef2f7",
    fg="#2c3e50"
)

titulo.pack(pady=10)


# ======= FORMULARIO =======

frame_form = tk.Frame(ventana,bg="#eef2f7")
frame_form.pack(pady=10)

label_font=("Segoe UI",10)

tk.Label(frame_form,text="ID",font=label_font,bg="#eef2f7").grid(row=0,column=0,padx=10,pady=5)

entry_id=tk.Entry(frame_form,state="readonly")
entry_id.grid(row=0,column=1,padx=10)


tk.Label(frame_form,text="Nombre",font=label_font,bg="#eef2f7").grid(row=1,column=0,padx=10,pady=5)

entry_nombre=tk.Entry(frame_form,width=25)
entry_nombre.grid(row=1,column=1,padx=10)


tk.Label(frame_form,text="Precio (COP)",font=label_font,bg="#eef2f7").grid(row=2,column=0,padx=10,pady=5)

entry_precio=tk.Entry(frame_form)
entry_precio.grid(row=2,column=1,padx=10)


tk.Label(frame_form,text="Cantidad",font=label_font,bg="#eef2f7").grid(row=3,column=0,padx=10,pady=5)

entry_cantidad=tk.Entry(frame_form)
entry_cantidad.grid(row=3,column=1,padx=10)


tk.Label(frame_form,text="Stock mínimo",font=label_font,bg="#eef2f7").grid(row=4,column=0,padx=10,pady=5)

entry_stock=tk.Entry(frame_form)
entry_stock.grid(row=4,column=1,padx=10)


# ======= BOTONES =======

frame_botones=tk.Frame(ventana,bg="#eef2f7")
frame_botones.pack(pady=10)

def crear_boton(texto,cmd,color):

    return tk.Button(
        frame_botones,
        text=texto,
        command=cmd,
        width=14,
        bg=color,
        fg="white",
        font=("Segoe UI",9,"bold"),
        relief="flat",
        cursor="hand2"
    )

crear_boton("Agregar",agregar_producto,"#27ae60").grid(row=0,column=0,padx=5)
crear_boton("Actualizar",actualizar_producto,"#2980b9").grid(row=0,column=1,padx=5)
crear_boton("Eliminar",eliminar_producto,"#c0392b").grid(row=0,column=2,padx=5)
crear_boton("Mostrar todo",mostrar_productos,"#7f8c8d").grid(row=0,column=3,padx=5)
crear_boton("Alerta stock",alerta_stock,"#f39c12").grid(row=0,column=4,padx=5)


# ======= TABLA =======

frame_tabla=tk.Frame(ventana)
frame_tabla.pack(pady=15)

columnas=("ID","Nombre","Precio","Cantidad","Stock mínimo")

tabla=ttk.Treeview(frame_tabla,columns=columnas,show="headings")

for col in columnas:

    tabla.heading(col,text=col)

    if col=="Nombre":
        tabla.column(col,width=220)
    else:
        tabla.column(col,width=120,anchor="center")

tabla.pack()

tabla.bind("<<TreeviewSelect>>",seleccionar_producto)


# ==============================
# INICIO
# ==============================

crear_db()
mostrar_productos()

ventana.mainloop()