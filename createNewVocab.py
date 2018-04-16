import xml.etree.ElementTree as ET
import os
import codecs
# -*- coding: utf-8 -*-

        
     
outputWords = []


with open("dev.en") as f:
    for line in f:
        for word in line.split():
            outputWords.append(word)

with open("train.en") as f:
    for line in f:
        for word in line.split():
            outputWords.append(word)

with open("test.en") as f:
    for line in f:
        for word in line.split():
            outputWords.append(word)           
    
  
vocabFile = codecs.open('vocabNew.en', 'w', "utf-8")    

for entry in set(outputWords):
    print(entry)
    vocabFile.write(entry + "\n")

vocabFile.close()

#import pdb; pdb.set_trace()


