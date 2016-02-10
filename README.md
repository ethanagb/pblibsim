# pblibsim

Update 1/8/2016:
This repo is under construction. I'll be pushing some usable updates soon, but they may require some adaptation to your configutations. Working on a more generalized version for the near future. 
******
*Here's a general pipeline for this code.  *
1. Get a reference genome/assembly by chromosome (ie. chr1.fa, chr2.fa,)  
2. Generate a distribution of chromosome lengths (generate_chrdist.py)  
3. simulation.py (many parameters still must be hard-coded in this draft version.)  This generates a BED file of simulated reads.   
4. sortBed.sh - sorts BED files by chromosome.  
5. getFasta.sh - requires BEDTools, generates simulated FASTA files. This is written to be easily parallelizable.   
6. (Specific for my purposes) countSimDimers.sh  
******
This is a draft version of pblibsim.

cleanfasta.py is the complete simulation done with respect to chromosome

nochr_sim.py is the core of the simulation done without respect to chromosome. 
nochrsimbootstrapped.py includes distribution building for simulation results. 
