#Code written in Python to find the lipase like box sequences in a given amount of sequences. 

import pandas as pd
import re
import matplotlib.pyplot as plt


def find_lipase_like_box(fasta_file, output_file):
    lipase_like_box_motifs = []
    lipase_box_motifs = []
    other_motifs = []
    combined_motifs = []

    with open(fasta_file, 'r') as f:
        fasta = f.read()

    sequences = re.findall('>(.*?)\n([A-Za-z\n]+)', fasta, re.DOTALL)
    for i, (header, sequence) in enumerate(sequences):
        microorganism = re.search('\[(.*?)\]', header).group(1)
        sequence = sequence.replace('\n', '')

        lipase_like_box_matches = re.finditer('([GS])\wC\w((?:A[GA]G)|(?:G(?:\w)?))', sequence)
        lipase_box_matches = re.finditer('G[A-Z]S[A-Z]G\w', sequence)
        other_lipase_box_matches = re.finditer('G[A-Z][^SG][A-Z]G\w', sequence)

        for match in lipase_like_box_matches:
            motif = match.group(0)
            lipase_like_box_motifs.append((header, microorganism, motif, i+1, sequence))  # Add motif, related information, and the entire sequence as a tuple
            combined_motifs.append(motif)

        for match in lipase_box_matches:
            lipase_box_motifs.append(match.group(0))  # Add motif directly to the list
            combined_motifs.append(match.group(0))

        for match in other_lipase_box_matches:
             other_motifs.append(match.group(0))  # Add motif directly to the list
             combined_motifs.append(match.group(0))

    # Create DataFrame for lipase_like_box motifs
    lipase_like_box_df = pd.DataFrame(lipase_like_box_motifs, columns=['Header', 'Microorganism', 'Motif', 'Position', 'Sequence'])
    combined_motifs_df = pd.DataFrame(combined_motifs, columns=['Motif'])

    # Save each DataFrame to a separate tab in the Excel file
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        lipase_like_box_df.to_excel(writer, sheet_name='Lipase-like motifs', index=False)
        pd.DataFrame(lipase_box_motifs, columns=['Motif']).to_excel(writer, sheet_name='Lipase box motifs', index=False)
        pd.DataFrame(other_motifs, columns=['Motif']).to_excel(writer, sheet_name='Other motifs', index=False)
        pd.DataFrame(combined_motifs, columns=['Motif']).to_excel(writer, sheet_name='Combined motifs', index=False)

    
fasta_file_path = "yourfile.txt"
output_file_path = "youroutput.xlsx"
find_lipase_like_box(fasta_file_path, output_file_path)
