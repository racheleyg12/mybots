import numpy as np
import os
import matplotlib.pyplot as plt
import constants as c

# Load fitness values
fitnessValues = np.load(os.path.join('data', 'FitnessValues.npy'))
print(fitnessValues)
# Plot fitness values
# for i in range(c.numberOfGenerations):
#     plt.plot(fitnessValues[i,:], label='Generation '+str(i+1), linewidth=1)
for i in range(c.populationSize):
    plt.plot(np.arange(1,c.numberOfGenerations+1), fitnessValues[i,:], label='Parent '+str(i+1), linewidth=1, color='blue')

# Formatting x ticks
x_ticks = np.arange(1, c.numberOfGenerations+1)
plt.xticks(x_ticks)
plt.xlabel("Generations")
plt.ylabel("Fitness Value")
plt.title('Parents Fitness Values Evolving over Generations')

# plt.legend()
plt.show()
exit()