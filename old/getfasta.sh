#!/bin/sh
#$ -S /bin/sh
#$ -cwd
#$ -v LD_LIBRARY_PATH
#$ -l m_mem_free=10G

cat bednames|while read x
do
	gunzip $x.bed.gz
	/opt/hpc/bin/bedtools getfasta -fi reads.formatted -bed $x.bed -fo $x.fa
	gzip $x.fa
	gzip $x.bed
done