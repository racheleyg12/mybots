import pyrosim.pyrosim as pyrosim

# Tell pyrosim where to store information about the world you'd like to create. 
# This world will currently be called box, because it will only contain a box (links can be spheres, cylinders, or boxes).
pyrosim.Start_SDF("box.sdf")

# Stores a box with initial position x=0, y=0, z=0.5, 
# and length, width and height all equal to 1 meter, in box.sdf.
length, width, height = 1, 2, 3
# a, b = 100, 200
pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[length, width, height])

# Finish generate.py by appending
pyrosim.End()