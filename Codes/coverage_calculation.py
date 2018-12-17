import argparse

'''
Caculate coverage rate for each gene
'''

def  coverage_calculate(infile, outfile):
    infhand = open(infile)
    outfhand = open(outfile, 'w')

    infhand.readline()
    for line in infhand:
        line = line.strip()
        gene, chr, size, coveredsize = line.split()
        size, coveredsize = float(size), float(coveredsize)
        covered_rate = round(coveredsize/size, 2)
        print('{}\t{}\t{}\t{}\t{}'.format(gene, chr, size, coveredsize, covered_rate), file=outfhand)

    infhand.close()
    outfhand.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Caculate coverage rate for whole pane and each gene')
    parser.add_argument('-i', '--input', metavar='', required=True, help='input coverage file')
    parser.add_argument('-o', '--output', metavar='', required=True, help='output coverage rate file')
    args = parser.parse_args()

    infile = args.input
    outfile = args.output

    coverage_calculate(infile, outfile)
