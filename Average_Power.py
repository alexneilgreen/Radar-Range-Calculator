# tab4
#TODO Finish Conversions
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
units_T = ["hr", "m", "s", "ms"]
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

#?#?#        Pₐᵥ₉ * Td * Gₜ * Gᵣ * λ² * σ
#?#?# SNR = -----------------------------
#?#?#          (4π)³ * R⁴ * Pₙ * Lₛ

def calculate(pavg, td, gt, gr, f, rcs, r, pn, ls, snr, pavg_unit, td_unit, f_unit, rcs_unit, r_unit, pn_unit):



    # Check if input is valid for calculation
    input = []
    input.append(pavg.get())
    input.append(td.get())
    input.append(gt.get())
    input.append(gr.get())
    input.append(f.get())
    input.append(rcs.get())
    input.append(r.get())
    input.append(pn.get())
    input.append(ls.get())
    input.append(snr.get())
    if validateInput(input) :
        return
    else : 
        pass



    # Calculations Start
    if not snr.get():

        print("Solve for SNR\n")

        pavg = float(pavg.get())
        td = float(td.get())
        gt = float(gt.get())
        gr = float(gr.get())
        f = float(f.get())
        rcs = float(rcs.get())
        r = float(r.get())
        pn = float(pn.get())
        ls = float(ls.get())

        print("\t Pₐᵥ₉ * Td * Gₜ * Gᵣ * λ² * σ")
        print("\t------------------------------ = SNR")
        print("\t   (4π)³ * R⁴ * Pₙ * Lₛ\n")

        w = (3 * pow(10, 8))/f

        num = pavg * td * gt * gr * pow(w, 2) * rcs
        den = pow((4 * 3.14159265), 3) * pow(r, 4) * pn * ls

        snr_f = round(num/den, 3)

        print(f"\t {pavg} * {td} * {gt} * {gr} * (C/{f})² * {rcs}")
        print(f"\t----------------------------------------------- = {snr_f}")
        print(f"\t   (4π)³ * {r}⁴ * {pn} * {ls}\n")

        print(f"SNR = {snr_f}")

        print("\n---------\n")

        snr.delete(0, tk.END)
        snr.insert(0, snr_f)

    elif not pavg.get():
        
        print("Solve for Pₐᵥ₉\n")

        td = float(td.get())
        gt = float(gt.get())
        gr = float(gr.get())
        f = float(f.get())
        rcs = float(rcs.get())
        r = float(r.get())
        pn = float(pn.get())
        ls = float(ls.get())
        snr = float(snr.get())

        print("\t SNR * (4π)³ * R⁴ * Pₙ * Lₛ")
        print("\t---------------------------- = Pₐᵥ₉")
        print("\t   Td * Gₜ * Gᵣ * λ² * σ\n")

        w = (3 * pow(10, 8))/f

        num =  snr * pow((4 * 3.14159265), 3) * pow(r, 4) * pn * ls
        den = td * gt * gr * pow(w, 2) * rcs

        pavg_f = round(num/den, 3)

        print(f"\t {snr} * (4π)³ * {r}⁴ * {pn} * {ls}")
        print(f"\t-------------------------------------  = {pavg_f}")
        print(f"\t {td} * {gt} * {gr} * {w}² * {rcs}\n")

        print(f"Pₐᵥ₉ = {pavg_f}")

        print("\n---------\n")

        pavg.delete(0, tk.END)
        pavg.insert(0, pavg)

    elif not td.get():

        print("Solve for Td\n")

        pavg = float(pavg.get())
        gt = float(gt.get())
        gr = float(gr.get())
        f = float(f.get())
        rcs = float(rcs.get())
        r = float(r.get())
        pn = float(pn.get())
        ls = float(ls.get())
        snr = float(snr.get())

        print("\t SNR * (4π)³ * R⁴ * Pₙ * Lₛ")
        print("\t---------------------------- = Td")
        print("\t  Pₐᵥ₉ * Gₜ * Gᵣ * λ² * σ\n")

        w = (3 * pow(10, 8))/f

        num =  snr * pow((4 * 3.14159265), 3) * pow(r, 4) * pn * ls
        den = pavg * gt * gr * pow(w, 2) * rcs

        td_f = round(num/den, 3)

        print(f"\t {snr} * (4π)³ * {r}⁴ * {pn} * {ls}")
        print(f"\t-------------------------------------  = {td_f}")
        print(f"\t {pavg} * {gt} * {gr} * {w}² * {rcs}\n")

        print(f"Td = {td_f}")

        print("\n---------\n")

        td.delete(0, tk.END)
        td.insert(0, td_f)

    elif not gt.get():

        print("Solve for Gₜ\n")

        pavg = float(pavg.get())
        td = float(td.get())
        gr = float(gr.get())
        f = float(f.get())
        rcs = float(rcs.get())
        r = float(r.get())
        pn = float(pn.get())
        ls = float(ls.get())
        snr = float(snr.get())

        print("\t SNR * (4π)³ * R⁴ * Pₙ * Lₛ")
        print("\t---------------------------- = Gₜ")
        print("\t  Pₐᵥ₉ * Td * Gᵣ * λ² * σ\n")

        w = (3 * pow(10, 8))/f

        num =  snr * pow((4 * 3.14159265), 3) * pow(r, 4) * pn * ls
        den = pavg * td * gr * pow(w, 2) * rcs

        gt_f = round(num/den, 3)

        print(f"\t {snr} * (4π)³ * {r}⁴ * {pn} * {ls}")
        print(f"\t-------------------------------------  = {gt_f}")
        print(f"\t {pavg} * {td} * {gr} * {w}² * {rcs}\n")

        print(f"Gₜ = {gt_f}")

        print("\n---------\n")

        gt.delete(0, tk.END)
        gt.insert(0, gt_f)

    elif not gr.get():

        print("Solve for Gᵣ\n")

        pavg = float(pavg.get())
        td = float(td.get())
        gt = float(gt.get())
        f = float(f.get())
        rcs = float(rcs.get())
        r = float(r.get())
        pn = float(pn.get())
        ls = float(ls.get())
        snr = float(snr.get())

        print("\t SNR * (4π)³ * R⁴ * Pₙ * Lₛ")
        print("\t---------------------------- = Gᵣ")
        print("\t  Pₐᵥ₉ * Td * Gₜ * λ² * σ\n")

        w = (3 * pow(10, 8))/f

        num =  snr * pow((4 * 3.14159265), 3) * pow(r, 4) * pn * ls
        den = pavg * td * gt * pow(w, 2) * rcs

        gr_f = round(num/den, 3)

        print(f"\t {snr} * (4π)³ * {r}⁴ * {pn} * {ls}")
        print(f"\t-------------------------------------  = {gr_f}")
        print(f"\t {pavg} * {td} * {gt} * {w}² * {rcs}\n")

        print(f"Gᵣ = {gr_f}")

        print("\n---------\n")

        gr.delete(0, tk.END)
        gr.insert(0, gr_f)

    elif not f.get():

        print("Solve for λ and ƒ\n")

        pavg = float(pavg.get())
        td = float(td.get())
        gt = float(gt.get())
        gr = float(gr.get())
        rcs = float(rcs.get())
        r = float(r.get())
        pn = float(pn.get())
        ls = float(ls.get())
        snr = float(snr.get())

        print("\t SNR * (4π)³ * R⁴ * Pₙ * Lₛ")
        print("\t---------------------------- = λ²")
        print("\t  Pₐᵥ₉ * Td * Gₜ * Gᵣ * σ\n")

        num =  snr * pow((4 * 3.14159265), 3) * pow(r, 4) * pn * ls
        den = pavg * td * gt * gr * rcs

        w = round(pow(num/den, 0.5), 3)

        f_f = round((3 * pow(10, 8))/w, 3)

        print(f"\t {snr} * (4π)³ * {r}⁴ * {pn} * {ls}")
        print(f"\t-------------------------------------  = {w}²")
        print(f"\t {pavg} * {td} * {gt} * {gr} * {rcs}\n")

        print(f"λ = {w}")
        print(f"ƒ = {f_f}")

        print("\n---------\n")

        f.delete(0, tk.END)
        f.insert(0, f_f)

    elif not rcs.get():

        print("Solve for σ\n")

        pavg = float(pavg.get())
        td = float(td.get())
        gt = float(gt.get())
        gr = float(gr.get())
        f = float(f.get())
        r = float(r.get())
        pn = float(pn.get())
        ls = float(ls.get())
        snr = float(snr.get())

        print("\t SNR * (4π)³ * R⁴ * Pₙ * Lₛ")
        print("\t---------------------------- = σ")
        print("\t  Pₐᵥ₉ * Td * Gₜ * Gᵣ * λ²\n")

        w = (3 * pow(10, 8))/f

        num =  snr * pow((4 * 3.14159265), 3) * pow(r, 4) * pn * ls
        den = pavg * td * gt * gr * pow(w, 2)

        rcs_f = round(num/den, 3)

        print(f"\t {snr} * (4π)³ * {r}⁴ * {pn} * {ls}")
        print(f"\t-----------------------------------  = {rcs_f}")
        print(f"\t {pavg} * {td} * {gt} * {gr} * {w}²\n")

        print(f"σ = {rcs_f}")

        print("\n---------\n")

        rcs.delete(0, tk.END)
        rcs.insert(0, rcs_f)

    elif not r.get():

        print("Solve for R\n")

        pavg = float(pavg.get())
        td = float(td.get())
        gt = float(gt.get())
        gr = float(gr.get())
        f = float(f.get())
        rcs = float(rcs.get())
        pn = float(pn.get())
        ls = float(ls.get())
        snr = float(snr.get())

        print("\t Pₐᵥ₉ * Td * Gₜ * Gᵣ * λ² * σ")
        print("\t------------------------------ = R⁴")
        print("\t  SNR * (4π)³ * Pₙ * Lₛ\n")

        w = (3 * pow(10, 8))/f

        num = pavg * td * gt * gr * pow(w, 2) * rcs
        den = snr * pow((4 * 3.14159265), 3) * pn * ls

        r_f = round(pow(num/den, 0.25), 3)

        print(f"\t {pavg} * {td} * {gt} * {gr} * (C/{f})² * {rcs}")
        print(f"\t----------------------------------------------- = {r_f}⁴")
        print(f"\t    {snr} * (4π)³ * {pn} * {ls}\n")

        print(f"R = {r_f}")

        print("\n---------\n")

        r.delete(0, tk.END)
        r.insert(0, r_f)

    elif not pn.get():

        print("Solve for Pₙ\n")

        pavg = float(pavg.get())
        td = float(td.get())
        gt = float(gt.get())
        gr = float(gr.get())
        f = float(f.get())
        rcs = float(rcs.get())
        r = float(r.get())
        ls = float(ls.get())
        snr = float(snr.get())

        print("\t Pₐᵥ₉ * Td * Gₜ * Gᵣ * λ² * σ")
        print("\t------------------------------ = Pₙ")
        print("\t  SNR * (4π)³ * R⁴ * Lₛ\n")

        w = (3 * pow(10, 8))/f

        num = pavg * td * gt * gr * pow(w, 2) * rcs
        den = pow((4 * 3.14159265), 3) * snr * pow(r, 4) * ls

        pn_f = round(num/den, 3)

        print(f"\t {pavg} * {td} * {gt} * {gr} * (C/{f})² * {rcs}")
        print(f"\t------------------------------------------------ = {pn_f}")
        print(f"\t   {snr} * (4π)³ * {r}⁴ * {ls}\n")

        print(f"Pₙ = {pn_f}")

        print("\n---------\n")

        pn.delete(0, tk.END)
        pn.insert(0, pn_f)

    elif not ls.get():

        print("Solve for Pₙ\n")

        pavg = float(pavg.get())
        td = float(td.get())
        gt = float(gt.get())
        gr = float(gr.get())
        f = float(f.get())
        rcs = float(rcs.get())
        r = float(r.get())
        pn = float(pn.get())
        snr = float(snr.get())

        print("\t Pₐᵥ₉ * Td * Gₜ * Gᵣ * λ² * σ")
        print("\t------------------------------ = Lₛ")
        print("\t  SNR * (4π)³ * R⁴ * Pₙ\n")

        w = (3 * pow(10, 8))/f

        num = pavg * td * gt * gr * pow(w, 2) * rcs
        den = pow((4 * 3.14159265), 3) * snr * pow(r, 4) * pn

        ls_f = round(num/den, 3)

        print(f"\t {pavg} * {td} * {gt} * {gr} * (C/{f})² * {rcs}")
        print(f"\t------------------------------------------------ = {ls_f}")
        print(f"\t   {snr} * (4π)³ * {r}⁴ * {pn}\n")

        print(f"Lₛ = {ls_f}")

        print("\n---------\n")

        ls.delete(0, tk.END)
        ls.insert(0, ls_f)

    else:
        print("Error")

    return

#!######## Calc ########## Calc ########## Calc ########## Calc ############
#/////////////////////////////////////////////////////////////////////////
########## GUI ########## GUI ########## GUI ########## GUI ############

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
    btn_plot = tk.Button(tab4, text="Calc", command=lambda: calculate(pavg_entry, td_entry, gt_entry, gr_entry, f_entry, rcs_entry, r_entry, pn_entry, ls_entry, 
                                                                      snr_entry, pavg_unit.get(), td_unit.get(), f_unit.get(), rcs_unit.get(), r_unit.get(), pn_unit.get()), 
                                                                      font=default_font, width=7, bg='darkgray')
    btn_plot.grid(row=10, column=3, padx=10, pady=10)

    # Insert image
    img = Image.open("Equations\APF.png")
    img = ImageTk.PhotoImage(img)
    label_img = tk.Label(tab4, image=img)
    label_img.image = img
    label_img.grid(row=1, column=4, columnspan=2, rowspan=10, padx=10, pady=10)

#!######## GUI ########## GUI ########## GUI ########## GUI ############