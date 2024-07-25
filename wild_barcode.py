#I made this to work with my barcode scanner as recreation of wild gunman for nes 

import keyboard
import time
import os
import random
def action(time_frame):
    start_time = time.time()
    while time.time() - start_time < time_frame:
        if keyboard.get_hotkey_name():
            os.system("figlet -c -f banner you win")
            return True
        time.sleep(0.01) 
    os.system("figlet -c -f banner game over")
    return False
x = 3
for i in range(3):
    os.system(f"figlet -f banner -c {x}")
    x -= 1
    time.sleep(1)
    os.system("clear")
os.system("figlet -f banner -c ACTION")
timef = random.uniform(0.5, 0.3)
action(timef)
