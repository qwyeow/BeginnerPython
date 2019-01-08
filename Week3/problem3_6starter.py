# -problem3_6.py *- coding: utf-8 -*-

import sys

filename1 = sys.argv[1]
filename2 = sys.argv[2]

infile = open(filename1)
outfile = open(filename2,'w')


for line in infile:
    line = line.strip("\n") 
    output = str(len(line))
    outfile.write(output + "\n")
    #print(len(line))
   
infile.close()
outfile.close()    