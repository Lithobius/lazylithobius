#!/usr/bin/env python
# -*- coding: utf-8 -*-


# This was from homework for introduction to bioinformatics, Harvard 2018


# Q11. The MAF files contain the mutations of each tumor compared to 
# the normal DNA in the patient blood. Write a python program to parse 
# out the mutations present in each tumor sample, and write out a table. 
# Rank the mutations by how many times the specific mutation happens in 
# the tumor samples provided, and submit the table with the top 20 mutations.



#counting function
def makecount(genelist):
    mutscnt = Counter()
    for g in genelist:
        mutscnt[g] += 1
    return mutscnt

#write whole table from both dictionaries            
def wholetable(typea, typeb):
    with open("gbmmuts.txt", "w") as out:
        fieldnames = ['Gene', 'CountA', "CountB"]
        writer = csv.DictWriter(out, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        genesall = []
        genesall = typea + typeb
        for key in genesall:
        #put in each row ; for any key, the count for both a and b type
                writer.writerow({'Gene': key, 'CountA' : mutscntA[key], 'CountB' : mutscntB[key]})


#write out top 20
def toptwenty(typea, typeb):
#make a new counter to hold totals
    genesall = typea + typeb
    #sort totals to top 20
    sortmuts = sorted(genesall, key=genesall.get, reverse=True)[:20]
    #write top 20 to file
    with open("gbmtop20.txt", "w") as out:
        fieldnames = ['Gene', 'CountA', 'CountB']
        writer = csv.DictWriter(out, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        for key in genesall:
        #only write totals from the sorted key
            if key in sortmuts:
                writer.writerow({'Gene': key, 'CountA' : mutscntA[key], 'CountB' : mutscntB[key]})
            else:
                pass
                

#main program
if __name__ == "__main__":  
#import needed packages
    import os
    import fileinput
    import csv
    from collections import Counter
#set up needed lists, paths and dictionaries
    genesA = []
    genesB = []
    mafsafiles = []
    mafsbfiles = []
    mafsa = "/Users/katelaptop/Documents/Harvard/STAT215/Homework/Homework6-master/data/mafs/A"
    mafsb = "/Users/katelaptop/Documents/Harvard/STAT215/Homework/Homework6-master/data/mafs/B"

    for file in os.listdir(mafsa):
    #add each file's name with the full path (because my computer needs I guess)
        mafsafiles.append("/Users/katelaptop/Documents/Harvard/STAT215/Homework/Homework6-master/data/mafs/A/" + file)
        #use fileinput to make a class of each file so they can be 
        #cycled through all in a row
    f = fileinput.input(files = mafsafiles)
          #cycle through each line in each file  
    for line in f:
        #split lines so we can extract only what we need
        fields = line.strip().split()
               #obviously we don't need these, go past
        if fields[0] == 'Hugo_Symbol' or fields[0] == 'Unknown':
            pass
        else:
            #add to genesA list
            genesA.append(fields[0] + "_" + fields[8])
    #ditto for B
    for file in os.listdir(mafsb):
    #append the directory so it can be found by my cpu (dir + file)
        mafsbfiles.append("/Users/katelaptop/Documents/Harvard/STAT215/Homework/Homework6-master/data/mafs/B/" + file)
    f = fileinput.input(files = mafsbfiles)
    for line in f:
        fields = line.strip().split()
        if fields[0] == 'Hugo_Symbol' or fields[0] == 'Unknown':
            pass
        else:
            genesB.append(fields[0] + "_" + fields[8])
    
    #make both dictionaries            
    mutscntA = makecount(genesA)
    mutscntB = makecount(genesB)
    #use counters to make tables
    wholetable(mutscntA, mutscntB)
    toptwenty(mutscntA, mutscntB)

