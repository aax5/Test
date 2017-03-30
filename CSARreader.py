import sys, re
affs = dict
for line in open(sys.argv[1]):
  vals = line.split()
  match = re.search(r'\/+/\', vals[1])
  if match:
    print match.group
  else:
    print 'error' + line
      
