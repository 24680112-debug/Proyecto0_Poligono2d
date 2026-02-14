import bpy
import math

# Limpiar escena
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Parámetros de la figura
radio = 3
angulo_actual = 0
paso_angular = 60

 # 360 / 60 = 6 círculos alrededor

# 1. Círculo Central
bpy.ops.mesh.primitive_circle_add(radius=radio, location=(0, 0, 0), vertices=64)

# --- IMPLEMENTACIÓN DEL CICLO WHILE ---

while angulo_actual < 360:
    # Calculamos la posición usando trigonometría
    # Convertimos grados a radianes porque math.cos y math.sin lo requieren
    x = radio * math.cos(math.radians(angulo_actual))
    y = radio * math.sin(math.radians(angulo_actual))
    
    # Creamos el círculo en la posición calculada
    bpy.ops.mesh.primitive_circle_add(radius=radio, location=(x, y, 0), vertices=64)
    
    # IMPORTANTE: Aumentamos el ángulo para que el bucle no sea infinito
    angulo_actual += paso_angular
