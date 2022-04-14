# -- coding: utf-8 --
# @Time : 2022/4/11 21:03
# @Author : codeking
# @File : 氨基酸.py
if __name__ == '__main__':
    aa_codes = {
        'ALA': 'A', 'CYS': 'C', 'ASP': 'D', 'GLU': 'E',
        'PHE': 'F', 'GLY': 'G', 'HIS': 'H', 'LYS': 'K',
        'ILE': 'I', 'LEU': 'L', 'MET': 'M', 'ASN': 'N',
        'PRO': 'P', 'GLN': 'Q', 'ARG': 'R', 'SER': 'S',
        'THR': 'T', 'VAL': 'V', 'TYR': 'Y', 'TRP': 'W'}
    seq = ''
    for line in open("1tld.pdb"):
        if line[0:6] == "SEQRES":
            columns = line.split()
            for resname in columns[4:]:
                seq = seq + aa_codes[resname]
    i = 0
    print(">1TLD")
    while i < len(seq):
        print(seq[i:i + 64])
        i = i + 64
