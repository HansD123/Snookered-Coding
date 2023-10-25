# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 14:44:53 2022

@author: hansd
"""

"""
This script is where the graphs for the main investigation are produced from.
Graphs will differ slightly each time the code is run due to the randomness
of the ball properties when using random_square function to generate large 
groups of balls
"""
import ball_s
b = ball_s.Ball
import simulationv2_s
s = simulationv2_s.Simulation2
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#%% Task 10 kinetic energy vs temperature
"""
Code produces a graph of temperature against kinetic energy. A simulation with
36 balls with random velocities, but constant mass and radius is created and
then the kientic energy and temperature are then measured. The simulation is
re-created 50 times with the randomness of the properties of the balls varying
the kinetic energy and temperature enough that the relationship between 
temperature and kinetic energy of the system can be graphed.
"""
kinetic_energies = np.array([])
temperatures =np.array([])
for j in range(50):
    circle10 = b(0,20,[0,0],[0,0],True)
    sim10 = s(circle10)
    s.random_square(sim10,6,5,False)
    kinetic_energies = np.append(kinetic_energies,s.kinetic_energy(sim10))
    temperatures = np.append(temperatures,s.temperature(sim10))
plt.xlabel("Temperature (K)")
plt.ylabel("Kinetic energy (J)")
plt.scatter(temperatures,kinetic_energies)
plt.show()
"""
Kinetic energy is directly proportional to temperature. This is as expected for
an ideal gas
"""
#%% conservation of momentum
"""
Momentum is also conserved in the system at all points
"""
circle10 = b(0,20,[0,0],[0,0],True)
sim10 = s(circle10)
s.random_square(sim10,6,5,True)
print("Initially:")
print("The momentum is",s.momentum(sim10),"kgm/s")
s.run(sim10,50,0.01,False)
print("After 50 collisions:")
print("The momentum is",s.momentum(sim10),"kgm/s")
s.run(sim10,50,0.01,False)
print("After a further 50 collisions:")
print("The momentum is",s.momentum(sim10),"kgm/s")
#%% Doubling velocity of simulation
"""
A simulation is created with 26 balls which all have the same velocity of 
(1,1)m/s. The temperature and pressure are caluclated and then the simultaion   
is repeated but with the balls having a velocity of (2,2)m/s
"""
circle10b = b(0,5,[0,0],[0,0],True)
sim10b = s(circle10b)
s.square_constant(sim10b,5,1)
s.run(sim10b,500,0.001,True)
print("For a velocity of (1,1)m/s for all balls:")
print("The pressure is",s.pressure(sim10b),"kgs-2")
print("The temperature is",s.temperature(sim10b),"K")
circle10c = b(0,5,[0,0],[0,0],True)
sim10c = s(circle10c)
s.square_constant(sim10c,5,2)
s.run(sim10c,500,0.001,True)
print("For a velocity of (2,2)m/s for all balls:")
print("The pressure is",s.pressure(sim10c),"kgs-2")
print("The temperature is",s.temperature(sim10c),"K")
"""
As expected, the pressure doubles as the velocity is doubled. This is because 
pressure is proportional to rms speed. When the velocity is doubled, the balls 
spread more quickly in the animation and balls cover larger distances between 
collisions. The temperature increases by a factor 4 or 2 squared because 
temperature is proportional to kinetic energywhich is proportional to velocity
squared and so will increase by the square of the increase of velocity.
"""
#%% Task 11 kientic energy conservation
"""
Plotting number of collisions against kientic energy of system
"""
circ11a = b(0,20,[0,0],[0,0],True)
sim11a = s(circ11a)
s.random_square(sim11a,6,5,True)
ke_conserve = np.array([])
for i in range(50):
    s.next_collision(sim11a)
    ke_conserve = np.append(ke_conserve,s.kinetic_energy(sim11a))
plt.scatter(np.linspace(1,50,50),ke_conserve)
plt.ylabel("Kinetic Energy (J)")
plt.xlabel("Collision number")
plt.show()
"""
Kinetic energy is the same after every collision
"""
#%% momentum conservation
"""
Plotting number of collisions against momentum vector
"""
circ11b = b(0,20,[0,0],[0,0],True)
sim11b = s(circ11b)
s.random_square(sim11b,3,0.1,True)
momentumx = np.array([])
momentumy = np.array([])
for i in range(50):
    s.next_collision(sim11b)
    momentumx = np.append(momentumx,s.momentum(sim11b)[0])
    momentumy = np.append(momentumy,s.momentum(sim11b)[1])
plt.scatter(np.linspace(1,50,50),momentumx)
plt.scatter(np.linspace(1,50,50),momentumy)
plt.ylabel("Momentum (m/s)")
plt.xlabel("Collision number")
plt.legend(["x momentum","y momentum"],loc="right")
plt.show()
"""
Momentum in both the x and y direction is also conserved between every collision
"""
#%% pressure vs temperature
"""
Plotting pressure against temperature
"""
"""
This is done by creating 50 simulations wuith a constant ball mass, radius and velocity constant and comparing the results
"""
pressures = np.array([])
temperatures = np.array([])
for j in range(50):
    circle11c = b(0,25,[0,0],[0,0],True)
    sim11c = s(circle11c)
    s.random_square(sim11c,6,5,False)
    pressures = np.append(pressures,s.pressure(sim11c))
    temperatures = np.append(temperatures,s.temperature(sim11c))

plt.ylabel("Pressure(kgs^-2)")
plt.xlabel("Temperature (K)")

plt.scatter(temperatures,pressures)

#%% pressure and temperature against areas
"""
Plotting area of container against temperature and area of container against
pressure by creating 50 simulations wih increasing radius of the container
and calculating the pressure and temperature of each simulation. The velocity 
is fixed at 1m/s in both directions for every ball, and the mass and radius are
constant
"""
pressures = np.array([])
temperatures = np.array([])
areas = np.array([])
for j in range(1,11):
    circle11d = b(0,(j+1),[0,0],[0,0],True)
    sim11d = s(circle11d)
    s.square_constant(sim11d,6,5)
    pressures = np.append(pressures,s.pressure(sim11d))
    temperatures = np.append(temperatures,s.temperature(sim11d))
    areas = np.append(areas,np.pi*((j+1))**2)
plt.figure(1)
plt.scatter(areas,temperatures)
plt.ylabel("Temperature(K)")
plt.xlabel("Area of container (m^2)")
plt.figure(2)
plt.scatter(areas,pressures)
plt.ylabel("Pressure(kgs^-2)")
plt.xlabel("Area of container (m^2)")
plt.show()
"""
Temperature is unaffected by the change in container area. This is because the 
internal energy of the particles remain the same if the only thing that is 
changing is the container area as the velocities remain the same
"""
"""
Pressure decreases exponentially as the area increases. This is because there
will be less collisions with the container wall if the container is bigger and 
so the pressure will decrease
"""
#%% pressure and temperature against number of balls
"""
Plotting the number of balls in the container against the pressure and 
temperature of the container. The radius of the container, the radii of the 
balls and the velocity of the balls are all the same between simulations
"""
pressures = np.array([])
temperatures = np.array([])
ball_numbers = np.array([])
for j in range(1,11):
    circle11e = b(0,20,[0,0],[0,0],True)
    sim11e = s(circle11e)
    s.square_constant(sim11e,j,5)
    pressures = np.append(pressures,s.pressure(sim11e))
    temperatures = np.append(temperatures,s.temperature(sim11e))
    ball_numbers = np.append(ball_numbers,j**2)
plt.figure(1)
plt.scatter(ball_numbers,temperatures)
plt.ylabel("Temperature(K)")
plt.xlabel("Number of Balls")
plt.figure(2)
plt.scatter(ball_numbers,pressures)
plt.ylabel("Pressure(kgs^-2)")
plt.xlabel("Number of Balls")
plt.show()
"""
The temperature remains constant as the average internal energy of the balls
remains the same when just the number of balls is changed
"""
"""
The pressure is directly proportional to the number of balls as with more balls,
the pressure increases directly
"""
#%% Task 12 possibly delete
"""
Investigating 2d ideal gas law, PA=N*Kb*T
"""
"""
Plotting pressure against temperature and using a square of completely
constant balls except for a varying velocity and plotting the reuslting
pressures and temperatures of the system against each other
"""
pressures = np.array([])
temperatures = np.array([])
for i in range(1,50):
    circle12a = b(0,30,[0,0],[0,0],True)
    sim12a = s(circle12a)
    s.square_constant(sim12a,6,i)
    pressures = np.append(pressures,s.pressure(sim12a))
    temperatures = np.append(temperatures,s.temperature(sim12a))

plt.scatter(temperatures,pressures)
plt.xlabel("Temperature(K)")
plt.ylabel("Pressure(kgs^-2)")

def linefit(x,m,c):
    return x*m + c

po,po_cov = curve_fit(linefit,temperatures,pressures)
print(po)
print(po_cov)
plt.plot(temperatures,linefit(temperatures,po[0],po[1]))
plt.show()
"""
The graph between pressure and temperature is a curve and so pressure and
temperature cannot fit the straight lin ideal gas equation PA=N*Kb*T
"""
#%%Task 12 pressure vs area
pressures = np.array([])
areas = np.array([])
for i in range(1,10):
    circle14 = b(0,i,[0,0],[0,0],True)
    sim14 = s(circle14)
    s.radii_square(sim14,6,0.9,1*1e23)
    pressures = np.append(pressures,s.pressure(sim14))
    areas = np.append(areas,np.pi*(i**2))
plt.scatter(areas,pressures)
plt.xlabel("Area (m2)")
plt.ylabel("Pressure (kgs^-2)")
"""
Pressure is inversely proportional to area, as is predicted by the ideal gas law
Pressure has already been shown to be proportional to temperature in task 11
"""
#%% Changing the ball radius
pressures = np.array([])
radii = np.array([])
temperatures = np.array([])

for i in range(1,50):
    circle13d = b(0,50,[0,0],[0,0],True)
    sim13d = s(circle13d)
    s.radii_square(sim13d,8,i/55,2)
    pressures = np.append(pressures,s.pressure(sim13d))
    temperatures = np.append(temperatures,s.temperature(sim13d))
    radii = np.append(radii,i*0.07142492739258055) #the long number is the radius of the balls when i=1
plt.figure(1)
plt.scatter(radii,temperatures)
plt.xlabel("Ball radius (m)")
plt.ylabel("Temperature (K)")
plt.figure(2)
plt.scatter(radii,pressures)
plt.ylabel("Pressure (kgs^-2)")
plt.xlabel("Ball radius (m)")
plt.show()    
"""
Changing the ball radius has no effect on the pressure of the system

Changing the ball radius has no effect on the temperature of the system
"""

#%% Task 13 Ball velocity distribution 
circle13 = b(0,25,[0,0],[0,0],True)
sim13 = s(circle13)
s.random_square(sim13,12,5,True)
velocities = s.all_velocities(sim13)
print("""Initially the velocities were distributed uniformly as they were created
using a uniform random function""")
plt.figure(1)
plt.hist(velocities[0])
plt.ylabel("Frequency")
plt.xlabel("X Velocity(m/s")
plt.figure(2)
plt.hist(velocities[1])
plt.xlabel("Y Velocity(m/s)")
plt.show()
print("For the X velocity:")
print("The mean is",np.mean(velocities[0]),"m/s")
print("The variance is",np.var(velocities[0]),"m/s")
print("For the Y velocity:")
print("The mean is",np.mean(velocities[1]),"m/s")
print("The variance is",np.var(velocities[1]),"m/s")

s.run(sim13,300,0.01,False)
velocities = s.all_velocities(sim13)
print("""After 300 collisions the velocities follow a model which is much closer
to the Maxwell-Boltzmann distribution of velocities of gas particles, with
a rough gaussian centered at 0m/s""")
plt.figure(3)
plt.ylabel("Frequency")
plt.xlabel("X Velocity(m/s")
plt.hist(velocities[0])
plt.figure(4)
plt.hist(velocities[1])
plt.xlabel("Y Velocity(m/s")
plt.show()
print("For the X velocity:")
print("The mean is",np.mean(velocities[0]),"m/s")
print("The variance is",np.var(velocities[0]),"m/s")
print("For the Y velocity:")
print("The mean is",np.mean(velocities[1]),"m/s")
print("The variance is",np.var(velocities[1]),"m/s")
#%% Distribution of speeds for two temperatures (takes 5 mins to run)
"""
This time the speed distribution of the particles is going to be compared
between two simulations at different speeds
"""
circle13 = b(0,25,[0,0],[0,0],True)
sim13c = s(circle13) #colder simulation
s.square_constant(sim13c,12,1)
sim13h=s(circle13) #hotter simulation
s.square_constant(sim13h,12,2)
s.run(sim13c,800,0.01,False)
s.run(sim13h,800,0.01,False)
def speed(array):
    speeds=np.array([])
    for i in range(0,len(array[0])):
        speeds = np.append(speeds,np.sqrt((array[0][i])**2 + (array[1][i])**2))
    return speeds
plt.hist(speed(s.all_velocities(sim13c)),bins=40,alpha = 0.7)
plt.hist(speed(s.all_velocities(sim13h)),bins=40,alpha = 0.7)
plt.xlabel("")
plt.ylabel("Frequency")
plt.legend(["Low Temperature","High Temperature"],loc='upper right')

"""
Defining a function for the Maxwell-Boltzmann distribution to plot alongside
the histogram for comparison
"""
def MaxBoltz(v,T,m):
    return v*np.exp(-(0.5*m*(v**2))/(1.381e-23*T))
v=np.linspace(0,7,1000)

Tc=s.temperature(sim13c)
Th =s.temperature(sim13h)
m = 1
plt.plot(v,22*MaxBoltz(v,Tc,m),color='b')
plt.plot(v,9*MaxBoltz(v,Th,m),color='orange')
plt.show()
"""
As expected, the speed distribution follows closely with the Maxwell-Boltzmann
distribution, with similar changes when the temperature is increased
"""
#%% Task 14 Van der Waals distribution possibly delete
pressures = np.array([])
areas = np.array([])
for i in range(1,25):
    circle14 = b(0,i,[0,0],[0,0],True)
    sim14 = s(circle14)
    s.square_constant(sim14,6,1,1*1e23)
    pressures = np.append(pressures,s.pressure(sim14))
    areas = np.append(areas,np.pi*(i**2))
plt.scatter(areas,pressures)
plt.xlabel("Area (m2)")
plt.ylabel("Pressure (kgs^-2)")

def vanderwaals(x,m1,m2,p):
    return m1/(x-p) - m2/(x**2)

po,po_cov = curve_fit(vanderwaals,areas,pressures)
print(po)
print(po_cov)
plt.plot(np.linspace(3,1800,1800),vanderwaals(np.linspace(3,1800,1800),po[0],po[1],po[2]))
plt.show()
print("a =",po[1]/36)
print("b =",po[2]/36)
#%%
pressures = np.array([])
temperatures = np.array([])
for i in range(50):
    circle11c = b(0,30,[0,0],[0,0],True)
    sim11c = s(circle11c)
    s.random_square(sim11c,7,5,False)
    pressures = np.append(pressures,s.pressure(sim11c))
    temperatures = np.append(temperatures,s.temperature(sim11c))

def linefit(x,m,c):
    return m*x + c
plt.ylabel("Pressure(kgs^-2)")
plt.xlabel("Temperature (K)")
po,po_cov = curve_fit(linefit,temperatures,pressures)
print(po)
print(po_cov)
plt.scatter(temperatures,pressures)
x = np.linspace(min(temperatures),max(temperatures),1000)
plt.plot(x,linefit(x,po[0],po[1]))
A = np.pi*30**2
b = A/49 - 1.3806e-23/po[0]
print("a =",(po[1]*(A**2)*(A - 49*b))/(b*(49**3) - A*(49**2)))
print("b =",b)
