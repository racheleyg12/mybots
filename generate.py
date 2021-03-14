import pyrosim.pyrosim as pyrosim

def Create_World():
	# Tell pyrosim where to store information about the world you'd like to create. 
	# Assignment 5, need a world.sdf
	# pyrosim.Start_SDF("world.sdf")
	# This world will currently be called box, because it will only contain a box (links can be spheres, cylinders, or boxes).
	pyrosim.Start_SDF("boxes.sdf")
	
	# Stores a box with initial position x=0, y=0, z=0.5, 
	# and length, width and height all equal to 1 meter, in box.sdf.
	length, width, height = 1, 1, 1
	x, y, z = -2, 2, 0.5
	pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length, width, height])
		
	# Finish generate.py by appending
	pyrosim.End()

# def Create_Robot():

def Generate_Body():
	# description of the robot's body in this urdf file
	pyrosim.Start_URDF("body.urdf")
	pyrosim.Send_Joint(name = "Torso_FrontLeg", parent= "Torso" , child = "FrontLeg" , type = "revolute", position = "2.0 0.0 1.0")
	pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[1, 1, 1])
	pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[1, 1, 1])
	pyrosim.Send_Joint(name = "Torso_BackLeg", parent= "Torso" , child = "BackLeg" , type = "revolute", position = "1.0 0.0 1.0")
	pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[1, 1, 1])
	pyrosim.End()

def Generate_Brain():
	pyrosim.Start_NeuralNetwork("brain.nndf")
	# This particular neuron is going to receive a value from sensor stored in Torso
	pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
	pyrosim.End()


Create_World()
Generate_Body()
Generate_Brain()