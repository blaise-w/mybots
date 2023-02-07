
A short description of my changes:

My goal was to create a car-like creature with spherical wheels to push a ball into a goal (think RocketLeague).

First, I rebuilt the robot to have spherical wheels and a car-like body using my own custom body.urdf file based on a CampusWire post.

Then, I added a ball and a wall to simulate a soccer ball and a goal.

To keep it simple, my goal was just a wall. In my fitness function I could keep track of whether or not a goal was scored by the z-position of the wall.

I trained my fitness function by optimizing on the x-position of the ball, the x-position of the car. I divided by the z-position of the wall to ensure that goal scoring was prioritized.
