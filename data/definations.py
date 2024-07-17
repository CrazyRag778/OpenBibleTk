'''
This is the the function definition files for the application.
For safe execution of the software, do not change any essential code.
Feel free to customise the code in your way to make the app better...


'''

from tkinter import ttk, Canvas, Scrollbar, messagebox
from tkinter import *
import webbrowser

def show_about():
    messagebox.showinfo("Developer", "The OpenBibleTK Project\nCrazyRag778, Dibyojit Datta\nFully Open Source") 
def open_pytbib_githbpg():
    webbrowser.open("https://github.com/avendesora/pythonbible")
def open_projct_githbpg():
    webbrowser.open("https://github.com/CrazyRag778/OpenBibleTk")
