''' practice different math expressions and calculations.'''
import math

#declare num_a and num_b

num_a =  12
num_b =  5
radius = 7489
side_length = 10
a = 5
b = 4
c = 3
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
#8. Calculate discriminant

discriminant = b ** 2 - 4 * a * c
print("discriminant =", discriminant)

#9. Calculate hypotenuse length
side1 = 7
side2 = 3

hypotenuse = math.sqrt(side1 **2 + side2 ** 2)
print(hypotenuse)

#10. Calculate cathetus length

cathetus = math.sqrt(hypotenuse ** 2 - side1 ** 2)
print("cathetus =", cathetus)

#11. Time converter

seconds = 149032
minutes = seconds // 60
hours = minutes // 60

print(seconds,minutes,hours)

#12. Student helper

angle = 67
sine = round(math.sin(angle), 1)
cosine = round(math.cos(angle), 1)
print("sine = ", sine, "cosine = ", cosine)

#13. Greetings

n = 12
lots_of_heys = n * "hey"

#14. Adding numbers
string_numbers = str(num_a) + str(num_b)


print(20 % 3)
