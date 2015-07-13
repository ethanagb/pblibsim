from __future__ import division

#Pull in list of base file names. Could implement as a flag at some point.
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

from numpy import random
#e = dict(zip(keys,probs))
counter = 0
while counter < 1000:
    selected_chrom = random.choice(keys,p=probs)
    print selected_chrom
    
# calculate mean reads required to achieve coverage (will eventually be specified parameter). Read lengths will eventually need to be modified to fit distribution.
required_reads = []
keys = []
desired_cov = 8
mean = 4076
std = 3076
sigma = (log(1+(float(mean)/(float(std))**2)))**0.5
mu = log(mean)-0.5*sigma**2
read_length = random.lognormal(mu,sigma)
for key in d:
    req_reads = (desired_cov*d[key])/mean
    required_reads.append(req_reads)
    keys.append(key)
    #print read_length, req_reads
req_read_dict = dict(zip(keys,required_reads))

#build list of read lengths 
read_counts = {}
for key in req_read_dict:
    n=[]
    counter = 0
    while counter < req_read_dict[key]:
        n.append(int(round(random.lognormal(mu,sigma))))
        counter += 1
    read_counts[key] = n 

#Build dictionary with simulated reads by chr, creates bed file for validation of coverage
sim_reads_dict = {}
for key in read_counts:
    seq = ""
    simreads = []
    with open(str(key) + 'clean.fa', 'r') as infile:
        for x in infile:
            seq += str(x)
    infile.close()
    with open(str(key) + '_simreads.bed','w+') as bedout:
        for length in read_counts[key]:
            buf = length/2
            x = random.randint(buf,d[key]-buf)
            low = x-buf
            hi = x+buf
            bedout.write(str(low) + '\t' + str(hi) + '\n')
            simread = seq[low:hi+1]
            simreads.append(simread)
    bedout.close()
    seq = None
    sim_reads_dict[key] = simreads
read_counts = None

#write outfiles of simulatied reads.
for key in sim_reads_dict:
    with open(str(key)+'_simreads.fa','w+') as fastaout:
        for i in xrange(0,len(sim_reads_dict[key])+1):
            fastaout.write('>' + str(key)+'_'+str(i) + '\n' + str(sim_reads_dict[key][i]) + '\n')
    fastaout.close()
sim_reads_dict = None

with open('terminal_dimer_dists.td','w+') as finalout:
    for key in d:
        n=[]
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
        with open(str(key) + '_simreads.fa', 'r') as fastain:
            lines = fastain.readlines()
            for l in lines:
                if not l.startswith('>'):
                    n.append(l)
            for i in xrange(0,len(n)-1):
                x = str(n[i])
                termdimer = x[-2:]
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
        fastain.close()
        total = AA + AT + AC + AG + TA +TT +TC+TG+GA+GT+GG+GC+CA+CT+CG+CC 
        outfile.write(str(key) + '\t' + str(AA/total) + '\t'+ str(AT/total)+ '\t'+ str(AC/total)+ '\t'+ str(AG/total) + '\t'+ str(TA/total) + '\t'+ str(TT/total) + '\t'+ str(TC/total) + '\t' + str(TG/total) + '\t'+str(GA/total) + '\t'+ str(GT/total) + '\t'+ str(GG/total) + '\t'+ str(GC/total)+ '\t'+ str(CA/total) + '\t'+ str(CT/total) + '\t'+ str(CG/total) + '\t'+ str(CC/total) + '\t'+ str(total) + '\n')
outfile.close()