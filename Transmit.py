import gmpy2
import random

from gmpy2 import mpz,mpq,mpfr,mpc

gmpy2.set_context(gmpy2.context())

def Transmit(k,n,a,myu):
    
    b = []

    l = mpz(random.randint(1,mpz(myu*k))) # mpz(myu,k) will turn it into an integer
    
    I = [] # I is the set of bad indices
    
    for i in range(0,l):
        x = mpz(random.randint(1,k))
        while x in I: #To generate a unique 'bad' index
            x = mpz(random.randint(1,k))
        I.append(x)
    
    for i in range(1,k+1):
        if i in I:
            x = mpz(random.randint(0,n[i-1]-1))
            while(x == a[i-1]): # To ensure b[i] != a[i]
                x = mpz(random.randint(0,n[i-1]-1))
            b.append(x)
        else:
            b.append(a[i-1])
    
    return b

n = [mpz(11),mpz(13),mpz(17),mpz(19),mpz(23),mpz(29)]
a = [mpz(8),mpz(2),mpz(6),mpz(7),mpz(12),mpz(19)]
myu = mpq(2,3)
k = mpz(6)

print(Transmit(k,n,a,myu))