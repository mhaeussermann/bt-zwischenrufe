import glob
import re

file_list = []
zwischenrufe = []
klammern = []
zwischenruf_trigger = "]:"

# Save list of protocols
for filepath in glob.glob('16/*.txt'):
    file_list.append(filepath)

# Extract text between parantheses
for item in file_list:
    with open(item) as file:  
        data = file.read() 
        zwischenrufe.append(re.findall(r'\(([^\)]+)\)', data))

# Extract the Zwischenrufe and clean them
for x in zwischenrufe:
    for amount in x:
        if zwischenruf_trigger in amount:
            klammern.append(amountword.replace('\n', ' ').replace('-\n', '').replace('\n\n', '').replace('\r\n', '').replace('- ','').replace('   ', ' ').replace('  ', ' ').replace('-  ', ''))

# Save cleaned text 
with open('zwischenruf-cleaned.txt', 'w') as f:
  for item in klammern:
    f.write("%s\n" % item)