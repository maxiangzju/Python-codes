newfile = open('newfile.tab', 'w')
less2 = open('lessthan2.tab', 'w')

fhand = open('oligo.tab')
for line in fhand:
    line = line.strip()
    pool,well,num,gene,null,seq = line.split('\t')
    
    if gene != 'Blank':
        gene = 'TET.' + gene
        if len(gene) > 30:
            gene = gene[:15] + gene[-15:]
        
    new_line = '\t'.join([pool,well,num,gene,null,seq])
    print(new_line, file=newfile)
    
    if seq.count('N') < 2 and gene != 'Blank':
        print(new_line, file=less2)

newfile.close()
less2.close()
