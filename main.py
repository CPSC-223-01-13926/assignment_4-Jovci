from weather import *


# file1 = "weather.dat"
filename = "w.dat"
weather = read_data(filename)
mychoice = 0

while True:
    print("      *** TUFFY TITAN WEATHER LOGGER MAIN MENU\n")
    print("1. Set data filename")
    print("2. Add weather data")
    print("3. Print daily report")
    print("4. Print historical report")
    print("9. Exit the program")

    mychoice = int(input("Enter menu choice: "))
    print()

    if mychoice == 1:
        myfile = input("Enter data filename: ")
        # weather = read_data(myfile)
        filename = myfile

    elif mychoice == 2:
        dt = input("Enter date (YYYYMMDD): ")
        tm = input("Enter time (hhmmss): ")
        t = int(input("Enter temperature: "))
        h = int(input("Enter humidity: "))
        r = float(input("Enter rainfall: "))
        weather[dt + tm] = {"t": t, "h": h, "r": r}
        # write_data(weather, myfile)
        write_data(weather, filename)

    elif mychoice == 3:
        d = input("Enter data: ")
        display = report_daily(weather, d)
        print(display)

    elif mychoice == 4:
        display = report_historical(weather)
        print(display)

    elif mychoice == 9:
        break
