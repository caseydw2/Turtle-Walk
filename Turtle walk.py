# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 17:12:31 2022

@author: Casey
"""
from PIL import Image, ImageDraw
from math import sin,cos,pi

factor = 100



def polar_to_xy(theta,radius):
    return radius*cos(theta),radius*sin(theta)

def new_coor(cur_coor,factor,theta):
    x,y = cur_coor[0], cur_coor[1]
    delx,dely = polar_to_xy(theta,factor)
    return x+delx,y+dely

def turtle_walk(factor = 100,rate_of_change=1,iteration=1000):
    size=(100* factor, 100* factor)
    x,y = round(size[0]/2), round(size[1]/2)
    im = Image.new("RGB",size)
    draw = ImageDraw.Draw(im)
    theta = 0
    for i in range(iteration):
        newx, newy = new_coor((x,y),factor,theta)
        draw.line([(x,y),(newx,newy)])
        x,y = newx,newy
        theta = theta + i*rate_of_change*pi/180
    
    im.show()
        
        