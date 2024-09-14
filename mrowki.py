import random
import os
import time

col = os.get_terminal_size(0)[0]
row = os.get_terminal_size(0)[1]
znak = [" ","#","0"]
while True:
    x = ""
    for i in range(row):
        for j in range(col):
            x += random.choice(znak)
            
        print(x)
    time.sleep(0.5)

