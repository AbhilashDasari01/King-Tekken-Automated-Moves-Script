import time
from pynput.keyboard import Key, Controller, Listener

# Initialize keyboard controller
keyboard = Controller()

# Default frame timing
default_frame_time = 1 / 60  # Assuming 60 FPS (~16.67ms per frame)
move_delay = default_frame_time * 1
button_hold_delay = default_frame_time * 2

# Move execution functions
def giant_swing_p1():
    print("Executing Giant Swing for P1...")
    keyboard.press('d')
    time.sleep(move_delay)
    keyboard.release('d')
    time.sleep(move_delay)
    keyboard.press('a')
    time.sleep(move_delay)
    keyboard.press('s')
    time.sleep(move_delay)
    keyboard.release('a')
    time.sleep(move_delay)
    keyboard.press('d')
    time.sleep(move_delay)
    keyboard.release('s')
    keyboard.press('j')  # Square (□)
    time.sleep(button_hold_delay)
    keyboard.release('d')
    keyboard.release('j')

def giant_swing_p2():
    print("Executing Giant Swing for P2...")
    keyboard.press('a')
    time.sleep(move_delay)
    keyboard.release('a')
    time.sleep(move_delay)
    keyboard.press('d')
    time.sleep(move_delay)
    keyboard.press('s')
    time.sleep(move_delay)
    keyboard.release('d')
    time.sleep(move_delay)
    keyboard.press('a')
    time.sleep(move_delay)
    keyboard.release('s')
    keyboard.press('j')  # Square (□)
    time.sleep(button_hold_delay)
    keyboard.release('a')
    keyboard.release('j')

def twister_p1():
    print("Executing Twister for P1...")
    keyboard.press('d')
    time.sleep(move_delay)
    keyboard.release('d')
    time.sleep(move_delay)
    keyboard.press('a')
    time.sleep(move_delay)
    keyboard.press('s')
    time.sleep(move_delay)
    keyboard.release('a')
    time.sleep(move_delay)
    keyboard.press('d')
    time.sleep(move_delay)
    keyboard.release('s')
    keyboard.press('i')  # Triangle (△)
    time.sleep(button_hold_delay)
    keyboard.release('d')
    keyboard.release('i')

def twister_p2():
    print("Executing Twister for P2...")
    keyboard.press('a')
    time.sleep(move_delay)
    keyboard.release('a')
    time.sleep(move_delay)
    keyboard.press('d')
    time.sleep(move_delay)
    keyboard.press('s')
    time.sleep(move_delay)
    keyboard.release('d')
    time.sleep(move_delay)
    keyboard.press('a')
    time.sleep(move_delay)
    keyboard.release('s')
    keyboard.press('i')  # Triangle (△)
    time.sleep(button_hold_delay)
    keyboard.release('a')
    keyboard.release('i')

def muscle_buster_p1():
    print("Executing Muscle Buster for P1...")
    keyboard.press('s')
    time.sleep(move_delay)
    keyboard.press('a')
    time.sleep(move_delay)
    keyboard.release('s')
    keyboard.press('p')  # 1+2 (Square + Triangle) **Simultaneous with Back**
    time.sleep(button_hold_delay)
    keyboard.release('a')
    keyboard.release('p')

def muscle_buster_p2():
    print("Executing Muscle Buster for P2...")
    keyboard.press('s')
    time.sleep(move_delay)
    keyboard.press('d')
    time.sleep(move_delay)
    keyboard.release('s')
    keyboard.press('p')  # 1+2 (Square + Triangle) **Simultaneous with Back**
    time.sleep(button_hold_delay)
    keyboard.release('d')
    keyboard.release('p')

# Crouch Dash for Player 1 (E) → f * d df (d * s s+d)
def crouch_dash_p1():
    print("Executing Crouch Dash for P1...")
    keyboard.press('d')
    time.sleep(move_delay)
    keyboard.release('d')
    time.sleep(move_delay)
    keyboard.press('s')
    time.sleep(move_delay)
    keyboard.press('d')
    time.sleep(button_hold_delay)
    keyboard.release('d')
    keyboard.release('s')

# Crouch Dash for Player 2 (Q) → f * d df (a * s s+a)
def crouch_dash_p2():
    print("Executing Crouch Dash for P2...")
    keyboard.press('a')
    time.sleep(move_delay)
    keyboard.release('a')
    time.sleep(move_delay)
    keyboard.press('s')
    time.sleep(move_delay)
    keyboard.press('a')
    time.sleep(button_hold_delay)
    keyboard.release('a')
    keyboard.release('s')

# Listen for key presses
def on_press(key):
    if hasattr(key, 'char'):
        if key.char == 'u':
            giant_swing_p1()
        elif key.char == 'h':
            giant_swing_p2()
        elif key.char == 'y':
            twister_p1()
        elif key.char == 'g':
            twister_p2()
        elif key.char == ']':
            muscle_buster_p1()
        elif key.char == '[':
            muscle_buster_p2()
        elif key.char == 'e':
            crouch_dash_p1()
        elif key.char == 'q':
            crouch_dash_p2()

# Start the key listener
with Listener(on_press=on_press) as listener:
    listener.join()