import solution
import constants as c
import copy

class HILL_CLIMBER:
    def __init__(self):
        self.parent = solution.SOLUTION()
        
    def Evolve(self):
        self.parent.Evaluate("DIRECT")
        for currentGeneration in range(c.numberOfGenerations):
            print("\ngeneration: " + str(currentGeneration))
            self.Evolve_For_One_Generation(currentGeneration)

    def Evolve_For_One_Generation(self, currentGeneration):
        self.Spawn()
        self.Mutate()
        if currentGeneration == 0:
            self.child.Evaluate("GUI")
        else:
            self.child.Evaluate("DIRECT")
        print("\n" + str(self.parent.fitness) + " " + str(self.child.fitness))
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Show_Best(self):
        self.parent.Evaluate("GUI")