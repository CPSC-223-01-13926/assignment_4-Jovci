import json
import calendar

def read_data(filename):
    try: 
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
            return {}


def write_data(data,filename):
    with open(filename, 'w') as file:
        json.dump(data,file)

def max_temperature(data, date):
    temperatures = []
    for item in data:
        if date == item[:8]:
            temperatures.append(data[item]["t"])

    return max(temperatures) if len(temperatures) else None


def min_temperature(data, date):
    temperatures = []
    for item in data:
        if date == item[:8]:
            temperatures.append(data[item]["t"])

    return min(temperatures) if len(temperatures) else None


def max_humidity(data, date):
    humidity = []
    for item in data:
        if date == item[:8]:
            humidity.append(data[item]["h"])

    return max(humidity) if len(humidity) else None


def min_humidity(data, date):
    humidity = []
    for item in data:
        if date == item[:8]:
            humidity.append(data[item]["h"])

    return min(humidity) if len(humidity) else None


def tot_rain(data, date):
    rainfalls = []
    for item in data:
        if date == item[:8]:
            rainfalls.append(data[item]["r"])

    return sum(rainfalls) if len(rainfalls) else None

def report_daily(data, date):
    display = '========================= DAILY REPORT ========================\n'
    display += 'Date                      Time  Temperature  Humidity  Rainfall\n'
    display += '====================  ========  ===========  ========  ========\n'

    for key in data:
        if date == key[0:8]:
            mdy = calendar.month_name[int(date[4:6])]+ ' ' + str(int(date[6:8])) + ', ' + str(int(date[0:4]))
            tm = key[8:10] + ':' + key[10:12] + ':' + key[12:14]
            t = data[key]['t']
            h = data[key]['h']
            r = data[key]['r']
            display = display + f'{mdy: <22}' + f'{tm: <10}' + f'{t: >11}' + f'{h: >10}' + f'{r: >10}\n'
    
    return display

def report_historical(data):
    display =  '============================== HISTORICAL REPORT ===========================\n'
    display += '                          Minimum      Maximum   Minumum   Maximum     Total\n'
    display += 'Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\n'
    display += '====================  ===========  ===========  ========  ========  ========\n'
    temp = None
    for key in data:
        date = key[0:8]
        if temp == date:
            continue
        m = (
            calendar.month_name[int(date[4:6])]
            + " "
            + str(int(date[6:8]))
            + ", "
            + str(int(date[0:4]))
        )
        min_t = min_temperature(data, date)
        max_t = max_temperature(data, date)
        min_h = min_humidity(data, date)
        max_h = max_humidity(data, date)
        total_r = tot_rain(data, date)
        display += f"{m:20}{min_t:13}{max_t:13}{min_h:10}{max_h:10}{total_r:10.2f}\n"
        temp = date
    return display