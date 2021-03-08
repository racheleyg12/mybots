import constants as c
import pyrosim.pyrosim as pyrosim
import numpy
import pybullet as p
class MOTOR:
	# defines a constructor for this class
	def __init__(self, jointName):
		self.jointName = jointName
		self.Prepare_To_Act()

	def	Prepare_To_Act(self):
		self.amplitude = c.amplitudeBackLeg
		self.frequency = c.frequencyBackLeg
		self.offset = c.phaseOffsetBackLeg
		
		# vector of values to send to the motor
		self.motorValues = self.amplitude * numpy.sin(self.frequency * (numpy.linspace(-numpy.pi, numpy.pi, 1000)) + self.offset)
		# motorValuesFrontLeg = amplitudeFrontLeg * numpy.sin(frequencyFrontLeg * (numpy.linspace(-numpy.pi, numpy.pi, 1000)) + phaseOffsetFrontLeg)
	    
	def	Set_Value(self, robot, t):
		# Making motor go
		pyrosim.Set_Motor_For_Joint(bodyIndex = robot.robot, jointName = self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = self.motorValues[t], maxForce = c.maxForce)