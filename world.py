import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
class WORLD:
	# defines a constructor for this class
	def __init__(self):		
		# Adding a floor
		self.planeId = p.loadURDF("plane.urdf")
		# Load a world
		self.objects = p.loadSDF("world.sdf")
		# Position of boxes
		PositionOfBoxes = []
		for i in range(20):
			posAndOrientation = p.getBasePositionAndOrientation(self.objects[i])
			position = posAndOrientation[0]
			PositionOfBoxes.append(position)
		self.PositionOfBoxes = PositionOfBoxes