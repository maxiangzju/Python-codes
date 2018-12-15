import Bio import SeqIO
import re

records = SeqIO.parse('dna.fasta', 'fasta')

for record in records:
    for strand, seq in (1, record.seq), (-1, record.seq.reverse_complement()):
        for frame in range(3):
            index = frame
            while index < len(record) - 6:
             # use regex to match the first reading frame
                match = re.match('(ATG(?:\S{3})*?T(?:AG|AA|GA))', str(seq[index:]))
                if match:
                    orf = match.group()
                    index += len(orf)
             # only keep orf longer than 1300 bp
                    if len(orf) > 1300:
                        pos = str(record.seq).find(orf) + 1 
                        print("{}...{} - length {}, strand {}, frame {}, pos {}, name {}".format\
                               (orf[:6], orf[-3:], len(orf), strand, frame, pos, record.id))
                else: index += 3
