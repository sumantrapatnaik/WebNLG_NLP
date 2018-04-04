# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import string
from bs4 import BeautifulSoup
#import io


class XMLParser(object):
    
    def __init__(self, xml_dir):
        self.xlm_dir = xml_dir
        file_paths1 = os.listdir(xml_dir)
        self.file_paths = [xml_dir + "/" + x for x in file_paths1]
        
    def update(self,file_vi,file_en):
        counter = 0
        for eachXmlFile in self.file_paths:
            infile = open(eachXmlFile,"r")
            contents = infile.read()
            soup = BeautifulSoup(contents,'xml')
            
            for entry in soup.find_all('entry'):
                for mtripleset in entry.find_all('modifiedtripleset'):
                    mtriple_list = []
                    for mtriple in mtripleset.find_all('mtriple'):
                        mtriple_list.append(mtriple.text)
                        mtriple_list.append(" | ")
                    #mtriple_list_str = str(mtriple_list)
                    mtriple_list_str = ''.join(map(str, mtriple_list))
                    #mtriple_list_str.replace(" | "," ")
                    mtriple_list_str_new = mtriple_list_str.replace(" | "," ")
                    file_vi.write(mtriple_list_str_new)
                    counter += 1
                    file_vi.write('\n')
                        #print "Mtriple : " + mtriple.text
                for lex in entry.find_all('lex'):
                    file_en.write(lex.text)
                    file_en.write('\n')
                     
        #print (counter)          
                        
                            
   
                            
"""                      
dev_dir = "challenge_data_train_dev/dev"
train_dir = "challenge_data_train_dev/train"

dev_triples_dir = os.listdir(dev_dir)
train_triples_dir = os.listdir(train_dir)
#print (dev_triples_dir)
#print (train_triples_dir)


f_dev_vi = open("challenge_data_train_dev/dev.vi",'w',encoding='utf8')
f_dev_en = open("challenge_data_train_dev/dev.en",'w',encoding='utf8')
f_train_vi = open("challenge_data_train_dev/train.vi",'w',encoding='utf8')
f_train_en = open("challenge_data_train_dev/train.en",'w',encoding='utf8')


for eachTripleDevDir in dev_triples_dir[1:]:
    df = XMLParser(dev_dir + "/" + eachTripleDevDir)
    df.update(f_dev_vi,f_dev_en)

  
for eachTripleTrainDir in train_triples_dir[1:]:
    tf = XMLParser(train_dir + "/" + eachTripleTrainDir)
    tf.update(f_train_vi,f_train_en)


#df = XMLParser("challenge_data_train_dev/dev/1Triples")
#df.update(f_dev_vi,f_dev_en)
f_dev_vi.close()
f_dev_en.close()
f_train_vi.close()
f_train_en.close()
"""

f_test_vi = open("challenge_data_train_dev/test.vi",'w',encoding='utf8')
f_test_en = open("challenge_data_train_dev/test.en",'w',encoding='utf8')
test_path = "testdata_unseen_with_lex.xml"
infile = open(test_path,"r")
contents = infile.read()
soup = BeautifulSoup(contents,'xml')
counter = 0
for entry in soup.find_all('entry'):
                for mtripleset in entry.find_all('modifiedtripleset'):
                    mtriple_list = []
                    for mtriple in mtripleset.find_all('mtriple'):
                        mtriple_list.append(mtriple.text)
                        mtriple_list.append(" | ")
                    #mtriple_list_str = str(mtriple_list)
                    mtriple_list_str = ''.join(map(str, mtriple_list))
                    #mtriple_list_str.replace(" | "," ")
                    mtriple_list_str_new = mtriple_list_str.replace(" | "," ")
                    f_test_vi.write(mtriple_list_str_new)
                    counter += 1
                    f_test_vi.write('\n')
                        #print "Mtriple : " + mtriple.text
                for lex in entry.find_all('lex'):
                    f_test_en.write(lex.text)
                    f_test_en.write('\n')

print (counter)
"""
f_vocab_vi = open("challenge_data_train_dev/vocab.vi",'w',encoding='utf8')
f_vocab_en = open("challenge_data_train_dev/vocab.en",'w',encoding='utf8')
vi_path = "challenge_data_train_dev/train.vi"
en_path = "challenge_data_train_dev/train.en"
enFile = open(en_path,"r")
viFile = open(vi_path,"r")
enfile_contents = enFile.readlines()
vifile_contents = viFile.readlines()

enTokenList = []
for enLine in enfile_contents:
    token_list_en = enLine.split()
    for token in token_list_en:
        if token not in enTokenList:
            enTokenList.append(token)

#enTokenList_str = ''.join(map(str, enTokenList))
            
for item in enTokenList:
    f_vocab_en.write(item)
    f_vocab_en.write('\n')

viTokenList = []
for viLine in vifile_contents:
    token_list = viLine.split()
    for token in token_list:
        if token not in viTokenList:
            viTokenList.append(token)

for item in viTokenList:
    f_vocab_vi.write(item)
    f_vocab_vi.write('\n')

f_vocab_vi.close()
f_vocab_en.close()
"""