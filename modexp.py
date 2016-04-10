import math

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

modexp(2,10203,101)

