from world import WORLD
from robot import ROBOT
import constants as c
import numpy
import pybullet as p
import pyrosim.pyrosim as pyrosim
import random 
import os
import time
import pybullet_data

class SIMULATION:
	# defines a constructor for this class
	def __init__(self):
		
		# Connected to pybullet
		# Creates an object, physicsClient, which handles the physics, and draws the results to a Graphical User Interface (GUI).
		physicsClient = p.connect(p.GUI)
		p.setAdditionalSearchPath(pybullet_data.getDataPath())

		self.world = WORLD()
		self.robot = ROBOT()

		# add gravity 
		p.setGravity(0,0,-9.8)

		
	def Run(self):
		# # write this vector to a file
		# numpy.save(os.path.join('data', 'motorValuesBackLeg.npy'), c.motorValuesBackLeg)
		# numpy.save(os.path.join('data', 'motorValuesFrontLeg.npy'), c.motorValuesFrontLeg)

		# #For loop that iterates 1000 times
		for i in range(c.numLoops):
			time.sleep(1/60)
			p.stepSimulation()
		#     # Saving sensor values
		#     c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
		#     c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
		#     # Making motors
		#     pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = "Torso_BackLeg", controlMode = p.POSITION_CONTROL, targetPosition = c.motorValuesBackLeg[i], maxForce = c.maxForce)
		#     pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = "Torso_FrontLeg", controlMode = p.POSITION_CONTROL, targetPosition = c.motorValuesFrontLeg[i], maxForce = c.maxForce)

		#     # time.sleep(1/60)
		#     time.sleep(1/600)
	# defines a destructor for this class   
	def __del__(self):
		p.disconnect()

