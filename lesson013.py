import random

# betavariate(alpha, beta)
# Returns a random float number between 0 and 1 based on the Beta distribution (used in statistics)
print(random.betavariate(1, 8))

# expovariate(lambd)
# Returns a random float number based on the Exponential distribution (used in statistics)
# lambd = 1/mean
print(random.expovariate(0.5))

# gammavariate(alpha, beta)
# Returns a random float number based on the Gamma distribution (used in statistics)
print(random.gammavariate(50, 24))

# gauss(mu, sigma)
# Returns a random float number based on the Gaussian distribution (used in probability theories)
print(random.gauss(50, 24))

# lognormvariate(mu, sigma)
# Returns a random float number based on a log-normal distribution (used in probability theories)
print(random.lognormvariate(0, 0.5))

# normalvariate(mu, sigma)
# Returns a random float number based on the normal distribution (used in probability theories)
print(random.normalvariate(50, 24))

# vonmisesvariate(mu, kappa)
# Returns a random float number based on the von Mises distribution (used in directional statistics)
print(random.vonmisesvariate(0, 4))

# paretovariate(alpha)
# Returns a random float number based on the Pareto distribution (used in probability theories)
print(random.paretovariate(5))

# weibullvariate(alpha, beta)
# Returns a random float number based on the Weibull distribution (used in statistics)
print(random.weibullvariate(1, 1.5))
