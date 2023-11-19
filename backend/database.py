import sqlite3
conn = sqlite3.connect('lion_dataset.db')
cursor = conn.cursor()


def create_db():
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS status (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                status INTEGER
            )
        ''')

        cursor.execute('''
            INSERT INTO status (status)
            VALUES (?)
        ''', ("1"))
    

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS instant_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                voltage REAL,
                current REAL,
                temperature REAL,
                soc REAL,
                status INTEGER
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cycle_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cycle_index INTEGER,
                discharge_time REAL,
                time_above_3_1v REAL,
                decrement_time_3_2v_3_1v REAL,
                max_voltage_discharge REAL,
                min_voltage_discharge REAL,
                average_discharge_current REAL,
                charging_time REAL,
                average_charging_current REAL,
                total_time REAL,
                start_timestamp TIMESTAMP,
                end_timestamp TIMESTAMP
            )
        ''')
        
        conn.commit()
        print("database created sucessfully...")
        print("Proceeding further...")
        return True
    except sqlite3.Error as e:
        print("database creation failed...")
        print("Exiting program...")
        print(f"Error: {e}")
        return False

def insert_to_instant_db(timestamp,voltage,current,temperature,soc,status):
        cursor.execute('''
            INSERT INTO instant_data (timestamp, voltage, current, temperature,soc, status)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (timestamp, voltage, current, temperature, soc, status))
        conn.commit()

def insert_to_cycle_db(data):
        cursor.execute('''
            INSERT INTO cycle_data (cycle_index,
                discharge_time,time_above_3_1v,
                decrement_time_3_2v_3_1v,
                max_voltage_discharge ,
                min_voltage_discharge ,
                average_discharge_current ,
                charging_time ,
                average_charging_current ,
                total_time)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (data.cycle_index,
                data.discharge_time,
                data.time_above_3_1v,
                data.decrement_time_3_2v_3_1v,
                data.max_voltage_discharge ,
                data.min_voltage_discharge ,
                data.average_discharge_current ,
                data.charging_time ,
                data.average_charging_current ,
                data.total_time))
        conn.commit()


def update_status(status):
        cursor.execute('''
            UPDATE status
            SET status = ?
            WHERE id = ?
        ''', (status, 1))
        conn.commit()

# def get_status():
#     cursor.execute('SELECT * FROM instant_data')
#     rows = cursor.fetchall()
#     return rows[0][0]


def get_instant_db():
    cursor.execute('SELECT * FROM instant_data')
    rows = cursor.fetchall()
    return rows

def get_cycle_db():
    cursor.execute('SELECT * FROM cycle_data')
    rows = cursor.fetchall()
    return rows

def get_prev_soc():
    cursor.execute('SELECT * FROM instant_data ORDER BY timestamp DESC LIMIT 1')
    row = cursor.fetchone()
    return row[5] if row else None

def get_prev_mode():
    cursor.execute('SELECT * FROM instant_data ORDER BY timestamp DESC LIMIT 1')
    row = cursor.fetchone()
    return row[6] if row else None

def get_prev_cycle_index():
    cursor.execute('SELECT * FROM cycle_data ORDER BY cycle_index DESC LIMIT 1')
    row = cursor.fetchone()
    return row[0] if row else None

def close_db():
    conn.close()