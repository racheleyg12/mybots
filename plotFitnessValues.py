import numpy as np
import os
import matplotlib.pyplot as plt
import constants as c

# Load fitness values
fitnessValuesA = np.load(os.path.join('data', 'FitnessValuesA.npy'))
fitnessValuesB = np.load(os.path.join('data', 'FitnessValuesB.npy'))

# Plot fitness values
plt.figure('Individual Parent Fitnesses')
for i in range(c.populationSize):
    plt.plot(np.arange(1,c.numberOfGenerations+1), fitnessValuesA[i,:], label='Parent '+str(i+1), linewidth=1, color='red')
for i in range(c.populationSize):
    plt.plot(np.arange(1,c.numberOfGenerations+1), fitnessValuesB[i,:], label='Parent '+str(i+1), linewidth=1, color='blue')

# Formatting x ticks
x_ticks = np.arange(1, c.numberOfGenerations+1)
plt.xticks(x_ticks)
plt.xlabel("Generations")
plt.ylabel("Fitness Value")
plt.title('Parents Fitness Values Evolving over Generations')
# plt.legend()
plt.show()

# 2nd Plot of the Averages
plt.figure('Average Fitness of Population')
plt.plot(np.arange(1,c.numberOfGenerations+1), np.mean(fitnessValuesA, axis=0), label='Test A', linewidth=2, color='red')
plt.plot(np.arange(1,c.numberOfGenerations+1), np.mean(fitnessValuesB, axis=0), label='Test B ', linewidth=2, color='blue')
plt.legend()
x_ticks = np.arange(1, c.numberOfGenerations+1)
plt.xticks(x_ticks)
plt.xlabel("Generations")
plt.ylabel("Fitness Value")
plt.title('Average Fitness Values of Population Evolving Over Generations')
plt.show()

# 3rd Plot of the Averages w/ SD
plt.figure('Average Fitness of Population w/ Standard Deviation')
plt.plot(np.arange(1,c.numberOfGenerations+1), np.mean(fitnessValuesA, axis=0) - np.std(fitnessValuesA, axis=0), label='Test A - SD', linewidth=1, color='red')
plt.plot(np.arange(1,c.numberOfGenerations+1), np.mean(fitnessValuesA, axis=0), label='Test A', linewidth=5, color='red')
plt.plot(np.arange(1,c.numberOfGenerations+1), np.mean(fitnessValuesA, axis=0) + np.std(fitnessValuesA, axis=0), label='Test A + SD', linewidth=1, color='red')
plt.plot(np.arange(1,c.numberOfGenerations+1), np.mean(fitnessValuesB, axis=0) - np.std(fitnessValuesB, axis=0), label='Test B - SD', linewidth=1, color='blue')
plt.plot(np.arange(1,c.numberOfGenerations+1), np.mean(fitnessValuesB, axis=0), label='Test B ', linewidth=5, color='blue')
plt.plot(np.arange(1,c.numberOfGenerations+1), np.mean(fitnessValuesB, axis=0) + np.std(fitnessValuesB, axis=0), label='Test B + SD', linewidth=1, color='blue')
plt.legend()
x_ticks = np.arange(1, c.numberOfGenerations+1)
plt.xticks(x_ticks)
plt.xlabel("Generations")
plt.ylabel("Fitness Value")
plt.title('Average Fitness Values of Population Evolving Over Generations')
plt.show()


