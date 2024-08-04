import sys
def isPrime(num): 
    factors = []
    if num == 2:
        return True
    else:
        for i in range(1, num + 1):
            if (num % i == 0):
                factors.append(i)
    if len(factors) == 2:
        return True
    else:
        return False

numbers = [] 
primes = [] 

for i in range(1,11):
    numbers.append(int(sys.argv[i]))


for i in numbers: 
    if isPrime(i):
        primes.append(i)

print("\nSum of the prime numbers is: " + str(sum(primes)))

