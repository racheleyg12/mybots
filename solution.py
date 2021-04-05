import pyrosim.pyrosim as pyrosim
import numpy
import os
import random
import time
class SOLUTION:
    # defines a constructor for this class
    def __init__(self, id):
        self.myID = id
        # 3-row x 2-column matrix of random values in a certain range
        self.weights = numpy.random.rand(3,2)
        self.weights = self.weights * 2 - 1

    # def Evaluate(self, directOrGUI):
    #     self.Start_Simulation(directOrGUI)
    #     self.Wait_For_Simulation_To_End()
    
    def Start_Simulation(self, directOrGUI): 
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        strId = str(self.myID)
        os.system("python3 simulate.py " + directOrGUI + " " + strId)

    def Wait_For_Simulation_To_End(self): 
        fitnessFileName = "fitness"+str(self.myID)+".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        f = open(fitnessFileName, "r")
        self.fitness = float(f.read())
        os.system("rm " + fitnessFileName)

    def Create_World(self):
        # Tell pyrosim where to store information about the world you'd like to create. 
        pyrosim.Start_SDF("world.sdf")
        # This world will currently be called box, because it will only contain a box (links can be spheres, cylinders, or boxes).
        pyrosim.Start_SDF("boxes.sdf")
        # Stores a box with initial position x, y, z and length, width and height all equal to 1 meter, in box.sdf.
        length, width, height = 1, 1, 1
        x, y, z = -2, 2, 0.5
        pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length, width, height])
        # Finish generate.py by appending
        pyrosim.End()

        while not os.path.exists("world.sdf"):
            time.sleep(0.01)

    def Create_Body(self):
        # Description of the robot's body in this urdf file
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Joint(name = "Torso_FrontLeg", parent= "Torso" , child = "FrontLeg" , type = "revolute", position = "2.0 0.0 1.0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[1, 1, 1])
        pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[1, 1, 1])
        pyrosim.Send_Joint(name = "Torso_BackLeg", parent= "Torso" , child = "BackLeg" , type = "revolute", position = "1.0 0.0 1.0")
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[1, 1, 1])
        pyrosim.End()

        while not os.path.exists("body.urdf"):
            time.sleep(0.01)

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        # Sensor neurons - going to receive a value from sensors stored in Torso, BackLeg, and FrontLeg
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        # Motor neurons - send values to the motor controlling joint Torso_BackLeg & Torso_FrontLeg
        pyrosim.Send_Motor_Neuron(name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 4 , jointName = "Torso_FrontLeg")

        # Generating synapses - Connects neuron i to neuron j with a synaptic with weight w
        # Outer loop  iterate over the names of the three sensor neurons
        for currentRow in range(3):
            # Inner loop  iterate over each of the two motor neurons
            for currentColumn in range(2):
                # generate a synapse that connects the ith sensor neuron to the jth motor neuron. 
                # send random synaptic weights in the range [-1,1]
                pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn+3 , weight = self.weights[currentRow][currentColumn] )

        pyrosim.End()

        while not os.path.exists("brain"+str(self.myID)+".nndf"):
            time.sleep(0.01)

    def Mutate(self):
        randomRow = random.randint(0, 2)
        randomColumn = random.randint(0, 1)
        self.weights[randomRow,randomColumn] = random.random() * 2 - 1

    def Set_ID(self, newId):
        self.myID = newId
