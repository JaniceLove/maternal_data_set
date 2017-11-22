#script to convert CHOP CHOP results table to proper csv functional file
#Date: Nov. 22, 2017
#Author: Janice Love

cat $1 | sed 'y/" "/","/' > $2≈
