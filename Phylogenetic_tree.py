#Code to create the phylogenetic trees with the result of the MSA. 



from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio import AlignIO

# Load the multiple sequence alignment from a file
alignment = AlignIO.read("MSA_ALTER.fa", "fasta")

# Calculate the distance matrix
calculator = DistanceCalculator('blosum62')
distance_matrix = calculator.get_distance(alignment)
   
    
# Build the phylogenetic tree
constructor = DistanceTreeConstructor(calculator, 'nj')
tree = constructor.build_tree(alignment)

# Remove labels from the tree nodes
for node in tree.get_nonterminals():
    node.name = ''

# Save the tree as a Newick file
Phylo.write(tree, "YourTree.nwk", "newick")

tree_file = "YourTree.nwk"

# Load the tree from the Newick file
tree = Phylo.read(tree_file, "newick")

# Customize the font size
plt.rcParams['font.size'] = 35

# Draw the tree
fig, ax = plt.subplots(figsize=(120, 100))
ax.set_facecolor('white')  # Set the background color to white
Phylo.draw(tree, axes=ax, do_show=False)

plt.savefig('YourTree.png')
