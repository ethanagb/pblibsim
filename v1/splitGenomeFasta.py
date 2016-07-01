import sys, os
import glob
from natsort import natsorted

def splitGenomeFasta(genome):
	origFile = False
	#Make the Silico working directory
	os.mkdir("SiLiCO_Scratch")

	#Read the genome file, set the header lines as names
	for l in open(str(genome),'r'):
		if l.startswith(">"):
			if origFile:
				f.close()
			name= l.rstrip().partition(">")[2]
			name = "%s.fa" % name
			#write non-header (sequence) lines following the header 
			f=open("SiLiCO_Scratch/" + str(name),"w+")
			origFile=True
			f.write(l)
		elif origFile:
			f.write(l)

	#Make a name list array and return it for use in subsequent steps.
	fastaNames = natsorted(glob.glob("SiLiCO_Scratch/chr*.fa")) 
	fastaNames = [str(x.split('.')[-2]) for x in fastaNames] #Only add the chrN portion of the name
	return fastaNames

if __name__ == "__main__":    
    splitGenomeFasta(genome)