
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# From introduction to bioinformatics, Harvard 2018

# For Part I, we ask you to use STAR to map 5M fragments and generate a SAM file. 
# Write a python program to calculate the average insert size 
# (distance between the 5’ ends of the +strand and -strand reads) of the 
# top 1000 fragments where both ends are mappable and their mapped distance 
# are between 50 and 2000bp. If the distance between the two reads 
# are out of range, skip to the next fragment.
# https://samtools.github.io/hts-specs/SAMv1.pdf

# Note on homework: 
# With this script, I originally had a more complicated setup before 
# realizing that it was as simple as stripping out tlen. 
# Instead of rewriting it to be simpler overall, I left the classes and functions 
# as is but stripped down so that if I wanted it to be more robust in the future 
# and add in more features it would be easier. I also left it this way 
# because it finished in a second or two on my laptop, and my laptop wouldn't 
# even open the .sam file due to "not enough memory" so I figured 
# if it isn't broken, don't fix it, and it seemed pretty easy on my system as-is.

#class for single reads to be pulled straight from the file
class samRead(object):

    def __init__(self, name, tlen):
        self.name = name
        self.tlen = tlen
                
#class for paired reads that will be combined for single reads
class samPairs(object):
    
    def __init__(self, nameP, tlenP):
        self.nameP = nameP
        self.tlenP = tlenP

#open the sam file and pull out the useful stuff        
def readSAM(sam):
    with open(sam) as f:
        for line in f:
            if line.startswith('@'):
                pass
            else:
                fields = line.strip().split()
                name = fields[0]
                tlen = fields[8]
                yield samRead(name, tlen)

#pull out theoretical pairs
def samReadPair():
    for r in singleReads:
        yield r, singleReads.next();

#match names and strip out useful information into
#pair class
def pairUP():
    for r1, r2 in samReadPair():
        if r1.name == r2.name:
            nameP = r2.name
            tlenP = abs(int(r2.tlen))
            #tlenP is absolute value from the start
            #so we don't have to worry about negatives
            #and turned into an integer because it told me
            #before it was a string so just to be safe.
            #picking r2 instead of r1 was arbitrary
            yield samPairs(nameP, tlenP)
        else:
            pass

#parse through our paired reads class to do the actual calculation
def avReadLen():        
    totals = []
    #make a list to store tlens in
    for p in pairing:
        if p.tlenP < 250 or p.tlenP > 2200:
        #a tlen of 250 would be the 50 minimum plus 100 bp for each read
        #a tlen of 2000 would be the maximum of 2000 plus 100 bp per read
        #this assumes we know the reads are 100 as in this file.
        #I suppose it would not work for a sam file generated by reads 
        #over or under 100 bp each. I originally had a more complex
        #calculation here that took into account varying lengths 
        #and I would reinstate it if I wanted to take this
        #script and make it more universal or distribute it.
        #It included extra fields in the classes, which I removed.
            pass
        elif len(totals) == 1000:
        #done at 1000
           break
        else:
        #add tlen to running list
            totals.append(p.tlenP)
    #after loop breaks, make an average
    #This is over len(totals) and not 1000 because my
    #test file yielded less than 1000 within the range and
    #if I were to make this script more universal I would leave
    #in the len(totals) in case of a sam file that never got to 
    #1000 and add something to tell me how many were in len(totals)
    answer = sum(totals)/len(totals)
    return answer
#now for the actual program:
if __name__ == "__main__": 
#run functions!
    samfile = '/Users/katelaptop/Documents/Harvard/STAT215/Homework/Homework/Homework3-master/STAR/star_outputAligned.out.sam'
    singleReads = readSAM(samfile) 
    pairing = samReadPair() 
    pairing = pairUP()
    #show result, it gives me 809
    print avReadLen() 
