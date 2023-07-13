import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Lista para almacenar los alimentos registrados
alimentos = []

def registrar_alimento():
    nombre = entrada_alimento.get()
    fecha_caducidad = calendario.selection_get().strftime("%d/%m/%Y")
    alimentos.append((nombre, fecha_caducidad))
    texto_resultado.config(text=f"El alimento '{nombre}' ha sido registrado. Fecha de caducidad: {fecha_caducidad}")
    actualizar_lista_alimentos()

def mostrar_alimentos():
    if len(alimentos) == 0:
        texto_resultado.config(text="No hay alimentos registrados.")
    else:
        texto_resultado.config(text="Alimentos registrados:\n" + "\n".join([alimento[0] for alimento in alimentos]))

def buscar_alimento():
    nombre_buscar = entrada_buscar.get()
    encontrados = [alimento[0] for alimento in alimentos if nombre_buscar.lower() in alimento[0].lower()]
    if len(encontrados) == 0:
        texto_resultado.config(text="No se encontraron alimentos con ese nombre.")
    else:
        texto_resultado.config(text=f"Alimentos encontrados con el nombre '{nombre_buscar}':\n" + "\n".join(encontrados))

def eliminar_alimento():
    if len(alimentos) == 0:
        texto_resultado.config(text="No hay alimentos registrados.")
    else:
        indice = lista_alimentos.curselection()
        if len(indice) == 0:
            texto_resultado.config(text="Selecciona un alimento de la lista.")
        else:
            alimento_eliminado = alimentos.pop(indice[0])
            texto_resultado.config(text=f"El alimento '{alimento_eliminado[0]}' ha sido eliminado.")
            actualizar_lista_alimentos()

def ver_fecha_caducidad():
    indice = lista_alimentos.curselection()
    if len(indice) == 0:
        texto_resultado.config(text="Selecciona un alimento de la lista.")
    else:
        alimento_seleccionado = alimentos[indice[0]]
        texto_resultado.config(text=f"Fecha de caducidad del alimento '{alimento_seleccionado[0]}': {alimento_seleccionado[1]}")

def calcular_cantidad_total():
    cantidad_total = len(alimentos)
    texto_resultado.config(text=f"La cantidad total de alimentos registrados es: {cantidad_total}")

def actualizar_lista_alimentos():
    lista_alimentos.delete(0, tk.END)
    for alimento in alimentos:
        lista_alimentos.insert(tk.END, alimento[0])

def mostrar_calendario():
    ventana_calendario = tk.Toplevel(ventana)
    calendario = ttk.Calendar(ventana_calendario)
    calendario.pack(padx=10, pady=10)

    def seleccionar_fecha():
        fecha_seleccionada = calendario.selection_get().strftime("%d/%m/%Y")
        entrada_fecha.delete(0, tk.END)
        entrada_fecha.insert(tk.END, fecha_seleccionada)
        ventana_calendario.destroy()

    boton_seleccionar = tk.Button(ventana_calendario, text="Seleccionar fecha", command=seleccionar_fecha)
    boton_seleccionar.pack(pady=10)

# Crear ventana
ventana = tk.Tk()
ventana.title("EAT ME FIRST")

# Marco para el formulario de registro
marco_registro = tk.Frame(ventana)
marco_registro.pack(pady=10)

# Etiqueta y campo de entrada para el nombre del alimento
etiqueta_alimento = tk.Label(marco_registro, text="Nombre del alimento:")
etiqueta_alimento.grid(row=0, column=0, sticky="w")
entrada_alimento = tk.Entry(marco_registro, width=30)
entrada_alimento.grid(row=0, column=1, padx=5)

# Etiqueta y campo de entrada para la fecha de caducidad
etiqueta_fecha = tk.Label(marco_registro, text="Fecha de caducidad:")
etiqueta_fecha.grid(row=1, column=0, sticky="w")
entrada_fecha = tk.Entry(marco_registro, width=12)
entrada_fecha.grid(row=1, column=1, padx=5)

boton_mostrar_calendario = tk.Button(marco_registro, text="Mostrar calendario", command=mostrar_calendario)
boton_mostrar_calendario.grid(row=1, column=2, padx=5)

# Botón para registrar el alimento
boton_registrar = tk.Button(marco_registro, text="Registrar alimento", command=registrar_alimento)
boton_registrar.grid(row=2, column=0, columnspan=2, pady=5)

# Marco para las opciones
marco_opciones = tk.Frame(ventana)
marco_opciones.pack(pady=10)

# Botón para mostrar todos los alimentos registrados
boton_mostrar = tk.Button(marco_opciones, text="Mostrar alimentos registrados", command=mostrar_alimentos)
boton_mostrar.grid(row=0, column=0, padx=5)

# Etiqueta y campo de entrada para buscar alimento por nombre
etiqueta_buscar = tk.Label(marco_opciones, text="Buscar alimento por nombre:")
etiqueta_buscar.grid(row=1, column=0, sticky="w")
entrada_buscar = tk.Entry(marco_opciones, width=30)
entrada_buscar.grid(row=1, column=1, padx=5)
boton_buscar = tk.Button(marco_opciones, text="Buscar alimento", command=buscar_alimento)
boton_buscar.grid(row=1, column=2, padx=5)

# Lista de alimentos registrados
lista_alimentos = tk.Listbox(ventana, width=50)
lista_alimentos.pack()

# Marco para las opciones adicionales
marco_opciones_adicionales = tk.Frame(ventana)
marco_opciones_adicionales.pack(pady=10)

# Botón para eliminar alimento seleccionado
boton_eliminar = tk.Button(marco_opciones_adicionales, text="Eliminar alimento seleccionado", command=eliminar_alimento)
boton_eliminar.grid(row=0, column=0, padx=5)

# Botón para ver la fecha de caducidad del alimento seleccionado
boton_ver_fecha = tk.Button(marco_opciones_adicionales, text="Ver fecha de caducidad", command=ver_fecha_caducidad)
boton_ver_fecha.grid(row=0, column=1, padx=5)

# Botón para calcular la cantidad total de alimentos registrados
boton_calcular = tk.Button(marco_opciones_adicionales, text="Calcular cantidad total de alimentos", command=calcular_cantidad_total)
boton_calcular.grid(row=0, column=2, padx=5)

# Etiqueta para mostrar el resultado
texto_resultado = tk.Label(ventana, text="", font=("Arial", 12))
texto_resultado.pack()

# Ejecutar ventana
ventana.mainloop()