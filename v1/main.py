import argv, sys, getopt, os, math
import numpy as np
import gzip
from splitGenomeFasta import splitGenomeFasta
from getRandomPosition import getRandomPosition
from findChromosome import findChromosome

def main():
	#Parse arguments
	try:
        opts, args = getopt.getopt(argv,"i:o:m:s:c:h",["infile=","outfile=","mean_read_length=-","standard_dev=", "coverage="])
    except getopt.GetoptError:
        print("Usage: python simulation.py -i </path/to/genome -o </path/to/outfile.bed> -m <mean read length> -s <standard dev of read lenghts> -c <coverage>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("Usage: python simulation.py --infile </path/to/ingenome.fa> --outfile </path/to/outfile.bed> -m <mean read length> -s <standard dev of read lenghts> -c <coverage>")
            sys.exit(2)
        elif opt in ("-i","--infile"):
            infileName = arg
        elif opt in ("-o","--outfile"):
            outfileName = arg
        elif opt in ("-m", "--mean_read_length"):
            mean = arg
        elif opt in ("-s", "--standard_dev"):
            std = arg
        elif opt in ("-c", "--coverage"):
            desired_cov = arg

    #Split the input genome to chromosomal fasta files and return the sorted list of chromosome names.
    names = splitGenomeFasta(infileName)

    #Generate a distribution of chromosome lenghts in the provided genome.
    generateChrDist() #This needs to be reconfigured...it won't need to take arguments any more

    #Generate simulated reads
    simulateReads() #Also will need to be reconfigured to take commnads from this function, not the command line


if __name__ == "__main__":
   main(sys.argv[1:])
