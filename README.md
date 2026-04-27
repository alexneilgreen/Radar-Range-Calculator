<!-- SHOWCASE: true -->

# Radar Range Calculator

> A multi-tab desktop GUI for solving and visualizing the radar range equation and related RF formulas.

![Status](https://img.shields.io/badge/status-complete-brightgreen)
![Language](https://img.shields.io/badge/language-Python-blue)

---

## Project Description

Radar Range Calculator is a Python desktop application built with tkinter that allows users to compute key radar and electronic warfare parameters using standard RF engineering equations. Each of the five tabs covers a distinct form of the radar range equation: received power, received thermal noise, signal-to-noise ratio, average power, and jammer one-way link. The user leaves exactly one field blank and the application solves for that unknown, with full unit conversion support across power, frequency, distance, and radar cross-section units. Each tab also includes a matplotlib-based plot showing how the solved variable changes with range across a logarithmic scale. This project was built as a personal learning tool to develop intuition for how the radar range equation works in practice.

---

## Screenshots / Demo

> _No screenshot available. Add one with: `![Demo](docs/your-image.png)`_

---

## Results

When a calculation is run successfully, step-by-step work is printed to the terminal alongside the numeric result. A representative example from the Received Power tab:

```
Solve for Pᵣ

     Pₜ * Gₜ * Gᵣ * λ² * σ
    ---------------------- = Pᵣ
          (4π)³ * R⁴

  1000.0 * 30.0 * 30.0 * (C/9.5e9)² * 1.0
  ------------------------------------------ = 3.142e-12
               (4π)³ * 50000.0⁴

Pᵣ = 3.142e-12

---------
```

The solved value is written back into the blank input field automatically. If the input is invalid (alphabetic characters, special characters, or an empty field), the terminal will list the offending rows and their error reasons before aborting. If all fields are filled, the application will prompt the user to clear one field before calculating. After a successful calculation, the "Graph" button opens a separate matplotlib window plotting the solved variable against range on a log scale. If a result appears unexpectedly large or small, check that the unit dropdowns match the values entered in each field.

---

## Key Concepts

`Radar Range Equation` `Jammer One-Way Link` `Signal-to-Noise Ratio` `Received Thermal Noise` `Average Power` `Unit Conversion` `Radar Cross-Section` `matplotlib Visualization` `tkinter GUI`

---

## Languages & Tools

- **Language:** Python 3
- **Framework/SDK:** tkinter (GUI), matplotlib (plotting), NumPy (numerical arrays), Pillow (image handling)
- **Hardware:** N/A
- **Build System:** None - run directly with the Python interpreter

---

## File Structure

```
RadarRangeCalculator/
├── Main.py                      # Entry point - creates the root window and tabbed notebook
├── requirements.txt
└── src/                         # All calculation and UI modules
    ├── Recieved_Power.py        # Tab 1 - received power form of the radar range equation
    ├── Recieved_Thermal_Noise.py # Tab 2 - received thermal noise calculation
    ├── Signal_to_Noise_Ratio.py # Tab 3 - signal-to-noise ratio calculation
    ├── Average_Power.py         # Tab 4 - average power calculation
    ├── Jammer_One_Way_Link.py   # Tab 5 - jammer one-way link equation
    └── UnitConversion.py        # Shared utility module for all unit conversions
└── Equations/                   # Reference assets
    ├── Equations.docx           # Document containing the source equations
    ├── APF.png                  # Average power formula image
    ├── JOWL.png                 # Jammer one-way link formula image
    ├── RPF.png                  # Received power formula image
    ├── RTN.png                  # Received thermal noise formula image
    └── SNR.png                  # Signal-to-noise ratio formula image
```

---

## Installation & Usage

### Prerequisites

- Python 3.9 or higher
- pip

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/alexneilgreen/RadarRangeCalculator.git
cd RadarRangeCalculator

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run
python Main.py
```

### Controls

| Action                | Description                                                      |
| --------------------- | ---------------------------------------------------------------- |
| Leave one field blank | The application solves for that unknown variable                 |
| Click "Calculate"     | Runs the solve and prints step-by-step work to the terminal      |
| Click "Graph"         | Opens a matplotlib window plotting the solved variable vs. range |
| Unit dropdowns        | Select the unit for each physical quantity before calculating    |

---

## Academic Integrity

This repository is publicly available for **portfolio and reference purposes only**.
Please do not submit any part of this work as your own for academic coursework.
