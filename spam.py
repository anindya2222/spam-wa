import random
import pyautogui as pg
import time

piknik=('ayo transfer','ayo bayar')
time.sleep(8)
for i in range(20):
    a=random.choice(piknik)
    pg.write("ndri" + a)
    pg.press('enter')
    
    
    