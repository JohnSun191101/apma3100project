# """
# (from wikipedia) 
# """


# def lcg(modulus, a, c, seed):
#     """Linear congruential generator."""
#     for i in range(3):
#         seed = (a * seed + c) % modulus
#         yield seed


rnumbers = []

def rng(seed, a, c, modulo, iter):
    exit_lst = []
    for i in range(int(iter)):
        seed = (a*seed + c) % modulo
        exit_lst.append(seed / modulo)
    
    return exit_lst

rnumbers = rng(1000, 24693, 3967, 2**15, 3)

print(rnumbers)

def iterator(random_number):
    global w 

    w = 0

    w += 6

    if random_number < 0.2:
        w += 4 
        #case where line is busy
    
    elif random_number < 0.3:
        w += 26 
        #case where customer is out of the office

    elif random_number < 0.5:
        #case where customer is at desk
        










