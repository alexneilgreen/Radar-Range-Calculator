# tab4

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
units_T = ["hr", "m", "s", "ms"]
units_f = ["GHz", "MHz", "kHz"]
units_rcs = ["m²", "cm²", "mm²"]
units_R = ["NMI", "KM", "M"]

#!######## Units ########## Units ########## Units ########## Units ############
#/////////////////////////////////////////////////////////////////////////////
########## Calc ########## Calc ########## Calc ########## Calc ############

#?#?#       Pₐᵥ₉ * Td * Gₜ * Gᵣ * λ² * σ
#?#?# Pᵣ = -----------------------------
#?#?#         (4π)³ * R⁴ * Pₙ * Lₛ

def calculate():
    # Placeholder function for plot button
    pass

########## Calc ########## Calc ########## Calc ########## Calc ############
#/////////////////////////////////////////////////////////////////////////
#!######## GUI ########## GUI ########## GUI ########## GUI ############

def create_AP_tab_content(tab4):
    
    tk.Label(tab4, text="Average Power Form Radar Range Equation", font=title_font).grid(row=0, column=0, columnspan=4, sticky="w", padx=10, pady=15)

    tk.Label(tab4, text="Pₐᵥ₉ : Average Power", font=default_font).grid(row=1, column=0, sticky="w", padx=10, pady=10)
    pavg_entry = tk.Entry(tab4)
    pavg_entry.grid(row=1, column=1, padx=10, pady=10)
    pavg_unit = tk.StringVar()
    pavg_unit_menu = ttk.Combobox(tab4, textvariable=pavg_unit, values=units_P, font=default_font, state="readonly", width=6)
    pavg_unit_menu.grid(row=1, column=2, padx=10, pady=10)

    tk.Label(tab4, text="Td : Time Dwell", font=default_font).grid(row=2, column=0, sticky="w", padx=10, pady=10)
    td_entry = tk.Entry(tab4)
    td_entry.grid(row=2, column=1, padx=10, pady=10)
    td_unit = tk.StringVar()
    td_unit_menu = ttk.Combobox(tab4, textvariable=td_unit, values=units_T, font=default_font, state="readonly", width=6)
    td_unit_menu.grid(row=2, column=2, padx=10, pady=10)

    tk.Label(tab4, text="Gₜ : Gain Transmitted", font=default_font).grid(row=3, column=0, sticky="w", padx=10, pady=10)
    gt_entry = tk.Entry(tab4)
    gt_entry.grid(row=3, column=1, padx=10, pady=10)
    tk.Label(tab4, text="dB", font=default_font).grid(row=3, column=2, sticky="w", padx=10, pady=10)

    tk.Label(tab4, text="Gᵣ : Gain Received", font=default_font).grid(row=4, column=0, sticky="w", padx=10, pady=10)
    gr_entry = tk.Entry(tab4)
    gr_entry.grid(row=4, column=1, padx=10, pady=10)
    tk.Label(tab4, text="dB", font=default_font).grid(row=4, column=2, sticky="w", padx=10, pady=10)

    # tk.Label(tab1, text="λ : Wavelength", font=default_font).grid(row=4, column=0, sticky="w", padx=10, pady=10)
    # w_entry = tk.Entry(tab1)
    # w_entry.grid(row=4, column=1, padx=10, pady=10)
    # w_unit = tk.StringVar()
    # w_unit_menu = ttk.Combobox(tab1, textvariable=w_unit, values=units_hz, font=default_font, state="readonly", width=6)
    # w_unit_menu.grid(row=4, column=2, padx=10, pady=10)

    tk.Label(tab4, text="ƒ : frequency", font=default_font).grid(row=5, column=0, sticky="w", padx=10, pady=10)
    f_entry = tk.Entry(tab4)
    f_entry.grid(row=5, column=1, padx=10, pady=10)
    f_unit = tk.StringVar()
    f_unit_menu = ttk.Combobox(tab4, textvariable=f_unit, values=units_f, font=default_font, state="readonly", width=6)
    f_unit_menu.grid(row=5, column=2, padx=10, pady=10)

    tk.Label(tab4, text="\u03C3 : Radar Cross Section", font=default_font).grid(row=6, column=0, sticky="w", padx=10, pady=10)
    rcs_entry = tk.Entry(tab4)
    rcs_entry.grid(row=6, column=1, padx=10, pady=10)
    rcs_unit = tk.StringVar()
    rcs_unit_menu = ttk.Combobox(tab4, textvariable=rcs_unit, values=units_rcs, font=default_font, state="readonly", width=6)
    rcs_unit_menu.grid(row=6, column=2, padx=10, pady=10)

    tk.Label(tab4, text="R : Range", font=default_font).grid(row=7, column=0, sticky="w", padx=10, pady=10)
    r_entry = tk.Entry(tab4)
    r_entry.grid(row=7, column=1, padx=10, pady=10)
    r_unit = tk.StringVar()
    r_unit_menu = ttk.Combobox(tab4, textvariable=r_unit, values=units_R, font=default_font, state="readonly", width=6)
    r_unit_menu.grid(row=7, column=2, padx=10, pady=10)

    tk.Label(tab4, text="Pₙ : Thermal Noise Power", font=default_font).grid(row=8, column=0, sticky="w", padx=10, pady=10)
    pn_entry = tk.Entry(tab4)
    pn_entry.grid(row=8, column=1, padx=10, pady=10)
    pn_unit = tk.StringVar()
    pn_unit_menu = ttk.Combobox(tab4, textvariable=pn_unit, values=units_P, font=default_font, state="readonly", width=6)
    pn_unit_menu.grid(row=8, column=2, padx=10, pady=10)

    tk.Label(tab4, text="Lₛ : System Loss", font=default_font).grid(row=9, column=0, sticky="w", padx=10, pady=10)
    ls_entry = tk.Entry(tab4)
    ls_entry.grid(row=9, column=1, padx=10, pady=10)

    tk.Label(tab4, text=f"SNR : Signal-to-Noise Ratio", font=default_font).grid(row=10, column=0, sticky="w", padx=10, pady=10)
    snr_entry = tk.Entry(tab4)
    snr_entry.grid(row=10, column=1, padx=10, pady=10)

    # Plot button
    btn_plot = tk.Button(tab4, text="Calc", command=calculate, font=default_font, width=7, bg='darkgray')
    btn_plot.grid(row=10, column=3, padx=10, pady=10)

    # Insert image
    img = Image.open("Equations\APF.png")
    img = ImageTk.PhotoImage(img)
    label_img = tk.Label(tab4, image=img)
    label_img.image = img
    label_img.grid(row=1, column=4, columnspan=2, rowspan=10, padx=10, pady=10)

#!######## GUI ########## GUI ########## GUI ########## GUI ############