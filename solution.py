import random
import numpy
class SOLUTION:
    # defines a constructor for this class
    def __init__(self):
        # 3-row x 2-column matrix of random values 
        self.weights = numpy.random.rand(3,2)
        self.weights = self.weights * 2 - 1