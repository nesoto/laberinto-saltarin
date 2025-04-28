import heapq

def movimientos_validos(i, j, grid):
    movimientos = []
    filas = len(grid)
    columnas = len(grid[0])
    salto = grid[i][j]

    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # arriba, abajo, izquierda, derecha

    for dx, dy in direcciones:
        ni, nj = i + dx * salto, j + dy * salto
        if 0 <= ni < filas and 0 <= nj < columnas:
            movimientos.append((ni, nj))

    return movimientos

def cargar_laberintos(nombre_archivo):
    laberintos = []

    with open(nombre_archivo, 'r') as archivo:
        while True:
            linea = archivo.readline()
            if not linea:
                break

            if linea.strip() == "0":
                break

            m, n, start_row, start_col, goal_row, goal_col = map(int, linea.strip().split())
            grid = []
            for _ in range(m):
                fila = list(map(int, archivo.readline().strip().split()))
                grid.append(fila)

            laberinto = {
                "rows": m,
                "cols": n,
                "start": (start_row, start_col),
                "goal": (goal_row, goal_col),
                "grid": grid
            }
            laberintos.append(laberinto)
    return laberintos

def dfs(laberinto):
    start = laberinto["start"]
    goal = laberinto["goal"]
    grid = laberinto["grid"]

    stack = [(start, [])]  # (posición, ruta)
    visitados = set()

    while stack:
        actual, ruta = stack.pop()

        if actual == goal:
            return len(ruta), ruta

        if actual in visitados:
            continue
        visitados.add(actual)

        for vecino in movimientos_validos(actual[0], actual[1], grid):
            if vecino not in visitados:
                stack.append((vecino, ruta + [vecino]))

    return "no hay solución", []


def costo_uniforme(laberinto):
    start = laberinto["start"]
    goal = laberinto["goal"]
    grid = laberinto["grid"]

    visitados = set()
    heap = []  # (costo, posición, ruta)
    heapq.heappush(heap, (0, start, []))

    while heap:
        costo, actual, ruta = heapq.heappop(heap)

        if actual == goal:
            return costo, ruta

        if actual in visitados:
            continue
        visitados.add(actual)

        for vecino in movimientos_validos(actual[0], actual[1], grid):
            if vecino not in visitados:
                heapq.heappush(heap, (costo + 1, vecino, ruta + [vecino]))

    return "no hay solución", []

def ruta_a_direcciones(ruta): # Para saber si va hacia arriba, abajo, izquierda o derecha
    direcciones = []
    for i in range(1, len(ruta)):
        actual = ruta[i - 1]
        siguiente = ruta[i]
        dx = siguiente[0] - actual[0]
        dy = siguiente[1] - actual[1]

        if dx < 0:
            direcciones.append("Arriba")
        elif dx > 0:
            direcciones.append("Abajo")
        elif dy < 0:
            direcciones.append("Izquierda")
        elif dy > 0:
            direcciones.append("Derecha")
    return direcciones


if __name__ == "__main__":
    laberintos = cargar_laberintos("laberintos.txt")
    for i, lab in enumerate(laberintos):
        print(f"Laberinto {i+1}:")

        pasos_dfs, ruta_dfs = dfs(lab)
        print("DFS →", pasos_dfs)
        if ruta_dfs:
            ruta_completa = [lab["start"]] + ruta_dfs
            print("Ruta:", ruta_completa)
            print("Movimientos:", ruta_a_direcciones(ruta_completa))

        pasos_uc, ruta_uc = costo_uniforme(lab)
        print("Costo uniforme →", pasos_uc)
        if ruta_uc:
            ruta_completa = [lab["start"]] + ruta_uc
            print("Ruta:", ruta_completa)
            print("Movimientos:", ruta_a_direcciones(ruta_completa))

        print()

