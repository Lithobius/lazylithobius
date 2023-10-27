#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
I have some scripts that feed a list of things into NCBI, etc. It keeps hanging up between 10pm and midnight, and this will remove all the lines that have already gone through so that I can keep it going. Otherwise I delete 50-70k lines manually.

It can be modified to remove lines in any txt file by changing the value of 'goal'.

Any license info also goes here
Author: "Kate Sheridan"
Version: "0.1.0"
Status: dev
insert copyright, license, additional credits etc if necessary
"""

# common libraries
from pyprojroot import here # like here in R

# less-known libraries
# own libraries/functions

# log-setup
# check logging module for more settings
# I'm mostly using the debug options for development
import logging

LOG_FILENAME = 'trim-log.txt'

logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
logging.info('Debut!')


# set up functions


def trim_list(to_files, to_trim, trimmed, goal):
    with open(here(to_files+trimmed), "w") as out, \
    open(here(to_files+to_trim), "r") as f:
        found = 0
        for line in f:
            if line.startswith('>'):
                query = line[1:-1]
                if found == 0:
                    if query != goal:
                        logging.info("skipped " + query)
                        pass
                    elif query == goal:
                        found = 1
                        logging.info("goal: " + query)
                        out.write(query + "\n")
                    elif found == 1:
                        logging.info("wrote " + query)
                        out.write(query + "\n")
                elif found == 1:
                    out.write(line)
            elif found == 0:
                pass
            elif found == 1:
                out.write(line)

# basic-body

if __name__ == "__main__":

    # don't forget to change the 'goal'
    goal = 'ASV2167_265'
    filepath = ("./rawdata/peco/fastq/allyears/")
    infile = ("20231023_peco-combined_12s_swarm_problems.fasta")
    outfile = ("20231023_peco-combined_12s_swarm_problems-trim.fasta")
    trim_list(filepath, infile, outfile, goal)


# end
logging.info('Fin!')
