# Proyecto0_Poligono2d
Explicación de como crear un polígono en 2d mediante código

# 1. Se crea la estructura y se registra la escena
```bash
import bpy
import math

def crear_poligono_2d(nombre, lados, radio):
    malla = bpy.data.meshes.new(nombre)
    objeto = bpy.data.objects.new(nombre, malla)
    
    
    bpy.context.collection.objects.link(objeto)

    vertices = []
    aristas = []
```

# 2. Cálculo de los vértices, se crean las aristas y y construcción final
```bash
 for i in range (lados):
        angulo = 2 * math.pi * i / lados
        x = radio * math.cos(angulo)
        y = radio * math.sin(angulo)
        vertices.append((x, y, 0))
          
    for i in range(lados):
        aristas.append((i, (i + 1) % lados))
        
    malla.from_pydata(vertices, aristas, [])
    malla.update()
```

# 3. Se limpia la escena y se llama a la función
```bash
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
        
        
crear_poligono_2d("Poligono2D", lados=6, radio=5)     

```

# 4. Resultado
<img width="862" height="566" alt="image" src="https://github.com/user-attachments/assets/84a94fdf-7de4-4318-965b-8238fab2cbf3" />








# Proyecto Flor de vida
Explicación de como crear una flor de vida en Blender mediante código


# 1. Se crea el limpiador de escena
```bash
import bpy
import math


bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
```

# 2. Se determinan los parametros de la figura
```bash
radio = 3
angulo_actual = 0
paso_angular = 60

 # 360 / 60 = 6 círculos alrededor
```

# 3. Se crea el círculo central
```bash
radio = 3
angulo_actual = 0
paso_angular = 60

 # 360 / 60 = 6 círculos alrededor
```

# 4. Implementamos un ciclo while
```bash
while angulo_actual < 360:
    # Calculamos la posición usando trigonometría
    # Convertimos grados a radianes porque math.cos y math.sin lo requieren
    x = radio * math.cos(math.radians(angulo_actual))
    y = radio * math.sin(math.radians(angulo_actual))
```

# 5. Creamos un círculo en la posición calculada
```bash
bpy.ops.mesh.primitive_circle_add(radius=radio, location=(x, y, 0), vertices=64)
```

# 6. Aumentamos el ángulo para que el bucle no sea infinito (IMPORTANTE)
```bash
 angulo_actual += paso_angular
```

# 7. Resultado
<img width="682" height="538" alt="image" src="https://github.com/user-attachments/assets/4e2d9b1b-e91e-4954-b738-653294782d6d" />

