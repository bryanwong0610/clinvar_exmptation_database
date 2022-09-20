import os
import re
from optparse import OptionParser
para=OptionParser()
## input the file 
def argument_get():
    parser=argparse.ArgumentParser(prog='Clinvar database exmptation',description='A python script for generate clinvar database')
    parser.add_argument('--Input','-i',type=str,help='raw clinvar data')
    args,_ = parser.parse_known_args()
    args = vars(args)
    print(args) #test
    return args
args= argument_get()
file_name= './'+args['Input']+'.avinput'

def clinvaravinput2annovardb(avinput_file, fields):
    annovar_db = '#Chr\tStart\tEnd\tRef\tAlt\tCLNALLELEID\tCLNDN\tCLNDISDB\tCLNREVSTAT\tCLNSIG\tCLNHGVS\tGENEINFO\n'
    with open(avinput_file) as input_file:
        content = input_file.readlines()
    for current_line in content:
        # get INFO field and keep interesting ones
        splitted_line = re.split(r'\t', current_line)
        # fill in the beginning chr start end ref alt
        i = 0
        # for field in splitted_line:
        if len(splitted_line) < 13:
            continue
        while i < 5:
            annovar_db += '{}\t'.format(splitted_line[i])
            i += 1
        # get info field, split and fill in annovar_db
        infos = re.split(r';', splitted_line[12])
        # to keep the order, we build a small dict
        info_dict = {}
        # initialize all required keys
        for field in fields:
            if field != 'ALLELEID':
                info_dict[field] = '.'
        for info in infos:
            info_list = re.split(r'=', info)
            if info_list[0] == 'ALLELEID':
                info_dict['CLNALLELEID'] = info_list[1]
            elif info_list[0] in fields:
                info_dict[info_list[0]] = info_list[1]
        annovar_db += '{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\n'.format(
            info_dict['CLNALLELEID'],
            info_dict['CLNDN'],
            info_dict['CLNDISDB'],
            info_dict['CLNREVSTAT'],
            info_dict['CLNSIG'],
            info_dict['CLNHGVS'],
            info_dict['GENEINFO']
        )
    # replace ',' with '\x2c in annovar fields'
    annovar_db_final = re.sub(r',', r'\\x2c', annovar_db)
    annovar_db_file = open('{}.txt'.format(os.path.splitext(avinput_file)[0]), "w")
    annovar_db_file.write(annovar_db_final)
    annovar_db_file.close()
    return '{}.txt'.format(os.path.splitext(avinput_file)[0])


if __name__ == '__main__':
    # for testing prupose
    clinvaravinput2annovardb(
        file_name,
        ['ALLELEID', 'CLNDN', 'CLNDISDB', 'CLNREVSTAT', 'CLNSIG','CLNHGVS','GENEINFO']
    )
