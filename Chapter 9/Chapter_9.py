# temperatureconverter.py
# GUI Temperature Converter
# Converts between Fahrenheit and Celsius

import tkinter as tk

# Convert Fahrenheit to Celsius
def fahrenheit_to_celsius():
    fahrenheit = float(fahrenheit_entry.get())
    celsius = (fahrenheit - 32) * 5 / 9

    celsius_entry.delete(0, tk.END)
    celsius_entry.insert(0, f"{celsius:.1f}")

# Convert Celsius to Fahrenheit
def celsius_to_fahrenheit():
    celsius = float(celsius_entry.get())
    fahrenheit = (celsius * 9 / 5) + 32

    fahrenheit_entry.delete(0, tk.END)
    fahrenheit_entry.insert(0, f"{fahrenheit:.1f}")

# Create window
window = tk.Tk()
window.title("Temperature Converter")

# Row 1 - Labels
tk.Label(window, text="Fahrenheit").grid(row=0, column=0, padx=10, pady=5)
tk.Label(window, text="Celsius").grid(row=0, column=1, padx=10, pady=5)

# Row 2 - Entry fields
fahrenheit_entry = tk.Entry(window, width=12)
fahrenheit_entry.grid(row=1, column=0, padx=10, pady=5)
fahrenheit_entry.insert(0, "32.0")

celsius_entry = tk.Entry(window, width=12)
celsius_entry.grid(row=1, column=1, padx=10, pady=5)
celsius_entry.insert(0, "0.0")

# Row 3 - Buttons
tk.Button(window, text=">>>>", command=fahrenheit_to_celsius).grid(row=2, column=0, pady=10)

tk.Button(window, text="<<<<", command=celsius_to_fahrenheit).grid(row=2, column=1, pady=10)

# Start the GUI
window.mainloop()
