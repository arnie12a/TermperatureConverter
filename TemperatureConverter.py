print("Would you like to convert from \n(1)Celcius to Fahrenheit\n(2)Fahrenheit to Celcius")
prompt = input()
if prompt == "1" or prompt.lower() == "one":
	print("What would you like to convert from Celcius to Fahrenheit")
	celcius = float(input())
	fahrenheit = (celcius * (9.0/5.0)) + 32
	fahrenheit = round(fahrenheit, 3)
	print(str(celcius) + "°C in fahrenheit is " +  str(fahrenheit) + "°F")

elif prompt == "2" or prompt.lower() == "two":
	print("What would you like to convert from Fahrenheit to Celcius")
	fahrenheit = float(input())
	celcius = (fahrenheit-32) * (5.0/9.0)
	celcius = round(celcius, 3)
	print(str(fahrenheit) + "°F in celcius is " + str(celcius) + "°C")
else:
	print("Invalid Input")
