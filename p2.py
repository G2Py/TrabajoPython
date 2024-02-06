import tkinter as tk
from tkinter import ttk, messagebox


# Función para actualizar el saldo total
def actualizar_saldo():
    moneda_simbolo = monedas_simbolo.get(moneda_var.get(), "")  # Obtener el símbolo de la moneda
    saldo_label.config(text=f"Saldo Total: {saldo_var.get()} {moneda_simbolo}")

# Función para manejar la selección de la moneda
def seleccionar_moneda(event):
    actualizar_saldo()

# Función para manejar la selección del mes
def seleccionar_mes(event):
    # Lógica para manejar la selección del mes
    pass

# Función para manejar la selección del año
def seleccionar_anio(event):
    # Lógica para manejar la selección del año
    pass

# Función para manejar el botón "Agregar Gasto/Ingreso"
def abrir_ventana_agregar():
    ventana_agregar = tk.Toplevel(ventana_principal)
    ventana_agregar.title("Agregar Gasto/Ingreso")

    label_tipo = tk.Label(ventana_agregar, text="Seleccione el tipo:")
    label_tipo.grid(row=0, column=0, padx=10, pady=10)

    tipo_var = tk.StringVar(ventana_agregar, value="Gasto")
    tipo_radiobutton_gasto = tk.Radiobutton(ventana_agregar, text="Gasto", variable=tipo_var, value="Gasto")
    tipo_radiobutton_gasto.grid(row=0, column=1, padx=10, pady=10)

    tipo_radiobutton_ingreso = tk.Radiobutton(ventana_agregar, text="Ingreso", variable=tipo_var, value="Ingreso")
    tipo_radiobutton_ingreso.grid(row=0, column=2, padx=10, pady=10)

    label_cantidad = tk.Label(ventana_agregar, text="Ingrese la cantidad:")
    label_cantidad.grid(row=1, column=0, padx=10, pady=10)

    cantidad_var = tk.DoubleVar(ventana_agregar, value=0.0)
    cantidad_entry = tk.Entry(ventana_agregar, textvariable=cantidad_var)
    cantidad_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

    label_categoria = tk.Label(ventana_agregar, text="Seleccione la categoría:")
    label_categoria.grid(row=2, column=0, padx=10, pady=10)

    categorias = ["Categoría 1", "Categoría 2", "Categoría 3", "Categoría 4", "Categoría 5"]
    categoria_var = tk.StringVar(ventana_agregar, value=categorias[0])
    categoria_dropdown = ttk.Combobox(ventana_agregar, values=categorias, textvariable=categoria_var)
    categoria_dropdown.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

    def agregar_gasto_ingreso():
        cantidad = cantidad_var.get()
        tipo = tipo_var.get()

        if tipo == "Gasto":
            categoria = categoria_var.get()
            if not categoria:
                messagebox.showwarning("Advertencia", "Por favor, seleccione una categoría para el gasto.")
                return

            # Aquí puedes agregar la lógica específica para el gasto con categoría
            nuevo_saldo = float(saldo_var.get()) - cantidad
        else:
            nuevo_saldo = float(saldo_var.get()) + cantidad

        saldo_var.set("{:.2f}".format(nuevo_saldo))
        actualizar_saldo()
        ventana_agregar.destroy()

    boton_agregar = tk.Button(ventana_agregar, text="Agregar", command=agregar_gasto_ingreso)
    boton_agregar.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Función para abrir la ventana de configuración
def abrir_ventana_configuracion():
    ventana_configuracion = tk.Toplevel(ventana_principal)
    ventana_configuracion.title("Configuración")

    # Etiqueta y entrada para el nombre del cliente
    label_nombre = tk.Label(ventana_configuracion, text="Nombre del Cliente:")
    label_nombre.grid(row=0, column=0, padx=10, pady=10)
    nombre_var = tk.StringVar(ventana_configuracion, value="")  # Puedes establecer el valor por defecto
    nombre_entry = tk.Entry(ventana_configuracion, textvariable=nombre_var)
    nombre_entry.grid(row=0, column=1, padx=10, pady=10)

    # Desplegable para seleccionar el idioma
    idiomas = ["Español", "Inglés", "Francés"]  # Agrega más idiomas si es necesario
    idioma_var = tk.StringVar(ventana_configuracion)
    idioma_var.set(idiomas[0])  # Idioma por defecto
    idioma_dropdown = ttk.Combobox(ventana_configuracion, values=idiomas, textvariable=idioma_var)
    idioma_dropdown.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

    # Desplegable para seleccionar la moneda con símbolo
    monedas_simbolo = {"EUR": "€", "USD": "$", "GBP": "£"}  # Puedes agregar más monedas si es necesario
    moneda_simbolo_var = tk.StringVar(ventana_configuracion)
    moneda_simbolo_var.set("€")  # Moneda por defecto
    moneda_simbolo_dropdown = ttk.Combobox(ventana_configuracion, values=list(monedas_simbolo.values()), textvariable=moneda_simbolo_var)
    moneda_simbolo_dropdown.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

    # Botón para cambiar la contraseña
    def cambiar_contrasena():
        # Lógica para cambiar la contraseña
        messagebox.showinfo("Cambiar Contraseña", "Función aún no implementada")

    boton_cambiar_contrasena = tk.Button(ventana_configuracion, text="Cambiar Contraseña", command=cambiar_contrasena)
    boton_cambiar_contrasena.grid(row=3, column=0, padx=10, pady=10)

    # Botón para cerrar sesión
    def cerrar_sesion():
        ventana_principal.destroy()  # Cerrar la ventana principal
        # Aquí puedes agregar la lógica para volver a la ventana de inicio de sesión
        messagebox.showinfo("Cerrar Sesión", "Función aún no implementada")

    boton_cerrar_sesion = tk.Button(ventana_configuracion, text="Cerrar Sesión", command=cerrar_sesion)
    boton_cerrar_sesion.grid(row=3, column=1, padx=10, pady=10)

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Página Principal")

# Título y Saldo Total
titulo_label = tk.Label(ventana_principal, text="Página Principal", font=("Helvetica", 16))
titulo_label.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

saldo_var = tk.StringVar(ventana_principal, value="00.00")
saldo_label = tk.Label(ventana_principal, text=f"Saldo Total: {saldo_var.get()} €")
saldo_label.grid(row=1, column=0, padx=10, pady=10)

# Desplegable de moneda
monedas = ["EUR", "USD", "GBP"]
monedas_simbolo = {"EUR": "€", "USD": "$", "GBP": "£"}  # Símbolos de las monedas
moneda_var = tk.StringVar(ventana_principal)
moneda_var.set(monedas[0])
moneda_dropdown = ttk.Combobox(ventana_principal, values=monedas, textvariable=moneda_var)
moneda_dropdown.grid(row=1, column=1, padx=10, pady=10)
moneda_dropdown.bind("<<ComboboxSelected>>", seleccionar_moneda)

# Mes actual y Año actual
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
mes_var = tk.StringVar(ventana_principal)
mes_var.set(meses[0])
mes_dropdown = ttk.Combobox(ventana_principal, values=meses, textvariable=mes_var)
mes_dropdown.grid(row=2, column=0, padx=10, pady=10)
mes_dropdown.bind("<<ComboboxSelected>>", seleccionar_mes)

anio_var = tk.StringVar(ventana_principal)
anio_var.set("2024")  # Puedes cambiar esto con el año actual
anio_entry = ttk.Entry(ventana_principal, textvariable=anio_var)
anio_entry.grid(row=2, column=1, padx=10, pady=10)
anio_entry.bind("<FocusOut>", seleccionar_anio)

# Botones
boton_agregar_gasto = tk.Button(ventana_principal, text="Agregar Gasto/Ingreso", command=abrir_ventana_agregar)
boton_agregar_gasto.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

boton_agregar_categoria = tk.Button(ventana_principal, text="Añadir Categoría", command=lambda: print("Agregar Categoría"))
boton_agregar_categoria.grid(row=3, column=2, padx=10, pady=10)

boton_configuracion = tk.Button(ventana_principal, text="Configuración", command=abrir_ventana_configuracion)
boton_configuracion.grid(row=3, column=3, padx=10, pady=10)

# Ejecutar la aplicación
ventana_principal.mainloop()