# lazylithobius

Scripts to automate my work because I'm super lazy and coding is easier than working.


Each script has its own folder with the script an an example input file.
Right now all of these are in Python 3.


## Contents

### bioinfo_assignments

These are small scripts from Introduction to Bioinformatics at Harvard, Spring 2018. They were part of homework assignments that were targeted towards very specific questions, usually calculations or generating summary statistics, and almost all on genetic data.

#### filter_partial_data.py

The researchers want to study a protein, and need records with both expression and transcription data. Filter out data with only one of the two types.

#### gene calculations.py

calculate: length of gene, length of transcript, export as TSV with ID and stats

#### top20_mutations.py

We had to identify mutations and rank them by the top 20 most frequent ones. I used a fairly simple compare and count

#### top1000_insertsize.py

We had a SAM file (some kind of genetics file I don't usually use) and had to pair the reads and calculate the insert size of the top 1000 fragments that met specific conditions. I generated classes for the reads, paired them, and ran a loop through them that determined if the sequences met the conditions, if yes, calculate and advance counter by 1 until we hit 1000, if no, skip.



### mcz

This folder contains MCZ related scripts

#### coord_add
Uses pandas to add coordinates to clusters for mapping, here because its all based on MCZbase records. 

#### mcz4dna

This script substitutes a specific number for another in a large batch of filenames.
I  needed it in GGs lab when I had dozens and dozens and hundreds of files with an old ID number that needed to be updated to another. 

I think it's a modified this4that and uses a csv key for all filenames in a directory. It was one of my earliest Python scripts and I've lost the example files.

#### this4that

This script was originally from utensils-master given to me by Ligia. it was originally written for python 2 but I modified it to work with python 3. You can also tell it wasn't written by me because it doesn't match my style and has no inline commenting haha. I don't even really understand some parts of it, but it is a good baseline to build similar scripts from.

### millipedes/lazypede

I think this one was my first 'real' Python script. It was a complicated replacement situation within FASTA files, but relatively simple to automate. I had to update the numbers with species names or something, so it makes a dictionary of replacements, regex, and rewrite. 

Editing FASTA files like this is best with Python.

### mPTP2csv

Here Shahan had some kind of file thing I was doing something with that I couldn't get back into R correctly. or something? Either way I wanted to extract information so I told it to read through the file and write out a csv.

Either way its a good example of using Python to get information that would otherwise be hard to get.

### NsertNs

GG asked me to put Ns into some fasta file for some reason. I forget what was wrong with it, some alignment issue? (yeah a gap from nonoverlapping primers in some sequences) but basically I decided that doing it manually sounded like actual work and told the computer to do it for me.

However I had already gone through the file and inserted a line with the correct number of Ns. It's a pretty rough and dirty script but it does the job.

### splitexcel

split2csv_seine2.py is from the PECO project, where we had partners record data on google sheets. I downloaded xls files and didn't want to open each one and save each page as a csv individually. Plus we kept getting updates so it would have been repeated work.

This script doesn't have super great documentation at the moment but basically it skips sheets that we don't care about, then takes any populated sheet and writes it to csv.

Key note with this is that it threw errors about files not being excels, and this was due to invisible .DS_store files as well as dotfiles created by excel when a file was open. It was necessary to use command line to see and remove ds store files. Stupid Apple.

### trimlist

I was searching/blasting a bunch of stuff on NCBI and when it stops I can trim the file to have it start at the ASV it left off. trimlist is for lists of accession numbers, trimfasta is for fasta files.

You enter the accession/asv/sample name in 'goal' and it will make a trimmed version of the list or fasta.

NOTE be sure to change your original script to APPEND instead of WRITE, or change the target file name. Otherwise the resumed search will overwrite your old search.

