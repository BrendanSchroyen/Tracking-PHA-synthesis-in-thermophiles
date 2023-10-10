# Code to alter the fasta headers AFTER the MSA. This code prepares the fasta headers for next steps. 
def edit_fasta_header(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as file:
        for line in lines:
            if line.startswith('>'):
                # Remove first characters before the first whitespace
                line = line.split(maxsplit=1)[1]
                # Replace whitespaces with underscores
                line = line.replace(' ', '_')
                line = '>' + line
            file.write(line)

input_file = Path('MSA.fa')
output_file = Path('MSA_ALTER.fa')

edit_fasta_header(input_file, output_file)
