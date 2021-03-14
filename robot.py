import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
	# defines a constructor for this class
	def __init__(self):
		# load and prepare to simulate body.urdf
		self.robot = p.loadURDF("body.urdf")
		# Pyrosim has to do some additional setting up when it is used to simulate sensors
		pyrosim.Prepare_To_Simulate("body.urdf")
		self.Prepare_To_Sense()
		self.Prepare_To_Act()
		self.nn = NEURAL_NETWORK("brain.nndf")

	def Prepare_To_Sense(self):
		# create an empty dictionary TO STORE SENSORS
		self.sensors = {}
		# gives us the name of every link in body.urdf
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)

	def Sense(self, t):
		# get all the sensors and fill them w/ sensor values
		for sensor in self.sensors:
			self.sensors[sensor].Get_Value(t)

	def Prepare_To_Act(self):
		# create an empty dictionary TO STORE MOTORS
		self.motors = dict()

		# gives us the name of every joint in body.urdf (attaching a motor to every joint)
		for jointName in pyrosim.jointNamesToIndices:
			self.motors[jointName] = MOTOR(jointName)

	def	Act(self, t):
		# We are now going to discard motorValues and use values from the motor neurons instead.
		# iterate over all the neurons in the neural network
		for neuronName in self.nn.Get_Neuron_Names():
			if self.nn.Is_Motor_Neuron(neuronName):
				print(neuronName)
		for motor in self.motors:
			self.motors[motor].Set_Value(self, t)

	def	Think(self):
		# flowing values from the sensors to the sensor neurons
		self.nn.Update()
		self.nn.Print()
