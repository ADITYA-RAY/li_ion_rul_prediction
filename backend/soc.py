from database import get_prev_soc
from variables import dx
dx = dx()
total_charge = 6

def get_soc(mode, current):
    prev_soc = get_prev_soc()
    if not prev_soc:
        prev_soc = 100
    charge = (dx * current) / 3600
    percent_soc = (charge / 6) * 100
    
    return prev_soc + percent_soc if mode else prev_soc - percent_soc
