import random

def grid_map():
    grid = []
    nodes = 81
    
    for node in range(nodes):
        randint = random.randint(0, 1)
        grid.append(randint)
        
    return grid

def create_block(colour, x, y, canvas):
    canvas.create_rectangle(x, y, x+50, y+50, fill=colour, outline=colour)

def create_terrain(map, canvas):
    xCount = 0
    yCount = 0
    
    for i in range(len(map)):
        if map[i] == 0:
            create_block("#005eff", xCount, yCount, canvas)
        elif map[i] == 1:
            create_block("#068a1e", xCount, yCount, canvas)
        
        if xCount >= 400:
            xCount = 0
            yCount += 50
        elif xCount < 400:
            xCount += 50
    
    canvas.pack()