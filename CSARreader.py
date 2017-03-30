import sys, re
proteins = dict
for line in open(sys.argv[1]):
  vals = line.split()
  match = re.search(r'/\w+/', vals[1])
  if match:
    print match.group()
    proteins[name] = match.group
  else:
    print 'error'
print proteins 
  
  
