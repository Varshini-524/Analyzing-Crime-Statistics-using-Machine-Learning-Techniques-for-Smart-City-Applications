#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 09:45:54 2018

@author: VarshiniSelvadurai
"""
# Convert matlab object to python list
import scipy.io as sio
import numpy as np
t = sio.loadmat('/Users/VarshiniSelvadurai/Downloads/grayscale pixel values by zipcode and PRA 180817a.mat')
GS_pra_list = t['GS_pra_list']
GS_zip_list = t['GS_zip_list']
GS_pra = []
for i in range(0,785):
    temp = GS_pra_list[i]
    temp = np.concatenate(temp).astype(None)
    GS_pra.append(temp)
 
GS_zip = []
for i in range(0,55):
    temp = GS_zip_list[i]
    temp = np.concatenate(temp).astype(None)
    GS_zip.append(temp)   


