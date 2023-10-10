#Code to extract the accession numbers of the sequences in the excel file created by the find_lipase_like_box script.

import pandas as pd
import re

# Read the Excel file
df = pd.read_excel("Yourexcel.xlsx", sheet_name='Lipase-like motifs')

# Extract the first characters before the whitespace from the first column
extracted_values = df.iloc[:, 0].str.split().str[0]

# Extract the text between square brackets on the same line
pattern = r"\[(.*?)\]"
extracted_text = df.iloc[:, 0].str.extract(pattern, expand=False)

# Modify the extracted values
modified_values = '>' + extracted_text + ' (AN:' + extracted_values +')'+ '\n' + df.iloc[:, 4].astype(str)

# Write the output to a text file
output_file_path = "YourAccessionNumbers.txt"
with open(output_file_path, 'w') as file:
    file.write('\n'.join(modified_values))

# Merge the output file with another file (This step ONLY needs to be done when you want to add the sequences of the known PhaC enzymes, this txt file can be found in the repository!!)
phaC_file_path = "Known_PhaC_Sequences.txt"
with open(phaC_file_path, 'r') as phaC_file:
    phaC_text = phaC_file.read()

with open(output_file_path, 'a') as output_file:
    output_file.write('\n' + phaC_text)
