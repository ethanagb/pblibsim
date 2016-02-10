from __future__ import division

with open('bednames','r') as infile:
    lines = infile.readlines()
    filenames =[str(e.strip()) for e in lines]
infile.close()

with open('simulationresults.td','w+') as finalout:
    finalout.write('Chr_Name' + '\t' + 'AA' + '\t'+ 'AT'+ '\t'+ 'AC'+ '\t'+ 'AG' + '\t'+ 'TA'+ '\t'+ 'TT' + '\t'+ 'TC' + '\t' + 'TG' + '\t'+'GA' + '\t'+ 'GT' + '\t'+ 'GG' + '\t'+ 'GC'+ '\t'+ 'CA' + '\t'+ 'CT' + '\t'+ 'CG' + '\t'+ 'CC' + '\t'+ 'Total_dimers' + '\n')
    for f in filenames:
        #g = f.split('_')[3]
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
        with open(str(f) + '.fa.gz','r') as infile:
            lines = infile.readlines()
            for line in lines:
                if line.startswith('>'):
                    pass
                else:
                    d = str(line.strip())
                    if d ==  'AA' :
                        AA += 1
                    elif d ==  'AT':
                        AG += 1
                    elif d ==  'AG':
                        AT += 1
                    elif d ==  'AC':
                        AC += 1
                    elif d ==  'TA':
                        TA += 1
                    elif d ==  'TT':
                        TT += 1
                    elif d ==  'TC':
                        TC += 1
                    elif d ==  'TG':
                        TG += 1
                    elif d ==  'CA':
                        CA += 1
                    elif d ==  'CT':
                        CT += 1
                    elif d ==  'CG':
                        CG += 1
                    elif d ==  'CC':
                        CC += 1
                    elif d ==  'GA':
                        GA += 1
                    elif d ==  'GT' :
                        GT += 1
                    elif d ==  'GC':
                        GC += 1
                    elif d ==  'GG':
                        GG += 1 
        infile.close()
        total = AA + AT + AC + AG + TA +TT +TC+TG+GA+GT+GG+GC+CA+CT+CG+CC 
        finalout.write(str(f) + '\t' + str(AA/total) + '\t'+ str(AT/total)+ '\t'+ str(AC/total)+ '\t'+ str(AG/total) + '\t'+ str(TA/total) + '\t'+ str(TT/total) + '\t'+ str(TC/total) + '\t' + str(TG/total) + '\t'+str(GA/total) + '\t'+ str(GT/total) + '\t'+ str(GG/total) + '\t'+ str(GC/total)+ '\t'+ str(CA/total) + '\t'+ str(CT/total) + '\t'+ str(CG/total) + '\t'+ str(CC/total) + '\t'+ str(total) + '\n')
finalout.close()

