import sys, re

if len(sys.argv) != 3:
    print "Need train file and affinities dictionary"
    sys.exit(1)

f = open(sys.argv[1])

affs = dict()
for line in open(sys.argv[2]):
  #get dictionary, sets all proteins in second file in dict
    (pdb,_,a) = line.split()
    affs[pdb] = float(a)

for line in f:
    vals = line.split()
    m = re.search(r'(\w+)_rec', vals[1])
    if m:
        pdb = m.group(1)
        a = affs[pdb]
        if a > 2 and pdb in affs:
          print line.rstrip()
    else:
        sys.stderr.write("Problem with: %s\n" % line)
