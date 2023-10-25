# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 15:12:00 2022

@author: hansd
"""
import numpy as np
import pylab as pl
class Ball:
    """
    Ball object which is made up of four parameters, mass(kg), radius(m)
    and 2-d arrays of position(m) and velocity(m/s)
    To create a container when initializing set container to True
    """
    def __init__(self,mass,radius,position,velocity,container=False):
        if mass <0 :
            raise Exception("The mass cannot be negative")
        if radius <= 0:
            raise Exception("The radius cannot be negative")
        self.__m =mass
        self.__r =radius
        self.__p = np.array(position)
        self.__v = np.array(velocity)
        if container == True:
            """
            An extra variables is used to define a container instead of creating
            a ball subclass as less code needs to be written
            """
            self.__c = True
            self.__v = np.array([0,0])
            self.__m = 10**9.
            """
            The container has an extremely high mass so that in momentum 
            calculations the momentum that has been transferred to the container
            is considered
            """
        else:
            self.__c = False
        if len(self.__v) != 2:
            raise Exception("Ball parameter velocity should be an array of size 2")
        if len(self.__p) != 2:
            raise Exception("Ball parameter position should be an array of size 2")
            """
            Makes sure the position and velocity is an array of size 2
            """
    def mass(self):
        print(self.__m,'kg')
        """
        Returns the mass of the ball
        """
    def rad(self):
        print(self.__r,'m')
        """
        Returns the radius of the ball
        """
    def pos(self):
        print(self.__p,'m') 
        """
        Returns the position of the ball
        """
    def mass_v(self):
        """ 
        The _v methods return just the value of the variable of the ball, and
        are used in the simulation class functions
        """
        return self.__m
    def pos_v(self):
        return self.__p
    def rad_v(self):
        return self.__r
    def vel_v(self):
        return self.__v
    def vel(self):
        print(self.__v,'m/s')
        """
        Returns the velocity of the ball
        """
    def move(self,dt):
        """
        Updates the balls position by moving the ball at its current velocity
        by time dt
        """
        self.__p = self.__p + (dt*self.__v)
    def is_container(self):
        """
        Function is used to check if a container object is used to inialize
        a simulation object in the simulation class, and to raise an exception
        if this is not the case
        """
        if self.__c == True: 
            return "Yes"
        else:
            return "No"
    def time_to_collision(self,other):
        if other.__c == False:
            """
            Time to collision for two balls
            """
            r = self.__p - other.__p
            v = self.__v - other.__v
            Ra = self.__r + other.__r
            Rb = self.__r - other.__r
            rr = np.dot(r,r)
            rv = np.dot(r,v)
            vv = np.dot(v,v)
            solutions = np.array([]) #array of possible positive time solutions
            number_of_solutions = 0
            discriminant_a = rv**2 - vv*(rr-Ra**2)
            discriminant_b = rv**2 - vv*(rr-Rb**2)
            """
            This section of code checks that the time solutions are real and
            greater than 0 and only returns them if this is the case.
            """
            if vv ==0:
                solution = 'The balls do not collide' # the final solution returned by the function
            else:
                if discriminant_a >= 0:
                    t1a = (-rv + np.sqrt(discriminant_a))/(vv)
                    t2a = (-rv - np.sqrt(discriminant_a))/(vv)
                    if t1a >= 0:
                        number_of_solutions += 1
                        solutions = np.append(solutions,t1a)
                    if t2a >= 0:
                        number_of_solutions += 1
                        solutions = np.append(solutions,t2a)
                if discriminant_b >= 0:
                    t1b = (-rv + np.sqrt(discriminant_b))/(vv)            
                    t2b = (-rv - np.sqrt(discriminant_b))/(vv)
                    if t1b >= 0 :
                        number_of_solutions += 1
                        solutions = np.append(solutions,t1b)
                    if t2b >= 0:
                        number_of_solutions += 1
                        solutions = np.append(solutions,t2b)
                if number_of_solutions == 0:
                    solution =  'The balls do not collide'
                else:   
                    """
                    If there is more than 1 solution the later solution could not
                    occur as the balls have already collided so will have diffrerent
                    velocities, therefore only the earlier solution is required.
                    """
                    solution =  np.min(solutions)
        else:
            """
            Time to collision for a ball and a container
            """
            a = other.__p[0]
            b = other.__p[1]    
            R2 = (other.__r - self.__r)**2 #Reducing radius of container due to radius of ball
            vx = self.__v[0]
            vy = self.__v[1]
            rx = self.__p[0]
            ry = self.__p[1]
            #Working out the y=mx + c parameters for the trajectory of the ball
            m = vy/vx    
            c = ry - (m*rx)
            """
            Subbing y=mx+c into cirlce equation to give quadratic for x in form
            Ax^2 + Bx + C = 0 to find coords of where trajectory of ball intercpets 
            with the circle
            """
            A = (1 + m**2)
            B = (-2)*a + 2*m*(c-b)
            C = a**2 + (c-b)**2 -R2
            x1 = (-B + np.sqrt(B**2 - 4*A*C))/(2*A)
            x2 = (-B - np.sqrt(B**2 - 4*A*C))/(2*A)
            def findy(x):
                return m*x + c
            def findx(y):
                return (y-c)/m
            if vx > 0:
                x = x1
                y = findy(x)
            if vx < 0:
                x = x2
                y = findy(x)
            if vx == 0:
                if vy > 0:
                    y = max(findy(x1),findy(x2))
                    x = findx(y)
                if vy < 0:
                    y = min(findy(x1),findy(x2))
                    x = findx(y)
                if vy == 0:
                    x = y = "Error"
                    solution = "The ball can never collide with the container"
            self.__cx = x   #stores x and y coords of collision to be reused in collision function
            self.__cy = y
            """
            Using the coordinates calculated and the velocity and position of the 
            ball to find how long it will take the ball to reach the edge of the 
            container, as long as a collision is possible:
            """
            if x != "Error":
                distance = np.sqrt((x-rx)**2 + (y-ry)**2)
                speed = np.sqrt(vx**2 + vy**2)
                solution = distance/speed
        return solution
                                        
        
    def collision(self,other):
        """
        Collision between two balls
        """
        v1 = self.__v
        v2 = other.__v
        r1 = self.__p
        r2 = other.__p 
        m1 = self.__m
        m2 = other.__m
        r12 = r1 - r2
        r21 = r2 - r1
        self.__v = v1 - (((2*m2)*np.dot(v1-v2,r12))/((m1+m2)*(r12[0]**2 + r12[1]**2)))*r12
        other.__v = v2 - (((2*m1)*np.dot(v2-v1,r21))/((m1+m2)*(r21[0]**2 + r21[1]**2)))*r21
        """
        Finds the component of velocity that is parallel to the axis of 
        collision and uses conservation rules to alter this component of velocity.
        This is then added with the perpendicular compnent to give the new velocity
        for each particle.
        """
    def getpatch(self):
        if self.__c == True:
            return pl.Circle([Ball.pos_v(self)[0],Ball.pos_v(self)[1]],self.__r,ec='black',fill=False,ls='solid')
        else:
            return pl.Circle([Ball.pos_v(self)[0],Ball.pos_v(self)[1]],self.__r,fc='b')
        """
        Creates a blue patch for a ball and a black outline patch for a container
        """

#%%  Delete section
#   vx = self.__v[0]
#            vy = self.__v[1]
#            a = other.__p[0]
#            b = other.__p[1] 
#            cx = self.__cx
#            cy = self.__cy
#            m = (cy - b)/(cx - a)
#            n_constant = 1/((m**2 + 1)**(1/2)) 
#            n_hat = np.array([n_constant,n_constant*m])
#            """
#            The gradient of the line from the centre of the container to the 
#            collision point is found and this is used to find the gradient 
#            of the tangent at the collision point. The normalised vector of this
#            tangent line is then found.
#            """
#            v = np.array([vx,vy]) #vector of balls velocity
#            v_perpendicular = np.dot(n_hat,v)*n_hat
#            v_parallel = np.subtract(v,v_perpendicular)
#            self.__v = np.add(v_parallel,-v_perpendicular)
#            """
#            The parallel and perpendicular components of the balls velocity to
#            the tangent are found. The perpendicular component is reversed and
#            then the two components are added back together to form the new
#            velocity vector of the ball post collision.
#            """     
        