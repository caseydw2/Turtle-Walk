# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 17:12:31 2022

@author: Casey
"""
from PIL import Image, ImageDraw
from math import sin,cos,pi


def polar_to_xy(theta,radius):
    return radius*cos(theta),radius*sin(theta)

def new_coor(cur_coor,factor,theta):
    x,y = cur_coor[0], cur_coor[1]
    delx,dely = polar_to_xy(theta,factor)
    return x+delx,y+dely

def turtle_walk(factor = 100,rate_of_change=1,iteration=1000,save=False):
    size=(5000* factor, 5000* factor)
    x,y = round(size[0]/2), round(size[1]/2)
    minx,maxx,miny,maxy = x,x,y,y
    im = Image.new("RGB",size)
    draw = ImageDraw.Draw(im)
    theta = 0
    for i in range(iteration):
        newx, newy = new_coor((x,y),factor,theta)
        if newx < minx:
            minx = newx
        if newx > maxx:
            maxx = newx
        if newy > maxy:
            maxy = newy
        if newy < miny:
            miny = newy
        draw.line([(x,y),(newx,newy)])
        x,y = newx,newy
        theta += i*rate_of_change*pi/180
    left,top,right,bottom = minx-5,miny-5,maxx+5,maxy+5
    im = im.crop((left,top,right,bottom))
    if save:
        im.save("Turtle Walk {},{},{},{}.png".format(factor,rate_of_change,iteration,size))
    im.show()
    
        