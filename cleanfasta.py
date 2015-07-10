
#Pull in list of base file names. Could implement as a flag at some point.
with open('/Users/Ethan/Desktop/CSHL/NickBioinformatics/namelist','r') as infile:
    lines = infile.readlines()
    names =[str(e.strip()) for e in lines]
infile.close()

for chrom in names:
    
    #Strip header lines from fasta for processing
    with open('/Users/Ethan/Desktop/CSHL/NickBioinformatics/' + str(chrom) + '.fa','r') as infile, open('/Users/Ethan/Desktop/CSHL/NickBioinformatics/' + str(chrom) + '.noheader.fa','w+') as outfile:
        for i, line in enumerate(infile):
            if i >= 0:
                if not line.startswith('>'):
                    outfile.write(line)
    infile.close()
    outfile.close()  
    
    #Remove any newline chars, remove undefined nts, make all nts uppercase for processing. 
    with open('/Users/Ethan/Desktop/CSHL/NickBioinformatics/' + str(chrom) + '.noheader.fa','r') as infile, open('/Users/Ethan/Desktop/CSHL/NickBioinformatics/' + str(chrom) + '.clean.fa','w+') as outfile:
        lines = infile.readlines()
        x = map(str.strip,lines)
        seq = ''
        for line in x:
            y = str(line)
            z = y.upper()
            w = z.replace('N','')
            seq += w
        outfile.write(seq)
    infile.close()
    outfile.close()