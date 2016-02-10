from Bio import SeqIO

############
pwd = "/seq/seq/ethan/Maize/Simulation/" #set the present working dir
############

with open(str(pwd) + "namelist.txt") as filenamesFile:
    filenames = filenamesFile.readlines()
    nameList =[str(e.strip()) for e in filenames]
filenamesFile.close()

for name in nameList:
    infile = open(str(pwd) + str(name) + ".fa", "rU")
    chroms = []
    for record in SeqIO.parse(infile, "fasta"):
        x = record.id
        chrom = x.split(":")[0] #Set the symbol + field # for text to sort file by
        chroms.append(chrom)
        with open(str(pwd) + str(name) + "_" + str(chrom) + ".fa","a+") as outfile: #this appends, should add a clean up step somehow first.
            SeqIO.write(record, outfile, "fasta")
            outfile.close
    infile.close()            
