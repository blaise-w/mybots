from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
last = False
if sys.argv[3] == "True":
    last = True

simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run(last)
simulation.Get_Fitness(solutionID)