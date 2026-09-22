# input() = is a function that allows user to input a value and store it in a variable

print('entering personal identity')
name = input('whats is your name: ')
age = int(input('how old are u: '))

age += 2

print(f"hello {name}, nice to meet u!, yo're {age} years old, right?") 

# firts exercise, rectangle area calc
print('\nentering rectangle area calc')
lenght = float(input('enter the lenght: '))
widht = float(input('enter the widht: '))

area = lenght * widht

print(f"the area of the rectangle is: {area}")

# second axercise, shoping cart
print('\nentering shoping cart')

item =  input("whats's item would u like to buy: ")
price = float(input(f"enter the price: "))
quantity = int(input('how many would u like to buy: '))
total = price * quantity

print(f"hi bro, u've bought {item} X {quantity}")
print(f"the total price is: {total}")