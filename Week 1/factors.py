def fac(num):
    factors = []
    i = 1
    while i<num:
        if num%i == 0:
            factors.append(i)
        i+=1
    return factors

def prime(num):
    i = 2
    while i < num:
        if num%i == 0:
            return False
        i += 1
    return True

choice = "y"
while True:
    num = int(input("Give a number: "))
    print(f"Factors: {fac(num)}")
    print(f"Is Prime? {prime(num)}")
    choice = input("Do you wish to continue? ")
    if choice!="y":
        exit()