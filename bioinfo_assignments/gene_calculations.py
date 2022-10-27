#!/usr/bin/env python
# -*- coding: utf-8 -*-

# From homework in Introduction to Bioinformatics at Harvard, 2018

# 9. Write a python program that can calculate the length of each gene (txStart to txEnd),
# length of full transcript (concatenated exons) and length of all introns concatenated.
# Write the output as a tab-delimited table, with RefSeq ID on first column, 
# and the three numbers (length of gene, transcript, introns) after.**



#class to be populated with the various fields we need
class gene(object):

    def __init__(self, refseq, geneStart, geneEnd, exStart, exEnd):
        self.refseq = refseq
        self.geneStart = geneStart
        self.geneEnd = geneEnd
        self.exstart = exStart
        self.exend = exEnd

#class to be popuated with the calculations
class gene2(object):

    def __init__(self, refseq, genelen, trans, intron):
        self.refseq = refseq
        self.genelen = genelen
        self.trans = trans
        self.intron = intron

#open the file and pull out the useful stuff        
def readrefGene(file):
    with open(file) as f:
        for line in f:
            fields = line.strip().split()
            refseq = fields[1]
            geneStart = int(fields[4])
            geneEnd = int(fields[5])
            exStart = fields[9]
            exEnd = fields[10]
            yield gene(refseq, geneStart, geneEnd, exStart, exEnd)

#do the calculations we need
def calculate(data):
    for g in data:
    #keep the things that are the same, the same
      refseq = g.refseq
      genelen = int(g.geneEnd) - int(g.geneStart)
      #empty lists to fill with exons
      transtemp1 = []
      transtemp2 = []
      #fill lists 
      for n in g.exstart:
          transtemp1.append(n)
      for n in g.exend:
          transtemp2.append(n)
      #format lists ; remove all commas and split up numbers
      transtemp2 = ''.join(transtemp2)
      transtemp2 = transtemp2.split(",")
      transtemp2 = transtemp2[:-1]
      transtemp1 = ''.join(transtemp1)
      transtemp1 = transtemp1.split(",")
      transtemp1 = transtemp1[:-1]
      #transcripts lengths
      transtemp3 = [int(transtemp2[x]) - int(transtemp1[x]) for x in range(len(transtemp1))]
      #total transcription length
      trans = sum(transtemp3)
      #introns!
      intron = int(genelen) - trans
      #put data into class for printing
      yield gene2(refseq, genelen, trans, intron)
      
    
#the program!
if __name__ == "__main__":
    import csv
    refGene = "/Users/katelaptop/Documents/Harvard/STAT215/Homework/Homework5-master/refGene.txt"
    genes = readrefGene(refGene)
    calcs = calculate(genes)
    #write file!
    with open("refGeneCalc.csv", "w") as out:
        writecsv = csv.writer(out, delimiter = '\t')
        writecsv.writerow(['RefSeq','GeneLength','TranscriptLength','IntronLength'])
        for g in calcs:
            writecsv.writerow([g.refseq, g.genelen, g.trans, g.intron])



