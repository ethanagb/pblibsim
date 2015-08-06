import gzip
import numpy as np

with open('namelist','r') as infile:
    lines = infile.readlines()
    names =[str(e.strip()) for e in lines]
infile.close()

with open('chrdist.td','w+') as outfile2:
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
outfile2.close()

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


correction_dict = {'chr1':0,'chr2':chr1_thresh,'chr3':chr2_thresh,'chr4':chr3_thresh,'chr5':chr4_thresh,'chr6':chr5_thresh, 'chr7':chr6_thresh, 'chr8':chr7_thresh, 'chr9':chr8_thresh,'chr10':chr9_thresh}  

#Calculate reads required for certain coverage.
mean = 10000
std = 2050
desired_cov = 8
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
    #print('########################################' + '\n' + 'THIS IS TRIAL ' + str(trial_counter) + ' of ' + str(trials) +'.\n##################################')
    #print(str(req_reads)+' are required for ' + str(desired_cov) +'x coverage. ' + str(len(readlengths)) + ' lengths were generated.')
    
    outfile = gzip.open('simulated_read_positions_trial_'+str(trial_counter) +'.bed','wb')
    for length in readlengths:
        x = int(round(length))
        buf = x/2
        while True:
            y = np.random.randint(0,total)
            if buf <= y <= chr1_thresh-buf or chr1_thresh + buf <= y <= chr2_thresh-buf or chr2_thresh + buf <= y <= chr3_thresh-buf or chr3_thresh + buf <= y <= chr4_thresh-buf or\
            chr4_thresh + buf <= y <= chr5_thresh-buf or chr5_thresh + buf <= y <= chr6_thresh-buf or chr6_thresh + buf <= y <= chr7_thresh-buf or chr7_thresh + buf <= y <= chr8_thresh-buf or\
            chr8_thresh + buf <= y <= chr9_thresh-buf or chr9_thresh + buf <= y <= chr10_thresh-buf:
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
        else:
            selected_chrom = 'chr?'
        outfile.write(str(selected_chrom) + '\t' + str(start_pos-correction_dict[str(selected_chrom)]) + '\t' + str(end_pos-correction_dict[str(selected_chrom)]) + '\t' + 'trial_'+str(trial_counter) +'_sim_read_' + str(name_counter) + '\n')
        #print('Positions recorded for read ' + str(name_counter) + '. ' + str(len(readlengths)-name_counter -1) + ' reads remain.')
        name_counter+=1
        x=None
        y=None
        selected_chrom=None
        start_pos=None
        end_pos=None
    outfile.close()
    trial_counter+=1
    #print('Done')
#print('El fin.')