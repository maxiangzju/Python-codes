import argparse
from Bio import SeqIO

'''
Extract insert sequence from bed files and reference fasta files
'''

def fasta_parse(fasta_file):
    # parse fasta file
    records = SeqIO.parse(fasta_file, 'fasta')
    return records

def coordinates_extraction(bed_file):
    # extract coordinates from bed files
    fhand = open(bed_file)
    coordinates = {}

    for line in fhand:
        line = line.strip()
        pieces = line.split()
        gene, start, end = pieces[0], pieces[1], pieces[2]
        coordinates[gene] = (start, end)
    fhand.close()
    return coordinates

def main(fasta_file, bed_file, outfile):
    # map coordinates to gene sequence to extract insert and output
    records = fasta_parse(fasta_file)
    coordinates = coordinates_extraction(bed_file)
    outfile = open(outfile, 'w')

    for r in records:
        start, end = int(coordinates[r.id][0]), int(coordinates[r.id][1])
        insert = r.seq[start : end]
        print('{}\t{}'.format(r.id, insert), file=outfile)

    outfile.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract insert sequence from bed files\
                                    and reference fasta files')
    parser.add_argument('-if', '--inputfasta', metavar='', required=True,
                        help='input fasta reference file')
    parser.add_argument('-ib', '--inputbed', metavar='', required=True,
                        help='input bed coordinates file')
    parser.add_argument('-o', '--outfile', metavar='', required=True,
                        help='output tab sequence file')
    args = parser.parse_args()

    fasta_file = args.inputfasta
    bed_file = args.inputbed
    outfile = args.outfile

    main(fasta_file, bed_file, outfile)
