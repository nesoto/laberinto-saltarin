# Laberinto Saltarín - Inteligencia Artificial 2025

Este proyecto implementa el "Laberinto Saltarín" para el curso de Inteligencia Artificial 2025, usando Python y PyGame.

## Contenido
- Visualización del laberinto en PyGame.
- Implementación de agentes:
  - **DFS** (Depth-First Search)
  - **Costo Uniforme** (Búsqueda óptima)
- Animación del recorrido de la solución.
- Soporte para múltiples laberintos y cambio entre ellos (barra espaciadora).
  
## Requisitos
- Python 3.8 o superior
- PyGame
- La existencia de un archivo `laberintos.txt` en el mismo directorio que el script.

## Cómo ejecutar

1. Crear un entorno virtual (opcional):

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

2. Instalar dependencias:

    ```bash
    pip install pygame
    ```

3. Ejecutar el visualizador:

    ```bash
    python3 game.py
    ```
## Adicionales
- Si se quiere ver el numero de movimientos y la ruta de la solución ejecute el programa con el siguiente comando

    ```bash
    python3 agente.py
    ```
