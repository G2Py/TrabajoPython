import tkinter as tk
from tkinter import messagebox

def verificar_login():
    # Aquí puedes agregar la lógica de verificación del correo y la contraseña
    correo = entry_correo.get()
    contrasenna = entry_contrasenna.get()

    # Verificación de ejemplo (reemplázala con tu lógica real)
    if correo == "ejemplo@gmail.com" and contrasenna == "admin":
        messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso")
    else:
        messagebox.showerror("Error", "Correo o contraseña incorrectos")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Inicio de Sesión")

# Crear etiquetas y campos de entrada para correo y contraseña
label_correo = tk.Label(ventana, text="Correo electrónico:")
label_correo.grid(row=0, column=0, padx=10, pady=10)

entry_correo = tk.Entry(ventana)
entry_correo.grid(row=0, column=1, padx=10, pady=10)

label_contrasenna = tk.Label(ventana, text="Contraseña:")
label_contrasenna.grid(row=1, column=0, padx=10, pady=10)

entry_contrasenna = tk.Entry(ventana, show="*")  # La contraseña se muestra como asteriscos
entry_contrasenna.grid(row=1, column=1, padx=10, pady=10)

# Botón de inicio de sesión
boton_login = tk.Button(ventana, text="Iniciar Sesión", command=verificar_login)
boton_login.grid(row=2, column=0, columnspan=2, pady=10)

# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()