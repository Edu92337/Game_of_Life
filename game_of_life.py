import pygame
import numpy as np

#CONSTANTES

WIDTH,HEIGHT = 600,600
CELL_SIZE = 10
GRID_WIDTH = WIDTH//CELL_SIZE
GRID_HEIGHT = HEIGHT//CELL_SIZE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Grid():

    def __init__(self):
        self.grid = np.random.choice([0,1],size=(GRID_WIDTH,GRID_HEIGHT))
        self.height = HEIGHT//CELL_SIZE
        self.width = WIDTH//CELL_SIZE
    def draw(self,screen):
        for linha in range(self.height):
            for coluna in range(self.width):
                cor = WHITE if self.grid[linha][coluna] == 1 else BLACK
                pygame.draw.rect(screen,cor,(CELL_SIZE*coluna,CELL_SIZE*linha,CELL_SIZE,CELL_SIZE))
    
    def update_grid(self):
        new_grid = self.grid.copy()
        for linha in range(GRID_HEIGHT):
            for coluna in range(GRID_WIDTH):
                neighbors = sum([
                    self.grid[(linha-1) % GRID_HEIGHT][(coluna-1) % GRID_WIDTH],  # Superior esquerdo
                    self.grid[(linha-1) % GRID_HEIGHT][coluna],                   # Superior
                    self.grid[(linha-1) % GRID_HEIGHT][(coluna+1) % GRID_WIDTH],  # Superior direito
                    self.grid[linha][(coluna-1) % GRID_WIDTH],                    # Esquerda
                    self.grid[linha][(coluna+1) % GRID_WIDTH],                    # Direita
                    self.grid[(linha+1) % GRID_HEIGHT][(coluna-1) % GRID_WIDTH],  # Inferior esquerdo
                    self.grid[(linha+1) % GRID_HEIGHT][coluna],                   # Inferior
                    self.grid[(linha+1) % GRID_HEIGHT][(coluna+1) % GRID_WIDTH]   # Inferior direito
                ])
                if self.grid[linha][coluna] == 1: 
                    if neighbors < 2 or neighbors > 3:
                        new_grid[linha][coluna] = 0  
                elif self.grid[linha][coluna] == 0:  
                    if neighbors == 3:
                        new_grid[linha][coluna] = 1  
        self.grid = new_grid
        
def main():
    pygame.init()
    screen = pygame.display.set_mode((HEIGHT,WIDTH))
    pygame.display.set_caption("Game of Life")
    clock = pygame.time.Clock()
    
    grid = Grid()

    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        grid.update_grid()
    
        screen.fill(BLACK)
        grid.draw(screen)
        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    main()