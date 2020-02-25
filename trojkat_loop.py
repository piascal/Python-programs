# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:39:30 2019

@author: pfenger
"""
def getmiddlethreechars(samplestr):
    middleindex = int(len(samplestr) / 2)
    print("Original string is", samplestr)
    middlethree = samplestr[middleindex-1: middleindex+2]
    print("Middle three chars are", middlethree)
    

getmiddlethreechars("LechKortez")
    