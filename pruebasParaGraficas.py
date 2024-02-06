import tkinter as tk
from tkinter import messagebox

import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from fontawesome import icons


# Datos de ejemplo
total_dinero = 1000  # Monto total que tienes
gastos = {'Comida': 200, 'Transporte': 50, 'Entretenimiento': 100, 'Otros': 75}

# Calcular el monto restante después de los gastos
monto_restante = total_dinero - sum(gastos.values())

# Campos y valores para el gráfico
campos = list(gastos.keys()) + ['Monto Restante']
valores = list(gastos.values()) + [monto_restante]
colores = ['lightcoral', 'lightskyblue', 'lightgreen', 'gold']

# Crear el gráfico de barras horizontales sin iconos
fig, ax = plt.subplots()

# Añadir barras horizontales
bars = ax.barh(campos, valores, color=colores)

# Añadir título
plt.title('Gastos vs. Monto Restante')

# Mostrar el gráfico
plt.show()




'''
# Datos de ejemplo
campos = ['Campo A', 'Campo B', 'Campo C', 'Campo D']
valores = [25, 30, 20, 25]
colores = ['lightcoral', 'lightskyblue', 'lightgreen', 'gold']
explode = (0.1, 0, 0, 0)  # Destacar un sector (opcional)

# Crear el gráfico circular
plt.pie(valores, labels=campos, colors=colores, autopct='%1.1f%%', startangle=140, explode=explode)

# Añadir un círculo en el centro para que parezca un donut (opcional)
centro_circulo = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centro_circulo)

# Añadir título
plt.title('Gráfico Circular con Campos')

# Mostrar el gráfico
plt.axis('equal')  # Aspecto igual para que parezca un círculo
plt.show()

# Datos de ejemplo
total_dinero = 1000  # Monto total que tienes
gastos = {'Comida': 200, 'Transporte': 50, 'Entretenimiento': 100, 'Otros': 75}

# Calcular el monto restante después de los gastos
monto_restante = total_dinero - sum(gastos.values())

# Campos y valores para el gráfico
campos = list(gastos.keys()) + ['Monto Restante']
valores = list(gastos.values()) + [monto_restante]
colores = ['#ffcccb','silver', 'lightskyblue', 'lightgreen', 'gold']

# Crear el gráfico circular
plt.pie(valores, labels=campos, colors=colores, autopct='%1.1f%%', startangle=140)

# Añadir un círculo en el centro para que parezca un donut (opcional)
centro_circulo = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centro_circulo)

# Añadir título
plt.title('Gastos vs. Monto Restante')

# Mostrar el gráfico
plt.axis('equal')  # Aspecto igual para que parezca un círculo
plt.show()
'''

