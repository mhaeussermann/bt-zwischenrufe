# -*- coding: utf-8 -*-
import os
import textract
import glob

for filepath in glob.iglob('16/*.pdf'):
        text = textract.process(filepath)
        filepath += ".txt"
        with open(filepath, "w") as f:
                f.write(text) 
                print(filepath)