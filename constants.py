#Constants
import math
import random
pi = math.pi
#BackLeg
amplitudeBL = pi/4
frequencyBL = 10
phaseOffsetBL = -20
#FrontLeg
amplitudeFrontleg = pi/4
frequencyFrontleg = 5
phaseOffsetFrontleg = -20
numberOfGenerations = 100
populationSize = 5


numLinks = 4
numSensorNeurons = random.randint(2, numLinks - 1)
numMotorNeurons = numSensorNeurons - 1
sensors = []
for i in range(numSensorNeurons):
    r = random.randint(0, numLinks)
    sensors.append(r)
motorJointRange = 2


