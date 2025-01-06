import tkinter as tk

dimension = '500'
grid_size = 8

root = tk.Tk()
root.title("Chess")
root.geometry(dimension + 'x' + dimension)

dimension = float(dimension)
gap = dimension / grid_size

canvas = tk.Canvas(root, width=dimension, height=dimension, background='grey75')
for i in range(1, grid_size):
    canvas.create_line(i * gap, 0, i * gap, dimension)
    canvas.create_line(0, i * gap, dimension, i * gap)
    canvas.pack()

root.mainloop()


