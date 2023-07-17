import math
print("Creator = Okmeque1")
n = int(input("Enter the maximum number to calculate primes : "))
count_of_primes = 0

for num in range(2, n):
    is_prime = True
    for factor in range(2, int(math.sqrt(num))+1):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        count_of_primes += 1
        
print(f"The number of prime numbers between 2 and {n} is {count_of_primes}")
