import constants as c
import pyrosim.pyrosim as pyrosim
import numpy
import pybullet as p
import os
class MOTOR:
	# defines a constructor for this class
	def __init__(self, jointName):
		self.jointName = jointName
		self.Prepare_To_Act()
		self.Save_Values()

	def	Prepare_To_Act(self):
		# Modify method so that one motor oscillates at half the frequency of the other (doesn't matter which one)
		if self.jointName == "Torso_BackLeg":
			self.frequency = c.frequencyBackLeg/2
		else:
			self.frequency = c.frequencyBackLeg
		self.amplitude = c.amplitudeBackLeg
		self.offset = c.phaseOffsetBackLeg
		
		# vector of values to send to the motor
		self.motorValues = self.amplitude * numpy.sin(self.frequency * (numpy.linspace(-numpy.pi, numpy.pi, 1000)) + self.offset)
		# motorValuesFrontLeg = amplitudeFrontLeg * numpy.sin(frequencyFrontLeg * (numpy.linspace(-numpy.pi, numpy.pi, 1000)) + phaseOffsetFrontLeg)
	    
	def	Set_Value(self, robot, desiredAngle):
		# Making motor go
		pyrosim.Set_Motor_For_Joint(bodyIndex = robot.robot, jointName = self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = desiredAngle, maxForce = c.maxForce)

	def	Save_Values(self):
		# write vector of values to a file
		numpy.save(os.path.join('data', 'motorValues.npy'), self.motorValues)
