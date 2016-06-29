import numpy as np
import sys, getopt
import os 

def GenerateChrDist(argv):
    #Get the list of chromosome names from command line 
    infileName=''
    try:
        opts, args = getopt.getopt(argv,hi:,["infile="])
    except getopt.GetoptError:
        print("Usage: python generate_chrdist.py --infile /path/to/infile")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("Usage: python generate_chrdist.py --infile </path/to/infile>")
        elif opt ==("-i","--infile"):
            infileName = arg

    #Open the file of chromosome names
    with open(infileName,'r') as infile:
        lines = infile.readlines()
        names =[str(e.strip()) for e in lines]
    infile.close()

    with open('chrdist.td','w+') as outfile2:
        for chrom in names:
            #Strip header lines from fasta for processing
            with open(str(chrom) + '.fa','r') as infile, open(str(chrom) + '.noheader.fa','w+') as outfile:
                for i, line in enumerate(infile):
                    if i >= 0:
                        if not line.startswith('>'):
                            outfile.write(line)
            infile.close()
            outfile.close()  
            #Remove any newline chars, remove undefined nts, make all nts uppercase for processing. 
            with open(str(chrom) + '.noheader.fa','r') as infile, \
            open(str(chrom) + '.clean.fa','w+') as outfile:
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
    #cleanup

    for chrom in names:
        os.remove(str(chrom) + '.noheader.fa')
        os.remove(str(chrom) + 'clean.fa')

if __name__ == "__main__":    
    GenerateChrDist(sys.argv[1:])

