#implementing the Euclidean Algorithm

def comp_gcd(vala, valb):
    if valb == 0:
        return vala
    else:
        return comp_gcd(valb, vala % valb)

print("Finding the GCD(a, b)")

print("Enter the value of a: ")
a = int(input())
print("Enter the value of b: ")
b = int(input())
print(comp_gcd(a, b))
