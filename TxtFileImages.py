# -*- coding: utf-8 -*-
"""
    File name: TextFileImages_2.py
    Author: Celine
    Date created: 7/18/2020
    Date last modified: 7/24/2020
    Python Version: 3.8
"""
#For replacing letters, numbers, etc.
import re

#Unicode characters
encoding = 'utf-8'
box = '■'

#Ask user to input a text file
fname = input("Enter file name: ")

#Use default one if no text file provided
if len(fname) < 1 :
    fname = "testimage.txt"

#Fill the white spaces and print results to a new text file
def replace_white_space(infile, outfile):
    #read input file and write to output file
    with open(infile, "rt") as fin:
        print("Processing...")
        with open(outfile, "wb") as fout:

            #replace white spaces with box and remove all other characters
            for line in fin:
                line = line.replace(' ', box)
                nline = re.sub('[^■\n]',' ', line)
                fout.write(nline.encode(encoding))
    return

replace_white_space(fname, "results.txt")
print("All finished!")
