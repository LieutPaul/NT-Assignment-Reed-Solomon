import gmpy2
from gmpy2 import mpz
gmpy2.set_context(gmpy2.context())

def egcd(a,b):
    
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

print(egcd(mpz(962),mpz(104)))
        

