#
# Count types and tokens in a .csv file (argument 1) and
# check that all the rows have the same number of cells as the header
#
# e.g.
# python evaluate.py 4solr.pahma.public.csv checked.csv > counts.csv
# head -4 counts.csv | expand -20
#
# id                  748756              748756
# objtype_s           8                   736597
# objcount_s          911                 737182
# objcountnote_s      1550                58810
#

import sys, csv, collections
# for python 2.6 :-(
from Counter import Counter


from unicode_hack import UnicodeReader, UnicodeWriter

delim = "\t"

types = {}
errors = 0

# keep these lines around for when we start to use python3
# with open(sys.argv[2], 'w', encoding='utf-8') as f2:
#    writer = csv.writer(f2, delimiter=delim, quoting=csv.QUOTE_NONE, quotechar=chr(255))
#    with open(sys.argv[1], 'r', encoding='utf-8') as f1:
#        reader = csv.reader(f1, delimiter=delim, quoting=csv.QUOTE_NONE, quotechar=chr(255))


with open(sys.argv[2], 'w') as f2:
    writer = UnicodeWriter(f2, delimiter=delim, quoting=csv.QUOTE_NONE, quotechar=chr(255))
    with open(sys.argv[1], 'r') as f1:
        reader = UnicodeReader(f1, delimiter=delim, quoting=csv.QUOTE_NONE, quotechar=chr(255))
        for lineno, row in enumerate(reader):
            if lineno == 0:
                header = row
                writer.writerow(row)
                for col in header:
                    types[col] = Counter()
                column_count = len(header)
            else:
                if len(row) != column_count:
                    print "%s%s%s" % ('error', delim, delim.join(row))
                    errors += 1
                    continue
                for i, cell in enumerate(row):
                    if cell != '':
                        types[header[i]][cell] += 1
                writer.writerow(row)

if errors > 0:
    print
    print "%s errors seen (i.e. data row and header row w different counts.)" % errors
    print

print "%s\t%s\t%s" % ('column', 'types', 'tokens')
for key in header:
    print "%s\t%s\t%s" % (key, len(types[key]), sum(types[key].values()))