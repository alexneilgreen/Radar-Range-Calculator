# tab2

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk



########## Units ########## Units ########## Units ########## Units ############

# Define fonts, units, and variables
default_font = ('Arial', 10)
title_font = ('Arial', 16, 'bold')
units_P = ["dBW", "W", "mW"]
units_hz = ["GHz", "MHz", "kHz"]
units_t = ["k°", "C°", "f°"]

#!######## Units ########## Units ########## Units ########## Units ############
#/////////////////////////////////////////////////////////////////////////////
########## Calc ########## Calc ########## Calc ########## Calc ############

#?#?# Pₙ = K * Tₛ * B

def calculate_SNT():
    # Placeholder function for plot button
    pass

#?#?# Pₙ = K * Tₒ * F * B

def calculate_ST():
    # Placeholder function for plot button
    pass

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
    rcs_entry = tk.Entry(tab2)
    rcs_entry.grid(row=4, column=1, padx=10, pady=10)
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

    # Plot button System Noise Temperature
    ts_btn_plot = tk.Button(tab2, text="Calc SNT", command=calculate_SNT, font=default_font, width=7, bg='darkgray')
    ts_btn_plot.grid(row=4, column=3, padx=10, pady=10)

    # Plot button Standard Temperature
    to_btn_plot = tk.Button(tab2, text="Calc ST", command=calculate_ST, font=default_font, width=7, bg='darkgray')
    to_btn_plot.grid(row=5, column=3, padx=10, pady=10)

    # Insert image
    img = Image.open("Equations\RTN.png")
    img = ImageTk.PhotoImage(img)
    label_img = tk.Label(tab2, image=img)
    label_img.image = img
    label_img.grid(row=1, column=4, columnspan=2, rowspan=6, padx=10, pady=10)
    
#!######## GUI ########## GUI ########## GUI ########## GUI ############