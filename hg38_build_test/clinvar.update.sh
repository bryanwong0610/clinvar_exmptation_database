#!/bin/bash

# loading VCF file & get file name
file_name=$(basename $1 .vcf)
echo ${file_name}
echo "preparing to generate annovar db"
docker run -v /mnt:/mnt -it -w=$PWD harbor.bio-it.cn:5000/library/annovar:latest convert2annovar.pl -format vcf4 --includeinfo $1 -outfile ${file_name}.avinput
docker run -it -v /mnt:/mnt -w=$PWD  anaconda3:biostats1.1.1  python generate.py
docker run -it -v /mnt:/mnt -w=$PWD  anaconda3:biostats1.1.1  python exmpt_clinvar_generate.py
rm  ${file_name}.avinput 
