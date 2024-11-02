from math import gcd

def find_lcm(a, b):
    return abs(a * b) // gcd(a, b)

def find_lcm_multiple(numbers):
    lcm = numbers[0]
    for num in numbers[1:]:
        lcm = find_lcm(lcm, num)
    return lcm

count = int(input("Enter the number of values: "))
numbers = []

for i in range(count):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

print("LCM of the numbers is:", find_lcm_multiple(numbers))
