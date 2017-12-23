def b():
    print("First eqaution:")
    a1 = input("a1 = ")
    b1 = input("b1 = ")
    c1 = input("c1 = ")
    print("\n")
    print("{ "+str(a1)+"x + "+str(b1)+" = "+str(c1))
    xpro = (c1 - b1)
    x = xpro/a1
    print("\n")
    print("x = "+str(x))
def bb():
    print("First equation:")
    a1 = input("a1 = ")
    b1 = input("b1 = ")
    c1 = input("c1 = ")
    print("Second equation:")
    a2 = input("a2 = ")
    b2 = input("b2 = ")
    c2 = input("c2 = ")
    print("\n")
    print("{ "+str(a1)+"x + "+str(b1)+"y = "+str(c1))
    print("{ "+str(a2)+"x + "+str(b2)+"y = "+str(c2))
    ypro = (c2*a1)-(c1*a2)
    y = ypro/((b2*a1)-(b1*a2))
    xpro = c1-(b1*y)
    x = xpro/a1
    print("\n")
    print("x = "+str(x))
    print("y = "+str(y))
def bbb():
    print("First equation:")
    a1 = input("a1 = ")
    b1 = input("b1 = ")
    c1 = input("c1 = ")
    d1 = input("d1 = ")
    print("Second equation:")
    a2 = input("a2 = ")
    b2 = input("b2 = ")
    c2 = input("c2 = ")
    d2 = input("d2 = ")
    print("Third equation")
    a3 = input("a3 = ")
    b3 = input("b3 = ")
    c3 = input("c3 = ")
    d3 = input("d3 = ")
    print("\n")
    print("{ "+str(a1)+"x + "+str(b1)+"y + "+str(c1)+"z = "+str(d1))
    print("{ "+str(a2)+"x + "+str(b2)+"y + "+str(c2)+"z = "+str(d2))
    print("{ "+str(a3)+"x + "+str(b3)+"y + "+str(c3)+"z = "+str(d3))

    zpro = ((d3*a2*b2*a1)-(d3*a2*b1*a2)-(d2*a3*b2*a1)+(d2*a3*b1*a2)-(d2*a1*b3*a2)+(d2*a1*b2*a3)+(d1*a2*b3*a2)-(d1*a2*b2*a3))
    z = zpro/((c3*a2*b2*a1)-(c3*a2*b1*a2)-(c2*a3*b2*a1)+(c2*a3*b1*a2)-(c2*a1*b3*a2)+(c2*a1*b2*a3)+(c1*a2*b3*a2)-(c1*a2*b2*a3))
    ypro = (d2*a1)-(c2*a1*z)-(d1*a2)+(c1*a2*z)
    y = ypro/((b2*a1)-(b1*a2))
    xpro = d3-(b3*y)-(c3*z)
    x = xpro/(a3)
    print("\n")
    print("x = "+str(x))
    print("y = "+str(y))
    print("z = "+str(z))
def is_prime(a):
    par = 0
    ter = 2
    while(True):
        if(ter*ter>=a):
            break
        if(a%ter == 0):
            par = 1
            break
        ter += 1
    if(par == 0):
        return 1;
    else:
        return 0
def prime(b):
    for i in range(b):
        if(is_prime(i) == 1):
            print(str(i)+"\n")
