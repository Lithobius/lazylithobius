This script inserts Ns in a properly formatted FASTA file (or any basic txt file I guess)

All you have to do is:
1) Make a line that says "N=50" and it will insert 50 N's.
2) Make sure NO OTHER LINES start with N (not usually a problem for a basic FASTA but reduces universal application for this script).

I guess you could change it to startswith('N=') == True if you needed to.
