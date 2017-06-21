# Extractmolecule

This Repo focusses on Data Extraction From PDF and Converting it into Json/Dictionary Form

# Requirements 
# NOTE (Your files and code should be in the same folder or place)
Python Installed on PC preferably(Python 3.5 or Python 3)

One .pdf data files for example here they are WHandbook.pdf 

Need to Install pdfminer3k for python3 by "pip install pdfminer3k"

# For Python 2.7

"pip install pdfminer" and some changes in code are required

# For running pdfmine.py (Data extraction)

Open Command Prompt

cd to the loaction of code and WHandbook.pdf

type "python pdfmine.py"

THE CODE WILL START

The final output in LTTextLine or LTTextBox format for WHandbook.pdf will be in convertedFile.txt 

# For running extract.py (Data Conversion)

Run this after running pdfmine.py

Open Command Prompt

cd to the loaction of code and convertedFile.txt file

type "python extract.py"

THE CODE WILL START

The final output dictionary will be printed and stored as JSON Format in saerch.txt 
