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

    def Start_Simulation(self, directOrGUI):
        self.Create_Body()
        self.Create_Brain(self.myID)
        self.Create_World()
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " &")

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
        
        

    def Create_Body(self):
        #print(self.legweights)
        length = c.snake_length
        pyrosim.Start_URDF("body.urdf")

        save_y = random.randint(1,5)
        if length + 1 in c.sensors:
            pyrosim.Send_Cube(name="Head", pos=[-10,20,2.5] , size=[random.randint(1,5), save_y, random.randint(1,5)], color="Green")
        else:
            pyrosim.Send_Cube(name="Head", pos=[-10,20,2.5] , size=[random.randint(1,5), save_y, random.randint(1,5)])
        pyrosim.Send_Joint(name = "Head_Link0", parent = "Head", child = "Link0", type = "revolute", position= [-10,20-save_y/2,2.5], jointAxis = "0 0 1")

        for i in range(length):
            save_y = random.randint(1,5)
            if i in c.sensors:
                pyrosim.Send_Cube(name="Link" + str(i), pos=[0,-save_y/2,0] , size=[random.randint(1,5), save_y, random.randint(1,5)], color = "Green")
            else:
                pyrosim.Send_Cube(name="Link" + str(i), pos=[0,-save_y/2,0] , size=[random.randint(1,5), save_y, random.randint(1,5)])
            if i == length - 1: continue
            pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(i+1), parent = "Link" + str(i), child = "Link" + str(i+1), type = "revolute", position= [0,-save_y,0], jointAxis = "0 0 1")

            

        # pyrosim.Send_Cube(name="Torso", pos=[0,0,0.5] , size=[2,1,0.4])

        # #pyrosim.Send_Joint(name = "Torso_Backleg", parent = "Torso", child = "Backleg", type = "revolute", position= [0,-0.5,1], jointAxis = "1 0 0")
        # #pyrosim.Send_Cube(name="Backleg", pos=[0,-0.5,0] , size=[0.2,1,0.2])
        # # pyrosim.Send_Joint(name = "Backleg_Backbottom", parent = "Backleg", child = "Backbottom", type = "revolute", position= [0,-1,0], jointAxis = "1 0 0")
        # # pyrosim.Send_Cube(name="Backbottom", pos=[0,0,-1] , size=[0.2,0.2,2])

        # # pyrosim.Send_Joint(name = "Torso_Frontleg", parent = "Torso", child = "Frontleg", type = "revolute", position= [0,0.5,1], jointAxis = "1 0 0")
        # # pyrosim.Send_Cube(name="Frontleg", pos=[0,0.5,0] , size=[0.2,1,0.2])
        # # pyrosim.Send_Joint(name = "Frontleg_Frontbottom", parent = "Frontleg", child = "Frontbottom", type = "revolute", position= [0,1,0], jointAxis = "1 0 0")
        # # pyrosim.Send_Cube(name="Frontbottom", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        # # pyrosim.Send_Joint(name = "Torso_Leftleg", parent = "Torso", child = "Leftleg", type = "revolute", position= [-0.5,0,1], jointAxis = "0 1 0")
        # # pyrosim.Send_Cube(name="Leftleg", pos=[-0.5,0,0] , size=[1,0.2,0.2])
        # # pyrosim.Send_Joint(name = "Leftleg_Leftbottom", parent = "Leftleg", child = "Leftbottom", type = "revolute", position= [-1,0,0], jointAxis = "0 1 0")
        # # pyrosim.Send_Cube(name="Leftbottom", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        # # pyrosim.Send_Joint(name = "Torso_Rightleg", parent = "Torso", child = "Rightleg", type = "revolute", position= [0.5,0,1], jointAxis = "0 1 0")
        # # pyrosim.Send_Cube(name="Rightleg", pos=[0.5,0,0] , size=[1,0.2,0.2])
        # # pyrosim.Send_Joint(name = "Rightleg_Rightbottom", parent = "Rightleg", child = "Rightbottom", type = "revolute", position= [1,0,0], jointAxis = "0 1 0")
        # # pyrosim.Send_Cube(name="Rightbottom", pos=[0,0,-1] , size=[0.2,0.2,2])

        # #backleft
        # pyrosim.Send_Joint(name = "Torso_Backleg", parent = "Torso", child = "Backleg", type = "revolute", position= [0.8,-0.74,0.5], jointAxis = "0 1 0")
        # pyrosim.Send_Cube(name="Backleg", pos=[0,0,0] , size=[0.5,0.5,0.5])

        # #backright
        # pyrosim.Send_Joint(name = "Torso_Frontleg", parent = "Torso", child = "Frontleg", type = "revolute", position= [0.8,0.74,0.5], jointAxis = "0 1 0")
        # pyrosim.Send_Cube(name="Frontleg", pos=[0,0,0] , size=[0.5,0.5,0.5])

        # #frontleft
        # pyrosim.Send_Joint(name = "Torso_Rightleg", parent = "Torso", child = "Rightleg", type = "revolute", position= [-0.8,-0.74,0.5], jointAxis = "0 1 0")
        # pyrosim.Send_Cube(name="Rightleg", pos=[0,0,0] , size=[0.5,0.5,0.5])

        # #frontright
        # pyrosim.Send_Joint(name = "Torso_Leftleg", parent = "Torso", child = "Leftleg", type = "revolute", position= [-0.8,0.74,0.5], jointAxis = "0 1 0")
        # pyrosim.Send_Cube(name="Leftleg", pos=[0,0,0] , size=[0.5,0.5,0.5])

        # # # kicker
        # # pyrosim.Send_Cube(name="Torso", pos=[0,1.5,1] , size=[1,1,2])
        # # pyrosim.Send_Joint(name = "Torso_Backleg", parent = "Torso", child = "Backleg", type = "revolute", position= [0,1,1.5], jointAxis = "0 1 0")
        # # pyrosim.Send_Cube(name="Backleg", pos=[0,-0.25,-0.6] , size=[0.5,0.5,1.2])
        
        pyrosim.End()

        

    def Create_Brain(self, ID):
        pyrosim.Start_NeuralNetwork("brain" + str(ID) + ".nndf")


        name_count = 0
        if c.snake_length + 1 in c.sensors:
            pyrosim.Send_Sensor_Neuron(name = name_count , linkName = "Head")
            pyrosim.Send_Motor_Neuron( name = name_count + 1 , jointName = "Head_Link0")
            name_count += 2


        for i in range(c.snake_length):
            if i in c.sensors:
                pyrosim.Send_Sensor_Neuron(name = name_count , linkName = "Link" + str(i))
                name_count += 1
                if i == c.snake_length - 1: continue
                pyrosim.Send_Motor_Neuron( name = name_count , jointName = "Link" + str(i) + "_Link" + str(i+1))
                name_count += 1


        # pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        # pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Backleg")
        # pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Frontleg")
        # pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "Leftleg")
        # pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "Rightleg")
        # # # pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "Backbottom")
        # # # pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "Frontbottom")
        # # # pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "Leftbottom")
        # # # pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "Rightbottom")
        # pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_Backleg")
        # pyrosim.Send_Motor_Neuron( name = 6, jointName = "Torso_Frontleg")
        # pyrosim.Send_Motor_Neuron( name = 7, jointName = "Torso_Leftleg")
        # pyrosim.Send_Motor_Neuron( name = 8, jointName = "Torso_Rightleg")
        # pyrosim.Send_Motor_Neuron( name = 13, jointName = "Backleg_Backbottom")
        # pyrosim.Send_Motor_Neuron( name = 14, jointName = "Frontleg_Frontbottom")
        # pyrosim.Send_Motor_Neuron( name = 15, jointName = "Leftleg_Leftbottom")
        # pyrosim.Send_Motor_Neuron( name = 16, jointName = "Rightleg_Rightbottom")

        #nested for loop from K below:
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + c.numSensorNeurons, weight = self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Create_World(self):
        pyrosim.Start_SDF("world1.sdf")
        pyrosim.Send_Sphere(name="Sphere", pos=[-300,0,0.5] , size=[0.5])
        pyrosim.Send_Cube(name="Goal", pos=[-100,0,1], size=[0.3,4,2])
        pyrosim.End()

    def Set_ID(self, ID):
        self.myID = ID