#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:34:36 2019

@author: begin
"""
from xclim import subset
import xarray as xr
from netCDF4 import Dataset,num2date, date2num,date2index, MFDataset
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime,timedelta,time
from statistics import mean


    
#def calculmoyenne_pr(a,b,mm):
variable='pr'
a=1981
b=1982 #année-1
h=np.arange(0,24,1)
mois=['06','07','08']
 #ouverture fichier 50 membres + période(an)
runs='kfd kda kdb kdc kdd'# kde kdf kdg kdh kdi kdj kdk kdl kdm kdn kdo kdp kdq kdr kds kdt kdu kdv kdw kdx kdy kdz kea keb kec ked kee kef keg keh kei kej kek kel kem ken keo kep keq ker kes ket keu kev kew kex'            
runsplit=runs.split(' ')
nc=[]
ds=[]
for kk in runsplit:
    hr=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    print(kk)
    for m in mois:
        yyyy=[]
        #creation liste d'année et mois (am) combiné        
        an=np.arange(a,b,1)
        for aa in an:
            seq=[str(aa)]+[m]
            yyyy.append(seq[0]+seq[1])
            for ee in yyyy:
                print("boucle annee:", ee)
                serie=('/klmx1/leduc/climex-core-qc/'+kk+'/series/'+ee+'/'+variable+'_'+kk+'_'+ee+'_se.nc')
                nc.append(serie)
ds=xr.open_mfdataset(nc,decode_times=False)
#df=ds.pr.resample(time='MS')       
       