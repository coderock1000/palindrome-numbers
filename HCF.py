num_largest = int(input('enter largest number : '))
num_smallest = int(input('enter smallest number : '))

while(num_smallest):
    num_Store = num_smallest
    num_smallest = num_largest % num_smallest
    num_largest = num_Store

print("HCF is : ", num_largest)