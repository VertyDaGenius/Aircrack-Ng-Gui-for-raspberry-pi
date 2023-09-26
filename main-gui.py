import tkinter as tk #not finished.
import subprocess
from tkinter import messagebox

def on_button_click():
    subprocess.Popen(["x-terminal-emulator", "-e", "sudo airodump-ng wlan0"])

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
label = tk.Label(window, text="Welcome to the aircrack gui for raspberry pi! (made by vertydagenius)")
label.pack()

# Create a button
button = tk.Button(window, text="Scan bssids", command=on_button_click)
button.pack()

# Create an exit button
exit_button = tk.Button(window, text="Exit", command=exit_script)
exit_button.pack()

# Start the main event loop
window.mainloop()
