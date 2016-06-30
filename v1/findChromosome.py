def findChromosome(start_pos,names,thresholdDict):
    #Figure out which chromosome this is in
    chromFound = False
    print("Finding which chromosome this read is from...")
        
    while chromFound == False: ##something is going wrong here 
        i=-1
        while i < len(names):
            i+=1
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
        if chromFound == False:
            sys.exit(2)
    return selected_chrom