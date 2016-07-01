import numpy as np
import sys
import os 

def generateChrDist(names):
    #Get the list of chromosome names from command line 
    with open('SiLiCO_Scratch/chrdist.td','w+') as outfile2:
        for chrom in names:
            #Strip header lines from fasta for processing
            with open("SiLiCO_Scratch/" + str(chrom) + '.fa','r') as infile, open("SiLiCO_Scratch/" + str(chrom) + '.noheader.fa','w+') as outfile:
                for i, line in enumerate(infile):
                    if i >= 0:
                        if not line.startswith('>'):
                            outfile.write(line)
            infile.close()
            outfile.close()  
            #Remove any newline chars, remove undefined nts, make all nts uppercase for processing. 
            with open("SiLiCO_Scratch/" + str(chrom) + '.noheader.fa','r') as infile, \
            open("SiLiCO_Scratch/" + str(chrom) + '.clean.fa','w+') as outfile:
                lines = infile.readlines()
                x = map(str.strip,lines)
                seq = ''
                for line in x:
                    y = str(line)
                    z = y.upper()
                    w = z.replace('N','')
                    seq += w
                outfile.write(seq)
                outfile2.write(str(chrom) + '\t' + str(len(seq)) + '\n')
            infile.close()
            outfile.close()
    outfile2.close()

    #Remove all temporary files from the scratch dir
    for chrom in names:
        os.remove("SiLiCO_Scratch/" + str(chrom) + '.noheader.fa')
        os.remove("SiLiCO_Scratch/" + str(chrom) + '.clean.fa')

if __name__ == "__main__":    
    generateChrDist(names)