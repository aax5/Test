import sys, re, random

proteins = dict()
for line in open(sys.argv[1]):
  vals = line.split()
  match = re.search(r'\w+/', vals[1])
  if match:
    #print match.group()
    name = match.group()
    proteins[name] = 0
    
  else:
    print 'error'
    
for line in open(sys.argv[1]):
  vals = line.split()
  match = re.search(r'\w+/', vals[1])
  if match:
    if match.group() in proteins:
      proteins[match.group()] += 1
      
#print proteins 
#print len(proteins)
randProteins = dict()
x = (sys.argv[2])
for i in range (0,int(x)): 
  name, val = random.choice(list(proteins.items()))
  randProteins[name] = val
  
  
for line in open(sys.argv[1]):
  vals = line.split()
  match = re.search(r'\w+/', vals[1])
  if match:
    #print match.group()
    if match.group() in randProteins:
      print line
