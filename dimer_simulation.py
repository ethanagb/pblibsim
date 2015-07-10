from Bio import SeqIO
from numpy import random
import csv


infile = open("completegenome.fa", 'r+')
outfile = open("dimersinlibsimulation.txt","a+")
for record in SeqIO.parse(infile, 'fasta'):
        nts_only = ""
        nts_only += record.seq
        b = str(nts_only.upper())
        wholefasta = str(b.replace('N',''))
infile.close()
#x = random.randint(0,intnts_only)),size=20000)
counter = 0
counter2 =0
samples2 = []
while counter < 10000:
    x = random.randint(0,len(nts_only)-20000)
    upperbound = x + 20000
    sample = wholefasta[x:upperbound+1]
    samples2.append(sample)
    samples = [d for d in samples2 if d]
    counter += 1
print samples
for s in samples:
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
    counter2 += 1
    r = str(s)
    for i in xrange(0, len(r), 2):
        q= r[i:i+2]
        w= r[i+1:i+3]
        if q == 'AA' or w == 'AA':
                AA += 1
        if q == 'AT' or w == 'AT':
            AG += 1
        if q == 'AG' or w == 'AG':
            AT += 1
        if q == 'AC' or w == 'AC':
            AC += 1
        if q == 'TA' or w == 'TA':
            TA += 1
        if q == 'TT' or w == 'TT':
            TT += 1
        if q == 'TC' or w == 'TC':
            TC += 1
        if q == 'TG' or w == 'TG':
            TG += 1
        if q == 'CA' or w == 'CA':
            CA += 1
        if q == 'CT' or w == 'CT':
            CT += 1
        if q == 'CG' or w == 'CG':
            CG += 1
        if q == 'CC' or w == 'CC':
            CC += 1
        if q == 'GA' or w == 'GA':
            GA += 1
        if q == 'GT' or w == 'GT':
            GT += 1
        if q == 'GC' or w == 'GC':
            GC += 1
        if q == 'GG' or w == 'GG':
            GG += 1            
    total = AA + AT + AC + AG + TA +TT +TC+TG+GA+GT+GG+GC+CA+CT+CG+CC 
    #headers = ['AA','AT','AC','AG','TA','TT','TC','TG','GA','GT','GG','GC','CA','CT','CG','CC']
    #writer = csv.DictWriter(outfile, headers, delimiter='\t')
    #writer.writeheader()
    outfile.write(str(counter2) + '\t' + str(AA) + '\t'+ str(AT)+ '\t'+ str(AC)+ '\t'+ str(AG) + '\t'+ str(TA) + '\t'+ str(TT) + '\t'+ str(TC) + '\t' + str(TG) + '\t'+str(GA) + '\t'+ str(GT) + '\t'+ str(GG) + '\t'+ str(GC)+ '\t'+ str(CA) + '\t'+ str(CT) + '\t'+ str(CG) + '\t'+ str(CC) + '\t'+ str(total) + '\n')
    