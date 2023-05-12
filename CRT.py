import gmpy2

from gmpy2 import mpz

gmpy2.set_context(gmpy2.context())

from GCD import binary_egcd

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