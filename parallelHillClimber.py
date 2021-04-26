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
        os.system("rm avoidFitness*.txt")
        os.system("rm tmp*.txt")
        self.nextAvailableID = 0
        self.parents = dict()
        # Intializes population of solutions
        for i in range(c.populationSize):   #range(x) is exclusive
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1
        

    def Evolve(self):
        # Evaluate each of the parents
        self.Evaluate(self.parents)
        # Evolving every generation
        for currentGeneration in range(c.numberOfGenerations): 
            self.Evolve_For_One_Generation(currentGeneration)
        

    def Evolve_For_One_Generation(self, gen):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        print("\n ")
        print("Generation:", gen+1)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = dict()
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1
        
    def Mutate(self):
        for key in self.children:
            self.children[key].Mutate()

    def Select(self):
        # Replaces the parent with its child, if the parent does worse
        for key in self.parents:
            if ((self.children[key].fitness*(-1.25))+self.children[key].avoidFitness > (self.parents[key].fitness*(-1.25))+self.parents[key].avoidFitness):
            # if (self.children[key].fitness/self.children[key].avoidFitness < self.parents[key].fitness/self.parents[key].avoidFitness):
            # if(self.children[key].fitness < self.parents[key].fitness and self.children[key].avoidFitness > self.parents[key].avoidFitness):
            # if((self.children[key].fitness < self.parents[key].fitness and self.children[key].avoidFitness > self.parents[key].avoidFitness) or (0.2 < self.parents[key].avoidFitness-self.children[key].avoidFitness and 1 < self.children[key].fitness-self.parents[key].fitness)):
                self.parents[key] = self.children[key]

    def Print(self):
        for key in self.parents:
            print("parent: ", self.parents[key].fitness,"|",self.parents[key].avoidFitness,"=", (self.parents[key].fitness*(-1))+self.parents[key].avoidFitness, " ", "child: ", self.children[key].fitness,"|",self.children[key].avoidFitness, "=", (self.children[key].fitness*(-1))+self.children[key].avoidFitness)
            
    def Show_Best(self):
        # initialize minFitness to the 1st instance
        # minFitness = 0
        # maxAvoidance = 26

        # minFitness = 0
        # maxAvoidance = 26
        # keyOfBest = 0
        maxfitness = 0
        for key in self.parents:
            if (self.parents[key].fitness*(-1.25))+self.parents[key].avoidFitness > maxfitness:
                maxfitness = (self.parents[key].fitness*(-1.25))+self.parents[key].avoidFitness
                keyOfBest = key

            # if (self.parents[key].fitness < minFitness and self.parents[key].avoidFitness > maxAvoidance):
                # minFitness = self.parents[key].fitness
                # maxAvoidance = self.parents[key].avoidFitness
                # keyOfBest = key
                

        print(keyOfBest)
        print(self.parents[keyOfBest].fitness, "/", self.parents[keyOfBest].avoidFitness)
        self.parents[keyOfBest].Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for i in range(c.populationSize):
            solutions[i].Start_Simulation("DIRECT")
        for i in range(c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()
        
             