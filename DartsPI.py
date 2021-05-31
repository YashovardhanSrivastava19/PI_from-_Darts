#Program to Calculate the approximate value of PI(3.141...) using Darts.
"""Dart_PI:This program computes the approximate value of PI by calculating the 
probability of a point being inside a circle (which is inscribed in a rectangle(sqaure)).
The probability of a point inside circle,as the number of points increases reaches
PI/4.We use this fact to calculate PI.
More information:https://www.cse.wustl.edu/~cytron/cs101/Lectures/5.html
"""
import random
import math      
class Dart_PI:
    """ [Class for calculating approximate value of PI using Darts] """
    def __init__(self,radius=1)->None:
        self.radius=radius
        self.points=[];self.rectangle_points=[];self.circle_points=[]

    def Randomly_Assigning_Points(self,numIterations:int=10000)->None:
        for i in range(numIterations):
            x=round(random.uniform(-2*self.radius,2*self.radius),3)
            y=round(random.uniform(-2*self.radius,2*self.radius),3)
            self.points.append((x,y))
        for x,y in self.points:
            #change rel_tol according to need (0.621 works fine)
            if math.isclose(x**2+y**2,self.radius**2,rel_tol=0.621):   
                self.circle_points.append((x,y))
            else:
                self.rectangle_points.append((x,y))     

    def ApproxPi(self)->float:    
        try:
            #here p is the probability of points being inside circle
            p=len(self.circle_points)/len(self.rectangle_points)  
            return 4*p
        except ZeroDivisionError:                        
            print("Try increaing the number of iteration")        

#Object Instantiation                                
pi=Dart_PI()
pi.Randomly_Assigning_Points()
print(pi.ApproxPi()) 
"""3.1890726096333575"""
