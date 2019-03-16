import glob
import re

file_list = []
zwischenruf_trigger = "]:"
counter = 12001

# Open all Parlamentsprotokolle
for filepath in glob.glob('Perioden/pp12-data/*.xml'):
    file_list.append(filepath)

#file_list = file_list[59:60]

# Extract specific text between parantheses
for item in file_list:
    klammern = []
    with open(item) as file:  
        data = file.read() 
        print(counter)
        zwischenrufe = re.findall(r'\(([^\)]+)\)', data)
        for x in zwischenrufe:
                if zwischenruf_trigger in x:
                    klammern.append(x.replace('-\n', '').replace('\n', ' '))
        print("Zwischenrufe: " + str(len(klammern)))
        applaus = re.findall(r'\([^()]*?Beifall[^()]*\)', data.replace('-\n', '').replace('\n', ' '))
        print("Applaus: " + str(len(applaus)))
        heiterkeit = re.findall(r'\([^()]*?Heiterkeit[^()]*\)', data.replace('-\n', '').replace('\n', ' '))
        print("Heiterkeit: " + str(len(heiterkeit)))
        print("\n")
        counter += 1
        #print(applaus)


import matplotlib.pyplot as plt
import numpy as np
def lineplot(x_data, y_data, x_label="", y_label="", title=""):
    # Create the plot object
    _, ax = plt.subplots()

    # Plot the best fit line, set the linewidth (lw), color and
    # transparency (alpha) of the line
    ax.plot(x_data, y_data, lw = 2, color = '#539caf', alpha = 1)

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)