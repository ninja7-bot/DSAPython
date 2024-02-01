def HCF(a, b):
    hcf = a
    while hcf <= a:
        if hcf % a == 0 and hcf % b == 0:
            print(f"{hcf} divides both {a} and {b}.")
            hcf = hcf
        else:
            hcf-1
    return hcf

x = 12
y = 18
print(f"The HCF of {x} and {y} is {HCF(x, y)}.")
