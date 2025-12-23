# IA-Hackathon
Software-based instrumentation amplifier for sensor signal monitoring
# Software-Based Instrumentation Amplifier for Sensor Signal Monitoring

## Project Description
This project simulates an instrumentation amplifier (IA) in Python. It takes two input signals (Vin+ and Vin−), subtracts them to get the differential signal, amplifies it by a gain of 5.6, and visualizes the output. The simulation demonstrates how weak sensor signals from sensors can be amplified and made reliable, even in the presence of noise.

This approach is inspired by real-world applications where small signals from sensors (like smoke detectors, air quality sensors, or biomedical devices) need to be amplified before processing or display.

---

## Features
- Differential signal amplification  
- Common-mode noise rejection  
- Visual output using Matplotlib  
- Beginner-friendly Python code  

---

## Problem Statement
Many sensors produce very small voltage signals that are difficult to measure accurately. These weak signals can easily be masked by noise, making readings unreliable. Beginners and hobbyists often struggle to interpret low-level signals correctly.  

---

## Solution
This software-based instrumentation amplifier simulates the amplification of small signals while rejecting common-mode noise. The output shows amplified signals that are clear and reliable, demonstrating the principles of real-world monitoring systems.

---

## Benefits
1. **Safety & Monitoring:** Can be applied to smoke detectors, air quality sensors, and industrial sensor systems.  
2. **Accuracy:** Amplifies weak signals and reduces noise for reliable readings.  
3. **Educational:** Demonstrates concepts of instrumentation amplifiers, signal amplification, and noise rejection.  
4. **Accessible:** Uses simple Python code that beginners can understand and modify.  
5. **Extendable:** Can be connected to Arduino, microcontrollers, or IoT dashboards for real-time monitoring.  

---

## Tech Stack
- Python (for simulation and signal processing)  
- Matplotlib (for plotting input and output signals)  

---

## How to Run
1. Open `IA_simulation.py` in Python (Spyder, VS Code, or any IDE).  
