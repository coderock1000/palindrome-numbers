num = int(input('enter your number: '))

org_num = num
reversed_number = 0

while num > 0:
    digit = num % 10
    reversed_number = reversed_number * 10 + digit
    num //= 10

if org_num == reversed_number:
    print(f'{org_num} is a palindrome.')
else:
    print(f'{org_num} is not a palindrome.')

    