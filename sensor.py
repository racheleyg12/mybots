import constants as c
import numpy
class SENSOR:
	# defines a constructor for this class
	def __init__(self, linkName):
		self.linkName = linkName

		# Create a numpy vector, filled with zeros, that has the same length as the number of iterations of your for loop, just before entering the for loop
		self.values = numpy.zeros(c.numLoops)