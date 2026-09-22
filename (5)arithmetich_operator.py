### Arithmetic Operators

students = 5
# students = students + 1 # addition
# students += 1
# students = students - 1 # subtraction
# students -= 1 
# students = students * 2 # multiplication
# students *= 2
# students = students / 2 # division
# students /= 2
# student = students // 2 # floor division
# students //= 2
# students = students ** 2 # exponentiation
# students **= 2
# students = students % 2 # modulus
# students %= 2

# print(f"yo're students is {students}")


### some built-in functions that can be used with numbers
x = 3.14
y = -6
z = 5

# result = round(x) # rounds to the nearest integer
# result = abs(y) # returns the absolute value of a number
# result = pow(z, 3) # raises z to the power of 3
# result = max(x, y, z) 
result = min(x, y, z)

# print(f"the result is {result}")
 
 
### continue with the math module
import math 

x = 9.9

# print(math.pi) 
# print(math.e)
# result2 = math.sqrt(x)
# result2 = math.ceil(x) # will round up to the nearest integer
# result2 = math.floor(x) # will round down to the nearest integer

# print(result2)


### calculating of circle circumference and area
radius = 10.5
circumference = 2 * math.pi * radius
# print(f"the circumference of a circle with radius {radius} is = {round(circumference, 2)}cm²")

area = math.pi * pow(radius, 2)
# print(f"the area of a circle with radius {radius} is = {round(area, 2)}cm²") 


### hypotenuse of a right triangle
a = 3
b = 4

c = math.sqrt(pow(a, 2) + pow(b, 2)) # returns the hypotenuse of a right triangle
result3 = math.hypot(a, b) # returns the hypotenuse of a right triangle
# print(f"the hypotenuse of a right triangle with sides {a} and {b} is = {result3}")

