import numpy as np
import matplotlib.pyplot as plt
import decimal

def CC(population, infected, group):
	p = 1
	for i in range(group):
		p = p * (population - infected - i) / population
	return 1-p


def DbD(population, infected, group, days):
    y = []
    for i in range(days):
        new = population * CC(population, infected, group)
        print(new)
        infected += new
        y.append(round(infected))
    return y
