import numpy
import os
import matplotlib.pyplot as plt

# Load sensor data
# backLegSensorValues = numpy.load(os.path.join('data', 'backLegSensorValues.npy'));
# frontLegSensorValues = numpy.load(os.path.join('data', 'frontLegSensorValues.npy'));

# print(backLegSensorValues)
# print(frontLegSensorValues)

# plt.plot(backLegSensorValues, label='BackLeg', linewidth=5)
# plt.plot(frontLegSensorValues, label='FrontLeg', linewidth=3)

# plt.xlabel("Time Step")
# plt.ylabel("Sensor Values")

# Load sinusoidally array
targetAngles = numpy.load(os.path.join('data', 'targetAnglesValues.npy'));
plt.plot(targetAngles, (numpy.pi/4)*numpy.sin(targetAngles))
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
plt.axis('tight')
plt.show()

# plt.legend()
# plt.show()

exit()