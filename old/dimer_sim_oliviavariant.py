from __future__ import division
import numpy as np
#Pull in list of base file names. Could implement as a flag at some point.


with open('namelist','r') as infile:
    lines = infile.readlines()
    names =[str(e.strip()) for e in lines]
infile.close()
"""
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
outfile2.close()"""

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
keys = []
probs = []
with open('chrdists.frac.td','w+') as outfile:
    for key in d:
        keys.append(key)
        frac = float(d[key])/total
        probs.append(frac)
        outfile.write(str(key) + '\t' + str(frac) + '\n')
outfile.close()
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
chrY_thresh=1
desired_cov = 8
mean = 10000
std = 2050
sigma = (np.log(1+(float(mean)/(float(std))**2)))**0.5
mu = np.log(mean)-0.5*sigma**2
req_reads = (desired_cov*total)/mean


trials = 1000 #SET NUMBER OF TRIALS HERE!
trial_counter = 1
while trial_counter <= trials:
    read_counter = 1 
    simreads=[]
    while read_counter <= req_reads:
        bedout = open('simulation_bed.bed','a+')
        selected_chrom = None
        #selected_chrom = np.random.choice(keys,p=probs) 
        seq = ""
        e = np.random.sample()
        if 0 <= e < chr1_thresh:
            selected_chrom='chr1'
        elif chr1_thresh <= e < chr2_thresh:
            selected_chrom='chr2'
        elif chr2_thresh <= e < chr3_thresh:
            selected_chrom='chr3'
        elif chr3_thresh <= e < chr4_thresh:
            selected_chrom='chr4'
        elif chr4_thresh <= e < chr5_thresh:
            selected_chrom='chr5'
        elif chr5_thresh <= e < chr6_thresh:
            selected_chrom='chr6'
        elif chr6_thresh <= e < chr7_thresh:
            selected_chrom='chr7'
        elif chr7_thresh <= e < chr8_thresh:
            selected_chrom='chr8'
        elif chr8_thresh <= e < chr9_thresh:
            selected_chrom='chr9'
        elif chr9_thresh <= e < chr10_thresh:
            selected_chrom='chr10'
        elif chr10_thresh <= e < chr11_thresh:
            selected_chrom='chr11'
        elif chr11_thresh <= e < chr12_thresh:
            selected_chrom='chr12'
        elif chr12_thresh <= e < chr13_thresh:
            selected_chrom='chr13'
        elif chr13_thresh <= e < chr14_thresh:
            selected_chrom='chr14'
        elif chr14_thresh <= e < chr15_thresh:
            selected_chrom='chr15'
        elif chr15_thresh <= e < chr16_thresh:
            selected_chrom='chr16'
        elif chr16_thresh <= e < chr17_thresh:
            selected_chrom='chr17'
        elif chr17_thresh <= e < chr18_thresh:
            selected_chrom='chr18'
        elif chr18_thresh <= e < chr19_thresh:
            selected_chrom='chr19'
        elif chr19_thresh <= e < chr20_thresh:
            selected_chrom='chr20'
        elif chr20_thresh <= e < chr21_thresh:
            selected_chrom='chr21'
        elif chr21_thresh <= e < chr22_thresh:
            selected_chrom='chr22'
        elif chr22_thresh <= e < chrX_thresh:
            selected_chrom='chrX'
        elif chrX_thresh <= e < chrY_thresh:
            selected_chrom='chrY'

        with open(str(selected_chrom) + '.clean.fa', 'r') as infile:
            for x in infile:
                seq += str(x)
        infile.close()
        read_length = int(round(np.random.lognormal(mu,sigma)))
        buf = read_length/2
        x = np.random.randint(buf,total-buf)
        low = int(x-buf)
        hi = int(x+buf)
        bedout.write(str(selected_chrom) +'\t' +str(low) + '\t' + str(hi) + '\n')
        bedout.close()
        simread = seq[low:hi+1]
        seq=None
        simreads.append(simread)
        print("Trial " + str(trial_counter) + ", Read " + str(read_counter) + ' complete. Now building FASTA...')
        read_counter =+1
    with open('simulatedreads_trial_'+str(trial_counter) + '.fa','w+') as fastaout:
        for i in xrange(0,len(simreads)):
            fastaout.write('>simualtedread_'+str(i) + '\n' + str(simreads[i]) + '\n')
        simreads=None
    fastaout.close()
    print("FASTA complete.")
    trial_counter += 1

print("Counting dimers...")
for i in xrange(1,trials+1):
    finalout = open('simulationresults_trial_'+str(i)+'.td','w+')
    finalout.write('Chr_Name' + '\t' + 'AA' + '\t'+ 'AT'+ '\t'+ 'AC'+ '\t'+ 'AG' + '\t'+ 'TA'+ '\t'+ 'TT' + '\t'+ 'TC' + '\t' + 'TG' + '\t'+'GA' + '\t'+ 'GT' + '\t'+ 'GG' + '\t'+ 'GC'+ '\t'+ 'CA' + '\t'+ 'CT' + '\t'+ 'CG' + '\t'+ 'CC' + '\t'+ 'Total_dimers' + '\n')
    with open('simulatedreads_trial_'+str(i) + '.fa','w+') as f: 
        AA = 0
        AT = 0
        AC = 0
        AG = 0
        TA = 0
        TT = 0
        TC = 0
        TG = 0
        CA = 0
        CT = 0
        CG = 0
        CC = 0
        GA = 0
        GT = 0
        GG = 0
        GC = 0
        n=[]
        lines = f.readlines()
        for l in lines:
            if not l.startswith('>'):
                n.append(l)
    f.close()
    lines=None
    for r in xrange(0,len(n)-1):
        x = str(n[r])
        y=x.strip()
        termdimer = y[-2:]
        if termdimer ==  'AA' :
            AA += 1
        elif termdimer ==  'AT':
            AG += 1
        elif termdimer ==  'AG':
            AT += 1
        elif termdimer ==  'AC':
            AC += 1
        elif termdimer ==  'TA':
            TA += 1
        elif termdimer ==  'TT':
            TT += 1
        elif termdimer ==  'TC':
            TC += 1
        elif termdimer ==  'TG':
            TG += 1
        elif termdimer ==  'CA':
            CA += 1
        elif termdimer ==  'CT':
            CT += 1
        elif termdimer ==  'CG':
            CG += 1
        elif termdimer ==  'CC':
            CC += 1
        elif termdimer ==  'GA':
            GA += 1
        elif termdimer ==  'GT' :
            GT += 1
        elif termdimer ==  'GC':
            GC += 1
        elif termdimer ==  'GG':
            GG += 1  
    total_dimers = AA + AT + AC + AG + TA +TT +TC+TG+GA+GT+GG+GC+CA+CT+CG+CC 
    finalout.write('Trial_' + str(i) + '\t' + str(AA) + '\t'+ str(AT)+ '\t'+ str(AC)+ '\t'+ str(AG) + '\t'+ str(TA) + '\t'+ str(TT) + '\t'+ str(TC) + '\t' + str(TG) + '\t'+str(GA) + '\t'+ str(GT) + '\t'+ str(GG) + '\t'+ str(GC)+ '\t'+ str(CA) + '\t'+ str(CT) + '\t'+ str(CG) + '\t'+ str(CC) + '\t'+ str(total) + '\n')                  
    print('Trial ' + str(i) + 'counting complete.')
finalout.close()
print('Fin')