import pybullet as p
import pyrosim.pyrosim as pyrosim
#To slow things down
import time
import pybullet_data
#Creates an object, physicsClient, which handles the physics, and draws the results to a Graphical User Interface (GUI).
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Adding a floor
planeId = p.loadURDF("plane.urdf")
planeId = p.loadURDF("body.urdf")

# add gravity 
p.setGravity(0,0,-9.8)
#Simulate the box
p.loadSDF("boxes.sdf")

# Pyrosim has to do some additional setting up when it is used to simulate sensors
pyrosim.Prepare_To_Simulate("body.urdf")

#For loop that iterates 1000 times
for i in range(1000):
    p.stepSimulation()
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    print(backLegTouch)
    time.sleep(1/60)
    
#To move: hold down CTRL,
#click and drag with a the mouse or press and drag on a trackpad.
p.disconnect()
