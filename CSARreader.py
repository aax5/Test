import sys
affs = dict
for line in open(sys.argv[1]):
  (x, name, a, b, c, d) = line.split()
  match = re.search(r'(\/+/\)', name)
  if match:
    print match.group
  else:
    print 'error' + line
      
