# tab3
#TODO Finish Conversions
#TODO Finish Second 2 buttons and equations
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

#?#?#       Pₜ * Gₜ * Gᵣ * λ² * σ
#?#?# Pᵣ = ----------------------
#?#?#         (4π)³ * R⁴ * Pₙ

#TODO not repopulating fields
def calculate(pt, gt, gr, f, rcs, r, pn, snr, pt_unit, f_unit, rcs_unit, r_unit, pn_unit):

    

    # Check if input is valid for calculation
    input = []
    input.append(pt.get())
    input.append(gt.get())
    input.append(gr.get())
    input.append(f.get())
    input.append(rcs.get())
    input.append(r.get())
    input.append(pn.get())
    input.append(snr.get())
    if validateInput(input) :
        return
    else : 
        pass



    # Calculations Start
    if not snr.get():

        print("Solve for SNR\n")

        pt = float(pt.get())
        gt = float(gt.get())
        gr = float(gr.get())
        f = float(f.get())
        rcs = float(rcs.get())
        r = float(r.get())
        pn = float(pn.get())

        print("\t Pₜ * Gₜ * Gᵣ * λ² * σ")
        print("\t---------------------- = SNR")
        print("\t  (4π)³ * R⁴ * Pₙ\n")

        w = (3 * pow(10, 8))/f

        num = pt * gt * gr * pow(w, 2) * rcs
        den = pow((4 * 3.14159265), 3) * pow(r, 4) * pn

        snr_f = round(num/den, 3)

        print(f"\t  {pt} * {gt} * {gr} * (C/{f})² * {rcs}")
        print(f"\t------------------------------------------ = {snr_f}")
        print(f"\t   (4π)³ * {r}⁴ * {pn}\n")

        print(f"SNR = {snr_f}")

        print("\n---------\n")

        snr.delete(0, tk.END)
        snr.insert(0, snr_f)

    elif not pt.get():
        
        print("Solve for Pₜ\n")

        gt = float(gt.get())
        gr = float(gr.get())
        f = float(f.get())
        rcs = float(rcs.get())
        r = float(r.get())
        pn = float(pn.get())
        snr = float(snr.get())

        print("\t SNR * (4π)³ * R⁴ * Pₙ")
        print("\t------------------------ = Pₜ")
        print("\t   Gₜ * Gᵣ * λ² * σ\n")

        w = (3 * pow(10, 8))/f

        num =  snr * pow((4 * 3.14159265), 3) * pow(r, 4) * pn
        den = gt * gr * pow(w, 2) * rcs

        pt_f = round(num/den, 3)

        print(f"\t {snr} * (4π)³ * {r}⁴ * {pn}")
        print(f"\t--------------------------------  = {pt_f}")
        print(f"\t {gt} * {gr} * {w}² * {rcs}\n")

        print(f"Pₜ = {pt_f}")

        print("\n---------\n")

        pt.delete(0, tk.END)
        pt.insert(0, pt_f)

    elif not gt.get():

        print("Solve for Gₜ\n")

        pt = float(pt.get())
        gr = float(gr.get())
        f = float(f.get())
        rcs = float(rcs.get())
        r = float(r.get())
        pn = float(pn.get())
        snr = float(snr.get())

        print("\t SNR * (4π)³ * R⁴ * Pₙ")
        print("\t---------------------- = Gₜ")
        print("\t  Pₜ * Gᵣ * λ² * σ\n")

        w = (3 * pow(10, 8))/f

        num =  snr * pow((4 * 3.14159265), 3) * pow(r, 4) * pn
        den = pt * gr * pow(w, 2) * rcs

        gt_f = round(num/den, 3)

        print(f"\t {snr} * (4π)³ * {r}⁴ * {pn}")
        print(f"\t--------------------------------  = {gt_f}")
        print(f"\t {pt} * {gr} * {w}² * {rcs}\n")

        print(f"Gₜ = {gt_f}")

        print("\n---------\n")

        gt.delete(0, tk.END)
        gt.insert(0, gt_f)

    elif not gr.get():

        print("Solve for Gᵣ\n")

        pt = float(pt.get())
        gt = float(gt.get())
        f = float(f.get())
        rcs = float(rcs.get())
        r = float(r.get())
        pn = float(pn.get())
        snr = float(snr.get())

        print("\t SNR * (4π)³ * R⁴ * Pₙ")
        print("\t----------------------- = Gᵣ")
        print("\t   Pₜ * Gₜ * λ² * σ\n")

        w = (3 * pow(10, 8))/f

        num =  snr * pow((4 * 3.14159265), 3) * pow(r, 4) * pn
        den = pt * gt * pow(w, 2) * rcs

        gr_f = round(num/den, 3)

        print(f"\t {snr} * (4π)³ * {r}⁴ * {pn}")
        print(f"\t--------------------------------  = {gr_f}")
        print(f"\t {pt} * {gt} * {w}² * {rcs}\n")

        print(f"Gᵣ = {gr_f}")

        print("\n---------\n")

        gr.delete(0, tk.END)
        gr.insert(0, gr_f)

    elif not f.get():

        print("Solve for λ and ƒ\n")

        pt = float(pt.get())
        gt = float(gt.get())
        gr = float(gr.get())
        rcs = float(rcs.get())
        r = float(r.get())
        pn = float(pn.get())
        snr = float(snr.get())

        print("\t SNR * (4π)³ * R⁴ * Pₙ")
        print("\t----------------------- = λ²")
        print("\t   Pₜ * Gₜ * Gᵣ * σ\n")

        num =  snr * pow((4 * 3.14159265), 3) * pow(r, 4) * pn
        den = pt * gt * gr * rcs

        w = round(pow(num/den, 0.5), 3)

        f_f = round((3 * pow(10, 8))/w, 3)

        print(f"\t {snr} * (4π)³ * {r}⁴ * {pn}")
        print(f"\t--------------------------------  = {w}²")
        print(f"\t {pt} * {gt} * {gr} * {rcs}\n")

        print(f"λ = {w}")
        print(f"ƒ = {f_f}")

        print("\n---------\n")

        f.delete(0, tk.END)
        f.insert(0, f_f)

    elif not rcs.get():

        print("Solve for σ\n")

        pt = float(pt.get())
        gt = float(gt.get())
        gr = float(gr.get())
        f = float(f.get())
        r = float(r.get())
        pn = float(pn.get())
        snr = float(snr.get())

        print("\t SNR * (4π)³ * R⁴ * Pₙ")
        print("\t----------------------- = σ")
        print("\t   Pₜ * Gₜ * Gᵣ * λ²\n")

        w = (3 * pow(10, 8))/f

        num =  snr * pow((4 * 3.14159265), 3) * pow(r, 4) * pn
        den = pt * gt * gr * pow(w, 2)

        rcs_f = round(num/den, 3)

        print(f"\t {snr} * (4π)³ * {r}⁴ * {pn}")
        print(f"\t--------------------------------  = {rcs_f}")
        print(f"\t {pt} * {gt} * {gr} * {w}²\n")

        print(f"σ = {rcs_f}")

        print("\n---------\n")

        rcs.delete(0, tk.END)
        rcs.insert(0, rcs_f)

    elif not r.get():

        print("Solve for R\n")

        pt = float(pt.get())
        gt = float(gt.get())
        gr = float(gr.get())
        f = float(f.get())
        rcs = float(rcs.get())
        pn = float(pn.get())
        snr = float(snr.get())

        print("\t Pₜ * Gₜ * Gᵣ * λ² * σ")
        print("\t---------------------- = R⁴")
        print("\t   SNR * (4π)³ * Pₙ\n")

        w = (3 * pow(10, 8))/f

        num = pt * gt * gr * pow(w, 2) * rcs
        den = pow((4 * 3.14159265), 3) * snr * pn

        r_f = round(pow(num/den, 0.25), 3)

        print(f"\t  {pt} * {gt} * {gr} * (C/{f})² * {rcs}")
        print(f"\t------------------------------------------ = {r_f}⁴")
        print(f"\t   SNR * (4π)³ * {pn}\n")

        print(f"R = {r_f}")

        print("\n---------\n")

        r.delete(0, tk.END)
        r.insert(0, r_f)

    elif not pn.get():

        print("Solve for Pₙ\n")

        pt = float(pt.get())
        gt = float(gt.get())
        gr = float(gr.get())
        f = float(f.get())
        rcs = float(rcs.get())
        r = float(r.get())
        snr = float(snr.get())

        print("\t Pₜ * Gₜ * Gᵣ * λ² * σ")
        print("\t---------------------- = Pₙ")
        print("\t   SNR * (4π)³ * R⁴\n")

        w = (3 * pow(10, 8))/f

        num = pt * gt * gr * pow(w, 2) * rcs
        den = pow((4 * 3.14159265), 3) * snr * pow(r, 4)

        pn_f = round(num/den, 3)

        print(f"\t  {pt} * {gt} * {gr} * (C/{f})² * {rcs}")
        print(f"\t------------------------------------------ = {pn_f}")
        print(f"\t   SNR * (4π)³ * {r}⁴\n")

        print(f"Pₙ = {pn_f}")

        print("\n---------\n")

        pn.delete(0, tk.END)
        pn.insert(0, pn_f)

    else:
        print("Error")

    return

#?#?#       Pₜ * Gₜ * Gᵣ * λ² * σ * nₚ
#?#?# Pᵣ = --------------------------
#?#?#            (4π)³ * R⁴ * Pₙ

def calculate_CMPE():
    # Placeholder function for plot button
    pass

#?#?#       Pₜ * Gₜ * Gᵣ * λ² * σ * nₚ
#?#?# Pᵣ = --------------------------
#?#?#         (4π)³ * R⁴ * Pₙ * Lₛ

def calculate_LC():
    # Placeholder function for plot button
    pass

#!######## Calc ########## Calc ########## Calc ########## Calc ############
#/////////////////////////////////////////////////////////////////////////
########## GUI ########## GUI ########## GUI ########## GUI ############

def create_SNR_tab_content(tab3):
    
    tk.Label(tab3, text="Signal-to-Noise Ratio Form Radar Range Equation", font=title_font).grid(row=0, column=0, columnspan=4, sticky="w", padx=10, pady=15)

    tk.Label(tab3, text="Pt : Power Transmitted", font=default_font).grid(row=1, column=0, sticky="w", padx=10, pady=10)
    pt_entry = tk.Entry(tab3)
    pt_entry.grid(row=1, column=1, padx=10, pady=10)
    pt_unit = tk.StringVar()
    pt_unit_menu = ttk.Combobox(tab3, textvariable=pt_unit, values=units_P, font=default_font, state="readonly", width=6)
    pt_unit_menu.grid(row=1, column=2, padx=10, pady=10)

    tk.Label(tab3, text="Gt : Gain Transmitted", font=default_font).grid(row=2, column=0, sticky="w", padx=10, pady=10)
    gt_entry = tk.Entry(tab3)
    gt_entry.grid(row=2, column=1, padx=10, pady=10)
    tk.Label(tab3, text="dB", font=default_font).grid(row=2, column=2, sticky="w", padx=10, pady=10)

    tk.Label(tab3, text="Gr : Gain Received", font=default_font).grid(row=3, column=0, sticky="w", padx=10, pady=10)
    gr_entry = tk.Entry(tab3)
    gr_entry.grid(row=3, column=1, padx=10, pady=10)
    tk.Label(tab3, text="dB", font=default_font).grid(row=3, column=2, sticky="w", padx=10, pady=10)

    # tk.Label(tab1, text="λ : Wavelength", font=default_font).grid(row=4, column=0, sticky="w", padx=10, pady=10)
    # w_entry = tk.Entry(tab1)
    # w_entry.grid(row=4, column=1, padx=10, pady=10)
    # w_unit = tk.StringVar()
    # w_unit_menu = ttk.Combobox(tab1, textvariable=w_unit, values=units_hz, font=default_font, state="readonly", width=6)
    # w_unit_menu.grid(row=4, column=2, padx=10, pady=10)

    tk.Label(tab3, text="ƒ : frequency", font=default_font).grid(row=4, column=0, sticky="w", padx=10, pady=10)
    f_entry = tk.Entry(tab3)
    f_entry.grid(row=4, column=1, padx=10, pady=10)
    f_unit = tk.StringVar()
    f_unit_menu = ttk.Combobox(tab3, textvariable=f_unit, values=units_hz, font=default_font, state="readonly", width=6)
    f_unit_menu.grid(row=4, column=2, padx=10, pady=10)

    tk.Label(tab3, text="σ : Radar Cross Section", font=default_font).grid(row=5, column=0, sticky="w", padx=10, pady=10)
    rcs_entry = tk.Entry(tab3)
    rcs_entry.grid(row=5, column=1, padx=10, pady=10)
    rcs_unit = tk.StringVar()
    rcs_unit_menu = ttk.Combobox(tab3, textvariable=rcs_unit, values=units_rcs, font=default_font, state="readonly", width=6)
    rcs_unit_menu.grid(row=5, column=2, padx=10, pady=10)

    tk.Label(tab3, text="R : Range", font=default_font).grid(row=6, column=0, sticky="w", padx=10, pady=10)
    r_entry = tk.Entry(tab3)
    r_entry.grid(row=6, column=1, padx=10, pady=10)
    r_unit = tk.StringVar()
    r_unit_menu = ttk.Combobox(tab3, textvariable=r_unit, values=units_R, font=default_font, state="readonly", width=6)
    r_unit_menu.grid(row=6, column=2, padx=10, pady=10)

    tk.Label(tab3, text="Pₙ : Thermal Noise Power", font=default_font).grid(row=7, column=0, sticky="w", padx=10, pady=10)
    pn_entry = tk.Entry(tab3)
    pn_entry.grid(row=7, column=1, padx=10, pady=10)
    pn_unit = tk.StringVar()
    pn_unit_menu = ttk.Combobox(tab3, textvariable=pn_unit, values=units_P, font=default_font, state="readonly", width=6)
    pn_unit_menu.grid(row=7, column=2, padx=10, pady=10)

    tk.Label(tab3, text=f"SNR : Signal-to-Noise Ratio", font=default_font).grid(row=8, column=0, sticky="w", padx=10, pady=10)
    snr_entry = tk.Entry(tab3)
    snr_entry.grid(row=8, column=1, padx=10, pady=10)

    # Plot buttons
    btn_plot = tk.Button(tab3, text="Calc", command=lambda: calculate(pt_entry, gt_entry, gr_entry, f_entry, rcs_entry, r_entry, pn_entry, snr_entry, 
                                                                      pt_unit.get(), f_unit.get(), rcs_unit.get(), r_unit.get(), pn_unit.get()), 
                                                                      font=default_font, width=7, bg='darkgray')
    btn_plot.grid(row=8, column=3, padx=10, pady=10)

    #TODO: btn_plot = tk.Button(tab3, text="Calc CMPE", command=calculate_CMPE, font=default_font, width=7, bg='darkgray')
    #TODO: btn_plot.grid(row=9, column=3, padx=10, pady=10)

    #TODO: btn_plot = tk.Button(tab3, text="Calc LC", command=calculate_LC, font=default_font, width=7, bg='darkgray')
    #TODO: btn_plot.grid(row=10, column=3, padx=10, pady=10)

    # Insert image
    img = Image.open("Equations\SNR.png")
    img = ImageTk.PhotoImage(img)
    label_img = tk.Label(tab3, image=img)
    label_img.image = img
    label_img.grid(row=1, column=4, columnspan=2, rowspan=8, padx=10, pady=10)

#!######## GUI ########## GUI ########## GUI ########## GUI ############