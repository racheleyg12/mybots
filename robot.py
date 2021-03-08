import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR

class ROBOT:
	# defines a constructor for this class
	def __init__(self):
		# create an empty dictionaries
		self.motors = dict()

		# load and prepare to simulate body.urdf
		self.robot = p.loadURDF("body.urdf")
		# Pyrosim has to do some additional setting up when it is used to simulate sensors
		pyrosim.Prepare_To_Simulate("body.urdf")
		self.Prepare_To_Sense()

	def Prepare_To_Sense(self):
		# create an empty dictionary
		self.sensors = {}
		# gives us the name of every link in body.urdf
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)

	def Sense(self, t):
		for sensors in self.sensors:
			self.sensors[sensors].Get_Value(t)
			# sensor.Get_Value(t)
	
