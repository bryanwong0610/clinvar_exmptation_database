#!/bin/bash

# loading VCF file & get file name
file_name=$(basename $1 .vcf.gz) 
echo ${file_name}
echo "unzip the VCF file"
gunzip  $1
echo "preparing to generate annovar db"
docker run -v /mnt:/mnt -it -w=$PWD harbor.bio-it.cn:5000/library/annovar:latest convert2annovar.pl -format vcf4 --includeinfo ${file_name}.vcf -outfile ${file_name}.avinput
docker run -it -v /mnt:/mnt -w=$PWD  anaconda3:biostats1.1.1  python generate.py  -i ${file_name}
docker run -it -v /mnt:/mnt -w=$PWD  anaconda3:biostats1.1.1  python exmpt_clinvar_generate.py -i ${file_name}
final_name=$(basename *_clinvar_exmpt.txt .txt)
perl annovar_idx.pl 1000 *_clinvar_exmpt.txt > ${final_name}.idx
rm  ${file_name}.avinput 
