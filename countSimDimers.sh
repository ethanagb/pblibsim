#!/bin/sh
#$ -S /bin/sh
#$ -cwd
#$ -v LD_LIBRARY_PATH
#$ -l m_mem_free=10G

/opt/hpc/pkg/python-2.7/bin/python count_sim_dimers.py
