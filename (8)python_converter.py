### python weight converter

weight = float(input('enter ur weight: '))
unit = input("Kilogram or Pounds (K or L)? ").upper()

if unit == 'K':
    weight = weight * 2.205
    unit = 'lbs.'
    print(f"ur weight is {round(weight, 2)}{unit}")
elif unit == 'L':
    weight = weight / 2.205
    unit = 'Kgs.'
    print(f"ur weight is {round(weight, 2)}{unit}")
else:
    print('ur input is invalid!')
    


### temperature converter

unit2 = input("is the temperature celcius or fahrenhiet (C or F): ").upper()
temp = float(input('enter the temperature: '))

if unit2 == 'C':
    temp = temp * 9 / 5 + 32 
    print(f"the temperature in fahrenhiet is {round(temp, 1)} F")
elif unit2 == 'F':
    temp = (temp - 32) * 5 / 9
    print(f"the temperature in celcius is {round(temp, 1)} C")
else:
    print(f"{temp} is invalid temperature measurable")
