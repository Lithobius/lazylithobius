#!/usr/bin/env python
# coding: utf-8

# # mcz4dna: change numbers in filenames
# 
# ##Instructions on how to use this script
# This script was designed to replace legacy numbers (DNA numbers) with MCZ numbers, but it can be lightly modified to replace any A->B in high volumes. It is best used in situations where you have many files with the same values to replace.
# 
# First, create a spreadsheet in csv format with two columns; MCZ_NUM for your MCZ numbers (or your replacement values if modifying) and DNA_NUM for your legacy numbers (or original values). In my original project there were several folders of repetitive replacement, and I was able to obtain this spreadsheet by downloading the data from MCZbase, deleting the extra columns, and removing "DNA Number=" and genbank/field numbers via grep (cmd+f, replace it with nothing, replace all ; regex for genbank numbers was "=KJ([0-9]{6})").
# One line of this csv looks like this:
# 136168,DNA105996
# 
# Then in the "def dnamczdic():" block, replace the value in 'sourcefile =' with the filepath to your csv. If your column names are different, change them in the annotated line.
# 
# The goal here is to create a dictionary that the script can reference, so it can replace the same numbers over and over if you have multiple instances of them, eg forward and reverse primers for 3 gene fragments in one folder!
# 
# Second, the replacement block!
# I designed this so it will put the modified files in a new folder. My original folder would be "18s" and the new one would be "18s_fix." If you don't want this, just replace "direct" and "direct_dest" with the same filepath instead of 2 different ones. IMPORTANT NOTE: I always run this script on copies of the original data just in case!
# 
# The key to this replacement is that my filenames looked like this: 18s1f_18s4r_DNA111111_taxonomy.abi
# I split the filenames using the underscores, then the 5th group would be just the DNA number. If your files have a different format, you'll want to change what it uses to split by modifiying the contents of "r'(_)'" with "r'(yourvalue)'". Remember that your character might need a '\' before it according to regex rules (eg: \. or \]). 
# 
# Because mine was on the 5th value, I replace it in the line starting with "dst[4]=" (Python numbering starts with 0). If you don't know which value yours will be you can uncomment the print line and run the script, then see how it looks after the split, then replace the value 4 with your intended value.
# 
# Additionally, I have added 'MCZ_IZ' + mcznumber. So the modified filename looks like this:
# 18s1f_18s4r_MCZ_IZ222222_taxonomy.abi
# If you don't want that added just delete 'MCZ_IZ +' or replace it with your own prefix.
# 
# If you want to see what your final names look like, or have a list of them, you can uncomment the print command in either of the two second locations depending on what you want to see.
# 
# A note on the exceptions; these cover instances where there's files that don't match the format or aren't included in the csv. These will get moved to the new folder with no change. If you notice there's a group of files with a different format, you can just move them back to the source folder, lightly modify your values, and run it again!
# 

# In[1]:


#Step 1: read in the number doc
import csv

def dnamczdic():
    #read in source
    #modify this line to be your own filepath
    sourcefile = '/Users/katesheridan/Documents/Harvard/Research/Neopilionidaescratch/scripts/fixlegacy/NeopilDNA-MCZ_copy.csv'
    #open source, set reader as csv.DictReader which will create dictionaries from the csv
    with open(sourcefile) as f:
        reader = csv.DictReader(f)
        for line in reader:
            #make a dictionary from the dictionary
            #if your column names are different change them here.
            mcz_num[line['DNA_NUM']] = line['MCZ_NUM']


#Step 2: replace filenames
import os
import re

def dna4mcz():
    #put your filepaths here
    direct = '/Users/katesheridan/Documents/Harvard/Research/Neopilionidaescratch/scripts/fixlegacy/18s/'
    dest_direct = '/Users/katesheridan/Documents/Harvard/Research/Neopilionidaescratch/scripts/fixlegacy/18s_fix/'
    for filename in os.listdir(direct):
        #replace "r'(_)'" with "r'(yourvalue)'"
        dst = re.split(r'(_)', filename)
        #remove the hashtag from the following line to see your split
        #print(dst)
        try:
            #replace 4 with intended value
            #'MCZ_IZ' can be deleted or replaced with intended prefix
            dst[4] = re.sub(dst[4], 'MCZ_IZ' + mcz_num[dst[4]], dst[4])
            #print(dst[4])
        except (KeyError, IndexError):
            pass
        dst = "".join(dst)
        #print(dst)
        src = direct + filename
        dst = dest_direct + dst
        #rename function
        os.rename(src, dst)
        
if __name__ == '__main__':
    #dictionary must be a global variable
    mcz_num = {}
    #read in csv
    dnamczdic()
    #rename files
    dna4mcz()

