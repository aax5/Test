#!/usr/bin/env pythonhttps://github.com/aax5/Test
import re
import math
import argparse
#PdbData = "2w0x  2.12  2009  IC50=625uM    // 2w0x.pdf (PD2) compound 4" #in here should go the line that is fed in from the data
parser = argparse.ArgumentParser(description = "Files to be used")
parser.add_argument("-i", "--input", help = "input file")
parser.add_argument("-o", "--output", help = "output file")
args = parser.parse_args()
with open(args.input) as file: 
  f = file.read()

#f = open('/home/dkoes/PDBbind/index/INDEX_general_PL.2016')
#test string
length = 0
proteinName = "" #name of the protein

restOfData = ""
#out = open('/home/aaz24/output.txt','w')
#creates output file
txtLength = 0 #how long the file should be
#for txtLength in xrange(len(PdbData))
newCounter = 0
for counter, line in enumerate(f,  1):
  #print line
#line is now string of single line in f
  if line[0] != "#":
    
    words = line.split()
    
    proteinName = words[0]
    restOfData = words[3]
    #finds the proteinName and the part of data with binding affinities

    match = re.search(r'(\S+[^<])[~=](\d+.?\d*)(\SM)', restOfData)
    """matches types: group(1) matches the nonspace chars before the "=", group(2) matches the numerical chars
    and ".", and group(3) matches the nonspace chars after those numbers  """
    if(match):
        source = match.group(1)
        #gives prefix before data
        baseNum = match.group(2)
        #gives baseNum before unit conversion
        #print baseNum
        measurementValue = match.group(3)
        #gives measurement unit
        #print measurementValue
      
        if (measurementValue == "mM"):
            endNum = float(baseNum)*(1e-3)    
        elif (measurementValue == "uM"):
            endNum = float(baseNum)*(1e-6) 
        elif (measurementValue == "nM"):
            endNum = float(baseNum)*(1e-9)  
        elif (measurementValue == "pM"):
            endNum = float(baseNum)*(1e-12)
        elif (measurementValue == "fM"):
            endNum = float(baseNum)*(1e-15)
        else:
            endNum = -1
        # converts from whatever measurement type given to M and saves it as an int, endNum    
        affinityValue = -math.log10(endNum)
        #finds -log10 value of endNum
        with open(args.output) as file:
          file.write(proteinName + " " + source + " " + str(affinityValue) + "\n")
          #prints to text file
    else:
        print "Error: Not \"=\"" + " " + str(counter) + " " +  line
        newCounter+= 1
  else:
     print "commentated file" + " " + str(counter) + line      
print "Number of files without \"=\" " +  str(newCounter)

