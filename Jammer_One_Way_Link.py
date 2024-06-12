# tab5

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
units_f = ["GHz", "MHz", "kHz"]
units_rcs = ["m²", "cm²", "mm²"]
units_R = ["NMI", "KM", "M"]

#!######## Units ########## Units ########## Units ########## Units ############
#/////////////////////////////////////////////////////////////////////////////
########## Calc ########## Calc ########## Calc ########## Calc ############

#?#?#             Pⱼ * Gⱼ * Gᵣⱼ * λ²
#?#?# Pᵣⱼ = -----------------------------
#?#?#        (4π)³ * Rⱼᵣ² * Lₜⱼ * Lₐ * Lᵣ

def calculate():
    # Placeholder function for plot button
    pass

#!######## Calc ########## Calc ########## Calc ########## Calc ############
#/////////////////////////////////////////////////////////////////////////
########## GUI ########## GUI ########## GUI ########## GUI ############

def create_JOWL_tab_content(tab5):
    
    tk.Label(tab5, text="Jammer One Way Link Form Radar Range Equation", font=title_font).grid(row=0, column=0, columnspan=4, sticky="w", padx=10, pady=15)

    tk.Label(tab5, text="Pⱼ : Jammer Transmitted Power", font=default_font).grid(row=1, column=0, sticky="w", padx=10, pady=10)
    pj_entry = tk.Entry(tab5)
    pj_entry.grid(row=1, column=1, padx=10, pady=10)
    pj_unit = tk.StringVar()
    pj_unit_menu = ttk.Combobox(tab5, textvariable=pj_unit, values=units_P, font=default_font, state="readonly", width=6)
    pj_unit_menu.grid(row=1, column=2, padx=10, pady=10)

    tk.Label(tab5, text="Gⱼ : Jammer Antenna Gain", font=default_font).grid(row=2, column=0, sticky="w", padx=10, pady=10)
    gt_entry = tk.Entry(tab5)
    gt_entry.grid(row=2, column=1, padx=10, pady=10)
    tk.Label(tab5, text="dB", font=default_font).grid(row=2, column=2, sticky="w", padx=10, pady=10)

    tk.Label(tab5, text="Gᵣⱼ : Radar Antenna Facing Jammer Gain", font=default_font).grid(row=3, column=0, sticky="w", padx=10, pady=10)
    gr_entry = tk.Entry(tab5)
    gr_entry.grid(row=3, column=1, padx=10, pady=10)
    tk.Label(tab5, text="dB", font=default_font).grid(row=3, column=2, sticky="w", padx=10, pady=10)

    # tk.Label(tab1, text="λ : Wavelength", font=default_font).grid(row=4, column=0, sticky="w", padx=10, pady=10)
    # w_entry = tk.Entry(tab1)
    # w_entry.grid(row=4, column=1, padx=10, pady=10)
    # w_unit = tk.StringVar()
    # w_unit_menu = ttk.Combobox(tab1, textvariable=w_unit, values=units_hz, font=default_font, state="readonly", width=6)
    # w_unit_menu.grid(row=4, column=2, padx=10, pady=10)

    tk.Label(tab5, text="ƒ : frequency", font=default_font).grid(row=4, column=0, sticky="w", padx=10, pady=10)
    f_entry = tk.Entry(tab5)
    f_entry.grid(row=4, column=1, padx=10, pady=10)
    f_unit = tk.StringVar()
    f_unit_menu = ttk.Combobox(tab5, textvariable=f_unit, values=units_f, font=default_font, state="readonly", width=6)
    f_unit_menu.grid(row=4, column=2, padx=10, pady=10)

    tk.Label(tab5, text="Rⱼᵣ : Jammer to Radar Range", font=default_font).grid(row=5, column=0, sticky="w", padx=10, pady=10)
    rjr_entry = tk.Entry(tab5)
    rjr_entry.grid(row=5, column=1, padx=10, pady=10)
    rjr_unit = tk.StringVar()
    rjr_unit_menu = ttk.Combobox(tab5, textvariable=rjr_unit, values=units_R, font=default_font, state="readonly", width=6)
    rjr_unit_menu.grid(row=5, column=2, padx=10, pady=10)

    tk.Label(tab5, text="Lₜⱼ : Transmit Jammer Loss", font=default_font).grid(row=6, column=0, sticky="w", padx=10, pady=10)
    ltj_entry = tk.Entry(tab5)
    ltj_entry.grid(row=6, column=1, padx=10, pady=10)

    tk.Label(tab5, text="Lₐ : Atmospheric Loss", font=default_font).grid(row=7, column=0, sticky="w", padx=10, pady=10)
    la_entry = tk.Entry(tab5)
    la_entry.grid(row=7, column=1, padx=10, pady=10)

    tk.Label(tab5, text="Lᵣ : Reciever Loss", font=default_font).grid(row=8, column=0, sticky="w", padx=10, pady=10)
    lr_entry = tk.Entry(tab5)
    lr_entry.grid(row=8, column=1, padx=10, pady=10)

    tk.Label(tab5, text=f"Pᵣⱼ : Power at Radar from Jammer", font=default_font).grid(row=9, column=0, sticky="w", padx=10, pady=10)
    prj_entry = tk.Entry(tab5)
    prj_entry.grid(row=9, column=1, padx=10, pady=10)
    prj_unit = tk.StringVar()
    prj_unit_menu = ttk.Combobox(tab5, textvariable=prj_unit, values=units_P, font=default_font, state="readonly", width=6)
    prj_unit_menu.grid(row=9, column=2, padx=10, pady=10)

    # Plot button
    btn_plot = tk.Button(tab5, text="Calc", command=calculate, font=default_font, width=7, bg='darkgray')
    btn_plot.grid(row=9, column=3, padx=10, pady=10)

    # Insert image
    img = Image.open("Equations\JOWL.png")
    img = ImageTk.PhotoImage(img)
    label_img = tk.Label(tab5, image=img)
    label_img.image = img
    label_img.grid(row=1, column=4, columnspan=2, rowspan=7, padx=10, pady=10)

#!######## GUI ########## GUI ########## GUI ########## GUI ############