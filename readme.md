# Clinvar exmptation database generate and update
## Clinvar data 
  From `ncbi clinvar` download the [VCF](https://ftp.ncbi.nlm.nih.gov/pub/clinvar/), run the clinvar.update.sh to generate or update the clinvar database for annovar using.
##  How to download and check the data
  ### hg19 
 
  ***wget https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh37/clinvar.[date].vcf.gz***
 
  ***wget https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh37/clinvar.[date].vcf.gz.md5***
 
  ### hg38
 
  ***wget https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/clinvar.[date].vcf.gz***

  ***wget https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/clinvar.[date].vcf.gz.md5***
  
  ### md5 check 
  openssl md5 clinvar.vcf.gz get the md5 value
  
  ***Judge `gz.md5 == openssl md5 *.gz`***
## rule of exmptation 
In clinvar.vcf, if it already recorded that 'pathogenic' in the description, the keep it, and add it into exmpt database.

the database will be like `1` in the colums `clinvar_exmpt`. 
## how to use this script
 this script do not write the jugde function to know the md5 value is equal to the raw md5 value 
 ***sh clinvar.update.sh $1***
 $1 is the clinvar.vcf.gz file 
finally will get the `hg19/hg38`_clinvar_exmpt.txt which can be using in annovar
