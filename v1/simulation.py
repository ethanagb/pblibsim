import gzip
import numpy as np
import sys
import getopt

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

for chrom in xrange(1,chrCount): #might have to change this because it will change chrX to chr24
    name = "chr"+str(chrom) #this name will go as key in dict
    if name =="chr1":
        thresholdDict[name]=lengthDict[name]
        correctionDict["chr1"]=0
    else:
        threshVal = 0
        correctedVal = 0
        i=1
        while (i<=chrom):
            name2 = "chr"+str(i)
            threshVal += lengthDict[name2]
            i += 1
        correctedVal = threshVal - lengthDict[name2] 
        thresholdDict[name2] = threshVal
        correctionDict[name2] = correctedVal

#Calculate reads required for certain coverage.

#These need to become parameters. 
mean = 10000
std = 2050
desired_cov = 8

#Some calculations for the log-normal distribution. 
sigma = (np.log(1+(float(mean)/(float(std))**2)))**0.5
mu = np.log(mean)-0.5*sigma**2
req_reads = (desired_cov*total)/mean

trial_counter=0
trials = 1000
while trial_counter < trials:
    read_length_counter = 0
    read_pos_counter = 0
    readlengths = None
    readlengths=np.random.lognormal(mu,sigma,req_reads)
    read_pos=[]
    name_counter = 0
   
    outfile = gzip.open('simulated_read_positions_trial_'+str(trial_counter) +'.bed.gz','wb')
    for length in readlengths:
        x = int(round(length))
        buf = x/2 #protects against end selection bias and simulated read bridging two chromosomes.
        while loopController = True:
            y = np.random.randint(0, genomeLength)

            #This is going to have to change to work for any number of chromosomes. 

            #chrN_thresh variables are now in the thresholdDict[]...
            #generate a name variable, check regions until something is satisfied...
            #this is going to need thorough testing

            for chrom in thresholdDict:
                k = 1 #a counter to get the next chromosome threshold.
                #Need to ensure this is iterating over key names (check this)
                if chrom == 'chr1':
                    t=0
                else:
                    t=thresholdDict[chrom]
                    r=thresholdDict[names[k]]
                if t+buf <= y <= t-buf or t+buf <= y <= r-buf:
                    loopController = False
                    break
                k += 1
                if k=chrCount:
                    loopController = False
                    break #would be out of bounds, so time to stop this loop (test this). 

            '''
            if buf <= y <= chr1_thresh-buf or chr1_thresh + buf <= y <= chr2_thresh-buf or chr2_thresh + buf <= y <= chr3_thresh-buf or chr3_thresh + buf <= y <= chr4_thresh-buf or\
            chr4_thresh + buf <= y <= chr5_thresh-buf or chr5_thresh + buf <= y <= chr6_thresh-buf or chr6_thresh + buf <= y <= chr7_thresh-buf or chr7_thresh + buf <= y <= chr8_thresh-buf or\
            chr8_thresh + buf <= y <= chr9_thresh-buf or chr9_thresh + buf <= y <= chr10_thresh-buf:
                break
            '''
        start_pos = y-buf
        end_pos = y+buf
        #Figure out which chromosome this is in
        #This is going to have to change to work for any number of chromosomes. 
        if 0<=start_pos<= chr1_thresh:
            selected_chrom = 'chr1'
        elif chr1_thresh < start_pos <= chr2_thresh:
            selected_chrom = 'chr2'
        elif chr2_thresh < start_pos <= chr3_thresh:
            selected_chrom = 'chr3'
        elif chr3_thresh < start_pos <= chr4_thresh:
            selected_chrom = 'chr4'
        elif chr4_thresh < start_pos <= chr5_thresh:
            selected_chrom = 'chr5'
        elif chr5_thresh < start_pos <= chr6_thresh:
            selected_chrom = 'chr6'
        elif chr6_thresh < start_pos <= chr7_thresh:
            selected_chrom = 'chr7'
        elif chr7_thresh < start_pos <= chr8_thresh:
            selected_chrom = 'chr8'
        elif chr8_thresh < start_pos <= chr9_thresh:
            selected_chrom = 'chr9'
        elif chr9_thresh < start_pos <= chr10_thresh:
            selected_chrom = 'chr10'
        else:
            selected_chrom = 'chr?'
        outfile.write(str(selected_chrom) + '\t' + str(start_pos-correction_dict[str(selected_chrom)]) + '\t' + str(end_pos-correction_dict[str(selected_chrom)]) + '\t' + 'trial_'+str(trial_counter) +'_sim_read_' + str(name_counter) + '\n')
        name_counter+=1
        x=None
        y=None
        selected_chrom=None
        start_pos=None
        end_pos=None
    outfile.close()
    trial_counter+=1
