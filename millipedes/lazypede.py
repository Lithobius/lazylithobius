import logging, os, re
from imp import reload
reload(logging)
#LOG_FILENAME = 'millipedelog.txt'

#logging.basicConfig(filename=LOG_FILENAME, level = logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s')
#logging.debug('Start of program')

#empty dictionary for formatted numbers and names
taxadic = {}
#directory for the fasta files that need formatting
genes = '/Users/katelaptop/LocalDocs/Research/millipede/genes/'
#already formatted list in csv format
in_list = '/Users/katelaptop/LocalDocs/Research/millipede/in_list.csv'
#make a regex for mczbase formatted text
MCZRegex = re.compile(r'(\D+)(\d+)') 

#this function takes the already-formatted taxon + IZ numbers and puts it in a list
def scrape():
    with open(in_list, 'r') as f: 
        for line in f:
            #make a search for the regex format
            m = MCZRegex.search(line)
            #the line has \r and \n on them so removed them
            #taxadic[key = group2 = mcznumber] = line it came from with full format
            taxadic[m.group(2)] = line[:-2]
            

#This function search and replaces!
def replace():
    for file in os.listdir(genes):
        #open both files at once
        with open("edit_" + file, 'w') as n, open(genes + file, 'r') as f:
            for line in f:
                #> indicates where the names should go
                if line.startswith('>'):
                    #don't want to search with the new line character or the '>', won't find matches.
                    mcznum = line[1:-1]
                    if mcznum in taxadic:
                        #this is the way strings are formatted in python3 apparently
                        #{!s} instead of %s, .format(what's in {!s})
                        #and because I removed \n, need to add it again!
                        n.write(">{!s}\n".format(taxadic[mcznum]))
                    else:
                        #if I already edited it or its an outgroup with no num
                        #make sure its written now
                        n.write(line)
                else:
                    #obviously we should write the gene information...
                    n.write(line)
            #don't forget to close the files!
            f.close
            n.close
            
        

#run functions!        
scrape()
replace()

#logging.debug('End of program')