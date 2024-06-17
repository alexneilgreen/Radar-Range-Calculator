import tkinter as tk
from tkinter import *
from tkinter import ttk
import Recieved_Power
import Recieved_Thermal_Noise
import Signal_to_Noise_Ratio
import Average_Power
import Jammer_One_Way_Link

root = tk.Tk()
root.title("Radar Calculator")
tabControl = ttk.Notebook(root)
# screenWidth = root.winfo_screenwidth()  # width of screen
# screenHeight = root.winfo_screenheight()  # height of screen

tabStyle = ttk.Style()
tabStyle.theme_use('default')
tabStyle.configure('TNotebook.Tab', background="darkgray")
tabStyle.map("TNotebook.Tab", background= [("selected", "#f0f0f0")])

tab1 = tk.Frame(tabControl)
tab2 = tk.Frame(tabControl)
tab3 = tk.Frame(tabControl)
tab4 = tk.Frame(tabControl)
tab5 = tk.Frame(tabControl)

tabControl.add(tab1, text='Recieved Power')
tabControl.add(tab2, text='Recieved Thermal Noise')
tabControl.add(tab3, text='Signal-to-Noise')
tabControl.add(tab4, text='Average Power')
tabControl.add(tab5, text='Jammer One Way Link')

tabControl.pack(expand=True, fill="both", padx= 5, pady=5)

Recieved_Power.create_RP_tab_content(tab1)
Recieved_Thermal_Noise.create_RTN_tab_content(tab2)
Signal_to_Noise_Ratio.create_SNR_tab_content(tab3)
Average_Power.create_AP_tab_content(tab4)
Jammer_One_Way_Link.create_JOWL_tab_content(tab5)

root.mainloop()
