import os, sys


x = sys.argv[1]
multiplier = sys.argv[2]
"""for counter in range(0,int(x)):
  
  os.system(cmd1)"""
for counter in range(0,int(x)):
  files = int(counter)*int(multiplier)
  for newcounter in range(0,3):
    
    dir1 = "/home/dkoes/PDBbind/refined-set/nopospdbbindtest" + str(newcounter) + ".types"
    dir2 = "/home/dkoes/PDBbind/refined-set/nopos/new" + str(files) + "nopospdbtest" + str(newcounter)+ ".types"
    cmd2 = "more " + dir1 + " > " + dir2
    os.system(cmd2)
    
    dir1 = "/home/dkoes/PDBbind/refined-set/nopospdbbindtrain" + str(newcounter) + ".types"
    dir2 = "/home/dkoes/PDBbind/refined-set/nopos/new" + str(files) + "nopospdbtrain" + str(newcounter) + ".types"

    cmd1 = ("shuf -n " + str(files) + " "  + dir1 + " > " + dir2)
    os.system(cmd1)
