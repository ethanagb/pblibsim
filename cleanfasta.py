#Strip header lines from fasta for processing
with open('/Users/Ethan/Desktop/CSHL/NickBioinformatics/fasta.fa','r') as infile, open('/Users/Ethan/Desktop/CSHL/NickBioinformatics/fasta.noheaders.fa','w+') as outfile:
    for i, line in enumerate(infile):
        if i >= 0:
            if not line.startswith('>'):
                outfile.write(line)
infile.close()
outfile.close()  

#Remove any newline chars, remove undefined nts, make all nts uppercase for processing. 
with open('/Users/Ethan/Desktop/CSHL/NickBioinformatics/fasta.noheaders.fa','r') as infile, open('/Users/Ethan/Desktop/CSHL/NickBioinformatics/fasta.clean.fa','w+') as outfile:
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