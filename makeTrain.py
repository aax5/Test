import os, sys


x = sys.argv[1]
"""for counter in range(0,int(x)):
  
  os.system(cmd1)"""
for counter in range(0,int(x)):
  files = int(counter)*1000
  for newcounter in range(0,3):
    
    dir1 = "/home/dkoes/PDBbind/refined-set/pdbbindtest" + str(newcounter) + ".types"
    dir2 = "/home/dkoes/PDBbind/refined-set/new" + str(files) + "pdbtest" + str(newcounter)+ ".types"
    cmd2 = "more " + dir1 + " > " + dir2
    os.system(cmd2)
    
    dir1 = "/home/dkoes/PDBbind/refined-set/pdbbindtrain" + str(newcounter) + ".types"
    dir2 = "/home/dkoes/PDBbind/refined-set/new" + str(files) + "pdbtrain" + str(newcounter) + ".types"

    cmd1 = ("shuf -n " + str(files) + " "  + dir1 + " > " + dir2)

