import pybullet as p
#Creates an object, physicsClient, which handles the physics, and draws the results to a Graphical User Interface (GUI).
physicsClient = p.connect(p.GUI)

p.disconnect()
