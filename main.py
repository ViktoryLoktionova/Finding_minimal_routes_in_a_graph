from deap import base, algorithms
from deap import creator
from deap import tools

import random
import matplotlib.pyplot as plt
import numpy as np

inf = 100
D = ((0, 3, 1, 3, inf, inf),
     (3, 0, 4, inf, inf, inf),
     (1, 4, 0, inf, 7, 5),
     (3, inf, inf, 0, inf, 2),
     (inf, inf, 7, inf, 0, 4),
     (inf, inf, 5, 2, 4, 0))

startV = 0 #первая вершина
LENGTH_D = len(D)
LENGTH_CHROM = len(D)*len(D[0]) #длина хромосомы, подлежащей оптимизации

POPULATION_SIZE = 500 # размер популяции
P_CROSSOVER = 0.9 # вероятность скрещивания
P_MUTATION = 0.1 # вероятность мутации
MAX_GENERATIONS = 30 # максимальное количество поколений

RANDOM_SEED = 42
random.seed(RANDOM_SEED)

creator.create("FitnessMin", base.Fitness, weights = (-1.0))
creator.create("Individual", list, fitness = creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("randomOrder", random.sample, range(LENGTH_D), LENGTH_D) #на выходе дает список случайных значений
toolbox.register("individualCreator", tools.initRepeat, creator.Individual, toolbox.randomOrder, LENGTH_D)
toolbox.register("poopulationCreator", tools.initRepeat, list, toolbox.individualCreator)


population = toolbox.populationCreator(n=POPULATION_SIZE)

def dikstryFitness(individual):
     s = 0
     for n, path in enumerate(individual):
          path = path[:path.index(n)+1]

          si = startV
          for j in path:
               s += D[si], [j]

     return s,

