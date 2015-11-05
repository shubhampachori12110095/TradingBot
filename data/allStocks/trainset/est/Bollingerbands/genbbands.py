#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Thiago Silva
# 
# This script generates a bunch of files, where each file has the bollinger bands to a given setting.
# The stocks prices come from ../../daily_candles folder.
# 

import numpy
import talib
import sys
from os import listdir, makedirs
from os.path import isfile, join, exists

xDays = [5, 7, 10, 15, 21]
path = '../../daily_candles'

def frange(b, e, s):
  while b < e:
    yield b
    b += s

def main():
  files = [ f for f in listdir(path) if isfile(join(path, f)) ]
  for f in files:
    close = []
    paper_file = open(path+'/'+f, 'r')
    for line in paper_file.readlines():
      close.append(float(line.split(',')[0]))
    close = numpy.array(close)
    paper_file.close()
    
    for x in xDays:
      for k in frange(1.5, 4, 0.5):
        upper, middle, lower = talib.BBANDS(close, x, k, k)
        outFile = open(f + "_"+ str(x) + "_" + str(k) + '_closebbands', 'w')
        for i in range(len(upper)):
          outFile.write(str(upper[i]))
          outFile.write(" ")
          outFile.write(str(middle[i]))
          outFile.write(" ")
          outFile.write(str(lower[i]))
          outFile.write("\n")
        outFile.close()


if __name__ == '__main__':
  main()
