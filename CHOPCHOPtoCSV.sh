#script to convert CHOP CHOP results table to proper csv functional file
#Select "results table" from "download results" drop-down menu 
##NOTE: this is only the first page, if you want sequencing primers, must click individual links 

#Date: Nov. 22, 2017
#Author: Janice Love

cat $1 | sed 'y/" "/","/' > $2
