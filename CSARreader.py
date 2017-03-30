import sys, re
proteins = dict()
name = ''
for line in open(sys.argv[1]):
  vals = line.split()
  match = re.search(r'/\w+/', vals[1])
  if match:
    print match.group()
    match.group() = name
    proteins[name] = proteins[entries] + 1
    
  else:
    print 'error'
print proteins 
  
  
