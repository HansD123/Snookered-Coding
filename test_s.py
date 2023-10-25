# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 15:52:36 2022

@author: hansd
"""
import ball_s
b = ball_s.Ball
import simulationv2_s
s = simulationv2_s.Simulation2
import numpy as np
import matplotlib.pyplot as plt

#%% Ball class test (Task 2)
ball_1 = b(1, 2, [3,4], [5,6])   #Testing initialization

b.mass(ball_1)    #Testing parameters of ball
b.rad(ball_1)
b.pos(ball_1)
b.vel(ball_1)

b.move(ball_1,7)   #Testing move function
b.pos(ball_1)



ball_1 = b(1, 2, [3,4],[5,6]) #Testing time_to_collision function
ball_2 = b(4,3,[2,1],[7,8]) 
time_12 = b.time_to_collision(ball_1, ball_2)
print("Balls 1 and 2 collide at",time_12,"s")

ball_3 = b(2,2,[-3,-4],[-5,-6])
time_13 = b.time_to_collision(ball_1,ball_3)
print(time_13)
#%% # Testing collision function
b.move(ball_1,time_12)
b.move(ball_2,time_12)
print("Before collision:")
print("Ball 1")
b.vel(ball_1)
b.pos(ball_1)
print("Ball 2")
b.vel(ball_2)
b.pos(ball_2)
b.collision(ball_1,ball_2)
print("After collision:")
print("Ball 1")
b.vel(ball_1)
b.pos(ball_1)
print("Ball 2")
b.vel(ball_2)
b.pos(ball_2)
"""
Position of the balls have stayed the same but their velocities have changed due
to the collision
"""
#%% Calling the ball class incorrectly
ball_error1 = b(-4,2,[3,1],[5,9])
#%%Calling the ball class incorrectly
ball_error2 = b(4,2,[3,2,1],[3,3])
#%% Testing collision with circle container by directly using ball functions
ball_1 = b(1,2,[3,4],[5,6])
circle_1 = b(0,20,[2,3],[0,0],True)
time_c1  = b.time_to_collision(ball_1, circle_1)
print("Collision occurs at",time_c1,"s")
b.move(ball_1,time_c1)
print("Before collision")
b.vel(ball_1)
b.collision(ball_1,circle_1)
print("After collision")
b.vel(ball_1)
#%% Testing simulation  (Task 3)
ball_1 = b(1,2,[3,4],[5,6])
sim = s(circle_1,ball_1)
s.container_variables(sim)
print("Ball variables before collision:")
s.ball_variables(sim,1)
s.next_collision(sim)#Collision of ball with container using simulation next_collision function
print("Ball variables after collision:")
s.ball_variables(sim,1)
#%% Calling the Simulation class incorrectly
sim_error1 = s(ball_1,ball_1)
#%% Calling the simulation class incorrectly
sim_error2 = s(circle_1,circle_1)
#%% Task 4
"""
Creating a cirlce with radius 10 centered at (0,0) and a ball with mass:11,
radius:1,position:(-5,0) and velocity:(1,0)
"""
c_task4 = b(0,10,[0,0],[0,0],True) 
b_task4 = b(1,1,[-5,0],[1,0])
sim_task4 = s(c_task4,b_task4)
print("Time to collision is",b.time_to_collision(b_task4,c_task4),"s")
s.next_collision(sim_task4)
print("Ball variables after collision:")
s.ball_variables(sim_task4,1)
"""
Running next_collision two more times
"""
s.next_collision(sim_task4)
print("Ball variables after collision 2:")
s.ball_variables(sim_task4,1)
s.next_collision(sim_task4)
print("Ball variables after collision 3:")
s.ball_variables(sim_task4,1)
"""
Now a ball with a velocity of (1,-5)m/s is used instead
"""
b_task4 = b(1,1,[-5,0],[1,-5])
sim_task4 = s(c_task4,b_task4)
print("Time to collision is now",b.time_to_collision(b_task4,c_task4),"s")
s.next_collision(sim_task4)
print("Ball variables after collision are now:")
s.ball_variables(sim_task4,1)
#%%Task 5 Animation (use %matplotlib auto to display correctly)
circle_task5 = b(0,30,[5,-8],[0,0],True)
ball_task5 = b(15,4,[10,0],[-4,-8])
sim_task5 = s(circle_task5,ball_task5)
s.run(sim_task5,50,0.4,True)
#%% Task 6
circle_task6 = b(0,30,[5,4],[0,0],True)
ball_task6 = b(5,4,[4,0],[2,-8])
sim_task6 = s(circle_task6,ball_task6)
"""
Conservation of energy
"""
print("Initially:")
print("The kinetic energy is",s.kinetic_energy(sim_task6),"J")
s.run(sim_task6,10,False)
print("After 10 collisions:")
print("The kinetic energy is",s.kinetic_energy(sim_task6),"J")
"""
Conservation of momentum
"""
print("Initially:")
print("The momentum is",s.momentum(sim_task6),"kgm/s")
s.run(sim_task6,9,False)
print("After 10 collisions:")
print("The momentum is",s.momentum(sim_task6),"kgm/s")
"""
Pressure calculation
"""
print("The pressure is",s.pressure(sim_task6),"kgs-2")
#%% Task 7 Adding 2 more balls to the simulation
circ7 = b(0,40,[0,0],[0,0],True)
ball71 = b(1,1,[5,0],[-1,0])
ball72 = b(1,1,[-5,0],[1,0])
ball73 = b(2,1,[-10,-10],[5,0])
sim7 = s(circ7,ball71)
s.add_ball(sim7,ball72)
s.add_ball(sim7,ball73)
s.run(sim7,50,0.5,True)
#%% Changing the container
circ7b = b(0,50,[0,1],[0,0],True)
s.change_container(sim7,circ7b)
s.run(sim7,10,0.5,True)
#%%Testing number of balls
circ7 = b(0,40,[0,0],[0,0],True)
ball71 = b(1,1,[5,0],[-1,0])
ball72 = b(1,1,[-5,0],[1,0])
ball73 = b(2,1,[-10,-10],[5,0])
sim7 = s(circ7,ball71)
s.add_ball(sim7,ball72)
s.add_ball(sim7,ball73)
print(s.number_balls(sim7))#There are initially 3 balls
ball74 = b(4,3,[0,5],[2,2])
s.add_ball(sim7,ball74) #adding a ball to check number changes
print(s.number_balls(sim7))
s.delete_balls(sim7)#deleting all balls
print(s.number_balls(sim7))
#%% Conservation of energy and momentum with multiple balls
print("The kinetic energy is",s.kinetic_energy(sim7),"J")
print("The momentum is",s.momentum(sim7),"kgm/s")
print("The pressure is",s.pressure(sim7),"kgs-2")
print("After 20 collisions")
s.run(sim7,20,0.01,False)
print("The kinetic energy is",s.kinetic_energy(sim7),"J")
print("The momentum is",s.momentum(sim7),"kgm/s")
print("The pressure is",s.pressure(sim7),"kgs-2")
#%% task 8 testing random square generation
circ7 = b(0,40,[0,0],[0,0],True)
sim8 = s(circ7)
s.random_square(sim8,5,5,False)
s.run(sim8,100,0.01,True)
"""
Creating a 5x5 square of balls with the same mass and radius and random velocities
which average to 0. The masses are all 1kg and the radii are all equal to 1/6 of the
distance between two adjacent balls in the square. The velocity x and y 
components are randomly generated real numbers from -5 to 5 m/s.
"""
sim8 = s(circ7)
s.random_square(sim8,8,5,True)

s.run(sim8,100,0.01,True)
"""
Creating a 5x5 square of balls with random mass and radius and random velocities
which average to 0. The masses are random real numbers from 1-10 kg, the radii
vary randomly from 1/10 to 1/4 of the distance between two adjacent balls in 
the square. The velocity x and y components are randomly generated real numbers
from -5 to 5 m/s.
"""
#%% Static test (use %matplotlib inline)
circ7 = b(0,40,[0,0],[0,0],True)
sim8 = s(circ7)
s.random_square(sim8,8,5,False)
s.static(sim8)
s.run(sim8,25,0.01,False)
s.static(sim8)
#%% Testing square_constant
circ7e = b(0,40,[0,0],[0,0],True)
sim8 = s(circ7e)
s.square_constant(sim8,4,2,1e23) #creates a simulation at 1e23 K
print(s.temperature(sim8)) #temperature matches what was called in the function
print(s.ball_variables(sim8,1))
print(s.ball_variables(sim8,3))
print(s.ball_variables(sim8,5))
"""
Balls have equal variables except for position
"""
#%% Testing radii_square
circ7e = b(0,40,[0,0],[0,0],True)
sim8 = s(circ7e)
s.radii_square(sim8,4,0.1,2)
s.static(sim8)
sim8 = s(circ7e)
s.radii_square(sim8,4,0.9,2)
s.static(sim8)
#%% Testing new kinetic energy, pressure and momentum formulae for multiple balls
"""
Simulating 49 balls inside a container with the same mass and radius and
random velocities
"""
circ8a = b(0,15,[5,5],[0,0],True)
sim81 = s(circ8a)
s.random_square(sim81,7,5,False)
print("Intitially:")
print("The kinetic energy is",s.kinetic_energy(sim81),"J")
print("The momentum is",s.momentum(sim81),"kgm/s")
print("The pressure is",s.pressure(sim81),"kgs-2")
s.run(sim81,100,0.01,True)
print("After 100 collisions:")
print("The kinetic energy is",s.kinetic_energy(sim81),"J")
print("The momentum is",s.momentum(sim81),"kgm/s")
print("The pressure is",s.pressure(sim81),"kgs-2")
"""
The kinetic energy and momenum vector are conserved as expected. Pressure is 
conserved beacause pressure is proportional to rms speed, and speed and velocity
are conserved between collisions because all balls have the same mass, thus the 
pressure will be constant between collisions.
"""
#%% Testing when a simulation is ran with no balls
circle1000 = b(0,20,[2,2],[0,0],True)
sim1000 = s(circle1000)
s.run(sim1000,50,0.5,False)
#%%
"""
Simultaing 36 balls inside a container with random mass, radius and velocity
"""
circ8b = b(0,10,[0,0],[0,0],True)
sim84 = s(circ8b)
s.random_square(sim84,6,5,True)
print("Intitially:")
print("The kinetic energy is",s.kinetic_energy(sim84),"J")
print("The momentum is",s.momentum(sim84),"kgm/s")
print("The pressure is",s.pressure(sim84),"kgs-2")
s.run(sim84,100,0.01,True)
print("After 100 collisions:")
print("The kinetic energy is",s.kinetic_energy(sim84),"J")
print("The momentum is",s.momentum(sim84),"kgm/s")
print("The pressure is",s.pressure(sim84),"kgs-2")
"""
The kinetic energy and momenum vector are conserved as expected. The pressure 
however is not conserved because when balls of different masses collide,
the velocity is not always conserved and so the total velocity and so speed
of the system will vary between collisions, resulting in the pressure varying
as it is proportional to rms speed
"""
#%% Task 9
"""
Producing histograms of distance from centre against number of balls for
100 balls with random velocities, mass and radius.
"""
circ9 = b(0,20,[2,1],[0,0],True)
sim9 = s(circ9)
s.random_square(sim9,10,5,True)
plt.title("Initially")
s.distance_from_centre(sim9)
s.run(sim9,100,0.01,False)
plt.title("After 100 collisions")
s.distance_from_centre(sim9)
s.run(sim9,100,0.01,False)
plt.title("After 200 collisions")
s.distance_from_centre(sim9)
s.run(sim9,100,0.01,False)
plt.title("After 300 collisions")
s.distance_from_centre(sim9)
s.run(sim9,100,0.01,False)
plt.title("After 400 collisions")
s.distance_from_centre(sim9)
"""
These histograms are as expected with there being more balls the further away 
from the centre. This is because for the histogram bar ranges that cover a large
distance from the centre, the proportion of the area of the circle that the bar 
represents is larger, and so balls are more likely to be there, meaning there 
are more balls further away from the centre than close to the centre.
"""
#%% Task 9 part 2
"""
Producing histograms of distance between the ball pairs against the number of ball
pairs, with 36 balls with random velocities but equal mass and radius
"""
circ9b = b(0,20,[2,1],[0,0],True)
sim9b = s(circ9b)
s.random_square(sim9b,6,5,False)
plt.title("Initially")
s.distance_between_balls(sim9b)
s.run(sim9b,10,0.01,False)
plt.title("After 100 collisions")
s.distance_between_balls(sim9b)
s.run(sim9b,100,0.01,False)
plt.title("After 200 collisions")
s.distance_between_balls(sim9b)
s.run(sim9b,100,0.01,False)
plt.title("After 300 collisions")
s.distance_between_balls(sim9b)
s.run(sim9b,100,0.01,False)
plt.title("After 400 collisions")
s.distance_between_balls(sim9b)
"""
These histograms are as expected. The balls are most likely to be around half
the diammeter of the container away from each other, and much less likely to
be the whole diammeter away or right next to each other. This results in a 
guassian distribution which is centered at the radius of the container and 
tails off as the distance approaches 0 and the diammeter of the container.
"""
#%% Temperature function
circt = b(0,30,[0,0],[0,0],True)
simt = s(circt)
s.random_square(simt, 8, 4)
s.run(simt,50,0.01,False)
print("The temperature is",s.temperature(simt),"K")
"""
The temperature is extremely high because the particles are modelled as having 
masses of in the kilograms which is many orders of magntitude higher than a
typical particles mass which is of 10-26 kg
"""