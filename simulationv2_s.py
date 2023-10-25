# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 15:40:34 2022

@author: hansd
"""

import ball_s
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
import random
b = ball_s.Ball

class Simulation2:
    """
    Simulation class which can be initialised with a container and a ball. All
    objects are stored in the self.__o array where the first object in the array
    is always the container and subsequent objects are always balls. Any additional
    balls added are added to the end of the array.
    """
    def __init__(self,container,ball=False):
        if b.is_container(container) == "No":
            raise Exception("A conatiner object is required to initialize a simulation object")
        self.__o = np.array([container]) #an array which stores every single object in the simulation
        if ball!=False:
            if b.is_container(ball) == "Yes":
                raise Exception("A ball object is required to initialize a simulation object")
            self.__o = np.append(self.__o,ball)
    def container_variables(self):
        return b.rad(self.__o[0]),b.pos(self.__o[0]) 
        """
        Returns container variables
        """
    def ball_variables(self,ball_number):
        return b.mass(self.__o[ball_number]),b.rad(self.__o[ball_number]),b.vel(self.__o[ball_number]),b.pos(self.__o[ball_number])
        """
        Returns ball variables of a ball based on its ball_number; the balls
        position in the object array
        """
    def number_balls(self):
        """
        Returns the number of balls in the simulation
        """
        return len(self.__o)-1
    def delete_balls(self):
        """
        Deletes all balls in the simulation
        """
        self.__o = np.array([self.__o[0]])
    def add_ball(self,ball):
        """
        Adds another ball to the simulation
        """
        if b.is_container(ball) == "Yes":
            raise Exception("Only ball objects can be added to this simulation.")
        self.__o = np.append(self.__o,ball)
    def change_container(self,container):
        """
        Swaps the container used in the simultaion
        """
        if b.is_container(container) == "No":
            raise Exception("A container object is required for this")
        self.__o[0] = container
    def next_collision(self):
        times = np.array([]) #array of all possible collision times
        objects = np.array([])#array of the two objects involved in each of the possible collisions
        """
        Empty arrays are created for the collision times and the objects involved
        in the collision to be entered into.
        """
        for i in range(len(self.__o)-1,0,-1):
            for j in range(i-1,-1,-1):
                collision_result = b.time_to_collision(self.__o[i],self.__o[j])
                if collision_result != "The balls do not collide":
                    times = np.append(times,collision_result)
                    objects = np.append(objects,[self.__o[i],self.__o[j]])
        """
        The code loops through all the objects in the simulation and 
        performs time_to_collision between all possible ball and container
        pairs such that each possible collision is only calculated once. As
        long as the collision is possible, the time of the collision is entered
        into the times array and the two objects involved in the collision 
        are entered at an equivalent position in the balls array.
        """
        min_time = min(times)
        min_time_pos = np.where(times==min_time)[0][0]
        for i in range(len(self.__o)-1,0,-1):
            b.move(self.__o[i],min_time)
        b.collision(objects[2*min_time_pos],objects[2*min_time_pos + 1])
        """
        The earliest collision is then performed with the object pair that matches
        with this collision. All balls are 
        then moved to this new position.
        """
        for i in range(len(self.__o)-1,0,-1):
            b.move(self.__o[i],0.00000000001)
            """
            All objects are then moved by an additional 0.00000000001 s so that
            if two balls have just collided they are not on top of each other
            so the code dosen't calculate that they will collide again in 0 s.
            """
    def run(self,num_frames,animation_speed=0.1,animate=False):
        if len(self.__o) == 1:
            raise Exception("You need to add a ball to the simulation to do this")
        if animate:
            pos_c = np.array(b.pos_v(self.__o[0]))
            r_c = b.rad_v(self.__o[0])
            ax = pl.axes(xlim=(pos_c[0]-r_c-2,pos_c[0]+r_c+2),ylim=(pos_c[1]-r_c-2,pos_c[1]+r_c+2))
            ax.add_artist(self.__o[0].getpatch())
               
            """
            The container is added to the animation and the axes are fitted to
            the size of the container so that they are centered on the centre
            of the container and extend by 2 in all directions beyond the 
            edge of the container
            """
            for frame in range(num_frames):
                ball_patches = np.array([0])
                for i in range(1,len(self.__o)):
                    ball_patches = np.append(ball_patches,self.__o[i].getpatch())
                    ax.add_patch(ball_patches[i])
                pl.pause(animation_speed)
                self.next_collision()
                for i in range(1,len(self.__o)):
                    ball_patches[i].remove()
                """
                All the balls are added to the animation, the next collision is
                performed, and then the old balls are removed and the new updated 
                balls are added in the next frame.
                This is then repeated num_frames times
                """
             
            pl.show()
        else:
            for frame in range(num_frames):
                self.next_collision()
            """
            If animate is set to false next_collision is performed num_frames times
            """
    def static(self):
        if len(self.__o) == 1:
            raise Exception("You need to add a ball to the simulation to do this")
        pos_c = np.array(b.pos_v(self.__o[0]))
        r_c = b.rad_v(self.__o[0])
        ax = pl.axes(xlim=(pos_c[0]-r_c-2,pos_c[0]+r_c+2),ylim=(pos_c[1]-r_c-2,pos_c[1]+r_c+2))
        ax.add_artist(self.__o[0].getpatch())
        ball_patches = np.array([0])
        for i in range(1,len(self.__o)):
            ball_patches = np.append(ball_patches,self.__o[i].getpatch())
            ax.add_patch(ball_patches[i])
        pl.show()
        """
        Displays static picture of the current positions of all objects in the 
        simulation
        """
    def kinetic_energy(self):
        """
        Loops through all objects in the system and calculates the kinetic
        energy of each object then adds them all together
        """
        Ke = 0
        for i in range(0,len(self.__o)):
            Ke += b.mass_v(self.__o[i])*(b.vel_v(self.__o[i])[0]**2 + b.vel_v(self.__o[i])[1]**2)  
        return 0.5*Ke
    def momentum(self):
        """
        Loops through all objects in the system and calculates the momentum
        as an array so that momentum conservation can be seen in both 
        dimensions
        """
        m = 0
        for i in range(0,len(self.__o)):
            m += b.mass_v(self.__o[i])*b.vel_v(self.__o[i])
        return m
    def pressure(self):
        """
        Calculates pressure using the rms velocity and the mass and number of
        particles
        As the system is 2d, the pressure formula has to be altered slightly
        to account for the fact that there are only two degrees of freedom of
        the gas and the container contains an area, not a volume.
        """
        total_v2 = 0
        total_m = 0
        for i in range(1,len(self.__o)):
            total_v2 += (b.vel_v(self.__o[i])[0]**2 + b.vel_v(self.__o[i])[1]**2) 
            total_m += b.mass_v(self.__o[i]) 
        rms = np.sqrt(total_v2/(len(self.__o)-1))   
        av_m = total_m/(len(self.__o)-1)
        return ((len(self.__o)-1)*av_m*rms)/(2*np.pi*(b.rad_v(self.__o[0])**2))
    def random_square(self,size_of_square,velocity_factor,random_variables=False):
        """
        size_of_square is the square root of the number of balls that are 
        generated in a square pattern. If random_variables if False, the radius 
        and mass of the balls are all the same,otherwise the radius and mass
        are random. velocity_factor determines the range of velocities that
        a random velocity can be generated from, for example for a velocity
        factor of 2, the velocities of the particles will be between -2 to 2 m/s
        """
        r = b.rad_v(self.__o[0])
        xa = b.pos_v(self.__o[0])[0]
        yb = b.pos_v(self.__o[0])[1]
        square_length = np.sqrt(2*(r**2))
        position = square_length/(size_of_square + 1)
        """
        Calculates the dimensions of a sqaure which will fit inside the container
        and calculates the distance between the balls if they were to be regularly
        distributed in the square
        """
        generated_balls = np.array([]) #array of all the balls that get generated
        for i in range(1,size_of_square + 1):
            for j in range(1,size_of_square + 1):
                if random_variables == False:
                    ball = b(1,position/6,[xa - square_length/2 + i*position,yb - square_length/2 + j*position],[random.uniform(-velocity_factor,velocity_factor),random.uniform(-velocity_factor,velocity_factor)],False)
                else:
                    ball = b(random.uniform(1,10),random.uniform(position/10,position/4),[xa - square_length/2 + i*position,yb - square_length/2 + j*position],[random.uniform(-velocity_factor,velocity_factor),random.uniform(-velocity_factor,velocity_factor)],False)
                generated_balls = np.append(generated_balls,ball)
                """
                Generates the balls with a random velocity that averages at 0 
                and random or fixed masses depending on how the function is called
                """
        Simulation2.delete_balls(self) #deletes any balls already in the simulation so ball positions dont overlap
        for i in range(1,len(generated_balls)+1):
            self.__o = np.append(self.__o,generated_balls[i-1])
            """
            Adds all the random balls to the simulation and gets rid of the original
            ball that was added in the simulation
            """
    def distance_from_centre(self):
        distances = np.array([])
        for i in range(1,len(self.__o)):
            displacement = b.pos_v(self.__o[i]) - b.pos_v(self.__o[0])
            distances = np.append(distances,np.sqrt(displacement[0]**2 + displacement[1]**2))
        plt.hist(distances)
        plt.xlabel("Distance from centre(m)")
        plt.ylabel("Number of balls")
        plt.show()
        """
        Calculates the distance of every ball from the centre and produces
        a histogram from the data
        """
    def distance_between_balls(self):
        distances =np.array([])
        for i in range(1,len(self.__o)):
            for j in range(i+1,len(self.__o)):
                displacement = b.pos_v(self.__o[i]) - b.pos_v(self.__o[j])
                distances = np.append(distances,np.sqrt(displacement[0]**2 + displacement[1]**2))
        plt.hist(distances)
        plt.xlabel("Distance between ball pairs(m)")
        plt.ylabel("Number of ball pairs at this distance")
        plt.show()
        """
        Calcualtes the distance between balls for every unique pair of balls 
        once and produces a histogram from the data
        """
    def temperature(self):
        """
        Calculates temperature using relationship with kinetic energy
        """
        return (6.02214*(10**23)*Simulation2.kinetic_energy(self))/(8.314*(len(self.__o)-1))
    def square_constant(self,size_of_square,velocity_factor,temp=False):
        """
        Creates a square of balls with constant mass, velocity and radius,
        method is otherwise identical to random_square
        The velocities of the balls can be made so that the balls have a certain
        temperature
        """
        r = b.rad_v(self.__o[0])
        xa = b.pos_v(self.__o[0])[0]
        yb = b.pos_v(self.__o[0])[1]
        square_length = np.sqrt(2*(r**2))
        position = square_length/(size_of_square + 1)
        generated_balls = np.array([])
        for i in range(1,size_of_square + 1):
            for j in range(1,size_of_square + 1):
                if temp == False:
                    ball = b(1,position/6,[xa - square_length/2 + i*position,yb - square_length/2 + j*position],[-velocity_factor,velocity_factor],False)
                else:
                    ball = b(1,position/6,[xa - square_length/2 + i*position,yb - square_length/2 + j*position],[np.sqrt((8.314*temp)/(6.022*10**23)),np.sqrt((8.314*temp)/(6.022*10**23))],False)
                generated_balls = np.append(generated_balls,ball)
        Simulation2.delete_balls(self)
        for i in range(1,len(generated_balls)+1):
            self.__o = np.append(self.__o,generated_balls[i-1])
    def all_velocities(self):
        """
        Returns an array of every single velocity in the simulation, is used
        in the velocity distribution graphs
        """
        velocities_x = np.array([])
        velocities_y = np.array([])
        for i in range(1,len(self.__o)):
            velocities_x = np.append(velocities_x,b.vel_v(self.__o[i])[0])
            velocities_y = np.append(velocities_y,b.vel_v(self.__o[i])[1])
        return [velocities_x,velocities_y]
    def radii_square(self,size_of_square,radius_percentage,velocity_factor):
        """
        Generates a square of balls with all variables kept constant except
        for ball radius which can be varied until the balls no longer fit in
        the container properly
        Radius_percentage determines the percentage of the distance between two
        adjacent balls that the balls radius will fill
        Function is otherwise identical to random_square
        """
        if radius_percentage < 0 or radius_percentage > 1:
            raise Exception("The radius_percentage is a decimal between 0 and 1")
        r = b.rad_v(self.__o[0])
        xa = b.pos_v(self.__o[0])[0]
        yb = b.pos_v(self.__o[0])[1]
        square_length = np.sqrt(2*(r**2))
        position = square_length/(size_of_square + 1)
        generated_balls = np.array([])
        for i in range(1,size_of_square + 1):
            for j in range(1,size_of_square + 1):
                ball = b(1,radius_percentage*position/2,[xa - square_length/2 + i*position,yb - square_length/2 + j*position],[-velocity_factor,velocity_factor],False)
                generated_balls = np.append(generated_balls,ball)
        Simulation2.delete_balls(self)
        for i in range(1,len(generated_balls)+1):
            self.__o = np.append(self.__o,generated_balls[i-1])
        
            