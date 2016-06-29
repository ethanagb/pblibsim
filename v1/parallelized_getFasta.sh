#!/bin/sh
#$ -S /bin/sh
#$ -cwd
#$ -v LD_LIBRARY_PATH
#$ -l m_mem_free=10G
#$ -o /seq/seq/ethan/Maize/Simulation/split_results/logs/
#$ -e /seq/seq/ethan/Maize/Simulation/split_results/logs/

samplefile="/seq/seq/ethan/Maize/Simulation/split_results/namelist.txt"
sample=$(head -n ${SGE_TASK_ID} ${samplefile} | tail -1 | awk '{print $2}')

/opt/hpc/bin/bedtools getfasta -fi ../reads.formatted -bed ${sample}.dimer.bed -fo ${sample}.fa