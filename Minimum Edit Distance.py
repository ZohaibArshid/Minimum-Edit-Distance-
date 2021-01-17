# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 04:16:50 2020

@author: Zohaib Arshad Tanoli

"""
import numpy as np


def minimum_dist(target, source): 
   
    # buliding matrix of correct size 
    target = [k for k in target]
    source = [k for k in source]
    
    sol = np.zeros((len(source), len(target)))
    #zeros() function creating numpy array containg all are zero
   
    #first row and column
    sol[0]= [j for j in range(len(target))]
    sol[:, 0]= [j for j in range(len(source))]
    
    #add anchor value
    if target[1] != source[1]:
        sol[1,1] = 2
    
    # Fill rest of value 
    
    # through every column
    for c in range(1, len(target)):
        # through every row
        for r in range(1, len(source)):
           
           # if c > r :
             #   source[r] += '*'
    
            #not same letter
            if target[c] != source[r]:
                sol[r,c] =min(sol[r-1,c], sol[r,c-1]) + 1
            # same letter
            else:
                sol[r,c] = sol[r-1, c-1]
                

                
                
    return sol
    