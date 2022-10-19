''' practice different math expressions and calculations.'''
import math

#declare num_a and num_b

num_a =  12
num_b =  5
radius = 7489
side_length = 10
#1. Sum and difference

sum = num_a + num_b
difference = num_a - num_b
print(f"{num_a} + {num_b} = {sum}")
print(f"{num_a} - {num_b} = {difference}")

#2. Float division
division = num_a / num_b

#3. Integer division
division2 = num_a // num_b

#4. Powerful operations

multiply_numbers = num_a * num_b
power = num_a ** num_b
remainder = num_a % num_b

#5. Find average

average = (num_a + num_b) / 2

#6. Area of a circle
circle_area = radius ** 2 * math.pi
print(circle_area)

#7. Area of an equilateral triangle

triangle_area = round(math.sqrt(side_length ** 2 - (side_length / 2 ) ** 2) * side_length / 2)
print(triangle_area)
