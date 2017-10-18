#maternal data file 
#Accession number: GSM5664742
#Code to split large file into smaller files, 5 chromosomes per file 

import pandas as pd 
import re 


maternal = pd.read_csv("GSM564427_Zebrafish_s1_zv7_final.gff", sep="\t", header = None )

out_file = open ("maternal_chr1_5", 'w')
out_file.close()

out_file = open ("nineteen", 'w')
#one = maternal.loc[maternal[0] == 'chr1']
nineteen = maternal.loc[maternal[0] == 'chr19']
nineteen.to_csv("nineteen", sep = "\t", header = None, index = False) 
out_file.close()
#