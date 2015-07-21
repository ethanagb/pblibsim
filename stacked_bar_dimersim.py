import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
N = 16
in_data = pd.read_csv("/Users/Ethan/Desktop/CSHL/NickBioinformatics/dimerdistsimresultswprob.txt", sep = '\t')
df = in_data.set_index('Chr_Name')

sns.set_style("whitegrid")
sns.set_context({"figure.figsize": (24, 10)})


chr1_data = []
for x in df.loc['chr1']:
    chr1_data.append(x)
    
chr2_data = []
for x in df.loc['chr2']:
    chr2_data.append(x)
  
chr3_data = []
for x in df.loc['chr3']:
    chr3_data.append(x)
    
chr4_data = []
for x in df.loc['chr4']:
    chr4_data.append(x)
    
chr5_data = []
for x in df.loc['chr5']:
    chr5_data.append(x)
  
chr6_data = []
for x in df.loc['chr6']:
    chr6_data.append(x)

chr7_data = []
for x in df.loc['chr7']:
    chr7_data.append(x)
  
chr8_data = []
for x in df.loc['chr8']:
    chr8_data.append(x)
    
chr9_data = []
for x in df.loc['chr9']:
    chr9_data.append(x)
    
chr10_data = []
for x in df.loc['chr10']:
    chr10_data.append(x)
  
chr11_data = []
for x in df.loc['chr11']:
    chr11_data.append(x)

chr12_data = []
for x in df.loc['chr12']:
    chr12_data.append(x)
  
chr13_data = []
for x in df.loc['chr13']:
    chr13_data.append(x)
    
chr14_data = []
for x in df.loc['chr14']:
    chr14_data.append(x)
    
chr15_data = []
for x in df.loc['chr15']:
    chr15_data.append(x)
  
chr16_data = []
for x in df.loc['chr16']:
    chr16_data.append(x)    

chr17_data = []
for x in df.loc['chr17']:
    chr17_data.append(x)
  
chr18_data = []
for x in df.loc['chr18']:
    chr18_data.append(x)
    
chr19_data = []
for x in df.loc['chr19']:
    chr19_data.append(x)
    
chr20_data = []
for x in df.loc['chr20']:
    chr20_data.append(x)
  
chr21_data = []
for x in df.loc['chr21']:
    chr21_data.append(x) 

chr22_data = []
for x in df.loc['chr22']:
    chr22_data.append(x)
    
chrX_data = []
for x in df.loc['chrX']:
    chrX_data.append(x)
  
chrY_data = []
for x in df.loc['chrY']:
    chrY_data.append(x)  
       
ind = np.arange(N)    # the x locations for the groups
width = 0.3      # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, chr1_data,   width, color='r')
p2 = plt.bar(ind, chr2_data, width, color='y',bottom=chr1_data)
p3 = plt.bar(ind, chr3_data, width, color='g',bottom=chr2_data)
p4 = plt.bar(ind, chr4_data, width, color='b',bottom=chr3_data)
p5 = plt.bar(ind, chr5_data, width, color='y',bottom=chr4_data)
p6 = plt.bar(ind, chr6_data, width, color='y',bottom=chr5_data)
p7 = plt.bar(ind, chr7_data, width, color='y',bottom=chr6_data)
p8 = plt.bar(ind, chr8_data, width, color='y',bottom=chr7_data)
p9 = plt.bar(ind, chr9_data, width, color='y',bottom=chr8_data)
p10 = plt.bar(ind, chr10_data, width, color='y',bottom=chr9_data)
p11 = plt.bar(ind, chr11_data, width, color='y',bottom=chr10_data)
p12 = plt.bar(ind, chr12_data, width, color='y',bottom=chr11_data)
p13 = plt.bar(ind, chr13_data, width, color='y',bottom=chr12_data)
p14 = plt.bar(ind, chr14_data, width, color='y',bottom=chr13_data)
p15 = plt.bar(ind, chr15_data, width, color='y',bottom=chr14_data)
p16 = plt.bar(ind, chr16_data, width, color='y',bottom=chr15_data)
p17 = plt.bar(ind, chr17_data, width, color='y',bottom=chr16_data)
p18 = plt.bar(ind, chr18_data, width, color='y',bottom=chr17_data)
p19 = plt.bar(ind, chr19_data, width, color='y',bottom=chr18_data)
p20 = plt.bar(ind, chr20_data, width, color='y',bottom=chr19_data)
p21 = plt.bar(ind, chr21_data, width, color='y',bottom=chr20_data)
p22 = plt.bar(ind, chr21_data, width, color='y',bottom=chr21_data)
pX = plt.bar(ind, chrX_data, width, color='y',bottom=chr22_data)
pY = plt.bar(ind, chrY_data, width, color='y',bottom=chrX_data)


plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind+width/2., ('chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16','chr17','chr18','chr19','chr20','chr21','chr22','chrX','chrY')) 
plt.yticks(np.arange(0,.02,0.005))
plt.legend( (p1[0], p2[0]), ('Men', 'Women') )

plt.show()