import sys, re
proteins = dict()
name = ''
for line in open(sys.argv[1]):
  vals = line.split()
  match = re.search(r'/\w+/', vals[1])
  if match:
    print match.group()
    name = match.group()
    proteins[name] = 0
    
    
  else:
    print 'error'
    
for line in open(sys.argv[1]):
  vals = line.split()
  match = re.search(r'/\w+/', vals[1])
  if match:
    if match.group() in proteins:
      proteins[match.group()] += 1
      
print proteins 
print len(proteins)
  
  
