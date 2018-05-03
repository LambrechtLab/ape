# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 15:02:15 2017

@author: keith
"""

import pyqchem
from argparse import ArgumentParser

def getArguments():
    parser = ArgumentParser(prog="Piezoelectric Matrix Evaluator", description="Returns piezo-matrix for atoms or system of atorms of a molecule of choice.")
    parser.add_argument("qchemFile", help='name of qchem input to file to serve as base', type=str)
    parser.add_argument("atomList1", help='1st list of atom indexes (integers) from qchem file (starting atom is 0)')
    parser.add_argument("atomList2", help='2nd list of atom indexes (integers) from qchem file (starting atom is 0)')
    #parser.add_argument("optQueue", help='frank queue to be used for optimization', default = 'shared', type= str)
    #parser.add_argument("freqQueue", help='frank queue to be used for frequency calculation', default= 'shared', type= str)
    parser.add_argument("optPPN", help='number of processors per node for opimization', default = 4, type= int)
    parser.add_argument("freqPPN", help= 'number of processor per node for frequency calculation', default = 16, type=int)
    parser.add_argument("optTime", help= 'number of hours allocated for optimization', default= 24, type = int)
    parser.add_argument("freqTime", help= 'number of hours allocated for frequency calculation', default= 48, type= int)
def goApe(qchemFile, atomList1, atomList2, optQueue, freqQueue, optPPN, freqPPN, optTime, freqTime):
    job = pyqchem.piezo.PiezoMoleculeSolver(qchemFile)
    #job.calculatePiezoelectricMatrix(atomList1,atomList2,optQueue = optQueue, optPpn= optPPN, optTiming=optTime, freqQueue =freqQueue, freqPpn= freqPPN, freqTiming= freqTime)
    job.calculatePiezoelectricMatrix(atomList1,atomList2, optPpn= optPPN, optTiming=optTime, freqPpn= freqPPN, freqTiming= freqTime)
    
    
    
if __name__ == "__main__":
    args = getArguments()
    goApe(args.qchemFile, args.atomList1, args.atomList2, args.optPPN, args.freqPPN, args.optTime, args.freqTime)
    
    