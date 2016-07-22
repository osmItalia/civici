#!/usr/bin/python
#

import os

path = "/Volumes/Macintosh HD/LinkedFolder/Download/_Export_nomi-vie_comuni_RER/"
dirs = os.listdir(path)
file_out = open("merge_lista_vie_RER.csv", 'w')

for file in sorted(dirs):
  comune = str.split(str.split(file,'_')[1],'.')[0]
  print comune
  file_in = open(path+file, 'r')
  for row in file_in:
    file_out.write(comune)
    file_out.write(",")
    file_out.write(row)

  file_in.close()

file_out.close()

#
