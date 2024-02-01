def prime(num):
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True

def primeBelow(num):
    primeNumbers = [1]
    i = 2
    while i < num:
        if prime(i) == True:
            primeNumbers.append(i)
        i += 1
    return primeNumbers

primes = []
def tillPrime(num):
    count = 0
    i = 1
    while count < num:
        if prime(i) ==  True:
            primes.append(i)
            count+=1
        i+=1
    return primes
        
def thatPrime(index):
    list = tillPrime(index+1)
    return list[index]

print(f"The prime number at the provided index is {thatPrime(int(input("Enter a number to check prime below that: ")))}")