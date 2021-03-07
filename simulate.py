import constants as c
import numpy
import pybullet as p
import pyrosim.pyrosim as pyrosim
import random 
# To write arrays to file
# import os
# # To slow things down
# import time
# import pybullet_data

# #Creates an object, physicsClient, which handles the physics, and draws the results to a Graphical User Interface (GUI).
# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())

# # Adding a floor
# planeId = p.loadURDF("plane.urdf")
# robot = p.loadURDF("body.urdf")

# # add gravity 
# p.setGravity(0,0,c.gravity)
# #Simulate the box
# p.loadSDF("boxes.sdf")

# # Pyrosim has to do some additional setting up when it is used to simulate sensors
# pyrosim.Prepare_To_Simulate("body.urdf")

# # write this vector to a file
# numpy.save(os.path.join('data', 'motorValuesBackLeg.npy'), c.motorValuesBackLeg)
# numpy.save(os.path.join('data', 'motorValuesFrontLeg.npy'), c.motorValuesFrontLeg)

# #For loop that iterates 1000 times
# for i in range(c.numLoops):
#     p.stepSimulation()
#     # Saving sensor values
#     c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#     # Making motors
#     pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = "Torso_BackLeg", controlMode = p.POSITION_CONTROL, targetPosition = c.motorValuesBackLeg[i], maxForce = c.maxForce)
#     pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = "Torso_FrontLeg", controlMode = p.POSITION_CONTROL, targetPosition = c.motorValuesFrontLeg[i], maxForce = c.maxForce)

#     # time.sleep(1/60)
#     time.sleep(1/600)

# # print(backLegSensorValues)
# # print(frontLegSensorValues)
# # Save backLegSensorValues in backLegSensorValues.npy folder
# numpy.save(os.path.join('data', 'backLegSensorValues.npy'), c.backLegSensorValues)
# numpy.save(os.path.join('data', 'frontLegSensorValues.npy'), c.frontLegSensorValues)

# #To move: hold down CTRL,
# #click and drag with a the mouse or press and drag on a trackpad.
# p.disconnect()
pass
