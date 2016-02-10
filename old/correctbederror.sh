#!/bin/sh
#$ -S /bin/sh
#$ -cwd
#$ -v LD_LIBRARY_PATH
#$ -l m_mem_free=10G

cat bednames|while read x
do
	gunzip $x.bed.gz
	sed 's/chr?/chr22/g' > $x.corrected.bed
	gzip $x.corrected.bed
	rm -f $x.bed
done