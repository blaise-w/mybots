
12/6: A short description of my changes

My goal was to create a car-like creature with spherical wheels to push a ball into a goal (think RocketLeague).

First, I rebuilt the robot to have spherical wheels and a car-like body using my own custom body.urdf file based on a CampusWire post.

Then, I added a ball and a wall to simulate a soccer ball and a goal.

To keep it simple, my goal was just a wall. In my fitness function I could keep track of whether or not a goal was scored by the z-position of the wall.

I trained my fitness function by optimizing on the x-position of the ball, the x-position of the car. I divided by the z-position of the wall to ensure that goal scoring was prioritized.




2/12: Random Snakes

I made modifications to mostly the solutions and constants files.

I generated a sequence of links of different sizes between 1-5 in length, width, and height.

The number of links was random 1-10. This was generated in the constants file as well as which links would be sensors.

Within my create_brain() function, I used the list of which links would be sensors (c.sensors) to generate the correct sensors.

Within my create_body() function, I looped over the length of the snake to create random links. I checked with c.sensors to determine the color of the link.

Other edited files were to modify joint angles and motor power to allow the snake to move, as well as allowing for color to be passed in create_link().




2/14: Random 3D Creatures

Again, I mainly made modifications in the solutions file.

This time I was modifying the code I wrote earlier this week to generate in 3 dimensions.

This pretty much only affected my Create_Body() function. I continued using a loop over the number of segments in the creature's body. But this time, I chose a direction to add in using a random number 1-5. This corresponded to -y, +y, -x, +x, and +z. I did not generate in the -z direction because I didn't want to deal with sections of the body going below the floor.

Just like with the snake, I would add a link one half the link-size in the direction we chose.

I wanted to choose a random place on the body to add the next link, so I used random.randint() againt to get a random link.

I had trouble with stopping links from generating inside eachother, so I implemented a simple loop that chose a new direction to add in if there was already a link coming out of the chosen link in that direction. If the link was completely full, I chose another link to add to.

Addtionally, I had a problem with adding in one direction (e.g. positive x) and immediately adding a link from the new link in the opposite direction (e.g. negative x from the link we just added). I solved this by choosing a different direction if opposite directions were immediately chosen.

The most difficult part of generating creatures in 3D was the joint placement. With the first join being 100% absolute, I wrote an if statement for each of the five possible directions to determine where the joint would go. This was the easy part. 

After i == 0, I had to take into account not only the next direction, but also the current direction. The result was 5 if statments for each of five directions, each with 5 if statements inside them. There may have been a more efficient way to do this. 

Other significant changes I made included the simulation file (removing the side bars in the display), the constants, and the motor file (these were to allow the robot to properly move with all the new and interlocking joints.

A short summary of the overall potential:

Any body type is possible as I went with a completely random approach. A shortcoming of this approach is that, despite my efforts it is still possible for limbs to overlap. Stopping this would likely require completely redoing my approach to body generation or keeping track of which 3d spaces are occupied

When it comes to the brain, motors are only controlled by the sensors they are adjacent to. I am unsure of what types of gaits these creatures will be able to develop as they simply jerk around randomly. My guess is that sensors connected to motors will simply act as legs to push the creature forward.

The end result are these screenshots:

<img width="252" alt="Screen Shot 2023-02-14 at 6 59 19 PM" src="https://user-images.githubusercontent.com/93502887/218897857-b8ccb09a-6b05-4c50-90ea-5b21e6462cbd.png">

<img width="311" alt="Screen Shot 2023-02-14 at 6 58 59 PM" src="https://user-images.githubusercontent.com/93502887/218898025-4b8f2ae6-3657-4118-99f3-014f820ad1d6.png">

A video of the random 3d creatures flailing around can be found here: https://www.youtube.com/watch?v=HFQinGk2pSI

Resources:
https://www.reddit.com/r/ludobots/
https://www.thunderheadeng.com/pyrosim
