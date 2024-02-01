def HCF(a, b):
    hcf = min(a, b)
    while hcf <= min(a, b):
        if a % hcf == 0 and b % hcf == 0:
            return hcf
        hcf = hcf-1
def LCM(a, b):
    return a*b//HCF(a,b)

choice = "y"
while choice == "y":
    a = int(input("Enter int 1: "))
    b = int(input("Enter int 2: "))

    print(f"The HCF of {a} and {b} is {HCF(a, b)}.")
    print(f"The LCM of {a} and {b} is {LCM(a, b)}.")

    choice = input("Type y to continue?\nResponse: ")
        
