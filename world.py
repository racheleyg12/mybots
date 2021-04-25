import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
class WORLD:
	# defines a constructor for this class
	def __init__(self):		
		# Adding a floor
		self.planeId = p.loadURDF("plane.urdf")
		# Load a world
		p.loadSDF("world.sdf")
		

		
