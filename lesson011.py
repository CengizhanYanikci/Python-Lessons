import random

# seed()        - Initialize the random number generator
# getstate()    - Returns the current internal state of the random number generator
# setstate()    - Restores the internal state of the random number generator
# getrandbits() - Returns a number representing the random bits
# randrange()   - Returns a random number between the given range
# randint()     - Returns a random number between the given range
# choice()      - Returns a random element from the given sequence
# choices()     - Returns a list with a random selection from the given sequence
# shuffle()     - Takes a sequence and returns the sequence in a random order
# sample()      - Returns a given sample of a sequence
# random()      - Returns a random float number between 0 and 1
# uniform()     - Returns a random float number between two given parameters
# triangular()  - Returns a random float number between two given parameters, you can also set a mode parameter to





# <-------DELETE------  random.seed(7)     
# After running this code, comment it out again, because you might get the wrong idea when learning some commands. 
# For example, the range function always produces the same values when random.seed is active.

print(random.random())  
# Prints a random float number between 0.0 and 1.0

#--------------------------------------------
print("--------------GET&SET-------------")
#--------------------------------------------
print(random.random())  
# Prints another random float number between 0.0 and 1.0

#--------------------------------------------
state = random.getstate()  
# Saves the current internal state of the random number generator to the variable 'state'

print(random.random())  
# Prints a new random float number; generator state has advanced

#--------------------------------------------
random.setstate(state)  
# Restores the random number generator to the previously saved state

print(random.random())  
# Prints the same number as the one after saving state, because the state was restored

#--------------------------------------------
print(random.getrandbits(12))  
# Generates a random integer using 12 random bits (range: 0 to 4095)

#--------------------------------------------
print(random.randrange(1, 10))  
# Prints a random integer from 1 to 9 (start included, stop excluded)

#--------------------------------------------
print(random.randint(1, 10))  
# Prints a random integer from 1 to 10 (both start and stop included)

#--------------------------------------------
