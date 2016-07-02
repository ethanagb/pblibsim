
#SiLiCO: Simulator of Long Read Sequencing in PacBio and Oxford Nanopore 

---

###Installation
---

###Usage Instructions
---

```
python SiLiCO.py -i </path/to/genome> [-o </path/to/outfile.bed> -m <mean read length> -s <standard dev of read lengths> -c <coverage> -t <trials> -f]

[ FILE I/O ]

-i, --infile=<str>, REQ			Input genome fasta file. See README for formatting requirments**.
-o, --output=<str>, OPT			Output directory for results. Default = Current directory

[ DISTRIBUTION PARAMETERS ]

-m, --mean_read_length=<int>, OPT	Mean read length for in-silico read generation. Default = 10000 bp
-s, --standard_dev=<int>, OPT		Standard deviation of in-silico reads. Default = 2050
-c, --coverage=<int>, OPT		Desired genome coverage of in-silico sequencing. Default = 8
-t, --trials=<int>, OPT			Number of trials. Default = 1 

[ MODES ] 

-f, --fasta, OPT 			FASTA Mode. When present, converts bed files to Fasta sequences using the provided reference genome.

[ DOCUMENTATION ] 

-h, --help				Display this message.
--version				What version of SiLiCO are you using?
--contact				Report a bug or get more help.
--citation				View the citation for SiLiCO.
```
---
###Formatting Requirements
---

Input genome fasta should ideally be a chromosomal assembly with header lines in the style >chr1, >chr2.


###About SiLiCO

If you use SiLiCO in your research please cite it as follows: 

[Citation Placeholder]:

`Ethan Alexander Garcia Baker, Mendivil Ramos, O., McCombie, W.R., "SiLiCO:A Simulator for Long Read Sequencing in PacBio and Oxford Nanopore". Bioinformatics. [Date]`

SiLiCO is made freely available under the GNU GPL 3.0 license.
This software may be freely modified and (re)distributed, but you must make your modifications freely available and cite SiLiCO.
View LICENSE.txt or [http://choosealicense.com/licenses/gpl-3.0/](http://choosealicense.com/licenses/gpl-3.0/) for more information.

(c) 2016
