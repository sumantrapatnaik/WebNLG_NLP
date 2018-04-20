import xml.etree.ElementTree as ET
import os
import codecs
import string
import shutil
# -*- coding: utf-8 -*-

        
     
outputWords = []
nonOutputWords=[]
table = str.maketrans({key: " " for key in string.punctuation})



with open("vocab.en") as f:
    for line in f:
        for word in line.split():
            outputWords.append(word)  

with open("dev.en") as f:
    for line in f:
        for word in line.translate(table).split():
            outputWords.append(word.translate(table))

with open("train.en") as f:
    for line in f:
        for word in line.translate(table).split():
            outputWords.append(word.translate(table))

with open("test.en") as f:
    for line in f:
        for word in line.translate(table).split():
            outputWords.append(word.translate(table))     
            
with open("dev.vi") as f:
    for line in f:
        for word in line.translate(table).split():
            outputWords.append(word.translate(table))

with open("train.vi") as f:
    for line in f:
        for word in line.translate(table).split():
            outputWords.append(word.translate(table))

with open("test.vi") as f:
    for line in f:
        for word in line.translate(table).split():
            outputWords.append(word.translate(table))             
    
  
print ("This will take a few minutes...")
  
vocabFile = codecs.open('vocabNew.en', 'w', "utf-8")    

for entry in outputWords:
    if entry not in nonOutputWords:
        #print(entry)
        vocabFile.write(entry + "\n")
        nonOutputWords.append(entry)

vocabFile.close()


shutil.copy2('vocabNew.en', 'vocabNew.vi')

#import pdb; pdb.set_trace()


