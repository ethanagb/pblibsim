#################################
######### SiLiCO v. 1.0 #########
### (c)2016 Ethan A. G. Baker ###
##### ethanagbaker@pitt.edu #####
#################################

from distutils.core import setup

setup(name='SiLiCO',
      version='1.0',
      description='A Simulator of Long Read Sequencing in PacBio and Oxford Nanopore',
      author='Ethan Alexander Garcia Baker',
      author_email='ethanagbaker@pitt.edu',
      url='https://ethanagbaker.github.io',
      license='GNU GPL'
      py_modules=['simulateReads','convertToFasta','generateChrDist','splitGenomeFasta','getRandomPosition','findChromosome','main'],
      requires=['numpy', 'natsort','pybedtools']
     )
