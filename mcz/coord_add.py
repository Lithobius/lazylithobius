#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 09:50:57 2019

@author: katesheridan
"""



if __name__ == "__main__":
#import needed packages
    import pandas as pd

#import csv's    
    clust = pd.read_csv("/Users/katesheridan/Documents/Harvard/Research/Neopilionidaescratch/maps/SAM_clusters_15.csv")
    coord = pd.read_csv("/Users/katesheridan/Documents/Harvard/Research/Neopilionidaescratch/maps/Neopil_SAM_data.csv")

#duplicate specimen names
    clust['CAT_NUM'] = clust['Specimen']
#regex out anything that isn't a number
    clust['CAT_NUM'] = clust['CAT_NUM'].str.replace('[A-Za-z_]+', '')
 #regex out the underscores from cat_num so that they match clust   
    coord['CAT_NUM'] = coord['CAT_NUM'].str.replace('_', '')
#make a dataframe where they're merged    
    bothcc = pd.merge(clust, coord, on = 'CAT_NUM')
#remove unnecessary columns when writing to CSV, no index column either
    bothcc.to_csv("/Users/katesheridan/Documents/Harvard/Research/Neopilionidaescratch/maps/Neopil_SAM_coord_clust.csv",columns = ['Specimen','x','DEC_LAT','DEC_LONG'], index = False)
                  
#To check for discrepancies
#    indexedcoord = coord.set_index('CAT_NUM')
#    indexedclust = clust.set_index('CAT_NUM')

#    bothcc2 = pd.concat([indexedclust, indexedcoord], axis = 1)
