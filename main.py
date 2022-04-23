import tkinter as tk
from map_maker import *

window = tk.Tk()
canvas = tk.Canvas(width=500, height=500)
window.title("Procedural World Gen")
window.geometry("500x500")

def new_world():
    noise_map = grid_map()
    create_terrain(noise_map, canvas)

button = tk.Button(window, text="New World", command=new_world)
button.pack()

window.mainloop()