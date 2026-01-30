import matplotlib.pyplot as plt
import numpy as np

def graficar_vectores(vectores, colores, titulo='Gráfica de Vectores', 
                      nombre_x='Eje X', nombre_y='Eje Y', alpha=1):
    
    plt.figure(figsize=(10, 8))
    plt.grid(color='grey', linestyle='--', linewidth=0.5, alpha=0.7)
    
    # Ejes principales
    plt.axvline(x=0, color='black', linewidth=1.5, zorder=1)
    plt.axhline(y=0, color='black', linewidth=1.5, zorder=1)
    
    # Límites dinámicos
    all_x = [v[0] for v in vectores] + [0]
    all_y = [v[1] for v in vectores] + [0]
    
    margin = 1.2
    plt.xlim(min(all_x) * margin if min(all_x) < 0 else -1, max(all_x) * margin)
    plt.ylim(min(all_y) * margin if min(all_y) < 0 else -1, max(all_y) * margin)

    for i, vector in enumerate(vectores):
        plt.quiver(0, 0, vector[0], vector[1], angles='xy', 
                   scale_units='xy', scale=1, color=colores[i], 
                   alpha=alpha, zorder=3)
    
    # --- Nuevas líneas para etiquetas ---
    plt.title(titulo, fontsize=16, fontweight='bold')
    plt.xlabel(nombre_x, fontsize=12)
    plt.ylabel(nombre_y, fontsize=12)
    # ------------------------------------

    plt.gca().set_aspect('equal')
    plt.show()