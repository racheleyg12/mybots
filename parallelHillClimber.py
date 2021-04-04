from solution import SOLUTION
import constants as c
import copy
import os
class PARALLEL_HILL_CLIMBER:
    # defines a constructor for this class
    def __init__(self):
        # delete files befor beginning
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        os.system("rm tmp*.txt")
        self.nextAvailableID = 0
        self.parents = dict()
        for i in range(c.populationSize):   #range(x) is exclusive
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1
        

    def Evolve(self):
        # Evaluate each of the parents
        for i in range(c.populationSize):
            self.parents[i].Start_Simulation("DIRECT")
        for i in range(c.populationSize):
            self.parents[i].Wait_For_Simulation_To_End()
        
        # self.parent.Evaluate("DIRECT")
        # os.system("python simulate.py GUI")

        for currentGeneration in range(c.numberOfGenerations): 
            self.Evolve_For_One_Generation()
        

    def Evolve_For_One_Generation(self):
        # self.Spawn()
        # self.Mutate()
        # self.child.Evaluate("DIRECT")
        # self.Print()
        # self.Select()
        pass

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        self.child.Set_ID(self.nextAvailableID)
        self.nextAvailableID = self.nextAvailableID + 1
    
    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        # Replaces the parent with its child, if the parent does worse
        if(self.child.fitness < self.parent.fitness):
            self.parent = self.child

    def Print(self):
        print("\n-------------------------------------------------")
        print(self.parent.fitness, " ",self.child.fitness)
        print("-------------------------------------------------")

    def Show_Best(self):
        # os.system("python simulate.py GUI")
        pass