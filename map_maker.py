import random
import pygame

colours = {
    "blue": (0, 94, 255),
    "green": (6, 138, 30),
    "grey": (132, 138, 148)
}

def grid_map():
    grid = []
    nodes = 81
    
    for node in range(nodes):
        rando = random.uniform(0, 1)
        grid.append(rando)
        
    return grid

def create_block(colour, x, y, surface):
    square = pygame.Rect(x, y, 25, 25)
    pygame.draw.rect(surface, colour, square)
    pygame.display.update()
    

def create_terrain(map, surface):
    xCount = 0
    yCount = 0
    
    for i in range(len(map)):
        if map[i] >= 0 and map[i] < 0.25:
            create_block(colours["blue"], xCount, yCount, surface)
        elif map[i] >= 0.25 and map[i] < 0.80:
            create_block(colours["green"], xCount, yCount, surface)
        else:
            create_block(colours["grey"], xCount, yCount, surface)
        
        if xCount >= 200:
            xCount = 0
            yCount += 25
        elif xCount < 200:
            xCount += 25
