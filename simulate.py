from simulation import SIMULATION
import constants as c
import numpy
import pybullet as p
import pyrosim.pyrosim as pyrosim
import random 
import os
import time
import pybullet_data

simulation = SIMULATION()
simulation.Run()
simulation.Get_Fitness()
