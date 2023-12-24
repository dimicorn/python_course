import json


f = open('seminar5/rna.fasta')
contents = f.readlines()
sequence_type = None
for line in contents:
    if line[0] == '>':
        sequence_type = line.split()[1].split('\n')[0]
    if sequence_type is not None:
        sequence = line
f.close()

with open('seminar5/rna_codon_table.json') as f:
    codon_table = json.load(f)


print(sequence_type)
print(sequence)
print(codon_table)