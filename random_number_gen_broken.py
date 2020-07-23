

def rng(seed, a, c, modulo, iter):
    for i in range(int(iter)):
        seed = (a*seed + c) % modulo
        print(seed / modulo)



rng(1000,24693,3967,2**15,3)

"""
(from wikipedia) 
"""


def lcg(modulus, a, c, seed):
    """Linear congruential generator."""
    for i in range(3):
        seed = (a * seed + c) % modulus
        yield seed

