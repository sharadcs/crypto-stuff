import math

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

#computes a^b (mod n)
def modexp(a,b,n):
    ans = 1
    powers = [a]
    max_power = int(math.log10(b)/math.log10(2))

    #generate subsequent squares of a
    for i in range(1,max_power+1):
        powers.append((powers[i-1]*powers[i-1])%n)

    #caculate exponent mod n using b in binary
    while(b != 0):
        max_power = int(math.log10(b)/math.log10(2))
        ans = ans*powers[max_power]%n
        b -= int(math.pow(2,max_power))
    
    print(ans)
    return(ans)

'''n = 718548065973745507 

e = 3449
d = 543546506135745129

exp = (e*d - 1)/4

x = modexp(2,exp,n)
y = modexp(3,exp,n)

[p,r,s] = GCD(n,x-y)
[q,t,u] = GCD(n,x+y)

print(p%n)
print(q%n)

print((p*q) % n)'''


'''n = 537069139875071

x = 85975324443166
y = 462436106261

GCD(n,x-y)
GCD(n,x+y)'''

'''n = 670726081

x = 33335
y = 670705093

GCD(n,x-y)
GCD(n,x+y)'''

m1 = 2469247531693
m2 = 11111502225583
m3 = 44444222221411

m = m1*m2*m3

a1 = 359335245251
a2 = 10436363975495
a3 = 5135984059593

z1 = m2*m3
y1 = GCD(z1%m1,m1)[1]%m1

z2 = m1*m3
y2 = GCD(z2%m2,m2)[1]%m2

z3 = m1*m2
y3 = GCD(z3%m3,m3)[1]%m3

x = (a1*z1*y1 + a2*z2*y2 + a3*z3*y3)%(m)
print(x)
