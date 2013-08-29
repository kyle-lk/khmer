#! /usr/bin/env python
import sys
from screed.fasta import fasta_iter
import re

outfp = open(sys.argv[2], 'w')

for n, record in enumerate(fasta_iter(open(sys.argv[1]))):
    if n % 100000 == 0:
        print >>sys.stderr, '...', n

    if 'N' in record['sequence']:
        splitseq = re.split('N+', record.sequence)
        for i in range(len(splitseq)):
            print >>outfp, '>%s.%d\n%s' % (record.name, i + 1, splitseq[i])

    else:
        print >>outfp, '>%s\n%s' % (record['name'], record['sequence'])
