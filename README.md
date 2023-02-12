
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
