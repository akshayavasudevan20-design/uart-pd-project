# uart-pd-project
UART Transmitter RTL to GDSII using OpenLane with Python PD metrics dashboard

# UART Transmitter — RTL to GDSII Physical Design

## Project Overview
A complete UART Transmitter designed from RTL to GDSII using OpenLane on sky130A PDK, with a Python tool to automate PD metrics analysis.

## What is UART?
UART (Universal Asynchronous Receiver Transmitter) is a serial communication protocol used in virtually every chip that communicates with the outside world — microcontrollers, sensors, GPS modules, and more.

## Project Structure
- src/uart_tx.v — Verilog RTL design
- config/config.json — OpenLane configuration
- config/constraints.sdc — Timing constraints
- dashboard/dashboard.py — Python PD metrics dashboard
## Tools Used
- **OpenLane** — open source RTL to GDSII flow
- **sky130A PDK** — Google/SkyWater 130nm process
- **Python** — PD metrics automation
- **KLayout** — layout viewer

## PD Flow
RTL → Synthesis → Floorplan → Placement → CTS → Routing → GDSII

## Results
- WNS: 0.0 ns ✅ (timing met)
- DRC Violations: 0 ✅ (clean layout)
- Total Cells: 37
- Area: 0.002568 mm²

## Python Dashboard
Automatically reads OpenLane metrics and compares multiple runs:
UART TX — Multi-Run PD Comparison
Metric               Run1 (0.5)      Run2 (0.6)      Run3 (0.7)
WNS (ns)                  0.0             0.0             0.0
Area (mm²)         0.002568        0.002568        0.002568
Total Cells              37              37              37
DRC Violations            0               0               0

## Author
Akshaya Vasudevan — ECE Student

