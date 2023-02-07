import pybullet as p
import pyrosim.pyrosim as pyrosim

class WORLD:

    def __init__(self):

        self.planeId = p.loadURDF("plane.urdf")
        self.ballId = p.loadSDF("world1.sdf")
        #p.loadSDF("world1.sdf")
