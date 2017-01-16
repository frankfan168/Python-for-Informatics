"""
Exercise 2.5 Write a program which prompts the user for a Celsius temperature, 
convert the temperature to Fahrenheit, and print out the converted temperature.
"""

temperature = float(raw_input('Please input a Celsius temperature: \n'))
F = temperature * 1.8 + 32
print "Temperature in Fahr: %.2f" %F