import constants as c
import pyrosim.pyrosim as pyrosim
import numpy
class SENSOR:
	# defines a constructor for this class
	def __init__(self, linkName):
		self.linkName = linkName

		# Create a numpy vector, filled with zeros, that has the same length as the number of iterations of your for loop, just before entering the for loop
		self.values = numpy.zeros(c.numLoops)

	def Get_Value(self, t):
		self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
		# Modify sensor.Get_Value() to only print these vectors at the last time step. You should see three vectors with no zeros in them.
		if t == (c.numLoops-1):
			print(self.values)