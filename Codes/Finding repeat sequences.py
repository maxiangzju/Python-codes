import sys
import getopt
from Bio import SeqIO

opt, arg = getopt.getopt(sys.argv[1:], 'i:o:')
opts = dict()
for option, value in opt:
    opts[option] = value

if '-i' in opts.keys():
    inname = opts['-i']
if '-o' in opts.keys():
    outname = opts['-o']

try:
    records = list(SeqIO.parse(inname, 'fasta'))
except:
    print('File not found!')

outfile = open(outname, 'w')

list_query = list()
for r in records:
    for i in range(len(r)):
        if len(r.seq[i: i+7]) < 7: continue
        list_query.append(str(r.seq[i: i+7]))
query = set(list_query)

count = dict()
for q in query:
    num = 0
    for r in records:
        num += r.seq.count_overlap(q) 
    count[q] = num
print(sorted([(v,k) for k,v in count.items() if v > 30], reverse = True), file=outfile)
 
