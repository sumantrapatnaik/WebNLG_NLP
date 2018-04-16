import xml.etree.ElementTree as ET
import os
import codecs
# -*- coding: utf-8 -*-

def parse(train_dev_test):
    fileList = []

    for root, dirs, files in os.walk('challenge_data_train_dev/'+train_dev_test+'/'):
        for name in files:
            if name.endswith((".xml")):
                fileList.append(os.path.join(root, name))
                
    englishFile = codecs.open(''+train_dev_test+'.en', 'w', "utf-8")
    tupleFile = codecs.open(''+train_dev_test+'.vi', 'w', "utf-8")    
           
    for path in fileList:
        tree = ET.parse(path)
        root = tree.getroot()
        for child in root[0]:
            mTripleConcat = ""
            for mTriple in child.find('modifiedtripleset').iter('mtriple'):
                mTripleConcat += (mTriple.text) + " | "
            
            for lex in child.iter('lex'):
                englishFile.write(lex.text + '\n')
                tupleFile.write(mTripleConcat[:-3].replace(" | ", " ") + '\n') 
            
    englishFile.close()
    tupleFile.close()    



parse('train')
parse('dev')
parse('test')