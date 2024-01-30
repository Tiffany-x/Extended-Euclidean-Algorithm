def comp_gcd(vala, valb):
    if vala == 0:
        return valb, 0, 1
    else:
        gcd, x1, y1 = comp_gcd(valb % vala, vala)
        x = y1 - (valb // vala) * x1
        y = x1
    return gcd, x, y
