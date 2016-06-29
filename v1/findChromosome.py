def findChromosome(start_pos,names,thresholdDict):
    #Figure out which chromosome this is in
    chromFound = False
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
    return selected_chrom