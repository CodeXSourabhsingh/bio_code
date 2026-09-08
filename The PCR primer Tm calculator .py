import panda 
import math
import pandas as pd
import mysql.connector
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

Y = input('Enter organism name : ').upper()
Z = input('Enter target gene name : ').upper()
X = input('Enter primer sequence : ').upper()
A = float(input('Enter salt_mM (default 50) : '))

bases = ['A', 'T', 'C', 'G']

if not all(base in bases for base in X):
    print('Invalid primer sequence. Please enter a valid sequence containing only A, T, C, and G.')
else:
    gc_count = X.count('G') + X.count('C')
    at_count = X.count('A') + X.count('T')
    primer_length = len(X)
    salt_molar = A / 1000  
    gc_percent = (gc_count / primer_length) * 100
    tm = 81.5 + (16.6 * math.log10(salt_molar)) + (0.41 * gc_percent) - (500 / primer_length)
    annealing_temp = tm - 5

    print(f'GC Content: {gc_count}')
    print(f'AT Content: {at_count}')
    print(f'Primer Length: {primer_length}')
    print(f'Tm (Melting Temperature): {tm} °C')
    print(f'Annealing Temperature: {annealing_temp} °C')
    print(f'recommended Annealing Temperature: {annealing_temp} °C')

salt_mM = A

data = {
        'Organism': [Y],
        'Target Gene': [Z],
        'Primer Sequence': [X],
        'GC Content': [gc_count],
        'AT Content': [at_count],
        'Primer Length': [primer_length],
        'Tm (Melting Temperature)': [tm],
        'Annealing Temperature': [annealing_temp]
    }

df = pd.DataFrame(data)
print('Primer Summary:')
print(df)


mydb = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE
)
cursor = mydb.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pcr_primers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        organism VARCHAR(100),
        target_gene VARCHAR(100),
        primer VARCHAR(100),
        gc_count INT,
        at_count INT,
        length INT,
        tm_c FLOAT,
        annealing_temp_c FLOAT,
        logged_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

sql = """INSERT INTO pcr_primers (organism, target_gene, primer, salt_mM, gc_count, at_count, length, tm_c, annealing_temp_c)
         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

values = (Y, Z, X, A, gc_count, at_count, primer_length, tm, annealing_temp)
cursor.execute(sql, values)

mydb.commit()

mydb.close()

print(" Data logged successfully into MySQL vault!")