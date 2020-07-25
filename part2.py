rnumbers = []


def rng(seed, a, c, modulo, iter):
    """
    This function generates a list of random numbers of length 'iter'
    We get the correct first three random numbers
    """
    exit_lst = []
    for i in range(int(iter)):
        seed = (a * seed + c) % modulo
        exit_lst.append(seed / modulo)

    return exit_lst


# print(rng(1000, 24693, 3967, 2**15, 3))


# Discrete Random Variable for availability:
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

import math
import statistics


def expo_variable(random_number):
    # this is the function responsbile for picking the random variable X, which describes the probability that the customer will come and pick up within X seconds
    # Essentially, this function takes in a probability and returns the X associated with it, basically an inverse CDF.

    """
    Random Variable X describing the number of seconds it takes for customer to pick up the phone
    1/lambda = 12
    FX(x) = 1 - e^(-1/12 * x)
    F_X^-1(x) = -12*ln(1-x)
    """

    return -12 * (math.log(1 - random_number))


"""
testing the expo_variable function
Test by realizing a known probability P(X <= x)
We know that P(X <= 20) = 0.8111243972, so inputting 0.8111243972, we should expect an X close to 20
running the following line: 
print(expo_variable(0.8111243972))
20.000000002386447 prints to console
Pretty darn close.
Extra testing code: 
p = rng(1000, 24693, 3967, 2**15, 1000)
testlist = []
for i in p[500:]:
    testlist.append(expo_variable(i))
print(statistics.mean(testlist))
"""


def phone_time(availability, random_seed):
    """
    Returns the phone time for each possible outcome
    :param availability: 0, 1, or 2, each having the meaning detailed above
    :param random_seed: a random number to determine how long a person will take to answer, if applicable
    :return: the call time for the salesperson, including hanging up and dialing
    """
    if availability == 2:
        time = expo_variable(random_seed)
        if time < 25:
            return time + 6
        else:
            return 32
    elif availability == 1:
        return 10
    else:
        return 32


def main(reps):
    """
    Returns a simulation of call times for reps number of people.  The salesperson calls up to 4 times and the total
    times are aggregated.  Max is 128 (doesn't pick up all 4 times), min is 6 (picks up right away)
    :param reps: number of trials desired
    :return: a list of call times
    """
    randoms = rng(1000, 24693, 3967, 2**15, reps*2)  # random variables for the availability and for the time seeds
    avail = randoms[0:reps]
    times = randoms[reps:reps*2]
    total_times = []
    incomplete_times = [0]*reps

    for i in range(4):  # represents the four times the telemarketer calls
        availability = []
        for m in range(len(incomplete_times)):  # determines the availability of the decreasing # of people
            availability.append(availability_Vargenerator(avail[m]))
        for j in range(len(availability)):  # determines the time for each call
            time = phone_time(availability[j], times[j])
            incomplete_times[j] += time  # adds each new time to the previous times
            if availability[j] == 2 and time <= 31:
                total_times.append(incomplete_times[j]) # if the person answers, add it to total times
        for k in total_times:
            if k in incomplete_times:
                incomplete_times.remove(k)  # delete all items just added to total times--they're no longer incomplete
    for i in incomplete_times:
        total_times.append(i)  # at the end, add all the leftovers (the ones they never reached)
    return total_times


print(main(500))
