# Number Theory (SM-404) Assignment 
## Reed Solomon Error Correction

Submission by Vikas K (IMT2021040) and Barath S Narayan(IMT2021524)

- There is a message (a) which needs to be transmitted from a sender to a receiver. It is given that a < M.
- The message is transmitted by calculating the residue (remainder) obtained by dividing 'a' by a sequence of prime numbers n1, n2, .. nk. These residues are transmitted to the receiver.
- However, there is a corruption rate 'myu' while transmitting the residues. This means that at most myu * k residues can be transmitted incorrectly.
- The algorithm allows the receiver to successfully reconstruct the message 'a' from the transmitted messages, by using the rational reconstruction method, given that the primes chosen, M and myu satisfy a specific condition.

Note: The IMT2021040_IMT2021524.ipynb file contains the entire algorithm and all the other files were used to debug individual blocks of code.


