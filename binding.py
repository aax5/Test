import re
PdbData = "2w0x  2.12  2009  IC50=625uM    // 2w0x.pdf (PD2) compound 4" #in here should go the line that is fed in from the data
f = open('/home/dkoes/PDBbind/index/INDEX_general_PL.2016')
#test string
length = 0
proteinName = "" #name of the protein
endString = ""
restOfData = ""
#
txtLength = 0 #how long the file should be
#for txtLength in xrange(len(PdbData))
for line in f
#line is now string of single line in f
  words = line.split()
  proteinName = words[0]
  restOfData = words[3]
  #finds the proteinName and the part of data with binding affinities

  match = re.search(r'(\S+)=(\d+.?\d*)(\SM)', PdbData)
  """matches types: group(1) matches the nonspace chars before the "=", group(2) matches the numerical chars
  and ".", and group(3) matches the nonspace chars after those numbers  """
  
  source = match.group(1)
  #gives prefix before data
  baseNum = match.group(2)
  #gives baseNum before unit conversion
  measurementValue = match.group(3)
  #gives measurement unit
  
  if (measurementValue == "mM"):
        endNum = float(baseNum)*0.001    
  elif (measurementValue == "uM"):
        endNum = float(baseNum)*0.000001  
  elif (measurementValue == "nM"):
        endNum = float(baseNum)*0.000000001   
  elif (measurementValue == "pM"):
        endNum = float(baseNum)*0.000000000001
  else:
        endNum = -1
  endString += source + " " + baseNum + " " + measurementValue + "\n"
    # converts from whatever measurement type given to M and saves it as an int, endNum
out = open('/home/aaz24/output.txt','w')
out.write(endString)
