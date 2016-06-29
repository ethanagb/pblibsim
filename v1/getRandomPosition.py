import numpy as np

def getRandomPosition(buf,genomeLength, thresholdDict,names,):
    loopController = True
    while loopController == True:
        y = np.random.randint(buf, genomeLength-buf)
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
            if k==len(names):
                loopController = False
                break #would be out of bounds, so time to stop this loop (test this). 
        return y
if __name__ == "__main__":
    getRandomPosition()