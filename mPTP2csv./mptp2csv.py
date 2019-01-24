# -*- coding: utf-8 -*-

#main program
if __name__ == "__main__":
#import needed packages
    import csv
    
    #dictionary and list to store data
    specimen_number = {}
    spec_num = []

#open file and loop through reading it
    with open('/Users/katesheridan/Documents/Harvard/Research/Neopilionidaescratch/NZNeo_delim_1547829377.txt','r+') as f:
        for line in f:
            #first make sure line isn't blank
            if not line.isspace():
                #remove info from mPTP
                if line.startswith('Command') or line.startswith('Number of edges') or line.startswith('Null-model') or line.startswith('Best score for') or line.startswith('Number of delimited') or line.startswith('LRT') == True:
                    pass
                #record species numbers
                #will overwrite anytime a new one pops up
                elif line.startswith('Species') == True:
                    fields = line.strip().split()
                    spec_num = fields[1][:-1]
                #add specimens to dictionary that follow the species number
                else:
                    specimen_number[line] = spec_num
            #skip blank lines
            else:
                pass

     #write to csv       
    with open("/Users/katesheridan/Documents/Harvard/Research/Neopilionidaescratch/NZNeo_20190124.csv", "w") as out:
        fieldnames = ['Specimen', 'SpeciesNum']
        writer = csv.DictWriter(out, fieldnames = fieldnames, delimiter = '\t')
        writer.writeheader()
        for key in specimen_number:
            writer.writerow({'Specimen': key, 'SpeciesNum' : specimen_number[key]})
