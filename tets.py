import tkinter as tk
from tkinter import messagebox

def open_custom_message_box():
    # Create a new window
    custom_box = tk.Toplevel(root)
    custom_box.title("Custom Message Box")

    # Add a message label
    message_label = tk.Label(custom_box, text="This is a custom message box.")
    message_label.pack(pady=10)

    # Add custom buttons
    button_frame = tk.Frame(custom_box)
    button_frame.pack(pady=10)

    def custom_button_click(button_value):
        custom_box.destroy()
        messagebox.showinfo("Button Clicked", f"You clicked the '{button_value}' button.")

    button1 = tk.Button(button_frame, text="Custom Button 1", command=lambda: custom_button_click("Custom Button 1"))
    button1.pack(side="left", padx=10)

    button2 = tk.Button(button_frame, text="Custom Button 2", command=lambda: custom_button_click("Custom Button 2"))
    button2.pack(side="left", padx=10)

    button3 = tk.Button(button_frame, text="Custom Button 3", command=lambda: custom_button_click("Custom Button 3"))
    button3.pack(side="left", padx=10)

# Create the main window
root = tk.Tk()
root.geometry("300x200")

# Add a button to open the custom message box
open_button = tk.Button(root, text="Open Custom Message Box", command=open_custom_message_box)
open_button.pack(pady=20)

root.mainloop()
