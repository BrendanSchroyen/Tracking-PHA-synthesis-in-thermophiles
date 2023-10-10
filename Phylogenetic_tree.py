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

from ete3 import Tree, TreeStyle, NodeStyle

# Load the tree from a Newick file
tree = Tree("YourTree.nwk", quoted_node_names=True)

# Create a TreeStyle object for customization
ts = TreeStyle()
ts.mode = "c"  # Circular layout
ts.arc_start = -90
ts.arc_span = 180
ts.branch_vertical_margin = 1

# Customize the branch color based on leaf names
for node in tree.traverse():
    if node.is_leaf() and 'Class_II' in node.name:
        node_color = "red"
        # Color the branches leading to the leaf node
        for ancestor in node.iter_ancestors():
            ancestor_style = NodeStyle()
            #ancestor_style["bgcolor"] = node_color
            #ancestor_style["hz_line_color"] = node_color
            #ancestor_style["fgcolor"] = node_color
            ancestor.set_style(ancestor_style)

# Additional customization options (optional)
ts.show_leaf_name = True
ts.scale = 600  # Controls the size of the tree

# Apply the TreeStyle to the tree and render it
tree.render("YourTree.svg", tree_style=ts)
