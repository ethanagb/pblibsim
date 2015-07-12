from __future__ import division

#Pull in list of base file names. Could implement as a flag at some point.
with open('/Users/Ethan/Desktop/CSHL/NickBioinformatics/namelist','r') as infile:
    lines = infile.readlines()
    names =[str(e.strip()) for e in lines]
infile.close()

with open('/Users/Ethan/Desktop/CSHL/NickBioinformatics/chrdist.td','w+') as outfile2:
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
        with open('/Users/Ethan/Desktop/CSHL/NickBioinformatics/' + str(chrom) + '.noheader.fa','r') as infile, \
        open('/Users/Ethan/Desktop/CSHL/NickBioinformatics/' + str(chrom) + '.clean.fa','w+') as outfile:
            lines = infile.readlines()
            x = map(str.strip,lines)
            seq = ''
            for line in x:
                y = str(line)
                z = y.upper()
                w = z.replace('N','')
                seq += w
            outfile.write(seq)
            outfile2.write(str(chrom) + '\t' + str(len(seq)) + '\n')
        infile.close()
        outfile.close()
outfile2.close()

#Calculate probability distribution of chromosomes.
with open('chrdist.td','r') as infile:
    lengths = []
    names = []
    for x in infile:
        length = x.split('\t')[1]
        name = x.split('\t')[0]
        lengths.append(int(length))
        names.append(str(name))
infile.close()
d = dict(zip(names,lengths))
total=0 
for n in lengths:
    total += n
with open('chrdists.frac.td','w+') as outfile:
    for key in d:
        frac = float(d[key])/total
        outfile.write(str(key) + '\t' + str(frac) + '\n')

