import glob
import os
import re
from collections import OrderedDict
import csv
from xml.etree import ElementTree as ET

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
    # Add data on Bundestagsperiode and Sitzungsnummer
    zwischenrufe_data["Bundestagsperiode"] = os.path.basename(item)[0:2]
    zwischenrufe_data["Sitzung"] = os.path.basename(item)[2:5]
    with open(item) as file:  
        data = file.read()
        root = ET.fromstring(data)
        # Add data on Sitzungsdatum
        zwischenrufe_data["Datum"] = root.find('DATUM').text
        # Extract Zwischenrufe and add their count
        zwischenrufe = re.findall(r'\(([^\)]+)\)', data)
        for x in zwischenrufe:
                if zwischenruf_trigger in x:
                    klammern.append(x.replace('-\n', '').replace('\n', ' '))
        zwischenrufe_data["Zwischenrufe"] = str(len(klammern))
        # Extract protocolar mentions of Beifall and add their count 
        beifall = re.findall(r'\([^()]*?Beifall[^()]*\)', data.replace('-\n', '').replace('\n', ' '))
        zwischenrufe_data["Beifall"] = str(len(beifall))
        # Extract protocolar mentions of Heiterkeit and add their count 
        heiterkeit = re.findall(r'\([^()]*?Heiterkeit[^()]*\)', data.replace('-\n', '').replace('\n', ' '))
        zwischenrufe_data["Heiterkeit"] = str(len(heiterkeit))
        # Create List of Dictionaries
        statistik.append(zwischenrufe_data)
        # Print the data for testing
        #print(statistik)

        with open('zwischenruf-korpus.txt', 'a') as f:
                for item in klammern:
                        f.write("%s\n" % item)

# Write the list of dicts to a CSV file
outfilename = "bt_statistik.csv"
with open(outfilename, 'w') as outfile:
    fp = csv.DictWriter(outfile, statistik[0].keys())
    fp.writeheader()
    fp.writerows(statistik)