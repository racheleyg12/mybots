from solution import SOLUTION

class HILL_CLIMBER:
    # defines a constructor for this class
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate()
        pass
