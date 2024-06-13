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

#?#?#             Pⱼ * Gⱼ * Gᵣⱼ * λ²
#?#?# Pᵣⱼ = -----------------------------
#?#?#        (4π)³ * Rⱼᵣ² * Lₜⱼ * Lₐ * Lᵣ

def calculate(pj, gj, grj, f, rjr, ltj, la, lr, prj, pj_unit, rjr_unit, prj_unit):
    
    

    # Check if input is valid for calculation
    input = []
    input.append(pj)
    input.append(gj)
    input.append(grj)
    input.append(f)
    input.append(rjr)
    input.append(ltj)
    input.append(la)
    input.append(lr)
    input.append(prj)
    if validateInput(input) :
        return
    else : 
        pass



    # Calculations Start
    if not prj:

        print("Solve for Pᵣⱼ\n")

        pj = float(pj)
        gj = float(gj)
        grj = float(grj)
        f = float(f)
        rjr = float(rjr)
        ltj = float(ltj)
        la = float(la)
        lr = float(lr)

        print("\t     Pⱼ * Gⱼ * Gᵣⱼ * λ²")
        print("\t----------------------------- = Pᵣⱼ")
        print("\t(4π)³ * Rⱼᵣ² * Lₜⱼ * Lₐ * Lᵣ\n")

        w = (3 * pow(10, 8))/f

        num = pj * gj * grj * pow(w, 2)
        den = pow((4 * 3.14159265), 3) * pow(rjr, 2) * ltj * la * lr

        prj = round(num/den, 3)

        print(f"\t   {pj} * {gj} * {grj} * (C/{f})²")
        print(f"\t------------------------------------- = {prj}")
        print(f"\t (4π)³ * {rjr}² * {ltj} * {la} * {lr}\n")

        print(f"Pᵣⱼ = {prj}")

        print("\n---------\n")

    elif not pj:

        print("Solve for Pⱼ\n")

        gj = float(gj)
        grj = float(grj)
        f = float(f)
        rjr = float(rjr)
        ltj = float(ltj)
        la = float(la)
        lr = float(lr)
        prj = float(prj)

        print("\tPᵣⱼ * (4π)³ * Rⱼᵣ² * Lₜⱼ * Lₐ * Lᵣ")
        print("\t---------------------------------- = Pⱼ")
        print("\t        Gⱼ * Gᵣⱼ * λ²\n")

        w = (3 * pow(10, 8))/f

        num = prj * pow((4 * 3.14159265), 3) * pow(rjr, 2) * ltj * la * lr
        den = gj * grj * pow(w, 2)

        pj = round(num/den, 3)

        print(f"\t {prj} * (4π)³ * {rjr}² * {ltj} * {la} * {lr}")
        print(f"\t--------------------------------------------- = {pj}")
        print(f"\t        {gj} * {grj} * (C/{f})²\n")

        print(f"Pⱼ = {pj}")

        print("\n---------\n")
    
    elif not gj:

        print("Solve for Gⱼ\n")

        pj = float(pj)
        grj = float(grj)
        f = float(f)
        rjr = float(rjr)
        ltj = float(ltj)
        la = float(la)
        lr = float(lr)
        prj = float(prj)

        print("\tPᵣⱼ * (4π)³ * Rⱼᵣ² * Lₜⱼ * Lₐ * Lᵣ")
        print("\t---------------------------------- = Gⱼ")
        print("\t        Pⱼ * Gᵣⱼ * λ²\n")

        w = (3 * pow(10, 8))/f

        num = prj * pow((4 * 3.14159265), 3) * pow(rjr, 2) * ltj * la * lr
        den = pj * grj * pow(w, 2)

        gj = round(num/den, 3)

        print(f"\t {prj} * (4π)³ * {rjr}² * {ltj} * {la} * {lr}")
        print(f"\t--------------------------------------------- = {gj}")
        print(f"\t        {pj} * {grj} * (C/{f})²\n")

        print(f"Gⱼ = {gj}")

        print("\n---------\n")
    
    elif not grj:

        print("Solve for Gᵣⱼ\n")

        pj = float(pj)
        gj = float(gj)
        f = float(f)
        rjr = float(rjr)
        ltj = float(ltj)
        la = float(la)
        lr = float(lr)
        prj = float(prj)

        print("\tPᵣⱼ * (4π)³ * Rⱼᵣ² * Lₜⱼ * Lₐ * Lᵣ")
        print("\t---------------------------------- = Gᵣⱼ")
        print("\t        Pⱼ * Gⱼ * λ²\n")

        w = (3 * pow(10, 8))/f

        num = prj * pow((4 * 3.14159265), 3) * pow(rjr, 2) * ltj * la * lr
        den = pj * gj * pow(w, 2)

        grj = round(num/den, 3)

        print(f"\t {prj} * (4π)³ * {rjr}² * {ltj} * {la} * {lr}")
        print(f"\t--------------------------------------------- = {grj}")
        print(f"\t        {pj} * {gj} * (C/{f})²\n")

        print(f"Gᵣⱼ = {grj}")

        print("\n---------\n")
    
    elif not f:

        print("Solve for λ and ƒ\n")

        pj = float(pj)
        gj = float(gj)
        grj = float(grj)
        rjr = float(rjr)
        ltj = float(ltj)
        la = float(la)
        lr = float(lr)
        prj = float(prj)

        print("\tPᵣⱼ * (4π)³ * Rⱼᵣ² * Lₜⱼ * Lₐ * Lᵣ")
        print("\t---------------------------------- = λ²")
        print("\t        Pⱼ * Gⱼ * Gᵣⱼ\n")

        num = prj * pow((4 * 3.14159265), 3) * pow(rjr, 2) * ltj * la * lr
        den = pj * gj * grj

        w = round(pow(num/den, 0.5), 3)

        f = round((3 * pow(10, 8))/w, 3)

        print(f"\t {prj} * (4π)³ * {rjr}² * {ltj} * {la} * {lr}")
        print(f"\t--------------------------------------------- = {w}²")
        print(f"\t        {pj} * {gj} * {grj}\n")

        print(f"λ = {w}")
        print(f"ƒ = {f}")

        print("\n---------\n")
    
    elif not rjr:

        print("Solve for Rⱼᵣ\n")

        pj = float(pj)
        gj = float(gj)
        grj = float(grj)
        f = float(f)
        ltj = float(ltj)
        la = float(la)
        lr = float(lr)
        prj = float(prj)

        print("\t     Pⱼ * Gⱼ * Gᵣⱼ * λ²")
        print("\t----------------------------- = Rⱼᵣ²")
        print("\tPᵣⱼ * (4π)³ * Lₜⱼ * Lₐ * Lᵣ\n")

        w = (3 * pow(10, 8))/f

        num = pj * gj * grj * pow(w, 2)
        den = prj * pow((4 * 3.14159265), 3) * ltj * la * lr

        rjr = round(pow(num/den, 0.5), 3)

        print(f"\t   {pj} * {gj} * {grj} * (C/{f})²")
        print(f"\t------------------------------------- = {rjr}²")
        print(f"\t {prj} * (4π)³ * {ltj} * {la} * {lr}\n")

        print(f"Rⱼᵣ = {rjr}")

        print("\n---------\n")
    
    elif not ltj:

        print("Solve for Lₜⱼ\n")

        pj = float(pj)
        gj = float(gj)
        grj = float(grj)
        f = float(f)
        rjr = float(rjr)
        la = float(la)
        lr = float(lr)
        prj = float(prj)

        print("\t     Pⱼ * Gⱼ * Gᵣⱼ * λ²")
        print("\t----------------------------- = Lₜⱼ")
        print("\tPᵣⱼ * (4π)³ * Rⱼᵣ² * Lₐ * Lᵣ\n")

        w = (3 * pow(10, 8))/f

        num = pj * gj * grj * pow(w, 2)
        den = prj * pow((4 * 3.14159265), 3) * pow(rjr, 2) * la * lr

        ltj = round(num/den, 3)

        print(f"\t   {pj} * {gj} * {grj} * (C/{f})²")
        print(f"\t------------------------------------- = {ltj}")
        print(f"\t {prj} * (4π)³ * {rjr}² * {la} * {lr}\n")

        print(f"Lₜⱼ = {ltj}")

        print("\n---------\n")
    
    elif not la:

        print("Solve for Lₐ\n")

        pj = float(pj)
        gj = float(gj)
        grj = float(grj)
        f = float(f)
        rjr = float(rjr)
        ltj = float(ltj)
        lr = float(lr)
        prj = float(prj)

        print("\t     Pⱼ * Gⱼ * Gᵣⱼ * λ²")
        print("\t----------------------------- = Lₐ")
        print("\tPᵣⱼ * (4π)³ * Rⱼᵣ² * Lₜⱼ * Lᵣ\n")

        w = (3 * pow(10, 8))/f

        num = pj * gj * grj * pow(w, 2)
        den = prj * pow((4 * 3.14159265), 3) * pow(rjr, 2) * ltj * lr

        la = num/den

        print(f"\t   {pj} * {gj} * {grj} * (C/{f})²")
        print(f"\t------------------------------------- = {la}")
        print(f"\t {prj} * (4π)³ * {rjr}² * {ltj} * {lr}\n")

        print(f"Lₐ = {la}")

        print("\n---------\n")
    
    elif not lr:

        print("Solve for lr\n")

        pj = float(pj)
        gj = float(gj)
        grj = float(grj)
        f = float(f)
        rjr = float(rjr)
        ltj = float(ltj)
        la = float(la)
        prj = float(prj)

        print("\t     Pⱼ * Gⱼ * Gᵣⱼ * λ²")
        print("\t------------------------------ = Lᵣ")
        print("\tPᵣⱼ * (4π)³ * Rⱼᵣ² * Lₜⱼ * Lₐ\n")

        w = (3 * pow(10, 8))/f

        num = pj * gj * grj * pow(w, 2)
        den = prj * pow((4 * 3.14159265), 3) * pow(rjr, 2) * ltj * la

        lr = round(num/den, 3)

        print(f"\t   {pj} * {gj} * {grj} * (C/{f})²")
        print(f"\t------------------------------------- = {lr}")
        print(f"\t {prj} * (4π)³ * {rjr}² * {ltj} * {la}\n")

        print(f"Lᵣ = {lr}")

        print("\n---------\n")

    else :
        print("Error")
    
    return

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
    gj_entry = tk.Entry(tab5)
    gj_entry.grid(row=2, column=1, padx=10, pady=10)
    tk.Label(tab5, text="dB", font=default_font).grid(row=2, column=2, sticky="w", padx=10, pady=10)

    tk.Label(tab5, text="Gᵣⱼ : Radar Antenna Facing Jammer Gain", font=default_font).grid(row=3, column=0, sticky="w", padx=10, pady=10)
    grj_entry = tk.Entry(tab5)
    grj_entry.grid(row=3, column=1, padx=10, pady=10)
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
    btn_plot = tk.Button(tab5, text="Calc", command=lambda: calculate(pj_entry.get(), gj_entry.get(), grj_entry.get(), f_entry.get(), rjr_entry.get(), 
                                                                      ltj_entry.get(), la_entry.get(), lr_entry.get(), prj_entry.get(), pj_unit.get(),
                                                                      rjr_unit.get(), prj_unit.get()), font=default_font, width=7, bg='darkgray')
    btn_plot.grid(row=9, column=3, padx=10, pady=10)

    # Insert image
    img = Image.open("Equations\JOWL.png")
    img = ImageTk.PhotoImage(img)
    label_img = tk.Label(tab5, image=img)
    label_img.image = img
    label_img.grid(row=1, column=4, columnspan=2, rowspan=7, padx=10, pady=10)

#!######## GUI ########## GUI ########## GUI ########## GUI ############