=========================================
King-Tekken-Automated-Moves-Script (Python)
=========================================

Description:
------------
This script automates King's move execution in Tekken.
It listens for specific key presses and simulates the correct input sequences  
to execute moves with frame-accurate timing.

The script is useful for practicing or testing certain moves that require  
precise execution, such as Giant Swing, Twister, and Muscle Buster.

Requirements:
-------------
- Python 3.x  
- `pynput` library (install using: `pip install pynput`)  
- PPSSPP emulator running **Tekken 6**  
- A properly configured keyboard for PPSSPP  

Setup Instructions:
-------------------
1. **Install Python**  
   - If you don’t have Python installed, download and install it from  
     https://www.python.org/downloads/  

2. **Install dependencies**  
   - Open a terminal or command prompt and run:  
     ```
     pip install pynput
     ```

3. **Run the script**  
   - Open a terminal or command prompt in the folder where the script is located.  
   - Run the script using:  
     ```
     python script.py
     ```

4. **Start PPSSPP and Tekken 6**  
   - Make sure the game is running and your keyboard controls match  
     the script’s expected input layout.

How It Works:
-------------
- The script continuously listens for specific key presses.  
- When a key is detected, it executes a pre-defined move by simulating  
  the correct button presses with accurate frame timing.  
- Timing is based on a **60 FPS frame rate** to ensure consistency.  

Move List & Key Bindings:
-------------------------
- **Giant Swing (P1)**  → Press `U`  
  - **Input sequence:** `→, ← ↓, → + Square`  
- **Giant Swing (P2)**  → Press `H`  
  - **Input sequence:** `←, → ↓, ← + Square`  

- **Twister (P1)**      → Press `Y`  
  - **Input sequence:** `→, ← ↓, → + Triangle`  
- **Twister (P2)**      → Press `G`  
  - **Input sequence:** `←, → ↓, ← + Triangle`  

- **Muscle Buster (P1)** → Press `]`  
  - **Input sequence:** `↓ ↙ ← + Square + Triangle`  
- **Muscle Buster (P2)** → Press `[`  
  - **Input sequence:** `↓ ↘ → + Square + Triangle`  

- **Crouch Dash (P1)**  → Press `E`  
  - **Input sequence:** `→ ↓ ↘` 
- **Crouch Dash (P2)**  → Press `Q`  
  - **Input sequence:** `← ↓ ↙`  

Timing and Frame Rate:
----------------------
- The script assumes a **60 FPS** frame rate (≈16.67ms per frame).  
- Each move uses a **move delay** to match in-game execution speed.  
- If it is lagging or running at a lower frame rate,  
  move execution **may be inaccurate**.  

Troubleshooting:
----------------

**1. The moves are coming out too slow or too fast.**  
   - Modify the `move_delay` value in the script to adjust timing.  
   - Ensure PPSSPP is running at **full speed (60 FPS)** for accuracy.  

**2. My keyboard inputs are different from the script.**  
   - Open PPSSPP and check **Controls Settings**.  
   - Change the script’s key bindings to match your PPSSPP configuration.  

Customization:
--------------
You can modify the script to adjust the following:
- **Key bindings:** Change the assigned keys for each move.  
- **Timing settings:** Adjust `move_delay` for different frame speeds.  
- **New moves:** Add more move sequences by following the same pattern.  

License:
--------
This script is free to use and modify.  
Use at your own risk—automated inputs may not be allowed in online play.  
