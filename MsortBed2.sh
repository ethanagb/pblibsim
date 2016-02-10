#!/bin/sh
#$ -S /bin/sh
#$ -cwd
#$ -v LD_LIBRARY_PATH
#$ -l m_mem_free=10G
cat names2| while read  x
do
	for chr in `cut -f 1 $x.dimer.bed | sort | uniq`
	do 
		grep -w $chr $x.dimer.bed > split_results/$x.$chr.dimer.bed
	done
done
