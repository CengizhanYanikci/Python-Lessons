import random

# Select a random element from a list
myList = ["Banana","Pineapple","Melon","Berry","Barry Allen",]
print(random.choice(myList))

#----------------------------------------

# Pick a random character from a string 
text = "Barry Allen is Savitas".replace(" ", "")
print(random.choice(text))

#----------------------------------------

# Select multiple random elements from a list with given weights
# k=30 means it will return a list of 30 randomly chosen items
myList = ["Banana","Pineapple","Melon","Berry","Barry Allen",]
print(random.choices(myList, weights=[5,1,2,6,8], k=30))

#----------------------------------------

# Shuffle the list in place (randomly reorder elements)
myList = ["Banana","Pineapple","Melon","Berry","Barry Allen",]
random.shuffle(myList)
print(myList)

#----------------------------------------

# Generate a random float number between 0 and 1
print(random.random())

#----------------------------------------

# Generate a random float between 10 and 14, then convert to integer
print(int(random.uniform(10,14)))

#----------------------------------------

# Generate a random float using triangular distribution
# Parameters: low=15, high=55, mode=17 (most frequent value around 17)
print(random.triangular(15,55,17))

#----------------------------------------
# ASCII graph representation of triangular distribution:
#
#         ^
#         |                           
#         |                    ****
#         |                  ***   ***
#         |                **         **
#         |               **            **
#         |              **               **
#         |             **                   *
#         |            **                       *
#         |           **                           *
#         |          *                                * 
#         |+------------------------------------------------->
#                    15          17                      55
