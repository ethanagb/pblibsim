import numpy as np

#names = ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15','chr16', 'chr17', 'chr18', 'chr19', 'chr20', 'chr21', 'chr22', 'chrX', 'chrY']

"""with open('namelist','r') as infile:
    lines = infile.readlines()
    names =[str(e.strip()) for e in lines]
infile.close()"""

"""with open('chrdist.td','w+') as outfile2:
    for chrom in names:
        
        #Strip header lines from fasta for processing
        with open(str(chrom) + '.fa','r') as infile, open(str(chrom) + '.noheader.fa','w+') as outfile:
            for i, line in enumerate(infile):
                if i >= 0:
                    if not line.startswith('>'):
                        outfile.write(line)
        infile.close()
        outfile.close()  
        
        #Remove any newline chars, remove undefined nts, make all nts uppercase for processing. 
        with open(str(chrom) + '.noheader.fa','r') as infile, \
        open(str(chrom) + '.clean.fa','w+') as outfile:
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
outfile2.close()"""

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

chr1_thresh= d['chr1']
chr2_thresh=d['chr1'] + d['chr2']
chr3_thresh=d['chr1'] + d['chr2'] + d['chr3']
chr4_thresh=d['chr1'] + d['chr2']+ d['chr3']+ d['chr4']
chr5_thresh=d['chr1'] + d['chr2']+ d['chr3']+ d['chr4']+ d['chr5']
chr6_thresh=d['chr1'] + d['chr2']+ d['chr3']+ d['chr4']+ d['chr5']+ d['chr6']
chr7_thresh=d['chr1'] + d['chr2']+ d['chr3']+ d['chr4']+ d['chr5']+ d['chr6']+ d['chr7']
chr8_thresh=d['chr1'] + d['chr2']+ d['chr3']+ d['chr4']+ d['chr5']+ d['chr6']+ d['chr7']+ d['chr8']
chr9_thresh=d['chr1'] + d['chr2']+ d['chr3']+ d['chr4']+ d['chr5']+ d['chr6']+ d['chr7']+ d['chr8']+ d['chr9']
chr10_thresh=d['chr1'] + d['chr2']+ d['chr3']+ d['chr4']+ d['chr5']+ d['chr6']+ d['chr7']+ d['chr8']+ d['chr9']+ d['chr10']
chr11_thresh=d['chr1'] + d['chr2']+ d['chr3']+ d['chr4']+ d['chr5']+ d['chr6']+ d['chr7']+ d['chr8']+ d['chr9']+ d['chr10']+ d['chr11']
chr12_thresh=d['chr1'] + d['chr2']+ d['chr3']+ d['chr4']+ d['chr5']+ d['chr6']+ d['chr7']+ d['chr8']+ d['chr9']+ d['chr10']+ d['chr11']+ d['chr12']
chr13_thresh=d['chr1'] + d['chr2']+ d['chr3']+ d['chr4']+ d['chr5']+ d['chr6']+ d['chr7']+ d['chr8']+ d['chr9']+ d['chr10']+ d['chr11']+ d['chr12']+ d['chr13']
chr14_thresh=d['chr1'] + d['chr2']+ d['chr3']+ d['chr4']+ d['chr5']+ d['chr6']+ d['chr7']+ d['chr8']+ d['chr9']+ d['chr10']+ d['chr11']+ d['chr12']+ d['chr13']+ d['chr14']
chr15_thresh=d['chr1'] + d['chr2']+ d['chr3']+ d['chr4']+ d['chr5']+ d['chr6']+ d['chr7']+ d['chr8']+ d['chr9']+ d['chr10']+ d['chr11']+ d['chr12']+ d['chr13']+ d['chr14']+ d['chr15']
chr16_thresh=d['chr1'] + d['chr2']+ d['chr3']+ d['chr4']+ d['chr5']+ d['chr6']+ d['chr7']+ d['chr8']+ d['chr9']+ d['chr10']+ d['chr11']+ d['chr12']+ d['chr13']+ d['chr14']+ d['chr15']+ d['chr16']
chr17_thresh=d['chr1'] + d['chr2']+ d['chr3']+ d['chr4']+ d['chr5']+ d['chr6']+ d['chr7']+ d['chr8']+ d['chr9']+ d['chr10']+ d['chr11']+ d['chr12']+ d['chr13']+ d['chr14']+ d['chr15']+ d['chr16']+ d['chr17']
chr18_thresh=d['chr1'] + d['chr2']+ d['chr3']+ d['chr4']+ d['chr5']+ d['chr6']+ d['chr7']+ d['chr8']+ d['chr9']+ d['chr10']+ d['chr11']+ d['chr12']+ d['chr13']+ d['chr14']+ d['chr15']+ d['chr16']+ d['chr17']+ d['chr18']
chr19_thresh=d['chr1'] + d['chr2']+ d['chr3']+ d['chr4']+ d['chr5']+ d['chr6']+ d['chr7']+ d['chr8']+ d['chr9']+ d['chr10']+ d['chr11']+ d['chr12']+ d['chr13']+ d['chr14']+ d['chr15']+ d['chr16']+ d['chr17']+ d['chr18']+ d['chr19']
chr20_thresh=d['chr1'] + d['chr2']+ d['chr3']+ d['chr4']+ d['chr5']+ d['chr6']+ d['chr7']+ d['chr8']+ d['chr9']+ d['chr10']+ d['chr11']+ d['chr12']+ d['chr13']+ d['chr14']+ d['chr15']+ d['chr16']+ d['chr17']+ d['chr18']+ d['chr19']+ d['chr20']
chr21_thresh=d['chr1'] + d['chr2']+ d['chr3']+ d['chr4']+ d['chr5']+ d['chr6']+ d['chr7']+ d['chr8']+ d['chr9']+ d['chr10']+ d['chr11']+ d['chr12']+ d['chr13']+ d['chr14']+ d['chr15']+ d['chr16']+ d['chr17']+ d['chr18']+ d['chr19']+ d['chr20']+ d['chr21']
chr22_thresh=d['chr1'] + d['chr2']+ d['chr3']+ d['chr4']+ d['chr5']+ d['chr6']+ d['chr7']+ d['chr8']+ d['chr9']+ d['chr10']+ d['chr11']+ d['chr12']+ d['chr13']+ d['chr14']+ d['chr15']+ d['chr16']+ d['chr17']+ d['chr18']+ d['chr19']+ d['chr20']+ d['chr21']+ d['chr22']
chrX_thresh=d['chr1'] + d['chr2']+ d['chr3']+ d['chr4']+ d['chr5']+ d['chr6']+ d['chr7']+ d['chr8']+ d['chr9']+ d['chr10']+ d['chr11']+ d['chr12']+ d['chr13']+ d['chr14']+ d['chr15']+ d['chr16']+ d['chr17']+ d['chr18']+ d['chr19']+ d['chr20']+ d['chr21']+ d['chr22']+ d['chrX']
chrY_thresh=total

#Calculate reads required for certain coverage.
mean = 10000
std = 2050
desired_cov = 8
sigma = (np.log(1+(float(mean)/(float(std))**2)))**0.5
mu = np.log(mean)-0.5*sigma**2
req_reads = (desired_cov*total)/mean

read_length_counter = 0
read_pos_counter = 0
readlengths=np.random.lognormal(mu,sigma,req_reads)
read_pos=[]
name_counter = 0
print(str(req_reads)+' are required for ' + str(desired_cov) +'x coverage. ' + str(len(readlengths)) + ' lengths were generated.')

outfile = open('simulated_read_positions.bed','w+')
for length in readlengths:
    x = int(round(length))
    buf = x/2
    while True:
        y = np.random.randint(0,total)
        if buf <= y <= chr1_thresh-buf or chr1_thresh + buf <= y <= chr2_thresh-buf or chr2_thresh + buf <= y <= chr3_thresh-buf or chr3_thresh + buf <= y <= chr4_thresh-buf or\
        chr4_thresh + buf <= y <= chr5_thresh-buf or chr5_thresh + buf <= y <= chr6_thresh-buf or chr6_thresh + buf <= y <= chr7_thresh-buf or chr7_thresh + buf <= y <= chr8_thresh-buf or\
        chr8_thresh + buf <= y <= chr9_thresh-buf or chr10_thresh + buf <= y <= chr11_thresh-buf or chr11_thresh + buf <= y <= chr12_thresh-buf or\
        chr12_thresh + buf <= y <= chr13_thresh-buf or chr13_thresh + buf <= y <= chr14_thresh-buf or chr14_thresh + buf <= y <= chr15_thresh-buf or\
        chr15_thresh + buf <= y <= chr16_thresh-buf or chr16_thresh + buf <= y <= chr17_thresh-buf or chr17_thresh + buf <= y <= chr18_thresh-buf or \
        chr18_thresh + buf <= y <= chr19_thresh-buf or chr19_thresh + buf <= y <= chr20_thresh-buf or chr20_thresh + buf <= y <= chr21_thresh-buf or\
        chr21_thresh + buf <= y <= chr22_thresh-buf or chr22_thresh + buf <= y <= chrX_thresh-buf or chrX_thresh + buf <= y <= chrY_thresh-buf:
            break
    start_pos = y-buf
    end_pos = y+buf
    #Figure out which chromosome this is in
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
    elif chr10_thresh < start_pos <= chr11_thresh:
        selected_chrom = 'chr11'
    elif chr11_thresh < start_pos <= chr12_thresh:
        selected_chrom = 'chr12'
    elif chr12_thresh < start_pos <= chr13_thresh:
        selected_chrom = 'chr13'
    elif chr13_thresh < start_pos <= chr14_thresh:
        selected_chrom = 'chr14'
    elif chr14_thresh < start_pos <= chr15_thresh:
        selected_chrom = 'chr15'
    elif chr15_thresh < start_pos <= chr16_thresh:
        selected_chrom = 'chr16'
    elif chr16_thresh < start_pos <= chr17_thresh:
        selected_chrom = 'chr17'
    elif chr17_thresh < start_pos <= chr18_thresh:
        selected_chrom = 'chr18'
    elif chr18_thresh < start_pos <= chr19_thresh:
        selected_chrom = 'chr19'
    elif chr19_thresh < start_pos <= chr20_thresh:
        selected_chrom = 'chr20'
    elif chr20_thresh < start_pos <= chr21_thresh:
        selected_chrom = 'chr21'
    elif chr21_thresh < start_pos <= chr21_thresh:
        selected_chrom = 'chr22'
    elif chr22_thresh < start_pos <= chrX_thresh:
        selected_chrom = 'chrX'
    elif chrX_thresh < start_pos <= chrY_thresh:
        selected_chrom = 'chrY'
    else:
        selected_chrom = 'chr?'
    outfile.write(str(selected_chrom) + '\t' + str(start_pos) + '\t' + str(end_pos) + '\t' + 'simulated_read_' + str(name_counter) + '\n')
    print('Positions recorded for read ' + str(name_counter) + '. ' + str(len(readlengths)-name_counter -1) + ' reads remain.')
    name_counter+=1
    x=None
    y=None
    selected_chrom=None
    start_pos=None
    end_pos=None
outfile.close()
print('Done')