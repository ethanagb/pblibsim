def getFastas(argv):
	import pybedtools
	threads = 1 #default
	try:
        opts, args = getopt.getopt(argv,hi:o:t:,["infile=","outfile=","threads="])
    except getopt.GetoptError:
        print("Usage: python getFastas.py --infile </path/to/infile.txt> --outfile </path/to/outfile.bed> -t <number of threads>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("Usage: python getFastas.py --infile </path/to/infile.txt> --outfile </path/to/outfile (name root)> -t <number of threads>")
        elif opt ==("-o","--outfile"):
            outfileName = arg
        elif opt ==("-i", "--infile"):
            bedNameFile = arg
        elif opt ==("-t", "--threads"):
            threads = arg
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