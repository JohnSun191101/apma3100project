"""
random number generator (linear congruential random number generator) This one doesn't work (doesn't generate the correct first three random numbers)
"""

def rng(seed, a, c, modulo, iter):
    for i in range(int(iter)):
        seed = (a*seed + c) % modulo
        print(seed)



rng(1000,24693,3967,2**15,3)

"""
This one doesn't work either (doesn't generate the correct first three random numbers) (from wikipedia) 
"""


def lcg(modulus, a, c, seed):
    """Linear congruential generator."""
    for i in range(3):
        seed = (a * seed + c) % modulus
        yield seed


""" 
parameters from project


definition of a linear congruential random number generator: 
𝑥𝑖=(𝑎 𝑥𝑖−1+𝑐)(𝑚𝑜𝑑𝑢𝑙𝑜 𝐾), (1a)
𝑢𝑖=𝑑𝑒𝑐𝑖𝑚𝑎𝑙 𝑟𝑒𝑝𝑟𝑒𝑠𝑒𝑛𝑡𝑎𝑡𝑖𝑜𝑛 𝑜𝑓 𝑥𝑖/𝐾, (1b)

starting value (seed) 𝑥0=1000,
multiplier 𝑎=24,693,
increment 𝑐=3967,
modulus 𝐾=215.

They yield the cycle of length 𝐾=213. The first three random numbers are 0.9303,0.2703,
0.6205.


"""