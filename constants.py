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
numberOfGenerations = 10
populationSize = 1

# snake length doesnt include head
snake_length = random.randint(1, 10)
numSensorNeurons = random.randint(1, 10)
numMotorNeurons = snake_length
sensors = []
for i in range(numSensorNeurons):
    r = random.randint(0, snake_length + 1)
    sensors.append(r)
motorJointRange = 50000
