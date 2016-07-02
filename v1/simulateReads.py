#################################
######### SiLiCO v. 1.0 #########
### (c)2016 Ethan A. G. Baker ###
##### ethanagbaker@pitt.edu #####
#################################

from __future__ import division
from natsort import natsorted
import numpy as np
import sys, getopt, math, gzip
from getRandomPosition import getRandomPosition
from findChromosome import findChromosome

def simulateReads(infileName,outfileName,mean,std,desired_cov,trialCount,names):
	#Initialize variables
	y=0
	loopController=True
	
	#Open the index file (chrdist.td)
	with open("SiLiCO_Scratch/chrdist.td",'r') as infile:
		lengths = []
		names = []
		for x in infile:
			length = x.split('\t')[1]
			name = x.split('\t')[0]
			lengths.append(int(length))
			names.append(str(name))
	infile.close()
	lengthDict = dict(zip(names,lengths))
	genomeLength=0 
	names=natsorted(names) #A sorted list of chromosome names.

	#Calculate the total genome length
	for n in lengths:
		genomeLength += n

	chrCount = len(lengths)
	thresholdDict={} #A dictionary of chromome thresholds (defined as end of a chromsome as determined by length from chrdist.td)
	correctionDict={} #A correction to get the start of the chromosome. Important for generating bed file. 

	#Generate the threshold dictionary.

	print("Building threshold dictionaries...")
	for chrom in range(0,len(names)): #might have to change this because it will change chrX to chr24 (build an array of names and use an index)
		name = str(names[chrom])#this name will go as key in dict
		print name
		if name =="chr1":
			thresholdDict[name]=lengthDict[name]
			#correctionDict["chr1"]=0
		else:
			threshVal = 0
			correctedVal = 0
			i=1
			while (i<=chrom+1):
				name2 = "chr"+str(i)
				threshVal += lengthDict[name2]
				i += 1
			correctedVal = threshVal - lengthDict[name2] 
			thresholdDict[name2] = threshVal
	
	#print("Done!")
	#print thresholdDict

	#Some calculations for the log-normal distribution. 
	print("Calculating distribution parameters...")
	
	sigma = (math.log(1+(float(mean)/(float(std))**2)))**0.5
	mu = math.log(float(mean))-0.5*sigma**2
	req_reads = int((int(desired_cov)*genomeLength)/float(mean))
	
	#print("Sigma:" + str(sigma))
	#print("Mu: " + str(mu))
	#print(str(req_reads) + " in-silico reads will be generated per trial.")
	
	#Begin generating in-silico reads
	trial_counter = 0
	while trial_counter < int(trialCount):
		print("This is trial " + str(trial_counter))
		read_length_counter = 0
		read_pos_counter = 0
		readlengths = None
		readlengths=np.random.lognormal(mu,sigma,req_reads) #Read lengths are randomly determined from the calculated log-normal distribution.
		read_pos=[]
		name_counter = 0
		
		outfile = gzip.open(str(outfileName) + '/simulated_read_positions_trial_'+str(trial_counter) +'.bed.gz','wb')
		for length in readlengths:
			x = int(round(length))
			buf = math.ceil(x/2) #protects against end selection bias and simulated read bridging two chromosomes, in the event of a .5, rounds up to the whole
			y=getRandomPosition(buf,genomeLength,thresholdDict,names)

			start_pos = int(y-buf)
			end_pos = int(y+buf)
			print("start = " + str(start_pos))
			print("end = " + str(end_pos))
			
			#Figure out which chromosome this is in
			selected_chrom = findChromosome(start_pos,names,thresholdDict)

			#Build correction dictionary
			for j in range(0,chrCount):
				chromName = str(names[j])
				if j-1 < 0: #chr1
					correctionDict[chromName] = 0
				elif j-1 >= 0:
					prevChromName = str(names[j-1])
					correctionDict[chromName] = thresholdDict[prevChromName]

			outfile.write(str(selected_chrom) + '\t' + str(start_pos-correctionDict[str(selected_chrom)]) + '\t' + str(end_pos-correctionDict[str(selected_chrom)]) + '\t' + 'trial_'+str(trial_counter) +'_sim_read_' + str(name_counter) + '\n')

			#count this run and reset reused variables. 
			name_counter+=1
			x=None
			y=None
			selected_chrom=None
			start_pos=None
			end_pos=None
		outfile.close()
		trial_counter+=1
		print("Completed trial " + str(trial_counter) + " of " + str(trialCount) + ". ("+ str(100*(float(trial_counter)/trialCount)) + "%)")

if __name__ == "__main__":
	simulateReads(infileName,outfileName,mean,std,desired_cov,trials,names)