import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons) * 2 - 1
        random.seed(2)
        self.sizeAndAxis = [random.random() for i in range(21)]
        self.directions = [random.randint(1, 5) for i in range(4)]
        self.adds = [random.randint(0, i) for i in range(3)]

    def Evaluate(self, directOrGUI):
        self.Create_Body()
        self.Create_Brain(self.myID)
        self.Create_World()
        directOrGUI = "GUI"
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " &")
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)
        f = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(f.read())
        print(self.fitness)
        f.close

    def Start_Simulation(self, directOrGUI, last=False):
        self.Create_Body(self.myID)
        self.Create_Brain(self.myID)
        self.Create_World()
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " " + str(last) + " &")

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)
        f = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(f.read())
        f.close
        os.system("rm" + " fitness" + str(self.myID) + ".txt")
        
        #print("\n" + str(self.fitness))

    def Mutate(self):
        #print(self.weights)
        randomRow = random.randint(0, c.numSensorNeurons -1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randomRow,randomColumn] = random.random() * 2 - 1
        r = random.randint(1, 3)
        if r == 1:
            index = random.randint(0, 20)
            self.sizeAndAxis[index] = random.random()
        elif r == 2:
            index = random.randint(0, 3)
            self.directions[index] = random.randint(1, 5)
        else:
            index = random.randint(0, 2)
            self.adds[index] = random.randint(0, index)
           

    def Create_Body(self, ID):
        #print()
        #print("Create Body")
        # How to stop from building inside itself?
        #print(self.legweights)
        length = c.numLinks
        pyrosim.Start_URDF("body" + str(ID) + ".urdf")

        # choose side to add to
        # 1 -y 2 +y 3 -x 4 +x 5 +z
        nextDirection = self.directions[0]
        directionsIndex = 1

        sizeAndAxisIndex = 0
        
        linkSizes = {}
        self.children = {}
        linkDirections = {}
        #absPositions = {}
        # for joint placement:
        relPositions = {}
        
        for i in range(0, length):
            #print(i)
            direction = nextDirection

            # add random axis later (this also depends on where we add it)
            # and other joint types
            # adjust starting z height


            save_x = self.sizeAndAxis[sizeAndAxisIndex]
            save_y = self.sizeAndAxis[sizeAndAxisIndex + 1]
            save_z = self.sizeAndAxis[sizeAndAxisIndex + 2]
            size = [save_x,save_y,save_z]

            sizeAndAxisIndex += 3
            # save_x = 1
            # save_y = 1
            # save_z = 1
            # size = [1, 1, 1]

            color = "Blue"
            if i in c.sensors: color = "Green"
            # can add a change to c.sensors in mutate

            name = "Link" + str(i)

            if i == 0:
                pos = [0, 0, 0]
                pyrosim.Send_Cube(name=name, pos=pos, size=size, color=color)

            # -y direction
            elif direction == 1:
                pos = [0,-save_y/2,0]
                pyrosim.Send_Cube(name=name, pos=pos, size=size, color=color)
    
           # +y
            elif direction == 2:
                pos=[0,save_y/2,0] 
                pyrosim.Send_Cube(name=name, pos=pos, size=size, color=color)
                    
            # -x
            elif direction == 3:
                pos=[-save_x/2,0,0] 
                pyrosim.Send_Cube(name=name, pos=pos, size=size, color=color)
                
            # +x
            elif direction == 4:
                pos=[save_x/2,0,0] 
                pyrosim.Send_Cube(name=name, pos=pos, size=size, color=color)
 
            # +z
            else:
                pos=[0,0,save_z/2] 
                pyrosim.Send_Cube(name=name, pos=pos, size=size, color=color)

            #print("p")
            #print(pos)

            linkSizes[i] = size
               
            if i == length - 1: continue
            nextDirection = self.directions[directionsIndex]
            directionsIndex += 1

            link = self.adds[i]
            linkName = "Link" + str(link)

            # get a direction that isnt taken
            # if full, get a new link
            # if (nextDirection == 1 and direction == 2) or (nextDirection == 2 and direction == 1):
            #     nextDirection = (nextDirection + random.randint(1, 4)) % 5
            # if (nextDirection == 3 and direction == 4) or (nextDirection == 4 and direction == 3):
            #     nextDirection = (nextDirection + random.randint(1, 4)) % 5

            if link not in linkDirections:
                linkDirections[link] = [nextDirection]
            else:
                if nextDirection not in linkDirections[link]:
                    linkDirections[link].append(nextDirection)
                else:
                    while True:
                        nextDirection = random.randint(1, 5)
                        if (nextDirection == 1 and direction == 2) or (nextDirection == 2 and direction == 1):
                            nextDirection = (nextDirection + random.randint(1, 4)) % 5
                        if (nextDirection == 3 and direction == 4) or (nextDirection == 4 and direction == 3):
                            nextDirection = (nextDirection + random.randint(1, 4)) % 5
                        if nextDirection not in linkDirections[link]:
                            linkDirections[link].append(nextDirection)
                            break
                        if len(linkDirections[link]) == 3:
                            link = random.randint(0, i)

            # need to take position into account bc first joint is 100% absolute
            if i == 0:
                if nextDirection == 1:
                    relPositions[link] = [0,-0.5*linkSizes[link][1],0]
                elif nextDirection == 2:
                    relPositions[link] = [0,0.5*linkSizes[link][1],0]
                elif nextDirection == 3:
                    relPositions[link] = [-0.5*linkSizes[link][0],0,0]
                elif nextDirection == 4:
                    relPositions[link] = [0.5*linkSizes[link][0],0,0]
                else:
                    relPositions[link] = [0,0,0.5*linkSizes[link][2]]
            else:
                if nextDirection == 1:
                    if direction == 1:
                        relPositions[link] = [0,-linkSizes[link][1],0]
                    elif direction == 2:
                        relPositions[link] = [0,0,0]
                    elif direction == 3:
                        relPositions[link] = [-0.5*linkSizes[link][0],-0.5*linkSizes[link][1],0]
                    elif direction == 4:
                        relPositions[link] = [0.5*linkSizes[link][0],-0.5*linkSizes[link][1],0]
                    else:
                        relPositions[link] = [0,-0.5*linkSizes[link][1],0.5*linkSizes[link][2]]
                elif nextDirection == 2:
                    if direction == 1:
                        relPositions[link] = [0,0,0]
                    elif direction == 2:
                        relPositions[link] = [0,linkSizes[link][1],0]
                    elif direction == 3:
                        relPositions[link] = [-0.5*linkSizes[link][0],0.5*linkSizes[link][1],0]
                    elif direction == 4:
                        relPositions[link] = [0.5*linkSizes[link][0],0.5*linkSizes[link][1],0]
                    else:
                        relPositions[link] = [0,0.5*linkSizes[link][1],0.5*linkSizes[link][2]]
                elif nextDirection == 3:
                    if direction == 1:
                        relPositions[link] = [-0.5*linkSizes[link][0],-0.5*linkSizes[link][1],0]
                    elif direction == 2:
                        relPositions[link] = [-0.5*linkSizes[link][0],0.5*linkSizes[link][1],0]
                    elif direction == 3:
                        relPositions[link] = [-linkSizes[link][0],0,0]
                    elif direction == 4:
                        relPositions[link] = [0,0,0]
                    else:
                        relPositions[link] = [-0.5*linkSizes[link][0],0,0.5*linkSizes[link][2]]
                elif nextDirection == 4:
                    if direction == 1:
                        relPositions[link] = [0.5*linkSizes[link][0],-0.5*linkSizes[link][1],0]
                    elif direction == 2:
                        relPositions[link] = [0.5*linkSizes[link][0],0.5*linkSizes[link][1],0]
                    elif direction == 3:
                        relPositions[link] = [0,0,0]
                    elif direction == 4:
                        relPositions[link] = [linkSizes[link][0],0,0]
                    else:
                        relPositions[link] = [0.5*linkSizes[link][0],0,0.5*linkSizes[link][2]]
                else:
                    # need to figure out a way to make this work for different sizes
                    if direction == 1:
                        relPositions[link] = [0,-0.5*linkSizes[link][1],0.5*linkSizes[link][2]]
                    elif direction == 2:
                        relPositions[link] = [0,0.5*linkSizes[link][1],0.5*linkSizes[link][2]]
                    elif direction == 3:
                        relPositions[link] = [-0.5*linkSizes[link][0],0,0.5*linkSizes[link][2]]
                    elif direction == 4:
                        relPositions[link] = [0.5*linkSizes[link][0],0,0.5*linkSizes[link][2]]
                    else:
                        relPositions[link] = [0,0,linkSizes[link][2]]

            #print("rp")
            #print(relPositions[link])

            if link in self.children:
                self.children[link].append(i+1)
            else:
                self.children[link] = [i+1]

            jointAxis = str(self.sizeAndAxis[sizeAndAxisIndex]) + " " + str(self.sizeAndAxis[sizeAndAxisIndex] + 1) + " " + str(self.sizeAndAxis[sizeAndAxisIndex] + 2)
            sizeAndAxisIndex += 3
            pyrosim.Send_Joint(name = linkName + "_Link" + str(i+1), parent = linkName, child = "Link" + str(i+1), type = "revolute", position= relPositions[link], jointAxis = jointAxis)
        
        pyrosim.End()

    def Find_Parent(self, joint):
        for parent, children in self.children.items():
            if joint in children:
                return parent

    def Create_Brain(self, ID):
        pyrosim.Start_NeuralNetwork("brain" + str(ID) + ".nndf")

        name_count = 0

        for i in range(0, c.numLinks):
            if i in c.sensors:
                pyrosim.Send_Sensor_Neuron(name = name_count , linkName = "Link" + str(i))
                name_count += 1
                if i == c.numLinks - 1: continue
                if i not in self.children: continue
                for child in self.children[i]:
                    pyrosim.Send_Motor_Neuron( name = name_count , jointName = "Link" + str(i) + "_Link" + str(child))
                    name_count += 1

        #nested for loop from K below:
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + c.numSensorNeurons, weight = self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Create_World(self):
        pyrosim.Start_SDF("world1.sdf")
        #pyrosim.Send_Sphere(name="Sphere", pos=[-300,0,0.5] , size=[0.5])
        #pyrosim.Send_Cube(name="Goal", pos=[-100,0,1], size=[0.3,4,2])
        pyrosim.End()

    def Set_ID(self, ID):
        self.myID = ID