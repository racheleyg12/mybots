import numpy
import pybullet as p
import pyrosim.pyrosim as pyrosim
#To slow things down
import time
import pybullet_data
#Creates an object, physicsClient, which handles the physics, and draws the results to a Graphical User Interface (GUI).
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Adding a floor
planeId = p.loadURDF("plane.urdf")
planeId = p.loadURDF("body.urdf")

# add gravity 
p.setGravity(0,0,-9.8*2)
#Simulate the box
p.loadSDF("boxes.sdf")

# Pyrosim has to do some additional setting up when it is used to simulate sensors
pyrosim.Prepare_To_Simulate("body.urdf")

# Create a numpy vector, filled with zeros, that has the same length as the number of iterations of your for loop, just before entering the for loop
backLegSensorValues = numpy.zeros(100)
frontLegSensorValues = numpy.zeros(100)

#For loop that iterates 1000 times
for i in range(100):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    # time.sleep(1/60)
    time.sleep(1/60)

print(backLegSensorValues)
print(frontLegSensorValues)
# Save backLegSensorValues in backLegSensorValues.npy folder
import os
numpy.save(os.path.join('data', 'backLegSensorValues.npy'), backLegSensorValues)
numpy.save(os.path.join('data', 'frontLegSensorValues.npy'), frontLegSensorValues)

#To move: hold down CTRL,
#click and drag with a the mouse or press and drag on a trackpad.
p.disconnect()
