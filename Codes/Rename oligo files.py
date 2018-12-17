import argparse

'''
Rename oligo name from primer files, if oligo name longer than 30, rename the oligo
to generate a new unique name
'''

def rename(infile, outfile):

    outfile = open(outfile, 'w')
    infhand = open(infile)

    for line in infhand:
        line = line.strip()
        group,well,num,gene,null,seq = line.split('\t')

        if gene != 'Blank':
            gene = 'TET.' + gene
            if len(gene) > 30:
                gene = gene[:15] + gene[-15:]

        new_line = '\t'.join([group,well,num,gene,null,seq])
        print(new_line, file=outfile)

    infhand.close()
    outfile.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='''
                    Rename oligo name from primer files, if oligo name longer than 30,
                    rename the oligo to generate a new unique name
                    ''')
    parser.add_argument('-i', '--input', metavar='', required=True, help='input oligo file')
    parser.add_argument('-o', '--output', metavar='', required=True, help='output oligo file')
    args = parser.parse_args()

    infile = args.input
    outfile = args.output
    rename(infile, outfile)
