from tkinter import ttk, Canvas, Scrollbar, font
from ttkthemes import ThemedTk

root = ThemedTk(theme="Radiance")
root.title("Holy Bible+")
root.geometry("900x900")

heading = ttk.Label(root, text="Choose Preferences:", font=("Comic Sans MS", 20, "bold"))
heading_font = font.Font(family = "Comic Sans MS", size = 20, weight = "bold")
heading.grid(row = 0, column = 0)

root.mainloop()
