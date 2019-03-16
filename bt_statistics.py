import glob
import os
import re
from collections import OrderedDict
import csv

file_list = []
zwischenruf_trigger = "]:"
statistik = []

# Open all Parlamentsprotokolle
for filepath in glob.glob('Perioden/*/*.xml'):
    file_list.append(filepath)

#file_list = file_list[59:60]

# Extract specific text between parantheses
for item in file_list:
    klammern = []
    zwischenrufe_data = OrderedDict()
    print(os.path.basename(item)[:5])
    with open(item) as file:  
        data = file.read() 
        zwischenrufe_data["Sitzung"] = os.path.basename(item)[:5]
        zwischenrufe = re.findall(r'\(([^\)]+)\)', data)
        for x in zwischenrufe:
                if zwischenruf_trigger in x:
                    klammern.append(x.replace('-\n', '').replace('\n', ' '))
        zwischenrufe_data["Zwischenrufe"] = str(len(klammern))
        applaus = re.findall(r'\([^()]*?Beifall[^()]*\)', data.replace('-\n', '').replace('\n', ' '))
        zwischenrufe_data["Applaus"] = str(len(applaus))
        heiterkeit = re.findall(r'\([^()]*?Heiterkeit[^()]*\)', data.replace('-\n', '').replace('\n', ' '))
        zwischenrufe_data["Heiterkeit"] = str(len(heiterkeit))
        # Create List of Dictionaries
        statistik.append(zwischenrufe_data)
        #print(statistik)

# Write the list of dicts to a TSV file
outfilename = "Perioden/statistik.csv"
#with open(outfilename, "w") as outfile:    
    
    # Write the rows using the values of the dictionaries
    #for row in statistik:
        #column_values = row.values()
        #line = ",".join(column_values) + '\n'
        #outfile.write(line)

with open(outfilename, 'w') as outfile:
    fp = csv.DictWriter(outfile, statistik[0].keys())
    fp.writeheader()
    fp.writerows(statistik)

#import matplotlib.pyplot as plt

#plt.bar(range(len(statistik)), list(statistik.values()), align='center')
#plt.xticks(range(len(statistik)), list(statistik.keys()))

#plt.show()
