import tkinter as tk
from tkinter import messagebox
import subprocess

def on_button_click():
    subprocess.call(['sudo', 'airodump-ng', 'wlan0'])

def exit_script():
    result = messagebox.askquestion("Exit", "Are you sure you want to exit?")
    if result == "yes":
        window.destroy()

# Create the main window
window = tk.Tk()
window.attributes("-fullscreen", True)

# Set the title
window.title("made by vertydagenius!")

# Set the title background color
window.configure(bg="black")
window.option_add('*titlebackground', 'black')

# Create a label
label = tk.Label(window, text="Welcome to the aircrack GUI for Raspberry Pi! (made by vertydagenius)")
label.pack()

# Create a button
button = tk.Button(window, text="Scan BSSIDs", command=on_button_click)
button.pack()

# Create an exit button
exit_button = tk.Button(window, text="Exit", command=exit_script)
exit_button.pack()

# Start the main event loop
window.mainloop()
