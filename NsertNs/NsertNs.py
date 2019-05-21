#!/usr/bin/env python
# coding: utf-8

# ##Nsert Ns!
# 
# This script exists because I had a bunch of 3-part genes where parts A and B were separated by a gap made by nonoverlapping primers. My instructions were to insert the correct number of Ns for the analysis. Because I'm lazy AF I had the computer do it for me.
# 
# First I aligned the sequences with Geneious.
# Copy/pasted the alignment Fasta, regex '-' replace with nothing, and '\n\n\n' replace with '\n' until I was happy. 
# Then I measured the gap between Contig 1 and 2 by dragging the mouse and entering what it said. There's probably a better/automated way to do this.
# 
# #Formatting for the file:
# FASTA file with...
# >specimen_1_name
# AAGGTTGG... (part a)
# 
# N=55
# 
# GCTAGCT... (part b+c)
# 
# >specimen_2_name....
# /end of file
# 
# The important part is having N=integer formatted exactly that way. This script will use the integer provided to insert that many Ns.
# 
# Afterwards you can remove newlines if you wish by regex: '\nN' replace with nothing, then 'N\n' replace with nothing.
# 
# Then you'll have your FASTA with a bunch of N's. The text isn't wrapped and it won't look pretty but it works.

# In[42]:


import re
import fileinput

def nsertns():
    #read in source
    #modify this line to be your own filepath
    sourcefile = '/Users/katesheridan/Documents/Harvard/Research/Neopilionidaescratch/scripts/nsertns/Legacy18swithNs.fasta'
    with fileinput.FileInput(sourcefile, inplace=True) as f:
        for line in f:
            #checks if line starts with N to modify
            if line.startswith("N") == True:
                numNs = re.split(r'(=)', line)
                numNs = 'N' * int(numNs[2])
                print(numNs, end = "")
            else:
                print(line, end = "")
            
if __name__ == '__main__':
    nsertns()

