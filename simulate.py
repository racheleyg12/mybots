import numpy
import pybullet as p
import pyrosim.pyrosim as pyrosim
import random 
# To write arrays to file
import os
# To slow things down
import time
import pybullet_data

amplitudeBackLeg = numpy.pi/4
frequencyBackLeg = 10
phaseOffsetBackLeg = 0

amplitudeFrontLeg = numpy.pi/4
frequencyFrontLeg = 10
phaseOffsetFrontLeg = numpy.pi/2

#Creates an object, physicsClient, which handles the physics, and draws the results to a Graphical User Interface (GUI).
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Adding a floor
planeId = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")

# add gravity 
p.setGravity(0,0,-9.8*2)
#Simulate the box
p.loadSDF("boxes.sdf")

# Pyrosim has to do some additional setting up when it is used to simulate sensors
pyrosim.Prepare_To_Simulate("body.urdf")

# Create a numpy vector, filled with zeros, that has the same length as the number of iterations of your for loop, just before entering the for loop
numLoops = 1000
backLegSensorValues = numpy.zeros(numLoops)
frontLegSensorValues = numpy.zeros(numLoops)

# a vector with values that vary sinusoidally over the range -pi to pi
x = numpy.linspace(-numpy.pi, numpy.pi, 1000)
targetAngles = (numpy.pi/4)*numpy.sin(numpy.linspace(-numpy.pi, numpy.pi, 1000))
# write this vector to a file
# numpy.save(os.path.join('data', 'targetAnglesValues.npy'), targetAngles)
motorValuesBackLeg = amplitudeBackLeg * numpy.sin(frequencyBackLeg * (numpy.linspace(-numpy.pi, numpy.pi, 1000)) + phaseOffsetBackLeg)
motorValuesFrontLeg = amplitudeFrontLeg * numpy.sin(frequencyFrontLeg * (numpy.linspace(-numpy.pi, numpy.pi, 1000)) + phaseOffsetFrontLeg)
# write this vector to a file
numpy.save(os.path.join('data', 'motorValuesBackLeg.npy'), motorValuesBackLeg)
numpy.save(os.path.join('data', 'motorValuesFrontLeg.npy'), motorValuesFrontLeg)

#For loop that iterates 1000 times
for i in range(numLoops):
    p.stepSimulation()
    # Saving sensor values
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    # Making motors
    pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = "Torso_BackLeg", controlMode = p.POSITION_CONTROL, targetPosition = motorValuesBackLeg[i], maxForce = 55)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = "Torso_FrontLeg", controlMode = p.POSITION_CONTROL, targetPosition = motorValuesFrontLeg[i], maxForce = 55)

    # time.sleep(1/60)
    time.sleep(1/600)

# print(backLegSensorValues)
# print(frontLegSensorValues)
# Save backLegSensorValues in backLegSensorValues.npy folder
numpy.save(os.path.join('data', 'backLegSensorValues.npy'), backLegSensorValues)
numpy.save(os.path.join('data', 'frontLegSensorValues.npy'), frontLegSensorValues)

#To move: hold down CTRL,
#click and drag with a the mouse or press and drag on a trackpad.
p.disconnect()
