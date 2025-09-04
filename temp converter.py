# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 21:08:45 2025

@author: Mritunjoy Paul
"""

def convert_temperature(temp, unit):
    
    
    if unit.upper() == 'F':  
        return round((temp - 32) * 5 / 9, 2)
    elif unit.upper() == 'C':
        return round((temp * 9 / 5) + 32, 2)
    else:
        return None  


temperature = float(input("Enter the temperature value: "))
unit = input("Enter the unit (F for Fahrenheit, C for Celsius): ")


result = convert_temperature(temperature, unit)

if result is not None:
    if unit.upper() == 'F':
        print(f"{temperature}°F is {result}°C")
    else:
        print(f"{temperature}°C is {result}°F")
else:
    print("Invalid unit entered! Please use 'F' or 'C'.")
