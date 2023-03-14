Evolving Virtual Creatures: An Introduction
Are you fascinated by the idea of creating robots that can adapt and evolve on their own? Do you want to learn how to use machine learning techniques to design and optimize robot behaviors? If so, then you're in the right place!

In this project, we explore the world of evolutionary robotics, where we use algorithms inspired by natural selection to evolve virtual creatures that can achieve locomotion. By randomly generating initial populations of robots and allowing them to evolve over multiple generations, we can create robots that are increasingly better at navigating their environments and completing tasks.

Getting Started
To get started with this project, simply clone the repository and follow the instructions in the README file. You'll need to have access to a computer with the necessary software installed (e.g., Python, Pybullet, Pyrosim, etc.) and preferrably some basic knowledge of programming concepts like data structures, algorithms, and machine learning. To run my code, simply run the search.py file. You may also want to specify the "numberOfGenerations" and "populationSize" variables in the constants.py file, which correspond to the number of times we select for a robot with better fitness, and the number of different random robots we have in each generation. These are defaulted at 1000 generations and 10 robots.

Generating and Mutating Robots
To generate the initial population of robots, we use a randomization process that creates a variety of body shapes and sizes. Each robot's body is defined by a set of parameters, such as the length and thickness of its limbs, the size and shape of its each body part, the direction a limb is placed in, and the location of its joints. Bodies are not simply defined to a torso and limbs-- during the generation process, any limb can be placed on any other limb on the body and in any direction and size (so long as it does not intersect or overlap with other limbs. Limbs are color-coded green and blue. A green limb is a sensor neuron and a blue limb is a motor neuron.

Sensor neurons feed information to the brain, a neural network that controls its movements. To generate the initial population of neural networks, we use a randomization process that creates a variety of connection weights. The brain relays information to the motor neurons, which fire to change the angle of the limb, allowing for the potential for movement. The brain is evolved by randomly changing weights in each generation, which, as in the body, are maintained in the population if they lead to an increase in fitness. This process runs concurrently with evolutions to the body.

After generating the initial population, we introduce genetic variation by mutating each robot's body. We do this by randomly changing a single value of the body parameters for each member of the population. A given mutation can change the size of a joint, the axis it rotates on, where it is placed, and the direction it is placed in. If this introduces new variations in body structure that lead to improved locomotion, the mutation remains in the population, otherwise no changes are made.

The Evolutionary Algorithm
At the heart of this project is the evolutionary algorithm, which is a process inspired by natural selection. This is contained in the parallelHillClimber.py file. We begin by creating a population of virtual creatures with random bodies and brains. Each step is simulated with fitness being determined by distance from the origin of the virtual environment. Each creature is evaluated based on its ability to achieve locomotion, and if a given creature has a higher fitness value than its parent, it replaces the parent in the population.

My Experiment
The way that robot bodies were mutated was by modifying a random value among three differents lists of random numbers. These numbers would then be used to generate the body of a given robot. The three different lists correspond to the size and axis of each limb, the directions each limb would be placed in, and where on the body each limb was placed. This led to three different possible types of mutations for a given robot. They were grouped this way simply for coding convenience, but it still raised the question-- how does the type of mutation affect the ability of a given population to achieve locomotion?

In our control trials, a given mutation occured by selecting one of these lists at 1/3 probability each and editing one value within the list. The experimental trials modified the probability of selecting each list for a mutation. In experimental group 1, the probability of changing the location of the limb placement was increased to 2/3 while the probability of the other types of mutations were reduced to 1/6 each. In experimental group 2, the probability of changing the limb directions was increased to 2/3 while the other mutation types were reduced. Likewise, in group 3, the probability mutations affecting the limb size and axis were increased.

For each of the four groups, 10 simulations were run, each having 10 creatures in the population and evolving over 1000 generations. This is a total of 400,000 simulated robots.

My Hypothesis
Changing the limb size or its rotational axis is a mutation that is likely to only affect a single limb-- even if the mutated limb has another limb coming from it, that limb will stay in relatively the same place. However, for mutations that affect the placement and direction of a limb, this may affect the structure of the entire creature. My hypothesis is that groups 1 and 2 will mutate faster and achieve much more variance in their fitness values, while group 3 will be much more consistent. I think that groups 1 and 2 will achieve the highest fitness values, but will, on average, have lower fitness values than the control group and group 3.

The Results
The results of our evolutionary algorithm are impressive. By allowing the creatures to evolve over multiple generations, we can create robots that are increasingly better at achieving locomotion. We can also explore the impact of different parameters on the performance of the creatures, such as the mutation rate, the population size, and the fitness function.

Overall, this project provides a fascinating glimpse into the world of evolutionary robotics and the potential for using machine learning to create intelligent and adaptive robots. I hope you find this project as engaging and inspiring as I did, and I encourage you to share it with your friends and colleagues. Let's continue to push the boundaries of what's possible with virtual creatures and evolutionary algorithms!

Resources:
CS 396 Artificial Life -- Prof. Sam Kriegman
https://www.reddit.com/r/ludobots/
https://www.thunderheadeng.com/pyrosim



