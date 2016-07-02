import getopt, multiprocessing, glob
import pybedtools

threads = multiprocessing.cpu_count() #default

def convertToFasta(genomeFile):
	bedfileslist = glob.glob("*.bed.gz")
	for file in bedfileslist:
		outfileCount = 0
		nameRoot = file.split('.')[-3]
		a = pybedtools.BedTool(file)
		seqs = a.sequence(fi=genomeFile)
		b = a.save_seqs(str(nameRoot) + ".fa")
		assert open(b.fn).read() == open(a.fn).read()
		outfileCount += 1
		
if __name__ == "__main__":
    convertToFasta(genomeFile)