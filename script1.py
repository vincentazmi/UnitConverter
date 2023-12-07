# print any unit of stuff in all other units

import csv, sys


def tryinput(string,start=0,end=0,aList=None):
    try:
        x = int(input(string)) if aList == None else input(string)
        if ((aList != None) and (x in aList)) or ((aList == None) and (not(x<start or x>end))): return x
        raise
    except: print("Please enter a valid input");return tryinput(string,start,end,aList)

def menu():
    u_input = tryinput("""
1) Weight
2) Distance/Lengths
3) Speed
4) Volume
5) Temperature
6) Exit Program
""",1,6)
    if u_input == 1:
        weight()
    elif u_input == 2:
        distance()
    elif u_input == 3:
        speed()
    elif u_input == 4:
        volume()
    elif u_input == 5:
        temp()
    elif u_input == 6:
        sys.exit(0)
    menu()

def weight():
    value = 0
    option = tryinput("""
1) Kilograms
2) Grams
3) Milligrams    
4) Ounce
5) Pound
6) Stone
7) Tonne
8) <-- Back
""",1,8)
    if option !=8:
        try:
            value = float(input("Enter value : "))
        except:
            print("Enter a number")
            return
    else:
        return
    if option == 8:
        return
    kgvalues = [value, value/1000, value/1000000, value/35.274, value/2.20462, value/0.157473, value/0.001]
    for i in range(option):
        kg = kgvalues[i]
    grams = round(kg*1000,2)
    milligrams = round(kg*1000000,2)
    ounce = round(kg*35.274,2)
    pound = round(kg*2.20462,2)
    stone = round(kg*0.157473,3)
    tonne = round(kg*0.001,3)
    printvalue(round(kg,2),"kg")
    printvalue(grams,"g")
    printvalue(milligrams,"mg")
    printvalue(ounce,"oz")
    printvalue(pound,"lb")
    printvalue(stone,"st")
    printvalue(tonne,"t")
    weight()

def distance():
    value = 0
    option = tryinput("""
1) Kilometers
2) Meters
3) Centimeters
4) Millimeters
5) Miles
6) Yards
7) Inches
8) <-- Back
""",1,8)
    if option !=8:
        try:
            value = float(input("Enter value : "))
        except:
            print("Enter a number")
            return
    else:
        return
    if option == 8:
        return
    kmvalues = [value, value/1000, value/100000, value/1000000, value/0.621371, value/1093.61, value/39370.1]
    for i in range(option):
        km = kmvalues[i]
    meters = round(km*1000,2)
    centimeters = round(km*100000,2)
    millimeters = round(km*1000000,2)
    miles = round(km*0.621371,2)
    yards = round(km*1093.61,2)
    inch = round(km*39370.1,2)
    printvalue(km,"km")
    printvalue(meters,"m")
    printvalue(centimeters,"cm")
    printvalue(millimeters,"mm")
    printvalue(miles,"mi")
    printvalue(yards,"yd")
    printvalue(inch,"in")
    distance()
    
def speed():
    value = 0
    option = tryinput("""
1) Kilometers/Hour
2) Miles/Hour
3) Meters/Second
4) Knots/Hour
5) Feet/Second
6) <-- Back
""",1,6)
    if option !=6:
        try:
            value = float(input("Enter value : "))
        except:
            print("Enter a number")
            return
    else:
        return
    if option == 6:
        return
    kmvalues = [value, value*1.60934, value*3.6, value*1.852, value*1.09728]
    for i in range(option):
        km = kmvalues[i]
    mph = round(km/1.60934,2)
    mps = round(km/3.6,3)
    knots = round(km/1.852,4)
    fts = round(km/1.09728,2)
    printvalue(km,"km/h")
    printvalue(mph,"mph")
    printvalue(mps,"m/s")
    printvalue(knots,"kn")
    printvalue(fts,"ft/s")
    speed()

def volume():
    value = 0
    option = tryinput("""
1) Kilometers³
2) Meters³
3) Foot³
4) Gallons
5) Litres
6) Pints
7) Inch³
8) <-- Back
""",1,8)
    if option !=8:
        try:
            value = float(input("Enter value : "))
        except:
            print("Enter a number")
            return
    else:
        return
    if option == 8:
        return
    kmvalues = [value, value/1000000000, value/35314666721.489, value/264172052358.15, value/1000000000000, value/1759753986392.7, value/61023744094732]
    for i in range(option):
        km = kmvalues[i]
    m = round(km*1000000000,2)
    ft = round(km*35314666721.489,2)
    g = round(km*264172052358.15,2)
    l = round(km*1000000000000,2)
    p = round(km*1759753986392.7,2)
    inch = km*61023744094732
    printvalue(round(km,2),"km³")
    printvalue(m,"m³")
    printvalue(ft,"ft³")
    printvalue(g,"gallons")
    printvalue(l,"L")
    printvalue(p,"pints")
    printvalue(inch,"inch³")
    volume()

def temp():
    value = 0
    option = tryinput("""
1) Celcius 
2) Fahrenheit
3) Kelvin
4) <-- Back
""",1,4)
    if option !=4:
        try:
            value = float(input("Enter value : "))
        except:
            print("Enter a number")
            return
    else:
        return
    if option == 4:
        return
    cvalues = [value, ((value - 32)*5/9), (value - 273.15)]
    for i in range(option):
        c = cvalues[i]
    f = ((c * 9/5) + 32)
    k = (c + 273.15)
    printvalue(c,"°C")
    printvalue(f,"°F")
    printvalue(k,"K")
    temp()
    
def printvalue(value,unit):
    print(str(value)+" "+unit)

menu()
