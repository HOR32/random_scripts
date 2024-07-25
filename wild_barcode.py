import keyboard
import time
import os
def action(time_frame):
    start_time = time.time()
    while time.time() - start_time < time_frame:
        if keyboard.get_hotkey_name():
            os.system("figlet -c you win")
            return True
        time.sleep(0.01) 
    os.system("figlet -c game over")
    return False
x = 3
for i in range(3):
    os.system(f"figlet -c {x}")
    x -= 1
    time.sleep(1)
    os.system("clear")
os.system("figlet -c ACTION")
timef = 0.5
action(timef)
