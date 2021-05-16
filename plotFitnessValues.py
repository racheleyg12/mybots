import numpy as np
import os
import matplotlib.pyplot as plt
import constants as c

# Load fitness values
fitnessValuesA = np.load(os.path.join('data', 'FitnessValuesA.npy'))
fitnessValuesB = np.load(os.path.join('data', 'FitnessValuesB.npy'))
fitnessValuesBLoop = np.load(os.path.join('data', 'FitnessValuesBLoop.npy'))
fitnessValuesBIf = np.load(os.path.join('data', 'FitnessValuesBIf.npy'))
# Plot fitness values
# for i in range(c.numberOfGenerations):
#     plt.plot(fitnessValues[i,:], label='Generation '+str(i+1), linewidth=1)

# for i in range(c.populationSize):
#     plt.plot(np.arange(1,c.numberOfGenerations+1), fitnessValues[i,:], label='Parent '+str(i+1), linewidth=1, color='b')

plt.figure('Individual Parent Fitnesses')
for i in range(c.populationSize):
    plt.plot(np.arange(1,c.numberOfGenerations+1), fitnessValuesBLoop[i,:], label='Parent '+str(i+1), linewidth=1, color='r')

for i in range(c.populationSize):
    plt.plot(np.arange(1,c.numberOfGenerations+1), fitnessValuesBIf[i,:], label='Parent '+str(i+1), linewidth=1, color='b')

for i in range(c.populationSize):
    plt.plot(np.arange(1,c.numberOfGenerations+1), fitnessValuesA[i,:], label='Parent '+str(i+1), linewidth=1, color='g')

# Formatting x ticks
x_ticks = np.arange(1, c.numberOfGenerations+1)
plt.xticks(x_ticks)
plt.xlabel("Generations")
plt.ylabel("Fitness Value")
plt.title('Parents Fitness Values Evolving over Generations')
# plt.legend()
plt.show()

plt.figure('Average of All Parent Fitnesses')
for i in range(c.populationSize):
    plt.plot(np.arange(1,c.numberOfGenerations+1), np.mean(fitnessValuesBLoop, axis=0), label='Parent '+str(i+1), linewidth=1, color='r')

for i in range(c.populationSize):
    plt.plot(np.arange(1,c.numberOfGenerations+1), np.mean(fitnessValuesBIf, axis=0), label='Parent '+str(i+1), linewidth=1, color='b')

for i in range(c.populationSize):
    plt.plot(np.arange(1,c.numberOfGenerations+1), np.mean(fitnessValuesA, axis=0), label='Parent '+str(i+1), linewidth=1, color='g')

plt.title('Average Parent Fitness Values Evolving over Generations')
plt.show()



