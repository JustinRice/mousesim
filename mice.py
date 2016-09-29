#!/usr/bin/env python

from parse import Parser
from sim import Simulation

#----- Main
print('This is a test!')
parser = Parser("sampledata.csv")
simulation = Simulation()
simulation.setUp(parser.getData())
done = False
while not done:
    inputStr = input("How long to move? ")
    if (int(inputStr) == 99):
        done = True
    else:
        simulation.updateAll(int(inputStr))
print(simulation.getAllPaths())

#print parser.getData()

#for key in parser.getData().keys():
#   print(key)

