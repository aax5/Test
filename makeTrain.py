import os, sys


x = sys.argv[1]
for counter in range(0,int(x)):
  files = int(counter)*1000
  dir1 = "/home/dkoes/PDBbind/refined-set/pdbbindtrain0.types"
  dir2 = "/home/dkoes/PDBbind/refined-set/new" + str(files) + "pdbtrain0.types"
  
  cmd1 = ("shuf -n " + files + " "  + dir1 + " > " + dir2)
  
  os.system(cmd1)