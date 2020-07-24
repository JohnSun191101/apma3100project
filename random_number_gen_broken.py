
rnumbers = []

def rng(seed, a, c, modulo, iter):
    """
    This function generates a list of random numbers of length 'iter'
    We get the correct first three random numbers
    """
    exit_lst = []
    for i in range(int(iter)):
        seed = (a*seed + c) % modulo
        exit_lst.append(seed / modulo)
    
    return exit_lst

print(rng(1000, 24693, 3967, 2**15, 3))



#Discrete Random Variable for availability: 
# x = 0: customer unavailable 
# x = 1: customer is using the line 
# x = 2: customer is available for call
# F_X(x): 
#   0, x < 0
#   0.3, 0 <= x < 1 
#   0.5, 1 <= x < 2 
#   1, X >= 2 

def availability_Vargenerator(u_1):
    """
    parameter is a random number between zero and 1
    this function is a discrete random variable generator, as defined by the project appendix page 4
    """
    if u_1 > 0.5: 
        return 2 
    elif u_1 <= 0.5 and u_1 > 0.3:
        return 1 
    elif u_1 <= 0.3: 
        return 0 


"""
testing the availability_Vargenerator function

rnumbers = rng(1000, 24693, 3967, 2**15, 10000)

x_list = []
for i in rnumbers: 
    x_list.append(availability_Vargenerator(u_1 = i))
    # print(availability_Vargenerator(i))

onelist = []
twolist = []
zerolist = []

for i in x_list:
    if i == 2:
        twolist.append(i)
    if i == 1: 
        onelist.append(i)
    if i == 0:
        zerolist.append(i)

print('Prop 0:', len(zerolist) / len(x_list))
print('Prop 1:', len(onelist) / len(x_list))
print('Prop 2:', len(twolist) / len(x_list))

running these lines will generate 10,000 realizations of the random variable X for availability. 
It will also print the proportion of zeroes, ones, and twos among those 10,000 realized random variables. 
Running these lines will print the following to console: 

Prop 0: 0.3009
Prop 1: 0.2044
Prop 2: 0.4947

This distribution is pretty darn close to the PMF of X measuring availability.
"""

def expo_variable(random_number):
    #this is the function responsbile for picking the random variable X, which describes the probability that the customer will come and pick up within X minutes

    """
    1/lambda = 12 
    FX(x) = 
    """


# def iterator(random_number):
#     global w 

#     w = 0

#     w += 6

#     if random_number < 0.2:
#         w += 4 
#         #case where line is busy
    
#     elif random_number < 0.3:
#         w += 26 
#         #case where customer is out of the office

#     elif random_number < 0.5:
#         #case where customer is at desk
        










