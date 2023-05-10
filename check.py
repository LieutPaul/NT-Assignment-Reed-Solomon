# Do pip3 install gmpy2

import gmpy2

from gmpy2 import mpz,mpq,mpfr,mpc

gmpy2.set_context(gmpy2.context())

a = mpz(int(input("Enter number: ")))
# b = mpz(int(input("Enter number: ")))
c = mpq(float(input("Enter float: ")))

print(mpz(a * mpq(2,4)))