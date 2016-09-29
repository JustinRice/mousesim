#!/usr/bin/env python

from parse import Parser

#----- Main
print('This is a test!')
parser = Parser("sampledata.csv")

print parser.getData()

for key in parser.getData().keys():
    print(key)

