import pandas as pd
import mysql.connector
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

Y = input('Enter organism name : ')
x = input("Enter RNA sequence for Translation : ").upper()

bases = ['A','U','G','C']

Codon_token = {
    'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAU':'N', 'AAC':'N',
    'GAU':'D', 'GAC':'D',
    'UGU':'C', 'UGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAU':'H', 'CAC':'H',
    'AUU':'I', 'AUC':'I', 'AUA':'I',
    'UUA':'L', 'UUG':'L', 'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
    'AAA':'K', 'AAG':'K',
    'AUG':'M',
    'UUU':'F', 'UUC':'F',
    'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S', 'AGU':'S', 'AGC':'S',
    'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'UGG':'W',
    'UAU':'Y', 'UAC':'Y',
    'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
    'UAA':'*', 'UAG':'*', 'UGA':'*'
}




Codon_full_name = {
    # Alanine
    'GCU': 'Alanine', 'GCC': 'Alanine', 'GCA': 'Alanine', 'GCG': 'Alanine',
    # Arginine
    'CGU': 'Arginine', 'CGC': 'Arginine', 'CGA': 'Arginine', 'CGG': 'Arginine', 'AGA': 'Arginine', 'AGG': 'Arginine',
    # Asparagine
    'AAU': 'Asparagine', 'AAC': 'Asparagine',
    # Aspartic acid
    'GAU': 'Aspartic acid', 'GAC': 'Aspartic acid',
    # Cysteine
    'UGU': 'Cysteine', 'UGC': 'Cysteine',
    # Glutamine
    'CAA': 'Glutamine', 'CAG': 'Glutamine',
    # Glutamic acid
    'GAA': 'Glutamic acid', 'GAG': 'Glutamic acid',
    # Glycine
    'GGU': 'Glycine', 'GGC': 'Glycine', 'GGA': 'Glycine', 'GGG': 'Glycine',
    # Histidine
    'CAU': 'Histidine', 'CAC': 'Histidine',
    # Isoleucine
    'AUU': 'Isoleucine', 'AUC': 'Isoleucine', 'AUA': 'Isoleucine',
    # Leucine
    'UUA': 'Leucine', 'UUG': 'Leucine', 'CUU': 'Leucine', 'CUC': 'Leucine', 'CUA': 'Leucine', 'CUG': 'Leucine',
    # Lysine
    'AAA': 'Lysine', 'AAG': 'Lysine',
    # Methionine
    'AUG': 'Methionine',
    # Phenylalanine
    'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
    # Proline
    'CCU': 'Proline', 'CCC': 'Proline', 'CCA': 'Proline', 'CCG': 'Proline',
    # Serine
    'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine', 'AGU': 'Serine', 'AGC': 'Serine',
    # Threonine
    'ACU': 'Threonine', 'ACC': 'Threonine', 'ACA': 'Threonine', 'ACG': 'Threonine',
    # Tryptophan
    'UGG': 'Tryptophan',
    # Tyrosine
    'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
    # Valine
    'GUU': 'Valine', 'GUC': 'Valine', 'GUA': 'Valine', 'GUG': 'Valine',
    # Stop
    'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop'
}

start_pos = x.find('AUG')
end_pos = len(x)
step_size = 3

RNA=[]

for i in range(start_pos, end_pos, step_size):
    codon = x[i:i+step_size]
    if codon == 'AUG':
        print(f"Start codon found: {codon}")
    elif codon in ['UAG', 'UAA', 'UGA']:
        print(f"Stop codon found: {codon}")
        break
    RNA.append(codon)

df = pd.DataFrame({'codon' : RNA})
df['weight'] = df['codon'].map(Codon_token)
df['full_name'] = df['codon'].map(Codon_full_name)
df = pd.DataFrame({'codon' : RNA})
df['weight'] = df['codon'].map(Codon_token)
df['full_name'] = df['codon'].map(Codon_full_name)
total_mass = df['weight'].sum(), df['full_name'].sum()
print(total_mass)



mydb = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE
)

cursor = mydb.cursor()

short_pepetide = ''.join(df['weight'])
full_description = '-'.join(df['full_name'])

sql = "INSERT INTO rna_protein_vault (organism_name, raw_rna, short_peptide, full_description) VALUES (%s, %s, %s, %s)"

values = (Y, x, short_pepetide, full_description)

cursor.execute(sql, values)

mydb.commit()
mydb.close()



