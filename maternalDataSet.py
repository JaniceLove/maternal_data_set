#maternal data file 
#Accession number: GSM564427
#Code to split large file into smaller files, each chromosome is its own file

import pandas as pd 



maternal = pd.read_csv("GSM564427_Zebrafish_s1_zv7_final.gff", sep="\t", header = None )

#change nineteen to chromosome number you want 
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

eleven = maternal.loc[maternal[0] == 'chr11']
eleven.to_csv("eleven", sep = "\t", header = None, index = False)

twelve = maternal.loc[maternal[0] == 'chr12']
twelve.to_csv("twelve", sep = "\t", header = None, index = False)

thirteen = maternal.loc[maternal[0] == 'chr13']
thirteen.to_csv("thirteen", sep = "\t", header = None, index = False)

fourteen = maternal.loc[maternal[0] == 'chr14']
fourteen.to_csv("fourteen", sep = "\t", header = None, index = False)

fifteen = maternal.loc[maternal[0] == 'chr15']
fifteen.to_csv("fifteen", sep = "\t", header = None, index = False)

sixteen = maternal.loc[maternal[0] == 'chr16']
sixteen.to_csv("sixteen", sep = "\t", header = None, index = False)

seventeen = maternal.loc[maternal[0] == 'chr17']
seventeen.to_csv("seventeen", sep = "\t", header = None, index = False)

eighteen = maternal.loc[maternal[0] == 'chr18']
eightteen.to_csv("eightteen", sep = "\t", header = None, index = False)

nineteen = maternal.loc[maternal[0] == 'chr19']
nineteen.to_csv("nineteen", sep = "\t", header = None, index = False)

twenty = maternal.loc[maternal[0] == 'chr20']
twenty.to_csv("twenty", sep = "\t", header = None, index = False)

twenty1 = maternal.loc[maternal[0] == 'chr21']
twenty1.to_csv("twenty1", sep = "\t", header = None, index = False)

twenty2 = maternal.loc[maternal[0] == 'chr22']
twenty2.to_csv("twenty2", sep = "\t", header = None, index = False)

twenty3 = maternal.loc[maternal[0] == 'chr23']
twenty3.to_csv("twenty3", sep = "\t", header = None, index = False)

twenty4 = maternal.loc[maternal[0] == 'chr24']
twenty4.to_csv("twenty4", sep = "\t", header = None, index = False)

twenty5 = maternal.loc[maternal[0] == 'chr25']
twenty5.to_csv("twenty5", sep = "\t", header = None, index = False)
 
out_file.close()
