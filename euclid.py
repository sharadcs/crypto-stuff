def GCD(a,b):

    x = [0,1]
    y = [1,0]

    if(a < b):
        r = a
        a = b
        b = r

    while(b != 0):
        q,r = divmod(a,b)
        a = b
        b = r
        x.append(-q*x[len(x)-1] + x[len(x)-2])
        y.append(-q*y[len(y)-1] + y[len(y)-2])

    print a,x[len(x)-2],y[len(y)-2]
    return a,x[len(x)-2],y[len(y)-2]


GCD(642401,422246)

''' m1 = 101
m2 = 201
m3 = 301

m = m1*m2*m3

a1 = 17
a2 = 18
a3 = 19

z1 = m2*m3
y1 = GCD(z1%m1,m1)[1]%m1

z2 = m1*m3
y2 = GCD(z2%m2,m2)[1]%m2

z3 = m1*m2
y3 = GCD(z3%m3,m3)[1]%m3

x = (a1*z1*y1 + a2*z2*y2 + a3*z3*y3)%(m)
print(x)'''
