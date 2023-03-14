**need to add abc from canvas
pickles + explanation to use
video, results


https://user-images.githubusercontent.com/93502887/225125639-c5f5ea70-3097-472b-b8b9-758dddffaa42.mp4

Evolving Virtual Creatures: An Introduction

Are you fascinated by the idea of creating robots that can adapt and evolve on their own? Do you want to learn how to use machine learning techniques to design and optimize robot behaviors? If so, then you're in the right place!

<img width="585" alt="Screen Shot 2023-03-13 at 11 38 12 PM" src="https://user-images.githubusercontent.com/93502887/224894682-cb48da86-af3b-47f5-9c8c-305c177f2b45.png">

<img width="581" alt="Screen Shot 2023-03-13 at 11 38 43 PM" src="https://user-images.githubusercontent.com/93502887/224894741-6822b4a2-2fc8-451f-a230-5274629e6da2.png">

In this project, we explore the world of evolutionary robotics, where we use algorithms inspired by natural selection to evolve virtual creatures that can achieve locomotion. By randomly generating initial populations of robots and allowing them to evolve over multiple generations, we can create robots that are increasingly better at navigating their environments and completing tasks.

Getting Started

To get started with this project, simply clone the repository and follow the instructions in the README file. You'll need to have access to a computer with the necessary software installed (e.g., Python, Pybullet, Pyrosim, etc.) and preferrably some basic knowledge of programming concepts like data structures, algorithms, and machine learning. To run my code, simply run the search.py file. You may also want to specify the "numberOfGenerations" and "populationSize" variables in the constants.py file, which correspond to the number of times we select for a robot with better fitness, and the number of different random robots we have in each generation. These are defaulted at 1000 generations and 10 robots.

Generating and Mutating Robots

To generate the initial population of robots, we use a randomization process that creates a variety of body shapes and sizes. Each robot's body is defined by a set of parameters, such as the length and thickness of its limbs, the size and shape of its each body part, the direction a limb is placed in, and the location of its joints. Bodies are not simply defined to a torso and limbs-- during the generation process, any limb can be placed on any other limb on the body and in any direction and size (so long as it does not intersect or overlap with other limbs. Limbs are color-coded green and blue. A green limb is a sensor neuron and a blue limb is a motor neuron. This is all randomized. The steps for body generation are diagramed below.

<img width="1315" alt="Screen Shot 2023-03-13 at 11 39 48 PM" src="https://user-images.githubusercontent.com/93502887/224894887-40af6ed6-1de2-4923-b83c-94e30c4b1d9d.png">

<img width="646" alt="Screen Shot 2023-03-13 at 11 40 09 PM" src="https://user-images.githubusercontent.com/93502887/224894926-b3bbc2eb-82ed-43a0-a98a-1dc2e9306ad5.png">

Sensor neurons feed information to the brain, a neural network that controls its movements. To generate the initial population of neural networks, we use a randomization process that creates a variety of connection weights. The brain relays information to the motor neurons, which fire to change the angle of the limb, allowing for the potential for movement. The brain is evolved by randomly changing weights in each generation, which, as in the body, are maintained in the population if they lead to an increase in fitness. This process runs concurrently with evolutions to the body.

After generating the initial population, we introduce genetic variation by mutating each robot's body. We do this by randomly changing a single value of the body parameters for each member of the population. A given mutation can change the size of a joint, the axis it rotates on, where it is placed, and the direction it is placed in. If this introduces new variations in body structure that lead to improved locomotion, the mutation remains in the population, otherwise no changes are made.

<img width="680" alt="Screen Shot 2023-03-13 at 11 41 03 PM" src="https://user-images.githubusercontent.com/93502887/224895030-268af67b-31c7-45c1-887d-f70b9bda3828.png">

<img width="1282" alt="Screen Shot 2023-03-13 at 11 41 23 PM" src="https://user-images.githubusercontent.com/93502887/224895078-7cb58d27-700b-45db-8867-19b1daedc7a3.png">

The Evolutionary Algorithm

At the heart of this project is the evolutionary algorithm, which is a process inspired by natural selection. This is contained in the parallelHillClimber.py file. We begin by creating a population of virtual creatures with random bodies and brains. Each step is simulated with fitness being determined by distance from the origin of the virtual environment. Each creature is evaluated based on its ability to achieve locomotion, and if a given creature has a higher fitness value than its parent, it replaces the parent in the population. Below is a example graph of the highest fitness value in the population as the number of generations evolved increases.

<img width="629" alt="Screen Shot 2023-03-13 at 4 40 39 PM" src="https://user-images.githubusercontent.com/93502887/224895623-5e7fefb7-7506-49c5-92ac-de43b40c1639.png">

My Experiment

The way that robot bodies were mutated was by modifying a random value among three differents lists of random numbers. These numbers would then be used to generate the body of a given robot. The three different lists correspond to the size and axis of each limb, the directions each limb would be placed in, and where on the body each limb was placed. This led to three different possible types of mutations for a given robot. They were grouped this way simply for coding convenience, but it still raised the question-- how does the type of mutation affect the ability of a given population to achieve locomotion? This is an important question for understanding evolution itself and could have potential biology applications. (E.g. what types of changes to DNA would most affect a real-life specimen).

<img width="678" alt="Screen Shot 2023-03-13 at 11 43 29 PM" src="https://user-images.githubusercontent.com/93502887/224895399-b1bd907a-4317-4390-8b95-f5a9168cff13.png">

<img width="579" alt="Screen Shot 2023-03-13 at 11 44 17 PM" src="https://user-images.githubusercontent.com/93502887/224895480-e3424766-2a79-4711-86f2-4091bd05df05.png">


In our control trials, a given mutation occured by selecting one of these lists at 1/3 probability each and editing one value within the list. The experimental trials modified the probability of selecting each list for a mutation. In experimental group 1, the probability mutations affecting the limb size and axis was increased to 2/3 while the probability of the other types of mutations were reduced to 1/6 each. In experimental group 2, the probability of changing the joint directions was increased to 2/3 while the other mutation types were smilarly reduced. Likewise, in group 3, the probability of changing the location of the limb placement was increased while other mutations types were reduced.

For each of the four groups, 10 simulations were run, each having 10 creatures in the population and evolving over 1000 generations. This is a total of 400,000 simulated robots.

My Hypothesis

Changing the limb size or its rotational axis is a mutation that is likely to only affect a single limb-- even if the mutated limb has another limb coming from it, that limb will stay in relatively the same place. However, for mutations that affect the placement and direction of a limb, this may affect the structure of the entire creature. My hypothesis is that groups 1 and 2 will mutate faster and achieve much more variance in their fitness values, while group 3 will be much more consistent. I think that groups 1 and 2 will achieve the highest fitness values, but will, on average, have lower fitness values than the control group and group 3.

The Results

In each trial, the same seeds, (the same random numbers) were used. The results are as follows:

Control Group:

<img width="629" alt="Screen Shot 2023-03-13 at 4 40 39 PM" src="https://user-images.githubusercontent.com/93502887/224895623-5e7fefb7-7506-49c5-92ac-de43b40c1639.png">

Group 1:

<img width="836" alt="Screen Shot 2023-03-14 at 6 37 48 PM" src="https://user-images.githubusercontent.com/93502887/225165747-f5a26f22-d97b-4f65-aca8-86f2e09b8a3e.png">

Group 2:

<img width="816" alt="Screen Shot 2023-03-14 at 6 36 31 PM" src="https://user-images.githubusercontent.com/93502887/225165567-b53cd378-bddf-4e75-a339-49937e0af523.png">

Group 3:

<img width="843" alt="Screen Shot 2023-03-14 at 6 34 58 PM" src="https://user-images.githubusercontent.com/93502887/225165390-61b3487b-2046-4814-a3cb-606e713ee8c9.png">

We can see that my hypothesis was incorrect-- the group that had higher rates of mutation in the joint axis and size achieved the highest fitness values of all, including those of the control group. It does seem that, as predicted, this group had more consistent success than the other experimental groups at achieving locomotion. However, it also should be noted that the control group had the fewest stationary robots-- ones that had a final fitness value of less than 10. I think that this can be attributed to the diversity of different mutations in the control group. If a robot

Group 3 had some interesting behavior that I predicted in my hypothesis. Group 3 had increased rates of mutation in joint placement. This meant that a single mutation could drastically change the entire structure of the body. We could see this realized in seeds 10 and 3 of group 3, which saw little to no movement and after a single mutation saw their fitness values spike. After these beneficial mutations, their fitness values did not increase any more, meaning that no other beneficial mutation occured.

With more time, I'd like to explore various groupings of potential mutation types as well as exploring additional mutations including those to the brain. An area with huge potential for behavioral changes in the creatures is implementing a layered neural network in the brain. Additionally, I'd like to explore how varying mutation rate over time affects the fitness of the population.

Overall, this project provides a fascinating glimpse into the world of evolutionary robotics and the potential for using machine learning to create intelligent and adaptive robots. I hope you find this project as engaging and inspiring as I did, and I encourage you to share it with your friends and colleagues. Let's continue to push the boundaries of what's possible with virtual creatures and evolutionary algorithms!

Resources:

CS 396 Artificial Life -- Prof. Sam Kriegman

https://www.reddit.com/r/ludobots/

https://www.thunderheadeng.com/pyrosim



