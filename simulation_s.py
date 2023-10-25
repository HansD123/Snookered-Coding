# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 18:59:56 2022

@author: hansd
"""
import ball_s
import pylab as pl
import numpy as np
import matplotlib as plt
b = ball_s.Ball

class Simulation:
    """
    Simulation class which can be initialised with a container and a ball
    """
    def __init__(self,container,ball):
        if b.is_container(container) == "No":
            raise Exception("A conatiner object is required to initialize a simulation object")
        if b.is_container(ball) == "Yes":
            raise Exception("A ball object is required to initialize a simulation object")
        self.__c = container
        self.__b = ball
    def variables(self):#delete this function
        #print(Simulation.c)
        #print(b.rad(Simulation.c))
        return b.rad(self.__c), 
    def Container_variables(self):
        return b.rad(self.__c),b.pos(self.__c)
    def Ball_variables(self):
        return b.mass(self.__b),b.rad(self.__b),b.vel(self.__b),b.pos(self.__b)
    def next_collision(self):
        time = b.time_to_collision(self.__b,self.__c)
        b.move(self.__b,time)
        b.collision(self.__b,self.__c)
    def run2(self, num_frames, animate=False):
        if animate:
            f = pl.figure()
            ax = pl.axes(xlim=(-100, 100), ylim=(-100, 100))
            ax.add_artist(self.__c.getpatch())
            ax.add_patch(self.__b.getpatch())
        for frame in range(num_frames):
            self.next_collision()
            pl.pause(0.001)
        if animate:
            pl.show()
    def run(self,num_frames,animation_speed=0.1,animate=False):
        if animate:
            pos_c = np.array(b.pos_v(self.__c))
            r_c = b.rad_v(self.__c)
            ax = pl.axes(xlim=(pos_c[0]-r_c-2,pos_c[0]+r_c+2),ylim=(pos_c[1]-r_c-2,pos_c[1]+r_c+2))
            ax.add_artist(self.__c.getpatch())        
            for frame in range(num_frames):
                ball_patch1 = self.__b.getpatch()
                ax.add_patch(ball_patch1)
                if animate:
                    pl.pause(animation_speed)
                    self.next_collision()
                    ball_patch1.remove()
             
            pl.show()
        else:
            for frame in range(num_frames):
                self.next_collision()
    def run3(self,num_frames,animate=False):
        if animate:
            pos_c = np.array(b.pos_v(self.__c))
            r_c = b.rad_v(self.__c)
            ax = pl.axes(xlim=(pos_c[0]-r_c-2,pos_c[0]+r_c+2),ylim=(pos_c[1]-r_c-2,pos_c[1]+r_c+2))
            ax.add_artist(self.__c.getpatch())  
            ax.add_artist(self.__b.getpatch())
        for frame in range(num_frames):
            self.next_collision()
            if animate:
                pl.pause(0.001)
        if animate:
            pl.show()
        
    def kineticEnergy(self):
        Ke = 0.5*b.mass_v(self.__b)*(b.vel_v(self.__b)[0]**2 + b.vel_v(self.__b)[1]**2)
        print("The kinetic energy is",Ke,"J")
    def momentum(self):
        m = b.mass_v(self.__b)*np.sqrt(b.vel_v(self.__b)[0]**2 + b.vel_v(self.__b)[1]**2)
        print("The momentum is",m,"kgm/s")
    def pressure(self):
        """
        As the system is 2d, the pressure formula has to be altered slightly
        to account for the fact that there are only two degrees of freedom of
        the gas and the container contains an area, not a volume.
        """
        rms = np.sqrt((b.vel_v(self.__b)[0]**2 + b.vel_v(self.__b)[1]**2)/1)
        p = (1*(b.mass_v(self.__b)/1)*rms)/(np.pi*b.rad_v(self.__c)**2)
        print("The pressure is",p,"kgs-2")
            
            
s=Simulation