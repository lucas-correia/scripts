import pyautogui
import time
from datetime import datetime, timedelta
import random


class Treino:
    def __init__(self):
        self.DELTA_TIME_USE_RING = datetime.now()
        self.DELTA_TIME_USE_SPELL = datetime.now()
        self.DELTA_TIME_USE_BOOTS = datetime.now()
        self.DELTA_TIME_USE_FOOD = datetime.now()
        self.DELTA_TIME_USE_GFB = datetime.now()


    def life_ring(self):
        if (datetime.now() > self.DELTA_TIME_USE_RING):
            self.DELTA_TIME_USE_RING = datetime.now() + timedelta(minutes=20)
            print('usou ring', datetime.now())
            pyautogui.press('l')
            time.sleep(1)

    def sd(self):
        if (datetime.now() > self.DELTA_TIME_USE_SPELL):
            self.DELTA_TIME_USE_SPELL = datetime.now() + timedelta(seconds=110)
            print('usou sd', datetime.now())
            pyautogui.press('o')
            time.sleep(1)
            
    def soft(self):
        if (datetime.now() > self.DELTA_TIME_USE_BOOTS):
            self.DELTA_TIME_USE_BOOTS = datetime.now() + timedelta(hours=4)
            print('usou soft', datetime.now())
            pyautogui.press('i')
            time.sleep(1)
            
    def food(self):
        if (datetime.now() > self.DELTA_TIME_USE_FOOD):
            self.DELTA_TIME_USE_FOOD = datetime.now() + timedelta(minutes=4)
            print('usou food', datetime.now())
            pyautogui.press('p')
            time.sleep(1)
            
    def gfb(self):
        if (datetime.now() > self.DELTA_TIME_USE_GFB):
            self.DELTA_TIME_USE_GFB = datetime.now() + timedelta(seconds=58)
            print('usou gfb', datetime.now())
            pyautogui.press('o')
            time.sleep(1)       
        
if __name__ == '__main__':
    treino = Treino()
    while(True):
        random_sleep = random.randrange(6, 12, 2)
        treino.life_ring()
        treino.sd()
        treino.soft()
        treino.food()
        #treino.gfb()
        
        while (random_sleep > 0):
            time.sleep(2)
            random_sleep -= 2 