from __future__ import division
import gzip
import numpy as np
import sys, getopt
import math
from getRandomPosition import getRandomPosition
from findChromosome import findChromosome

def simulateReads(argv):
    #parse args and intialize variables 
    global mean, outfileName, std, desired_cov,y
    outfileName = 'simulationResults.bed'
    mean = 10000
    std = 2050
    desired_cov = 8 
    y=0
    loopController=True
    
    try:
        opts, args = getopt.getopt(argv,"i:o:m:s:c:h",["infile=","outfile=","mean_read_length=-","standard_dev=", "coverage="])
    except getopt.GetoptError:
        print("Usage: python simulation.py --infile </path/to/chrdist.td> --outfile </path/to/outfile.bed> -m <mean read length> -s <standard dev of read lenghts> -c <coverage>")
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
    print("SiLiCO will simulate sequencing results with the following paramters:" + '\n' + "Mean Read Length = " + str(mean) + '\n' + "Standard Deviation of Read Length = " + str(std) + '\n' + 'Coverage = ' + str(desired_cov) + '\n')
    #generate chrdist.td file
    
    with open('chrdist.td','r') as infile:
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

    #calculating total genome length
    for n in lengths:
        genomeLength += n

    chrCount = len(lengths)
    thresholdDict={} #dictionary of chromome thresholds (defined as end of a chromsome as determined by length from chrdist.td)
    correctionDict={} #A correction to get the start of the chromosome as well. Important for generating bed file. (Maybe can get rid of this eventually?)

    #Generate a dictionary of chromosome thresholds (replaces hard-coded previous version)
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
            #correctionDict[name2] = correctedVal
    print("Done!")
    print thresholdDict
    print("Calculating distribution parameters...")
    #Some calculations for the log-normal distribution. 
    sigma = (math.log(1+(float(mean)/(float(std))**2)))**0.5
    mu = math.log(float(mean))-0.5*sigma**2
    req_reads = int((int(desired_cov)*genomeLength)/float(mean))
    print("sigma:" + str(sigma))
    print("mu: " + str(mu))
    print(str(req_reads) + " in-silico reads will be generated per trial.")
    
    trial_counter=0
    trials = 1000
    while trial_counter < trials:
        print("This is trial " + str(trial_counter))
        read_length_counter = 0
        read_pos_counter = 0
        readlengths = None
        readlengths=np.random.lognormal(mu,sigma,req_reads)
        read_pos=[]
        name_counter = 0
        print(len(readlengths))       
        outfile = gzip.open('simulated_read_positions_trial_'+str(trial_counter) +'.bed.gz','wb')
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
            """chromFound = False
            print("Finding which chromosome this read is from...")
                
            while chromFound == False: ##something is going wrong here 
                for i in range(0,len(names)):
                    chromName = str(names[i])
                    print("testing:")
                    print chromName
                    if i-1 >= 0:
                        prevChromName = str(names[i-1])
                        if thresholdDict[prevChromName] < start_pos <= thresholdDict[chromName]:
                            selected_chrom = chromName
                            chromFound = True
                            if chromFound == True:
                                print("Chrom found!")
                            break
                    
                    elif i-1 < 0: #chr1
                        if 0<=start_pos<=thresholdDict[chromName]:
                            selected_chrom = chromName
                            chromFound = True
                            if chromFound == True:
                                print("Chrom found!")
                            break
                print("still running the while loop")"""

            print("This is on " + str(selected_chrom))
            #build correction dictionary
            print("correcting positions...")
            for j in range(0,chrCount):
                #print("j= " + str(j)) 
                chromName = str(names[j])
                if j-1 < 0: #chr1
                    correctionDict[chromName] = 0
                elif j-1 >= 0:
                    prevChromName = str(names[j-1])
                    correctionDict[chromName] = thresholdDict[prevChromName]

            print("Writing this read to the outfile for this trial...")
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

if __name__ == "__main__":
    simulateReads(sys.argv[1:])