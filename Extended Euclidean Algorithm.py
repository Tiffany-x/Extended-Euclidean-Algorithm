def comp_gcd(vala, valb):
    if vala == 0:
        return valb, 0, 1
    else:
        gcd, x1, y1 = comp_gcd(valb % vala, vala)
        x = y1 - (valb // vala) * x1
        y = x1
    return gcd, x, y

print("Finding the GCD(a, b) and Bezouts coefficients")

print("Enter the value of a: ")
a = int(input())
print("Enter the value of b: ")
b = int(input())
print(comp_gcd(a, b))
