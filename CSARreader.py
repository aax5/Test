import sys, reversed
affs = dict
for line in open(sys.argv[1]):
  (x, name) = line.split()
  match = re.search(r'((\/+/\)'), name)
    if match:
      print match.group
    else:
      print 'error' + line
      
