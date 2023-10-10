#Code to visualize the MSA with the MSAViz package

pip install pymsaviz
from pymsaviz import MsaViz

# Read the MSA file
msa_file = "MSA_ALTER.fa"

#The argument wrap_length can be changed to show a longer/shorter stretch of the MSA on one line. start = x and end = y arguments can be given if only a part of the MSA needs to be visualized. 
mv = MsaViz(msa_file, wrap_length=100, color_scheme = 'Clustal',show_consensus=True)

# Extract MSA positions less than 50% consensus identity
pos_ident_less_than_50 = []
ident_list = mv._get_consensus_identity_list()
for pos, ident in enumerate(ident_list, 1):
    if ident <= 50:
        pos_ident_less_than_50.append(pos)

# Add markers (change the 475 and 480 if you want to the position of the lipase-like box in your specific example)
mv.add_text_annotation((475, 480), "Lipase-like box", text_color="red", range_color="red")

mv.savefig("YourMSA.svg")
