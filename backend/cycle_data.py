from database import get_prev_cycle_index, get_cycle_db
from variables import dx

prev_index = get_prev_cycle_index()
db = get_cycle_db()
dx = dx()
data = {}

def cycle_calculations():
    charge_points = 0
    max_voltage_discharge , min_voltage_discharge = 0, 10
    above_voltage , between_voltage = 0, 0
    chargeing_current, discharging_current = 0, 0

    if not prev_index:
        index = 1
    else:
        index+=prev_index

    for row in db:
        if row[6]:
            charge_points += 1
            charging_current += row[2] 
        else:
            max_voltage_discharge = max(max_voltage_discharge, row[1])
            min_voltage_discharge = min(min_voltage_discharge, row[1])
            
            if row[1] > 3.1:
                above_voltage+=1
            if 3.2 > row[1] > 3:
                between_voltage+=1 
            
            discharging_current += row[2]

    discharge_points = len(db) - charge_points

    data["prev_index"] = index
    data["discharge_time"] = dx * discharge_points
    data["charging_time"] = dx * charge_points
    data["total_time"] = len(db) * dx
    data["max_voltage_discharge"] = max_voltage_discharge
    data["min_voltage_discharge"] = min_voltage_discharge
    data["time_above_3_1v"] = dx * above_voltage
    data["decrement_time_3_2v_3_1v"] = dx * between_voltage
    data["average_discharge_current"] = discharging_current / len(db)
    data["average_charging_current"] = charging_current / len(db)

    return data

