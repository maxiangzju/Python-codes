import argparse
from Bio import SeqIO

'''
For a given fasta file, find the repeats of given number 'n' of bases with the specified
occurrence number 'frequence' 
'''

def find_repeats(infile, outfile, n, frequence):
    try:
        records = list(SeqIO.parse(infile, 'fasta'))
    except:
        print('File not found!')
        return

    outfile = open(outfile, 'w')

    list_query = list()
    for r in records:
        for i in range(len(r)):
            if len(r.seq[i: i+n]) < n: continue
            list_query.append(str(r.seq[i: i+n]))
    query = set(list_query)

    count = dict()
    for q in query:
        num = 0
        for r in records:
            num += r.seq.count_overlap(q)
        count[q] = num
    print(sorted([(v,k) for k,v in count.items() if v > frequence], reverse = True), file=outfile)
    outfile.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Find repeats in given fasta files')
    parser.add_argument('-i', '--input', metavar='', required=True, help='input fasta file')
    parser.add_argument('-o', '--output', metavar='', required=True, help='output sequence with occurrence file')
    parser.add_argument('-f', '--frequence', type=int, metavar='', required=True, help='repeat sequence frequence')
    parser.add_argument('-n', '--numberbase', type=int, metavar='', required=True, help='number of bases of repeat sequences')
    args = parser.parse_args()

    infile = args.input
    outfile = args.output
    frequence = args.frequence
    n = args.numberbase

    find_repeats(infile, outfile, n, frequence)
