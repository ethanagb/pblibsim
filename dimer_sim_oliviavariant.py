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
 
"""while counter < 1000:
    selected_chrom = random.choice(keys,p=probs)
    print selected_chrom"""
    
desired_cov = 8
mean = 10000
std = 2500
sigma = (np.log(1+(float(mean)/(float(std))**2)))**0.5
mu = np.log(mean)-0.5*sigma**2
req_reads = (desired_cov*total)/mean

counter = 0 
while counter < req_reads:
      selected_chrom = None
      selected_chrom = np.random.choice(keys,p=probs) 
      with open
for chrom in names:
    #print(str(chrom))
    r = 0
   """ with open('terminaldimerdist_' + str(chrom) + '.td','w+') as finalout:
        finalout.write('Chr_Name' + '\t' + 'AA' + '\t'+ 'AT'+ '\t'+ 'AC'+ '\t'+ 'AG' + '\t'+ 'TA'+ '\t'+ 'TT' + '\t'+ 'TC' + '\t' + 'TG' + '\t'+'GA' + '\t'+ 'GT' + '\t'+ 'GG' + '\t'+ 'GC'+ '\t'+ 'CA' + '\t'+ 'CT' + '\t'+ 'CG' + '\t'+ 'CC' + '\t'+ 'Total_dimers' + '\n')
        while r < 5000:
            desired_cov = 8
            mean = 4076
            std = 3076
            sigma = (np.log(1+(float(mean)/(float(std))**2)))**0.5
            mu = np.log(mean)-0.5*sigma**2
            req_reads = (desired_cov*d[chrom])/mean""" #added this part to calc req_reads for whole genome
            n=[]
            counter = 
            while counter < req_reads:
                n.append(int(round(np.random.lognormal(mu,sigma))))
                counter += 1
            seq = ""
            simreads = []
            with open(str(chrom) + '.clean.fa', 'r') as infile:
                for x in infile:
                    seq += str(x)
            infile.close()
            with open(str(chrom) + '_simreads.bed','w+') as bedout:
                for length in n:   #n has all of the read lengths, now get the reads using those lengths. 
                    buf = length/2
                    x = np.random.randint(buf,d[chrom]-buf)
                    low = int(x-buf)
                    hi = int(x+buf)
                    bedout.write(str(low) + '\t' + str(hi) + '\n')
                    simread = seq[low:hi+1]
                    simreads.append(simread)
            bedout.close()
            seq = None
            read_counts = None
            with open(str(chrom)+'_simreads.fa','w+') as fastaout:
                for i in xrange(0,len(simreads)):
                    fastaout.write('>' + str(chrom)+'_'+str(i) + '\n' + str(simreads[i]) + '\n')
            fastaout.close()
            sim_reads_dict = None
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
            with open(str(chrom) + '_simreads.fa', 'r') as fastain:
                lines = fastain.readlines()
                for l in lines:
                    if not l.startswith('>'):
                        n.append(l)
                for i in xrange(0,len(n)-1):
                    x = str(n[i])
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
                fastain.close()
                total = AA + AT + AC + AG + TA +TT +TC+TG+GA+GT+GG+GC+CA+CT+CG+CC 
            finalout.write(str(chrom) + '\t' + str(AA/total) + '\t'+ str(AT/total)+ '\t'+ str(AC/total)+ '\t'+ str(AG/total) + '\t'+ str(TA/total) + '\t'+ str(TT/total) + '\t'+ str(TC/total) + '\t' + str(TG/total) + '\t'+str(GA/total) + '\t'+ str(GT/total) + '\t'+ str(GG/total) + '\t'+ str(GC/total)+ '\t'+ str(CA/total) + '\t'+ str(CT/total) + '\t'+ str(CG/total) + '\t'+ str(CC/total) + '\t'+ str(total) + '\n')
            r += 1
    finalout.close()