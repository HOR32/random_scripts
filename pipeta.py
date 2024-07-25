#simple tool to show rgb value of mouse cursor

import pyautogui
import keyboard
def print_c(text, r, g, b):
    color_code = f"\033[38;2;{r};{g};{b}m"
    reset_code = "\033[0m"
    print(f"{color_code}{text}{reset_code}")

while True:
    if keyboard.read_key() == "space":
        x, y = pyautogui.position()
        px = pyautogui.pixel(x,y)
        r,g,b = px
        print_c(f"color {r},{g},{b}",r,g,b)
    elif keyboard.read_key() == "q":
        exit()
