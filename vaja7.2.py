u = int(input("Vnesi stevilo ur: "))
m = int(input("Vnesi stevilo minut: "))

if m > 30:
    st1 = 60 - m
    u = u + 1
    print("Ura je " + str(st1) + " minut do " + str(u))
elif 30 > m > 1:
    print("Ura je " + str(m) + " minut cez " + str(u))
elif m == 30:
    u = u + 1
    print("Ura je pol " + str(u))
if m == 00:
    print("Ura je " + str(u))

