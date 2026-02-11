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
