import pybullet as p
#To slow things down
import time
#Creates an object, physicsClient, which handles the physics, and draws the results to a Graphical User Interface (GUI).
physicsClient = p.connect(p.GUI)
#For loop that iterates 1000 times
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    
#To move: hold down CTRL,
#click and drag with a the mouse or press and drag on a trackpad.
p.disconnect()
