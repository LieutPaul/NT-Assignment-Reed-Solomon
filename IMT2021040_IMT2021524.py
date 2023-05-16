from gmpy2 import mpz,mpq
import random
from math import floor

def binary_egcd(a,b):
    
    r = mpz(a)
    r_d = mpz(b)
    e = mpz(0)
    
    while (((r % 2) == 0) and ((r_d % 2) == 0)):
        r = r >> 1
        r_d = r_d >> 1
        e += 1
    
    a_t = r
    b_t = r_d
    s,t,s_d,t_d = mpz(1),mpz(0),mpz(0),mpz(1)
    
    while (r_d != 0):
        
        while((r % 2) == 0):
            r = r >> 1
            if ((s % 2) == 0 and ((t % 2) == 0)):
                s = s >> 1
                t = t >> 1
            else:
                s = (s + b_t) >> 1
                t = (t - a_t) >> 1
        
        while((r_d % 2) == 0):
            r_d = r_d >> 1
            if (((s_d % 2) == 0) and ((t_d % 2) == 0)):
                s_d = s_d >> 1
                t_d = t_d >> 1
            else:
                s_d = (s_d + b_t) >> 1
                t_d = (t_d - a_t) >> 1

        if(r_d < r):
            r, s, t, r_d, s_d, t_d = r_d, s_d, t_d, r, s, t
        
        r_d = r_d - r
        s_d = s_d - s
        t_d = t_d - t
    
    d = ((1 << e) * r)
    return (d,s,t)


def egcd(a,b,r_star):
    r = mpz(a)
    r_d = mpz(b)
    s, s_d, t, t_d = mpz(1), mpz(0), mpz(0), mpz(1)
    while(r_d != 0):
        q = mpz(r // r_d)
        r_dd = mpz(r % r_d)
        r, s, t, r_d, s_d, t_d = r_d, s_d, t_d, r_dd, mpz(s - (s_d * q)), mpz(t - (t_d * q))
        if(r < r_star):
            return r,s,t
    d = mpz(r)
    return d, s, t

def CRT(a,n):
    
    x, N = mpz(0), mpz(1)
    
    for i in n:
        N *= i
    
    for i in range(len(n)):
        
        N_k = mpz(N // n[i])
        (d, x_k, t) = binary_egcd(N_k,n[i])
        
        if(d != mpz(1)):
            x = mpz(-1)
            break
        
        x += mpz( mpz(a[i] * N_k * x_k) % mpz(N) )
    
    return mpz(x)

def GlobalSetup(mu,M):
    l=[] #This is the list of primes
    i=mpz(2)
    product_of_primes = mpz(1)
    found = False
    while(i<M):
        ni = mpz(i)
        if(ni.is_prime()):
            product_of_primes *= i
            l.append(ni)
            L = mpz(floor(mu*mpz(len(l))))
            P = mpz(1)
            for j in range(L):
                P *= l[-j - 1]
            if(product_of_primes > 2 * M * P * P):
                found = True
                break
        i = i + 1
    if found:
        return l
    else:
        return []

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

def ReedSolomonSend(a,l,mu):
    msglist = [] # List of ai's
    am = mpz(a)
    for i in range(len(l)):
        msglist.append(mpz(am%l[i]))
    return Transmit(len(l),l,msglist,mu) 

def ReedSolomonReceive(msglist, n, M, mu):
    P = mpz(1)
    for i in range(floor(mu*mpz(len(n)))):
        P *= n[-i-1]
    r_star = M * P 
    b = CRT(msglist,n)
    product_of_n = mpz(1)
    for i in n:
        product_of_n *= i    
    r,s,t = egcd(product_of_n,b,r_star)
    if(r%t==0):
        return mpz(r//t)
    else:
        return "ERROR"

mu = mpq(3,10)
M = mpz(10000001)
a = mpz(9999999)
l = GlobalSetup(mu,M) # l is the list of primes
print(l)
b = ReedSolomonSend(a,l,mu)
print(b)
print(ReedSolomonReceive(b,l,M,mu))
