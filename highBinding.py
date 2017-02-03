import argparse
#PdbData = "2w0x  2.12  2009  IC50=625uM    // 2w0x.pdf (PD2) compound 4" #in here should go the line that is fed in from the data
parser = argparse.ArgumentParser(description = "Files to be used")
parser.add_argument("-i", "--input", help = "input file")
parser.add_argument("-o", "--output", help = "output file")
args = parser.parse_args()
f = open(args.input)
outputFile = open(args.output, 'w')
for line in f:
  words=line.split()
  if(float(words[2] > 5)
     outputFile.write(line)
