import os
from hillclimber import HILL_CLIMBER

# creates an instance of HILL_CLIMBER called hc
hc = HILL_CLIMBER()
hc.Evolve()
hc.Show_Best()

# for i in range(5):
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")