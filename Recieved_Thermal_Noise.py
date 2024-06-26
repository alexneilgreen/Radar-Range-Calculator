# tab2
#TODO Finish Conversions
import numpy as np
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
import UnitConversion



########## Units ########## Units ########## Units ########## Units ############

# Define fonts, units, and variables
default_font = ('Arial', 10)
title_font = ('Arial', 16, 'bold')
units_P = ["dBW", "W", "mW"]
units_hz = ["GHz", "MHz", "kHz"]
units_t = ["k°", "C°", "f°"]

#!######## Units ########## Units ########## Units ########## Units ############
#/////////////////////////////////////////////////////////////////////////////
########## Init ########## Init ########## Init ########## Init ############

ts_f = 0.0
b_f = 0.0
pn_f = 0.0

#!######## Init ########## Init ########## Init ########## Init ############
#///////////////////////////////////////////////////////////////////////////
########## Calc ########## Calc ########## Calc ########## Calc ############

def validateInput(input):
    
    index = 0
    invalid_input = []

    special_characters = "[$&+,:;=?@#|'\"<>_^*()%!]"

    for child in input:

        if any(char.isalpha() for char in child):
            invalid_input.append(index)
            invalid_input.append("Alphabetic Character")

        elif any(char in child for char in special_characters):
            invalid_input.append(index)
            invalid_input.append("Special Character")

        elif child == "":
            invalid_input.append(index)
            invalid_input.append("Null input")

        index += 1
    
    if len(invalid_input)/2 > 1:

        index = 0

        print(f"Invalid input - {len(invalid_input)/2} fields")

        for child in invalid_input:

            if (index % 2) == 0 :
                print(f"\tInvalid Entry on row {child}")
            else :
                print(f"\t\tReason {child}")

            index += 1
        
        print("\n---------\n")
        
        return True
    
    elif len(invalid_input) == 0 :

        print(f"Invalid input - All fields are full")
        print(f"\tPlease clear one field to calculate")
        print("\n---------\n")

        return True
    
    else :

        return False

def graph():
    global ts_f, b_f, pn_f
    
    # Generate 50 points below pr_f and 50 points above pr_f using logarithmic scale
    points_below = np.logspace(np.log10(pn_f/100), np.log10(pn_f), num=50, endpoint=False)
    points_above = np.logspace(np.log10(pn_f), np.log10(pn_f*100), num=50, endpoint=True)
    
    # Combine both lists
    x_values = np.concatenate((points_below, points_above))
    
    # Generate corresponding y values based on recalculated r for each pr value
    y_values = []
    for pn in x_values:
        num = b_f * 1.38**-23
        den = pn
        ts = (num / den)
        y_values.append(ts)
    
    # Determine the maximum range value
    xmax_range = max(x_values) * 1.1
    ymax_range = max(y_values) * 1.1

    xmin_range = max(x_values) * -0.05
    ymin_range = max(y_values) * -0.05

    # Plotting
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values)#, marker='o', linestyle='-')
    plt.title('Received Thermal Noise of Radar Range Equation')
    plt.xlabel('Recieved Thermal Noise')
    plt.ylabel('Temperature')
    plt.xlim(xmin_range, xmax_range)
    plt.ylim(ymin_range, ymax_range)
    plt.grid(True, which="both", ls="--")
    plt.show()

    return

#?#?# Pₙ = K * Tₛ * B

def calculate_SNT(ts, b, b_unit, pn, pn_unit):
    
    # Check if input is valid for calculation
    input = []
    input.append(ts.get())
    input.append(b.get())
    input.append(pn.get())
    if validateInput(input) :
        return
    else : 
        pass



    # Global Variables
    global ts_f
    global b_f
    global pn_f



    if not pn.get():

        print("Solve for Pₙ\n")

        ts_f = float(ts.get())
        b_f = float(b.get())

        print("\tK * Tₛ * B = Pₙ\n")

        pn_f = round(ts_f * pow(1.38, -23) * b_f, 3)

        print(f"\tK * {ts_f} * {b_f} = {pn_f}\n")

        print(f"Pₙ = {pn_f}")

        print("\n---------\n")

        pn.delete(0, tk.END)
        pn.insert(0, pn_f)

    elif not ts.get():

        print("Solve for Tₛ\n")

        b_f = float(b.get())
        pn_f = float(pn.get())

        print("\t  Pₙ")
        print("\t------ = Tₛ")
        print("\tK * B\n")

        num = pn_f
        den = pow(1.38, -23) * b_f

        ts_f = round(num/den, 3)

        print(f"\t  {pn_f}")
        print(f"\t------ = {ts_f}")
        print(f"\tk * {b_f}\n")

        print(f"Tₛ = {ts_f}")

        print("\n---------\n")

        ts.delete(0, tk.END)
        ts.insert(0, ts_f)

    elif not b.get():

        print("Solve for B\n")

        ts_f = float(ts.get())
        pn_f = float(pn.get())

        print("\t  Pₙ")
        print("\t------ = B")
        print("\tK * Tₛ\n")

        num = pn_f
        den = pow(1.38, -23) * ts_f

        b_f = round(num/den, 3)

        print(f"\t  {pn_f}")
        print(f"\t------ = {b_f}")
        print(f"\tk * {ts_f}\n")

        print(f"B = {b_f}")

        print("\n---------\n")

        b.delete(0, tk.END)
        b.insert(0, b_f)

    else:
        print("Error")

    return

#?#?# Pₙ = K * Tₒ * F * B

def calculate_ST(f, b, b_unit, pn, pn_unit):
    
    # Check if input is valid for calculation
    input = []
    input.append(f.get())
    input.append(b.get())
    input.append(pn.get())
    if validateInput(input) :
        return
    else : 
        pass

    if not pn.get():

        print("Solve for Pₙ\n")

        f_f = float(f.get())
        b_f = float(b.get())

        print("\tK * Tₒ * F * B = Pₙ\n")

        pn_f = round(pow(1.38, -23) * 290 * f_f * b_f, 3)

        print(f"\tK * Tₒ * {f_f} * {b_f} = {pn_f}\n")

        print(f"Pₙ = {pn_f}")

        print("\n---------\n")

        pn.delete(0, tk.END)
        pn.insert(0, pn_f)

    elif not f.get():

        print("Solve for F\n")

        b_f = float(b.get())
        pn_f = float(pn.get())

        print("\t    Pₙ")
        print("\t---------- = F")
        print("\tK * Tₒ * B\n")

        num = pn_f
        den = pow(1.38, -23) * 290 * b_f

        f_f = round(num/den, 3)

        print(f"\t    {pn_f}")
        print(f"\t---------- = {f_f}")
        print(f"\tK * Tₒ * {b_f}\n")

        print(f"F = {f_f}")

        print("\n---------\n")

        f.delete(0, tk.END)
        f.insert(0, f_f)

    elif not b.get():

        print("Solve for B\n")

        f_f = float(f.get())
        pn_f = float(pn.get())

        print("\t    Pₙ")
        print("\t---------- = B")
        print("\tK * Tₒ * F\n")

        num = pn_f
        den = pow(1.38, -23) * 290 * f_f

        b_f = round(num/den, 3)

        print(f"\t    {pn_f}")
        print(f"\t---------- = {b_f}")
        print(f"\tK * Tₒ * {f_f}\n")

        print(f"B = {b_f}")

        print("\n---------\n")

        b.delete(0, tk.END)
        b.insert(0, b_f)

    else:
        print("Error")

    return

#!######## Calc ########## Calc ########## Calc ########## Calc ############
#/////////////////////////////////////////////////////////////////////////
########## GUI ########## GUI ########## GUI ########## GUI ############

def create_RTN_tab_content(tab2):
    
    tk.Label(tab2, text="Reciever Thermal Noise Form Radar Range Equation", font=title_font).grid(row=0, column=0, columnspan=4, sticky="w", padx=10, pady=15)

    tk.Label(tab2, text="K : Boltzman Constant", font=default_font).grid(row=1, column=0, sticky="w", padx=10, pady=10)
    tk.Label(tab2, text="1.38 x 10⁻²³", font=default_font).grid(row=1, column=1, sticky="w", padx=10, pady=10)
    tk.Label(tab2, text="Watt-sec/K", font=default_font).grid(row=1, column=2, sticky="w", padx=10, pady=10)

    tk.Label(tab2, text="B : Instant Reciever Bandwidth", font=default_font).grid(row=2, column=0, sticky="w", padx=10, pady=10)
    b_entry = tk.Entry(tab2)
    b_entry.grid(row=2, column=1, padx=10, pady=10)
    b_unit = tk.StringVar()
    b_unit_menu = ttk.Combobox(tab2, textvariable=b_unit, values=units_hz, font=default_font, state="readonly", width=6)
    b_unit_menu.grid(row=2, column=2, padx=10, pady=10)

    tk.Label(tab2, text="F : Noise Figure of Reciever", font=default_font).grid(row=3, column=0, sticky="w", padx=10, pady=10)
    f_entry = tk.Entry(tab2)
    f_entry.grid(row=3, column=1, padx=10, pady=10)

    tk.Label(tab2, text="Tₛ : System Noise Temperature", font=default_font).grid(row=4, column=0, sticky="w", padx=10, pady=10)
    ts_entry = tk.Entry(tab2)
    ts_entry.grid(row=4, column=1, padx=10, pady=10)
    tk.Label(tab2, text="k°", font=default_font).grid(row=4, column=2, sticky="w", padx=10, pady=10)

    tk.Label(tab2, text="Tₒ : Standard Temperature", font=default_font).grid(row=5, column=0, sticky="w", padx=10, pady=10)
    tk.Label(tab2, text="290", font=default_font).grid(row=5, column=1, sticky="w", padx=10, pady=10)
    tk.Label(tab2, text="k°", font=default_font).grid(row=5, column=2, sticky="w", padx=10, pady=10)

    tk.Label(tab2, text=f"Pₙ : Thermal Noise Power", font=default_font).grid(row=6, column=0, sticky="w", padx=10, pady=10)
    pn_entry = tk.Entry(tab2)
    pn_entry.grid(row=6, column=1, padx=10, pady=10)
    pn_unit = tk.StringVar()
    pn_unit_menu = ttk.Combobox(tab2, textvariable=pn_unit, values=units_P, font=default_font, state="readonly", width=6)
    pn_unit_menu.grid(row=6, column=2, padx=10, pady=10)

    # Calc button System Noise Temperature
    ts_btn_plot = tk.Button(tab2, text="Calc SNT", command=lambda: calculate_SNT(ts_entry, b_entry, b_unit.get(), pn_entry, pn_unit.get()), font=default_font, width=7, bg='darkgray')
    ts_btn_plot.grid(row=4, column=3, padx=10, pady=10)

    # Calc button Standard Temperature
    to_btn_plot = tk.Button(tab2, text="Calc ST", command=lambda: calculate_ST(f_entry, b_entry, b_unit.get(), pn_entry, pn_unit.get()), font=default_font, width=7, bg='darkgray')
    to_btn_plot.grid(row=5, column=3, padx=10, pady=10)

    # Plot button
    to_btn_plot = tk.Button(tab2, text="Plot", command=lambda: graph(), font=default_font, width=7, bg='darkgray')
    to_btn_plot.grid(row=6, column=3, padx=10, pady=10)

    # Insert image
    img = Image.open("Equations\RTN.png")
    img = ImageTk.PhotoImage(img)
    label_img = tk.Label(tab2, image=img)
    label_img.image = img
    label_img.grid(row=1, column=4, columnspan=2, rowspan=6, padx=10, pady=10)
    
#!######## GUI ########## GUI ########## GUI ########## GUI ############