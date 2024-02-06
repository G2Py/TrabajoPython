import tkinter as tk
from tkinter import messagebox
import mysql.connector

def verificar_login():
    correo = entry_correo.get()
    contrasenna = entry_contrasenna.get()

    try:
        # Conectar a la base de datos MySQL en localhost
        db_connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='gastos_personales'
        )
        cursor = db_connection.cursor()

        # Verificar credenciales en la base de datos MySQL
        cursor.execute('SELECT * FROM Usuarios WHERE correo = %s AND contraseña = %s', (correo, contrasenna))
        user_data = cursor.fetchone()

        if user_data:
            messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso")
        else:
            messagebox.showerror("Error", "Correo o contraseña incorrectos")

    except mysql.connector.Error as err:
        messagebox.showerror("Error de conexión", f"Error: {err}")

    finally:
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()

def abrir_ventana_registro():
    ventana_registro = tk.Toplevel(ventana)
    ventana_registro.title("Registro")

    # Etiquetas y campos de entrada para el registro
    label_nombre = tk.Label(ventana_registro, text="Nombre:")
    label_nombre.grid(row=0, column=0, padx=10, pady=10)

    entry_nombre = tk.Entry(ventana_registro)
    entry_nombre.grid(row=0, column=1, padx=10, pady=10)

    label_apellidos = tk.Label(ventana_registro, text="Apellidos:")
    label_apellidos.grid(row=1, column=0, padx=10, pady=10)

    entry_apellidos = tk.Entry(ventana_registro)
    entry_apellidos.grid(row=1, column=1, padx=10, pady=10)

    label_correo_registro = tk.Label(ventana_registro, text="Correo electrónico:")
    label_correo_registro.grid(row=2, column=0, padx=10, pady=10)

    entry_correo_registro = tk.Entry(ventana_registro)
    entry_correo_registro.grid(row=2, column=1, padx=10, pady=10)

    label_contrasenna_registro = tk.Label(ventana_registro, text="Contraseña:")
    label_contrasenna_registro.grid(row=3, column=0, padx=10, pady=10)

    entry_contrasenna_registro = tk.Entry(ventana_registro, show="*")
    entry_contrasenna_registro.grid(row=3, column=1, padx=10, pady=10)

    # Botón de registro
    boton_registro = tk.Button(ventana_registro, text="Registrarse", command=lambda: registrar_usuario(
        entry_nombre.get(),
        entry_apellidos.get(),
        entry_correo_registro.get(),
        entry_contrasenna_registro.get()
    ))
    boton_registro.grid(row=4, column=0, columnspan=2, pady=10)

def registrar_usuario(nombre, apellidos, correo, contrasenna):
    try:
        # Conectar a la base de datos MySQL en localhost
        db_connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='gastos_personales'
        )
        cursor = db_connection.cursor()

        # Insertar nuevo usuario en la base de datos MySQL
        cursor.execute('INSERT INTO Usuarios (nombre, apellidos, correo, contraseña) VALUES (%s, %s, %s, %s)',
                       (nombre, apellidos, correo, contrasenna))
        db_connection.commit()

        messagebox.showinfo("Registro exitoso", "Usuario registrado exitosamente")

    except mysql.connector.Error as err:
        messagebox.showerror("Error de conexión", f"Error: {err}")

    finally:
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Inicio de Sesión")

# Etiquetas y campos de entrada para correo y contraseña
label_correo = tk.Label(ventana, text="Correo electrónico:")
label_correo.grid(row=0, column=0, padx=10, pady=10)

entry_correo = tk.Entry(ventana)
entry_correo.grid(row=0, column=1, padx=10, pady=10)

label_contrasenna = tk.Label(ventana, text="Contraseña:")
label_contrasenna.grid(row=1, column=0, padx=10, pady=10)

entry_contrasenna = tk.Entry(ventana, show="*")  # Contraseña mostrada como asteriscos
entry_contrasenna.grid(row=1, column=1, padx=10, pady=10)

# Botones de inicio de sesión y registro
boton_login = tk.Button(ventana, text="Iniciar Sesión", command=verificar_login)
boton_login.grid(row=2, column=0, pady=10)

boton_registro = tk.Button(ventana, text="Registrarse", command=abrir_ventana_registro)
boton_registro.grid(row=2, column=1, pady=10)

# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()