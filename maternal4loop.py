#maternal data file 
#Accession number: GSM5664742
#Code to split large file into smaller files, 5 chromosomes per file 

import pandas as pd 



maternal = pd.read_csv("GSM564427_Zebrafish_s1_zv7_final.gff", sep="\t", header = None )


out_file = open ("nineteen", 'w')

one = maternal.loc[maternal[0] == 'chr1']
one.to_csv("one", sep = "\t", header = None, index = False)

two = maternal.loc[maternal[0] == 'chr2']
two.to_csv("two", sep = "\t", header = None, index = False)

three = maternal.loc[maternal[0] == 'chr3']
three.to_csv("three", sep = "\t", header = None, index = False)

four = maternal.loc[maternal[0] == 'chr4']
four.to_csv("four", sep = "\t", header = None, index = False)

five = maternal.loc[maternal[0] == 'chr5']
five.to_csv("five", sep = "\t", header = None, index = False)

six = maternal.loc[maternal[0] == 'chr6']
six.to_csv("six", sep = "\t", header = None, index = False)

seven = maternal.loc[maternal[0] == 'chr7']
seven.to_csv("seven", sep = "\t", header = None, index = False)

eight = maternal.loc[maternal[0] == 'chr8']
eight.to_csv("eight", sep = "\t", header = None, index = False)

nine = maternal.loc[maternal[0] == 'chr9']
nine.to_csv("nine", sep = "\t", header = None, index = False)

ten = maternal.loc[maternal[0] == 'chr10']
ten.to_csv("ten", sep = "\t", header = None, index = False)

nineteen = maternal.loc[maternal[0] == 'chr19']
nineteen.to_csv("nineteen", sep = "\t", header = None, index = False)



 
out_file.close()
