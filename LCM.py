def find_lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if greater % a == 0 and greater % b == 0:
            lcom = greater
            break
        greater += 1

    return lcom

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("LCM of", num1, "and", num2, "is:", find_lcm(num1, num2))
