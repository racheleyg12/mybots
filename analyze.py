import numpy
import os
import matplotlib.pyplot as plt

#Load sensor data
backLegSensorValues = numpy.load(os.path.join('data', 'backLegSensorValues.npy'));
frontLegSensorValues = numpy.load(os.path.join('data', 'frontLegSensorValues.npy'));

print(backLegSensorValues)
print(frontLegSensorValues)

plt.plot(backLegSensorValues, label='BackLeg', linewidth=5)
plt.plot(frontLegSensorValues, label='FrontLeg', linewidth=3)

plt.xlabel("Time Step")
plt.ylabel("Sensor Values")

# line, = ax.plot(backLegSensorValues, label='BackLeg Sensor Values')
# line, = ax.plot(frontLegSensorValues, label='FrontLeg Sensor Values')

plt.legend()
plt.show()

exit()