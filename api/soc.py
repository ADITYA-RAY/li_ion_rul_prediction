import numpy as np
from numpy import trapz

def get_socc(current,mode):
    area = round(trapz(current, dx=1/360),2)
    soc = abs(area/6)*100 if mode == "Charging" else ((6 - area)/6)*100
    return round(soc,2)
