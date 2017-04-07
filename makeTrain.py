import os, sys


x = sys.argv[1]
"""for counter in range(0,int(x)):
  files = int(counter)*1000
  dir1 = "/home/dkoes/PDBbind/refined-set/pdbbindtrain2.types"
  dir2 = "/home/dkoes/PDBbind/refined-set/new" + str(files) + "pdbtrain2.types"
  
  cmd1 = ("shuf -n " + str(files) + " "  + dir1 + " > " + dir2)
  
  os.system(cmd1)"""
for counter in range(0,int(x)):
  files = int(counter)*1000
  for newcounter in range(0,3):
    
    dir1 = "/home/dkoes/PDBbind/refined-set/pdbbindtest" + str(newcounter) + ".types"
    dir2 = "/home/dkoes/PDBbind/refined-set/new" + str(files) + "pdbtrain" + str(newcounter-1)+ ".types"
    cmd2 = "more " + dir1 + " > " + dir2
    os.system(cmd2)
