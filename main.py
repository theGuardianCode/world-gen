import pygame
from map_maker import *
pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("3d Procedural Generation")

def new_world():
    noise_map = grid_map()
    create_terrain(noise_map, window)
    
def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                new_world()
                
    
    pygame.quit()
    
main()