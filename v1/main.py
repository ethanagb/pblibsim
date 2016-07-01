import sys, getopt, os, math
import numpy as np
import gzip
from splitGenomeFasta import splitGenomeFasta
from getRandomPosition import getRandomPosition
from findChromosome import findChromosome
from generateChrDist import generateChrDist
from simulateReads import simulateReads

def main(argv):
	#set default/placeholder values
	global mean, outfileName, std, desired_cov,y
	outfileName = 'simulationResults.bed'
	mean = 10000
	std = 2050
	desired_cov = 8 
	trialCount = 1000
	#Parse arguments
	try:
		opts, args = getopt.getopt(argv,"i:o:m:s:c:th",["infile=","outfile=","mean_read_length=","standard_dev=", "coverage=","trials="])
	except getopt.GetoptError:
		print("Usage: python simulation.py -i </path/to/genome> -o </path/to/outfile.bed> -m <mean read length> -s <standard dev of read lengths> -c <coverage>")
		print("-i, --infile=, REQ" + '\t\t' + "Input genome fasta file")
		print("-o, --output=, OPT" + '\t\t' + "Output directory for results. Default = Current directory")
		print("\n" + "DISTRIBUTION PARAMETERS")
	 	print("-m, --mean_read_length=, OPT" + '\t\t' + "Mean read length for in-silico read generation. Default = 10000 bp")
		print("-s, --standard_dev=, OPT" + '\t\t' + "Standard deviation of in-silico reads. Default = 2050")
		print("-c, --coverage=, OPT" + '\t\t' + "Desired genome coverage of in-silico sequencing. Default = 8")
		print("-t, --trials=, OPT" + '\t\t' + "Number of trials. Default = 1000")
		print("-h" + '\t\t' + "Display this message")
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print("Usage: python simulation.py -i </path/to/genome> -o </path/to/outfile.bed> -m <mean read length> -s <standard dev of read lengths> -c <coverage>")
			print("-i, --infile=, REQ" + '\t\t' + "Input genome fasta file")
			print("-o, --output=, OPT" + '\t\t' + "Output directory for results. Default = Current directory")
			print("\n" + "DISTRIBUTION PARAMETERS")
			print("-m, --mean_read_length=, OPT" + '\t\t' + "Mean read length for in-silico read generation. Default = 10000 bp")
			print("-s, --standard_dev=, OPT" + '\t\t' + "Standard deviation of in-silico reads. Default = 2050")
			print("-c, --coverage=, OPT" + '\t\t' + "Desired genome coverage of in-silico sequencing. Default = 8")
			print("-h" + "\t\t" + "Display this message")
			sys.exit(2)
		elif opt in ("-i","--infile"):
			infileName = arg
		elif opt in ("-o","--outfile"):
			outfileName = arg
		elif opt in ("-m", "--mean_read_length"):
			mean = int(arg)
		elif opt in ("-s", "--standard_dev"):
			std = int(arg)
		elif opt in ("-c", "--coverage"):
			desired_cov = int(arg)
		elif opt in ("-t", "--trials"):
			trialCount = int(arg)

	#Split the input genome to chromosomal fasta files and return the sorted list of chromosome names.
	names = splitGenomeFasta(infileName)

	#Generate a distribution of chromosome lenghts in the provided genome.
	generateChrDist(names) #This needs to be reconfigured...it won't need to take arguments any more - done?
	
	#Generate simulated reads
	simulateReads(infileName,outfileName,mean,std,desired_cov,trialCount,names) #Also will need to be reconfigured to take commnads from this function, not the command line


if __name__ == "__main__":
   main(sys.argv[1:])
