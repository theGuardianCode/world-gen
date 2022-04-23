import random

def grid_map():
    grid = []
    nodes = 121
    
    for node in range(nodes):
        rando = random.uniform(0, 1)
        grid.append(rando)
        
    return grid

def create_block(colour, x, y, canvas):
    canvas.create_rectangle(x, y, x+25, y+25, fill=colour, outline=colour)

def create_terrain(map, canvas):
    xCount = 0
    yCount = 0
    
    for i in range(len(map)):
        if map[i] >= 0 and map[i] < 0.25:
            create_block("#005eff", xCount, yCount, canvas)
        elif map[i] <= 1 and map[i] > 0.80:
            create_block("#848a94", xCount, yCount, canvas)
        else:
            create_block("#068a1e", xCount, yCount, canvas)
        
        if xCount >= 250:
            xCount = 0
            yCount += 25
        elif xCount < 250:
            xCount += 25
    
    canvas.pack()