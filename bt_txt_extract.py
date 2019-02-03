# -*- coding: utf-8 -*-
import glob
import re

file_list = []
klammern = []
zwischenrufe = []
klammern_clean = []
zwischenruf_trigger = "]:"

# Open all Parlamentsprotokolle
for filepath in glob.glob('16/*.txt'):
    file_list.append(filepath)

# Extract text between parantheses
for item in file_list:
    with open(item) as file:  
        data = file.read() 
        zwischenrufe.append(re.findall(r'\(([^\)]+)\)', data))

#print(zwischenrufe)

# Extract the Zwischenrufe
for x in zwischenrufe:
    for amount in x:
        if zwischenruf_trigger in amount:
            klammern.append(amount)

# Clean the text
for word in klammern:
    klammern_clean.append(word.replace('\n', ' ').replace('-\n', '').replace('-\n\n', '').replace('\n\n', '').replace('\r\n', '').replace('- ','').replace('   ', ' ').replace('  ', ' ').replace('-  ', ''))

with open('zwischenruf-clean.txt', 'w') as f:
    for item in klammern_clean:
        f.write("%s\n" % item)