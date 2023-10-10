# Tracking-PHA-synthesis-in-thermophiles

This repository was created as supporting documentation for the paper X published in X on X. The paper can be accessed through this link X. 

The main goal of this code is to identify potential PhaC sequences in a big database or within a big query of sequences. The input of the code is always a text file with fasta sequences. The output of the Find_lipase_like_box.py is an excel file with all of the hits (including hits which only have a true lipase box or another motif, seperated on different sheets of the excel file). After this, it is a personal choice to go further with these and create a multiple sequence alignment with for example COBALT. If one is interested in this, the 'Preparation_Multiple_Sequence_Alignment.py' code can be used to extract the accession codes out of the excel file and create a file which can be uploaded to COBALT. Next to this, there are additional scripts in this file which can be used to visualize the MSA (Visualize_MSA.py) and/or to create a phylogenetic tree out of the MSA (Phylogenetic_tree.py). 
