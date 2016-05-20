import getopt, multiprocessing
import pybedtools

threads = multiprocessing.cpu_count() #default
bedNameFile = 'bedNames.txt'
def getFastas(argv):
	with open(bedNameFile, 'r') as infile:
		bedfileslist = infile.readlines().strip()
	infile.close()
	for file in bedfileslist:
		outfileCount = 1
		a = pybedtools.BedTool(bedfile)
		seqs = a.sequence(fi=genomeFile)
		b = a.save_seqs(outfileName + "_" + str(outfileCount) + ".fa")
		assert open(b.fn).read() == open(a.fn).read()
		outfileCount += 1
		
if __name__ == "__main__":
    getFastas(sys.argv[1:])