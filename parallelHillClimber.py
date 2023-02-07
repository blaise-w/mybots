import solution
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        #os.system("rm brain" + ".nndf")
        #os.system("rm fitness" + ".nndf")
        self.nextAvailableID = 0
        self.parents = {}
        for key in range(c.populationSize):
            val = solution.SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
            self.parents[key] = val
        
        
    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            #print("\ngeneration: " + str(currentGeneration))
            self.Evolve_For_One_Generation(currentGeneration)

    def Evolve_For_One_Generation(self, currentGeneration):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        # if currentGeneration == 0:
        #     self.child.Evaluate("GUI")
        # else:
        #     self.child.Evaluate("DIRECT")
        # print("\n" + str(self.parent.fitness) + " " + str(self.child.fitness))
        self.Select()

    def Spawn(self):
        self.children = {}
        for i in range(len(self.parents)):
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

        # self.child = copy.deepcopy(self.parent)
        # self.child.Set_ID(self.nextAvailableID)
        # self.nextAvailableID += 1
        

    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()

    def Select(self):
        for key in self.parents:
            if self.parents[key].fitness > self.children[key].fitness:
                self.parents[key] = self.children[key]

    def Show_Best(self):
        lowest = 999999999999999
        for key in self.parents:
            if self.parents[key].fitness < lowest:
                lowest = self.parents[key].fitness
                best = self.parents[key]
        #print(best.legweights)
        best.Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for parent in solutions:
            solutions[parent].Start_Simulation("DIRECT")
        for parent in self.parents:
            solutions[parent].Wait_For_Simulation_To_End()

    def Print(self):
        print()
        for key in self.parents:
            pass
            #print(str(self.parents[key].fitness) + " " + str(self.children[key].fitness))
        #print()