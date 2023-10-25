# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 15:34:18 2022

@author: hansd
"""
#Code is obsolute
import numpy as np
class Container_circle:
    """
    Circlular container object which will 
    contain ball objects.It has a centre and radius and ball object will collide
    with the edge of the container.
    """
    def __init__(self,centre,radius):
        if len(centre) != 2:
            raise Exception("Centre should be an array of size 2.")
        self.a = centre[0]
        self.b = centre[1]
        self.r = radius
    def centre(self):
        print("Centre is at",[self.a,self.b],"m")
    def radius(self):
        print("Radius is",self.r,"m")