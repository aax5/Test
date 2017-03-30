import sys, re
affs = dict
for line in open(sys.argv[1]):
  
  match = re.search(r'(\/+/\)', line.split(1))
  if match:
    print match.group
  else:
    print 'error' + line
      
