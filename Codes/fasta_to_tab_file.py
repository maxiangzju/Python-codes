import argparse
from Bio import SeqIO

'''
Convert fasta file to tab file
'''

def fasta_parse(infile, outfile):
    records = SeqIO.parse(infile, 'fasta')
    outfile = open(outfile, 'w')
    for r in records:
        gene = r.id
        length = len(r)
        sequence = r.seq
        print('{}\t{}\t{}'.format(gene, length, sequence), file=outfile)
    outfile.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert fasta file to tab file')
    parser.add_argument('-i','--input',type=str,metavar='', required=True,
                        help='input fasta infile')
    parser.add_argument('-o','--output',type=str,metavar='',required=True,
                        help='output tab infile')
    args = parser.parse_args()

    infile = args.input
    outfile = args.output

    fasta_parse(infile, outfile)
