import random as rn

N = 20
numb = []

for _ in range(N):
    
    numb.append(rn.randint(0,10))

def is_even(x):
    return x % 2 == 0

numbers = [1,2,5,3,8,9,10,3,6,7,4,4]

even_numbers = list(filter(is_even, numbers))

print(numbers)
print(even_numbers)

print()

even_numbers = list(filter(is_even, numb))

print(numb)
print(even_numbers)