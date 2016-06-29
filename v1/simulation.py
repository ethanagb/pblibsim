import gzip
import numpy as np
import sys, getopt
import math

def simulateReads(argv):
    #parse args and intialize variables 
    global mean, outfileName, std, desired_cov
    outfileName = 'simulationResults.bed'
    mean = 10000
    std = 2050
    desired_cov = 8 
    y=0
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
    for chrom in range(1,chrCount): #might have to change this because it will change chrX to chr24 (build an array of names and use an index)
        name = "chr"+str(chrom) #this name will go as key in dict
        if name =="chr1":
            thresholdDict[name]=lengthDict[name]
            #correctionDict["chr1"]=0
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
            #correctionDict[name2] = correctedVal
    print("Done!")
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
            buf = x/2 #protects against end selection bias and simulated read bridging two chromosomes.
            try:
                while loopController == True:
                    y = np.random.randint(0, genomeLength)
                    print("y = " + str(y))
                    #chrN_thresh variables are now in the thresholdDict[]...
                    #generate a name variable, check regions until something is satisfied...
                    #this requires thorough testing

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
                        if k==chrCount:
                            loopController = False
                            break #would be out of bounds, so time to stop this loop (test this). 
            except UnboundLocalError:
                pass
            start_pos = y-buf
            end_pos = y+buf
            print("start = " + str(start_pos))
            print("end = " + str(end_pos))
            
            #Figure out which chromosome this is in
            chromFound = False
            print("Finding which chromosome this read is from...")
            while chromFound == False: ##something is going wrong here 
                for i in range(1,chrCount):
                    chromName = "chr" + str(i)
                    prevChromName ="chr" + str(i-1)
                    #print("testing:")
                    #print chromName, prevChromName
                    if i==1:
                        if 0<=start_pos<=thresholdDict[chromName]:
                            selected_chrom = chromName
                            chromFound = True
                            break
                    else:
                        if thresholdDict[prevChromName] < start_pos <= thresholdDict[chromName]:
                            selected_chrom = chromName
                            chromFound = True
                            break
            print("This is on " + str(selected_chrom))
            #build correction dictionary
            print("correcting positions...")
            for j in range(1,chrCount):
                chromName = "chr"+ str(j)
                prevChromName = "chr" + str(j-1)
                print chromName, prevChromName

                if chromName == "chr1":
                    correctionDict[chromName] = 0
                else:
                    correctionDict[chromName] = thresholdDict[chromName]
            print("Writing this read to the outfile for this trial...")
            outfile.write(str(selected_chrom) + '\t' + str(start_pos-correction_dict[str(selected_chrom)]) + '\t' + str(end_pos-correction_dict[str(selected_chrom)]) + '\t' + 'trial_'+str(trial_counter) +'_sim_read_' + str(name_counter) + '\n')

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