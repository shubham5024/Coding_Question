#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 22:41:04 2020

@author: shubham
"""

def spiral(mat):
    left=top=0
    right=len(mat[0])
    bottom=len(mat)
    
    while (True):
        if (left>right):break;
        
        ## left line
        for i in range(right):
            print(mat[top][i],end=" ")
        top=top+1
        
        if (top>bottom):break;
        
        ## top to bottom
        
        for i in range(top,bottom):
            #print(i,right-1)
            print(mat[i][right-1],end =" ")
            
            
        right=right-1
        
        ## right to left
        if (left>right):break
    
        for i in range(r-2,l-1,-1):
            
            print(mat[bottom-1][i-1],end=" ")
        bottom=bottom-1
        if (top>bottom):break
        for i in range(bottom,top,-1):
            print(mat[i][left],end=" ")
        left=left+1
        
mat=[[1,2,3,4],
        [12,13,14,5],
        [11,16,15,6],
        [10,9,8,7]]
spiral(matrix)