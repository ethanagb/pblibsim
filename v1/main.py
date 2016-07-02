import sys, getopt, os, math, gzip
import numpy as np
from splitGenomeFasta import splitGenomeFasta
from getRandomPosition import getRandomPosition
from findChromosome import findChromosome
from generateChrDist import generateChrDist
from simulateReads import simulateReads
from convertToFasta import convertToFasta

def main(argv):
	#set default/placeholder values
	global mean, outfileName, std, desired_cov,y
	outfileName = 'simulationResults.bed'
	mean = 10000
	std = 2050
	desired_cov = 8 
	trialCount = 1000
	FASTA_MODE = False
	#Parse arguments
	try:
		opts, args = getopt.getopt(argv,"i:o:m:s:c:tfh",["infile=","outfile=","mean_read_length=","standard_dev=", "coverage=","trials=","fasta"])
	except getopt.GetoptError:
		print("\n####################################################################\n## SiLiCO: Simulator of Long Read Sequencing in PacBio and Oxford Nanopore ##\n####################################################################")
		print("\nUsage: python simulation.py -i </path/to/genome> -o </path/to/outfile.bed> -m <mean read length> -s <standard dev of read lengths> -c <coverage>")
		print("-i, --infile=<str>, REQ" + '\t\t' + "Input genome fasta file")
		print("-o, --output=<str>, OPT" + '\t\t' + "Output directory for results. Default = Current directory")
		print("\n" + "DISTRIBUTION PARAMETERS")
		print("-m, --mean_read_length=<int>, OPT" + '\t' + "Mean read length for in-silico read generation. Default = 10000 bp")
		print("-s, --standard_dev=<int>, OPT" + '\t\t' + "Standard deviation of in-silico reads. Default = 2050")
		print("-c, --coverage=<int>, OPT" + '\t\t' + "Desired genome coverage of in-silico sequencing. Default = 8")
		print("-t, --trials=<int>, OPT" + '\t\t\t' + "Number of trials. Default = 1000 +\n")
		print("OTHER + \n")
		print("-f, --fasta, OPT \t\t FASTA Mode. When present, converts bed files to Fasta sequences using the provided reference genome. D")
		print("-h" + '\t\t\t' + "Display this message")
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print("\n####################################################################\n## SiLiCO: Simulator of Long Read Sequencing in PacBio and Oxford Nanopore ##\n####################################################################")
			print("\nUsage: python simulation.py -i </path/to/genome> -o </path/to/outfile.bed> -m <mean read length> -s <standard dev of read lengths> -c <coverage> -t <trials> [-f] \n")
			print("-i, --infile=<str>, REQ" + '\t\t' + "Input genome fasta file")
			print("-o, --output=<str>, OPT" + '\t\t' + "Output directory for results. Default = Current directory")
			print("\n" + "DISTRIBUTION PARAMETERS")
			print("-m, --mean_read_length=<int>, OPT" + '\t' + "Mean read length for in-silico read generation. Default = 10000 bp")
			print("-s, --standard_dev=<int>, OPT" + '\t\t' + "Standard deviation of in-silico reads. Default = 2050")
			print("-c, --coverage=<int>, OPT" + '\t\t' + "Desired genome coverage of in-silico sequencing. Default = 8")
			print("-t, --trials=<int>, OPT" + '\t\t\t' + "Number of trials. Default = 1000 +\n")
			print("OTHER \n")
			print("-f, --fasta, OPT \t\t FASTA Mode. When present, converts bed files to Fasta sequences using the provided reference genome. D")
			print("-h" + '\t\t\t\t' + " Display this message")
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
		elif opt in ("-f", "--fasta"):
			FASTA_MODE = True

	#Split the input genome to chromosomal fasta files and return the sorted list of chromosome names.
	names = splitGenomeFasta(infileName)

	#Generate a distribution of chromosome lenghts in the provided genome.
	generateChrDist(names) #This needs to be reconfigured...it won't need to take arguments any more - done?
	
	#Generate simulated reads
	simulateReads(infileName,outfileName,mean,std,desired_cov,trialCount,names) #Also will need to be reconfigured to take commnads from this function, not the command line

	#If -f/--fasta flag is found, convert to fasta file using the reference genome.
	if FASTA_MODE == True:
		convertToFasta(infileName)

if __name__ == "__main__":
   main(sys.argv[1:])
