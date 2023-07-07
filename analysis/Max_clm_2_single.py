# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 10:15:25 2022

@author: rhonda
"""

import numpy as np
import iris

import iris.coord_categorisation
import iris.analysis.cartography

def rfg_mean_clm(RFG1, RFG2, RFG3, cam02): ## cam02: "CCT", "MSB", "" (put nothing for clm)
    RFG1_weigh = weigh_mean(RFG1)
    RFG2_weigh = weigh_mean(RFG2)
    RFG3_weigh = weigh_mean(RFG3)
    
    RFG2_weigh = RFG2_weigh.data
    RFG2_weigh = RFG2_weigh.tolist()
    if cam02 == "CCT":
        RFG2_weigh.insert(264, (RFG1_weigh[264] + RFG3_weigh[264])/2)
    if cam02 == "MSB":
        RFG2_weigh.insert(531, (RFG1_weigh[531] + RFG3_weigh[531])/2)
        
    RFG1_weigh = RFG1_weigh.data
    RFG1_weigh = RFG1_weigh.tolist()
    
    RFG3_weigh = RFG3_weigh.data
    RFG3_weigh = RFG3_weigh.tolist()
    
    RFG1_roll = year_roll_mean(RFG1_weigh)
    RFG2_roll = year_roll_mean(RFG2_weigh)
    RFG3_roll = year_roll_mean(RFG3_weigh)
    
    RFG_mean = (RFG1_roll + RFG2_roll + RFG3_roll) / 3
    return(RFG_mean, RFG1_roll, RFG2_roll, RFG3_roll)

def rcp_mean_clm(RCP, cam02):
    RCP_weigh = weigh_mean(RCP)
    RCP_roll = year_roll_mean(RCP_weigh)
    
    return(RCP_roll)

def weigh_mean(RFG):
    RFG_weigh = iris.analysis.cartography.cosine_latitude_weights(RFG)
    RFG_weigh_mean = RFG.collapsed(["latitude","longitude"], iris.analysis.MEAN, weights = RFG_weigh).data 
    return(RFG_weigh_mean)

def year_roll_mean(RFG):
    RFG_mean = []
    i = 0
    while i in range(0, len(RFG)):
        RFG_mean.append(max(RFG[i:i+12]))
        i = i + 12
    RFG_mean = moving_average(RFG_mean, 21)
    return(RFG_mean)

def moving_average(x, w): # x = array, w = 21 JJAs
    return np.convolve(x, np.ones(w), 'valid') / w

def rfg_mean_clm_month(RFG1, RFG2, RFG3, cam02, month): ## cam02: "CCT", "MSB", "" (put nothing for clm)
    RFG1_weigh = weigh_mean(RFG1)
    RFG2_weigh = weigh_mean(RFG2)
    RFG3_weigh = weigh_mean(RFG3)
    
    RFG2_weigh = RFG2_weigh.data
    RFG2_weigh = RFG2_weigh.tolist()
    if cam02 == "CCT":
        RFG2_weigh.insert(264, (RFG1_weigh[264] + RFG3_weigh[264])/2)
    if cam02 == "MSB":
        RFG2_weigh.insert(531, (RFG1_weigh[531] + RFG3_weigh[531])/2)
        
    RFG1_weigh = RFG1_weigh.data
    RFG1_weigh = RFG1_weigh.tolist()
    
    RFG3_weigh = RFG3_weigh.data
    RFG3_weigh = RFG3_weigh.tolist()
    
    RFG_mean = []
    
    for i in range(0, len(RFG1_weigh)):
        RFG_mean.append((RFG1_weigh[i] + RFG2_weigh[i] + RFG3_weigh[i]) / 3)
    
    RFG_roll = year_roll_mean(RFG_mean)   
    
    return(RFG_roll)

def rcp_mean_clm_month(RCP, cam02, month):
    RCP_weigh = weigh_mean(RCP)
    RCP_roll = month_roll_mean(RCP_weigh, month)
    return(RCP_roll)

def month_roll_mean(RFG, month):
    RFG_mean = []
    i = 0
    while i in range(0, len(RFG)):
        RFG_mean.append(max(RFG[i + month]))
        i = i + 12
    RFG_mean = moving_average(RFG_mean, 21)
    return(RFG_mean)

def rfg_mean_clm_LR(RFG1, RFG2, RFG3, cam02): ## cam02: "CCT", "MSB", "" (put nothing for clm)
    RFG1_weigh = weigh_mean(RFG1)
    RFG2_weigh = weigh_mean(RFG2)
    RFG3_weigh = weigh_mean(RFG3)
    
    RFG2_weigh = RFG2_weigh.data
    RFG2_weigh = RFG2_weigh.tolist()
    if cam02 == "CCT":
        RFG2_weigh.insert(264, (RFG1_weigh[264] + RFG3_weigh[264])/2)
    if cam02 == "MSB":
        RFG2_weigh.insert(531, (RFG1_weigh[531] + RFG3_weigh[531])/2)
        
    RFG1_weigh = RFG1_weigh.data
    RFG1_weigh = RFG1_weigh.tolist()
    
    RFG3_weigh = RFG3_weigh.data
    RFG3_weigh = RFG3_weigh.tolist()
    
    RFG_mean = []
    
    for i in range(0, len(RFG1_weigh)):
        RFG_mean.append((RFG1_weigh[i] + RFG2_weigh[i] + RFG3_weigh[i]) / 3)
    
    RFG_roll = year_roll_mean(RFG_mean)    
    
    return(RFG_roll)
