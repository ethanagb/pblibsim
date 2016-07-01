import sys, os
import glob
from natsort import natsorted

def splitGenomeFasta(genome):
	origFile = False
	os.mkdir("SiLiCO_Scratch")
	for l in open(str(genome),'r'):
		if l.startswith(">"):
			if origFile:
				f.close()
			name= l.rstrip().partition(">")[2]
			name = "%s.fa" % name
			f=open("SiLiCO_Scratch/" + str(name),"w+")
			origFile=True
			f.write(l)
		elif origFile:
			f.write(l)

	#Make a name list
	fastaNames = natsorted(glob.glob("SiLiCO_Scratch/chr*.fa"))
	fastaNames = [str(x.split('.')[-2]) for x in fastaNames]
	return fastaNames
if __name__ == "__main__":    
    splitGenomeFasta(genome)