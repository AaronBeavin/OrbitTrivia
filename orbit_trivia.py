import tkinter as tk
from tkinter import messagebox

# Planet data
planets = {
    "Mercury": "Mercury is the closest planet to the Sun.",
    "Venus": "Venus is the hottest planet in our solar system.",
    "Earth": "Earth is the only planet known to support life.",
    "Mars": "Mars is known as the Red Planet.",
    "Jupiter": "Jupiter is the largest planet in our solar system."
}

# Function to show planet info
def show_info(planet):
    messagebox.showinfo(planet, planets[planet])

# Create window
window = tk.Tk()
window.title("OrbitTrivia 🌌")
window.geometry("400x400")

title = tk.Label(window, text="OrbitTrivia 🪐", font=("Arial", 20))
title.pack(pady=20)

info = tk.Label(window, text="Click a planet to learn about it!", font=("Arial", 12))
info.pack(pady=10)

# Create buttons for planets
for planet in planets:
    btn = tk.Button(window, text=planet, width=20, command=lambda p=planet: show_info(p))
    btn.pack(pady=5)

window.mainloop()