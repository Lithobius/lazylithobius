#!/usr/bin/env python
# -*- coding: utf-8 -*-


# This was from homework for introduction to bioinformatics, Harvard 2018

# Different histone marks are enriched in different elements of the genome
# and have different effect on gene expression. In this homework, we want
# to look at the K562 cell line with gene expression data and ChIP-seq
# profiles of 10 different histone marks: H3K4me1, H3K4me2, H3K4me3,
# H3K9me3, H3K9ac, H3K27me3, H3K27ac, H3K79me2, H3K36me3, H4K20me1. The
# gene expression data for each RefSeq transcript is summarized in a file
# called `data/k562expr.txt`.

# For each histone mark ChIP-seq data, we already parsed out the following
# read counts for each RefSeq sequence (in the file
# `data/histone_marks_read_count_table.txt`): distal promoter [-5KB, -1KB] from
# transcription start site (TSS), proximal promoter [-1kb, +1kb] from TSS,
# gene body (from transcription start to end, including all exons and
# introns), transcript (concatenate all the exons), first 1/3 of
# transcript (concatenate all the exons, length-wise), middle 1/3 of
# transcript, last 1/3 of transcript, all the introns (concatenate all the
# introns). The table has one line for each RefSeq, and 81 columns (RefSeq
# ID, 10 histone marks, each with 8 features, so 1 + 10 * 8), the value is
# log read count for each feature.

# 10. Write a quick python script to filter out RefSeq that have only histone mark 
# or expression data available but not both.

def expr(infile):
    expr_l = []
    with open(infile) as f:
        for line in f:
            if line.startswith('ref'):
                pass
            else:
                fields = line.strip().split()
                expr_l.append(fields[0])
        return expr_l
        
def both(file):
    both_l = []
    with open(file) as f:
        hist = open("histone_rct2.txt", "w")
        for line in f:
            fields = line.strip().split()
            if fields[0] in expr_list:
                both_l.append(fields[0])
                hist.write(line)
            else:
                pass
        return both_l
        
def expr2(infile):
    with open(infile) as f:
        ex = open("K562expr2.txt", "w")
        for line in f:
            fields = line.strip().split()
            if fields[0] in both_list:
                ex.write(line)
            else:
                pass
              
    
in_expr = "/Users/katelaptop/Documents/Harvard/STAT215/Homework/Homework5-master/data/K562expr.txt"
in_hist = "/Users/katelaptop/Documents/Harvard/STAT215/Homework/Homework5-master/data/histone_marks_read_count_table.txt"
expr_list = expr(in_expr)
both_list = both(in_hist)
expr2(in_expr)


