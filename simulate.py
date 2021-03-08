from simulation import SIMULATION

import constants as c
import numpy
import pybullet as p
import pyrosim.pyrosim as pyrosim
import random 
import os
import time
import pybullet_data







# # print(backLegSensorValues)
# # print(frontLegSensorValues)
# # Save backLegSensorValues in backLegSensorValues.npy folder
# numpy.save(os.path.join('data', 'backLegSensorValues.npy'), c.backLegSensorValues)
# numpy.save(os.path.join('data', 'frontLegSensorValues.npy'), c.frontLegSensorValues)

# #To move: hold down CTRL,
# #click and drag with a the mouse or press and drag on a trackpad.
# p.disconnect()

simulation = SIMULATION()
simulation.Run()
