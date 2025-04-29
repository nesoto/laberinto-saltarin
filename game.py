import pygame
import sys
from agente import costo_uniforme, cargar_laberintos, dfs

pygame.init()

# Configuración de la pantalla

CELL_SIZE = 50
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
START_COLOR = (100, 255, 100)
GOAL_COLOR = (255, 100, 100)
PATH_COLOR = (100, 100, 255) 


def draw_grid(grid, start, goal, ruta=[]):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pos = (row, col)

            if pos == start:
                color = START_COLOR
            elif pos == goal:
                color = GOAL_COLOR
            elif pos in ruta:
                color = PATH_COLOR
            else:
                color = WHITE

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)

            font = pygame.font.SysFont(None, 24)
            text = font.render(str(grid[row][col]), True, BLACK)
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)



def preparar_laberinto(lab):
    global ruta_completa, ruta_mostrar, indice_ruta, ROWS, COLS, WIDTH, HEIGHT, screen

    # Resolver laberinto
    _, ruta = costo_uniforme(lab)
    # _, ruta = dfs(lab) Descomentar para usar DFS
    ruta_completa = [lab["start"]] + ruta if ruta else []

    # Reset animación
    ruta_mostrar = [lab["start"]]
    indice_ruta = 0

    # Configurar pantalla
    ROWS, COLS = lab["rows"], lab["cols"]
    WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Laberinto Saltarín")


if __name__ == "__main__":
    pygame.init()

    # Cargar laberintos
    laberintos = cargar_laberintos("laberintos.txt")
    indice_laberinto = 0

    preparar_laberinto(laberintos[indice_laberinto])

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Siguiente laberinto usando en el espacio
                    indice_laberinto = (indice_laberinto + 1) % len(laberintos)
                    preparar_laberinto(laberintos[indice_laberinto])

        screen.fill(WHITE)
        draw_grid(laberintos[indice_laberinto]["grid"], 
                  laberintos[indice_laberinto]["start"], 
                  laberintos[indice_laberinto]["goal"], 
                  ruta_mostrar)
        pygame.display.flip()

        # Aca se anima la ruta del agente al resolver usando costo uniforme
        pygame.time.delay(500)
        if indice_ruta < len(ruta_completa) - 1:
            indice_ruta += 1
            ruta_mostrar.append(ruta_completa[indice_ruta])

        clock.tick(60)

    pygame.quit()
    sys.exit()